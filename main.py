import urllib.request
import datetime
import threading
import os
import shutil
import requests
from bs4 import BeautifulSoup

ARG_TYPES = [
    'Affirmatives',
    'Case Negatives',
    'Counterplans',
    'Disadvantages',
    'Impact Files',
    'Kritik Answers',
    'Kritiks',
    'Politics',
    'Theory',
    'Topicality'
]
PREFIX_URL = "https://openev.debatecoaches.org/"


def feedback(file_name):
    print(f"Downloading: {file_name}")


def download(num, urls):
    # Fetching raw HTML
    response = requests.get(urls[num])

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading and categorizing files
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for span_link in span_links:
        download_url = span_link.find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(
                download_url, os.path.join(f"./downloads/{num + 1}. {ARG_TYPES[num]}", file_name))


def main():
    # Removing folders if they already exist
    if os.path.isdir(f"./downloads/"):
        shutil.rmtree(f"./downloads/")

    # Creating respective folders
    os.mkdir("./downloads/")
    for num, arg in enumerate(ARG_TYPES):
        os.mkdir(f"./downloads/{num + 1}. {arg}")

    # Getting current debate year
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    if current_month >= 1 and current_month < 8:
        current_year -= 1
    debate_year = str(current_year)

    # Generating URLs
    urls = [
        f"{PREFIX_URL}{debate_year}/Affirmatives",
        f"{PREFIX_URL}{debate_year}/Case%20Negatives",
        f"{PREFIX_URL}{debate_year}/Counterplans",
        f"{PREFIX_URL}{debate_year}/Disadvantages",
        f"{PREFIX_URL}{debate_year}/Impact%20Files",
        f"{PREFIX_URL}{debate_year}/Kritik%20Answers",
        f"{PREFIX_URL}{debate_year}/Kritiks",
        f"{PREFIX_URL}{debate_year}/Politics",
        f"{PREFIX_URL}{debate_year}/Theory",
        f"{PREFIX_URL}{debate_year}/Topicality"
    ]

    # Creating download threads
    threads = [threading.Thread(target=download, args=(i, urls,))
               for i in range(len(ARG_TYPES))]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
