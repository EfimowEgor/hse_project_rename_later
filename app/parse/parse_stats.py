from itertools import product
import asyncio
import re
import requests
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def parse_rating_table(url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            response = await page.goto(url)

            if response.status == 404:
                print(f"Page not found (404): {url}")
                await browser.close()
                return []

            await page.wait_for_selector("div.table-wrapper__inner", timeout=200)

            html = await page.content()
            soup = BeautifulSoup(html, 'html.parser')
            data = soup.select("tbody tr")

            await browser.close()
            return data
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            await browser.close()
            return []

async def get_all_froms(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        try:
            await page.wait_for_selector("div.first_child.last_child", timeout=200)
        except Exception as e:
            print(f"Error: Timeout waiting for 'from' selector on {url}: {e}")
            await browser.close()
            return []

        html = await page.content()

        soup = BeautifulSoup(html, 'html.parser')

        data = soup.select("div.first_child.last_child select[name='from']")

        await browser.close()

        return data

async def get_all_courses(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        await page.goto(url)

        try:
            await page.wait_for_selector("div.first_child.last_child", timeout=200)
        except Exception as e:
            print(f"Error: Timeout waiting for 'course' selector on {url}: {e}")
            await browser.close()
            return []

        html = await page.content()

        soup = BeautifulSoup(html, 'html.parser')

        data = soup.select("div.first_child.last_child select[name='course']")

        await browser.close()

        return data

def process_stats(table_row):
    tds = table_row.find_all('td')
    values = []

    for pos, td in enumerate(tds):
        if td.get('style') and 'display: none' in td.get('style'):
            continue

        cell_content = td.text.strip()

        if not cell_content and pos == 4:
            values.append(None)
        elif not cell_content and pos == 5:
            values.append(None)
        else:
            values.append(cell_content)

    return tuple(values)

def process_rating_name(rating_name: str):
    years_match = re.search(r"(\d{4}/\d{4})", rating_name)
    years = years_match.group(1) if years_match else None

    rating_type = None
    if "Текущий рейтинг после пересдач" in rating_name:
        rating_type = "retake"
    elif "Текущий рейтинг" in rating_name:
        rating_type = "current"
    elif "Кумулятивный рейтинг" in rating_name:
        rating_type = "cumulative"
    elif "Рейтинг выпускников" in rating_name:
        rating_type = "grad"

    type2id = {
        "current": 1,
        "cumulative": 2,
        "grad": 3,
        "retake": 4
    }

    semester = None
    semester_match = re.search(r"\((\d)\s*семестр\)", rating_name)
    if semester_match:
        semester = int(semester_match.group(1))

    modules = None
    modules_match = re.search(r"(\d-\d)", rating_name)
    if modules_match:
        modules = modules_match.group(1)
    elif semester:
        modules = "1-2" if semester == 1 else "3-4"

    return {
        "years": years,
        "rating_type": type2id[rating_type],
        "modules": modules,
    }


async def process_program(url, semaphore):
    async with semaphore:
        print(f"Processing program: {url}")
        url += "/ratings"
        try:
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, 'html.parser')

            pname_elements = soup.select("div.header-content h2.h1 a")

            if pname_elements:
                pname = pname_elements[0]
            else:
                print("Элемент не найден.")

            match = re.search(r'«(.*?)»', pname.text.strip())

            if match:
                extracted_text = match.group(1)
            else:
                print("Текст в кавычках не найден.")

            froms = await get_all_froms(url)
            courses = await get_all_courses(url)

            froms_val_to_year = {}
            for item in froms:
                value = item.find_all("option")
                for option in value:
                    from_val = option.get("value")
                    rating_name = option.text.strip()
                    name_parts = process_rating_name(rating_name)
                    if name_parts["years"]:
                        froms_val_to_year[from_val] = (
                            name_parts["years"],
                            name_parts["rating_type"],
                            name_parts["modules"]
                        )

            courses_a = []
            for item in courses:
                value = item.find_all("option")
                for option in value:
                    courses_a.append(option.get("value"))

            unique_froms_val = sorted(froms_val_to_year.keys(), key=lambda x: froms_val_to_year[x][0], reverse=True)
            num_unique_froms = len(unique_froms_val)
            num_courses = len(courses_a)

            for i, (from_val, course_val) in enumerate(product(unique_froms_val, courses_a)):
                year, rating_type, modules = froms_val_to_year[from_val]

                address = url + f"/?course={course_val}&from={from_val}"
                print(address)

                data = await parse_rating_table(address)

                if data:
                    for row in data:
                        try:
                            name, rating, g_mean, g_min, percentile, gpa = process_stats(row)
                            course = course_val

                            yield (
                                name,
                                rating,
                                g_mean,
                                g_min,
                                percentile,
                                gpa,
                                course,
                                year,
                                rating_type,
                                modules,
                                extracted_text,
                            )

                        except AttributeError:
                            print(f"Cannot parse stats table")
                else:
                    print(f"No data parsed for {address}")

        except Exception as e:
            print(f"Error processing program {url}: {e}")
    
async def main():
    semaphore = asyncio.Semaphore(5)

    urls = [
        "https://perm.hse.ru/ba/se",  # Программная-инженерия
        "https://perm.hse.ru/ba/bi",  # Бизнес-информатика,
        "https://perm.hse.ru/ba/isystems"  # РИС
    ]

    async def process_and_collect(url, semaphore):
        results = []
        async for result in process_program(url, semaphore):
            results.append(result)
        return results

    tasks = [process_and_collect(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)

    return results


# if __name__ == "__main__":
#     asyncio.run(main())
    