from itertools import product
import asyncio
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

async def process_program(url, fio_set, semaphore):
    async with semaphore:
        print(f"Processing program: {url}")
        url += "/ratings"
        try:
            froms = await get_all_froms(url)
            courses = await get_all_courses(url)

            froms_a = []
            courses_a = []

            for item in froms:
                value = item.find_all("option")
                for option in value:
                    froms_a.append(option.get("value"))

            for item in courses:
                value = item.find_all("option")
                for option in value:
                    courses_a.append(option.get("value"))

            for elem in product(*[froms_a, courses_a]):
                address = url + f"/?course={elem[1]}&from={elem[0]}"
                print(address)

                data = await parse_rating_table(address)
                if data:
                    for row in data:
                        try:
                            fio = row.find("td", class_="special-table__cell special-table__cell--stud").text.strip()
                            fio_set.add(fio)
                        except AttributeError:
                            print(f"  Could not find FIO in row for {address}")
                else:
                    print(f"  No data parsed for {address}")

        except Exception as e:
            print(f"Error processing program {url}: {e}")
    
async def main():
    """Main function to run the asynchronous operations."""
    # urls = get_program_links()
    # unique_urls = set(urls)

    semaphore = asyncio.Semaphore(5)
    fio_set = set()

    urls = [
        "https://perm.hse.ru/ba/se", # Программная-инженерия
        "https://perm.hse.ru/ba/bi", # Бизнес-информатика,
        "https://perm.hse.ru/ba/isystems" # РИС
    ]

    tasks = [process_program(url, fio_set, semaphore) for url in urls]
    await asyncio.gather(*tasks)

    return fio_set
    