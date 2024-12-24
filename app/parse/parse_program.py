import os
from dotenv import load_dotenv
import requests

from bs4 import BeautifulSoup


load_dotenv()

name2level = {
    "ba": "bachelor",
    "ma": "magister"
}

def get_program_names_by_level(level: str):
    res = requests.get(os.getenv("ROOT_PATH")+name2level[level])

    soap = BeautifulSoup(res.content, "html.parser")

    programs = []
    program_path = "div.edu-programm__group div.b-row"

    data = soap.select(program_path)

    for div in data:
        style = div.get("style", "")
        if "display: none" not in style:
            item = div.find("a", {"class": "link"})

            if level in item.get("href", "").split('/'):
                programs.append(item.text)

    return programs

def get_program_links():
    links = []
    for level in ["ba", "ma"]:
        res = requests.get(os.getenv("ROOT_PATH")+name2level[level])

        soap = BeautifulSoup(res.content, "html.parser")
        program_path = "div.edu-programm__group div.b-row"

        data = soap.select(program_path)

        for div in data:
            style = div.get("style", "")
            if "display: none" not in style:
                item = div.find("a", {"class": "link"})
                link = item.get("href", "")

                if level in item.get("href", "").split('/'):
                    links.append(link[:-1])

    return links
