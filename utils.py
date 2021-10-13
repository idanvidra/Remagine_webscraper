import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
from tqdm import tqdm
import time


headers = requests.utils.default_headers()
headers.update(
    {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
url = "https://finder.startupnationcentral.org/company_page/crowded" 
results = requests.get(url, headers) 
specific_soup = BeautifulSoup(results.text, "html.parser")
company_profile_card = specific_soup.find("div", class_='metadata-wrapper')
side_bar = specific_soup.find(class_="zyno-card-4")
row_bar = specific_soup.find(class_="row-container space-between js-startup-classification-section w-105")


# print(company_profile_card.findAll(
#             "div", class_="metadata-description")[2].text)
# print(company_profile_card.findAll(
#             "div", class_="zyno-card-4"))
# print(company_profile_card.find(
#             "div", class_="metadata-description").next_element)
# print(company_profile_card.find(
#             "div", class_="metadata-description").next_element.next_element)

# print(specific_soup.find(text="GEOGRAPHICAL MARKETS").parent.parent.find(class_="metadata-description").text.strip())

# tags_list = specific_soup.find(class_="tags-wrapper")
# print(tags_list)
# tags_list = ([tag.text for tag in tags_list])
# print(tags_list)

# verticals = specific_soup.findAll(class_="tags-wrapper")[1].findAll('a')
# verticals = ([vertical.text for vertical in verticals])
# print(verticals)

# team_members = []
# team_members_soup = specific_soup.find(class_="team-member-cards-wrapper js-team-member-carousel")
# for member in team_members_soup.findAll(class_="card-wrapper"):
#     member_name = member.find(class_="card-title").text.strip()
#     member_title = member.find(class_="card-subtitle").text.strip()
#     try:
#         member_linkedin_url = member.find('a')['href']
#     except:
#         member_linkedin_url = '-'
#     member_full_credits = (member_name, member_title, member_linkedin_url)
#     team_members.append(member_full_credits)
# print(team_members)


# sectors = row_bar.find(lambda tag:tag.name=="div" and "Sector" in tag.text).findAll('a')
# sectors = ([sector.text.strip() for sector in sectors])
# print(sectors)

core_technologies = row_bar.find(lambda tag:tag.name=="div" and "Core Technology" in tag.text).findAll('a')
core_technologies = ([core_technology.text.strip() for core_technology in core_technologies])
print(core_technologies)


