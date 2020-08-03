# Developed by Ian Draves
# Apache License 2.0

import time
import datetime
import threading
import os
import shutil
import traceback
from itertools import cycle
    
try:
    import requests
    from bs4 import BeautifulSoup
    from lxml.html import fromstring
except:
    os.system("pip3 install requests")
    os.system("pip3 install bs4")
    os.system("pip3 install lxml")

# Getting current debate year
current_year = datetime.date.today().year
current_month = datetime.date.today().month
if current_month >= 1 and current_month < 8:
    current_year -= 1
debate_year = str(current_year)

# Defining variables
arg_types = [
    '1. Affirmatives',
    '2. Case Negatives',
    '3. Counterplans',
    '4. Disadvantages',
    '5. Impact Files',
    '6. Kritik Answers',
    '7. Kritiks',
    '8. Politics',
    '9. Theory',
    '10. Topicality'
]
urls = [
    'https://openev.debatecoaches.org/' + debate_year +'/Affirmatives', 
    'https://openev.debatecoaches.org/' + debate_year + '/Case%20Negatives',
    'https://openev.debatecoaches.org/' + debate_year + '/Counterplans',
    'https://openev.debatecoaches.org/' + debate_year + '/Disadvantages',
    'https://openev.debatecoaches.org/' + debate_year + '/Impact%20Files',
    'https://openev.debatecoaches.org/' + debate_year + '/Kritik%20Answers',
    'https://openev.debatecoaches.org/' + debate_year + '/Kritiks',
    'https://openev.debatecoaches.org/' + debate_year + '/Politics',
    'https://openev.debatecoaches.org/' + debate_year + '/Theory',
    'https://openev.debatecoaches.org/' + debate_year + '/Topicality'
]

# Removing folders if they already exist
for x in range(len(arg_types)):
    exists = os.path.isdir(arg_types[x])
    if exists:
        shutil.rmtree(arg_types[x])

# Creating respective folders
for x in range(len(arg_types)):
    os.mkdir(arg_types[x])

# Feedback function
def feedback(file_name):
    print("Downloading: " + file_name)

# Affirmatives
def affs():
    response = requests.get(urls[0])        

    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[0], file_name))

# Case negatives
def caseNegs():
    response = requests.get(urls[1])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[1], file_name))

# Counterplans
def cps():
    response = requests.get(urls[2])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        feedback(file_name)
        urllib.request.urlretrieve(download_url, os.path.join(arg_types[2], file_name))

# Disadvantages
def das():
    response = requests.get(urls[3])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[3], file_name))

# Impact Files
def impactFiles():
    response = requests.get(urls[4])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[4], file_name))

        
# Kritik Answers
def kAnswers():
    response = requests.get(urls[5])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[5], file_name))


# Kritiks
def ks():
    response = requests.get(urls[6])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[6], file_name))

        
# Politics
def politics():
    response = requests.get(urls[7])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[7], file_name))

        
# Theory
def theory():
    response = requests.get(urls[8])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[8], file_name))

# Topicality
def t():
    response = requests.get(urls[9])

     # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Downloading entire dataset and organizing it
    span_links = soup.findAll("span", {"class": "wikiexternallink"})
    for i in range(len(span_links)):
        download_url = span_links[i].find("a").get("href").replace(" ", "%20")
        file_name = download_url.rsplit('/', 1)[-1].replace("%20", " ")
        if os.path.splitext(file_name)[1] != ".docx":
            pass
        else:
            feedback(file_name)
            urllib.request.urlretrieve(download_url, os.path.join(arg_types[9], file_name))

if __name__ == "__main__":
    # Initializing threads
    aff_files = threading.Thread(target = affs) 
    neg_files = threading.Thread(target = caseNegs) 
    cp_files = threading.Thread(target = cps) 
    da_files = threading.Thread(target = das) 
    impact_files = threading.Thread(target = impactFiles) 
    kanswer_files = threading.Thread(target = kAnswers) 
    k_files = threading.Thread(target = ks) 
    politics_files = threading.Thread(target = politics) 
    theory_files = threading.Thread(target = theory) 
    t_files = threading.Thread(target = t) 

    # Starting threads 
    aff_files.start() 
    neg_files.start() 
    cp_files.start() 
    da_files.start() 
    impact_files.start() 
    kanswer_files.start() 
    k_files.start() 
    politics_files.start() 
    theory_files.start() 
    t_files.start() 
  
    # Waiting until threads are executed 
    aff_files.join() 
    neg_files.join() 
    cp_files.join() 
    da_files.join() 
    impact_files.join() 
    kanswer_files.join() 
    k_files.join() 
    politics_files.join() 
    theory_files.join() 
    t_files.join() 
