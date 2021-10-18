# Made by Idan Dov Vidra

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from tqdm import tqdm
import time

from utils import get_SNC_url

def scrape():   

    # Spoofing the headers we send along with our requests to make it look like we're a legitimate browser
    headers = requests.utils.default_headers()
    headers.update(
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    url = get_SNC_url()

    # Store request.get action
    results = requests.get(url, headers) 

    # Var to assign the method BeautifulSoup to (specifies the desired format)
    # Allows Python to read the components of the page rather than treating it as one long string
    soup = BeautifulSoup(results.text, "html.parser")

    # Headers for excel
    headers_for_excel = ['Name', 'Finder Page', 'Business Model', 'Founding Year', 'Description', 'Number of Employees',
                        'Funds Raised', 'Funding Stage', 'Product Stage', 'Company Website', 'Tags', 'Target Markets', 
                        'Sectors', 'Target Industry', 'Core Technologies']

    # Init empty lists to store data
    name_list = []  # v
    page_url_list = []  # v
    about_list = []  # v
    team_list = []  
    year_founded_list = []  # v
    business_model_list = []  # v
    employees_list = []  # v
    funding_stage_list = []  # v
    product_stage_list = []  # v
    funds_raised_list = []  # v
    company_website_list = []
    tags_list = []
    verticals_list = []
    sectors_list = []
    target_industries_list = []
    core_technologies_list = []

    # Placeholder when feature is not found
    not_found = '-'

    # List of all feature lists
    list_of_feature_lists = [name_list, page_url_list, business_model_list, year_founded_list, about_list,
                            employees_list, funds_raised_list, funding_stage_list, product_stage_list, 
                            company_website_list,tags_list,verticals_list,sectors_list, target_industries_list, 
                            core_technologies_list]

    # Store all the div containers with a class of zyno card
    company_cards_div = soup.find_all(
        'div', class_='js-company-item js-advanced-search-item')

    # Iterate through every div container we stored in company_cards_div
    print("Company cards")
    for container in tqdm(company_cards_div):
        # Get the name
        try:
            name = container.find('a')['data-report-label']
        except:
            name = not_found
        name_list.append(name)

        # Get the URL
        try:
            url = container.find('a')['href']
        except:
            url = not_found
        page_url_list.append(url)

    # Iterate and search in the specific page for every company found
    print("Pages")
    for page in tqdm(page_url_list):
        company_url = "https://finder.startupnationcentral.org" + page
        company_specific_results = requests.get(company_url, None)
        specific_soup = BeautifulSoup(company_specific_results.text, "html.parser")

        # Get Company Profile so we can get: Employees, Funding stage, Money raised, and Product stage
        company_profile_card = specific_soup.find("div", class_='metadata-wrapper')

        # Get different bars to gain access to data
        side_bar = specific_soup.find(class_="zyno-card-4")
        row_bar = specific_soup.find(class_="row-container space-between js-startup-classification-section w-105")

        # Get company description
        description = specific_soup.findAll(
            "div", {"class": "section-description about js-company-description"})
        about_string = ''
        for x in description:
            current_line = x.find('p').text
            about_string += current_line
        about_list.append(about_string)

        # Get the business model
        try:
            business_model = company_profile_card.find(text="BUSINESS MODEL").parent.parent.find(class_="metadata-description").text
        except:
            business_model = not_found
        business_model_list.append(business_model)

        # Get the year founded
        try:
            year_founded = company_profile_card.find(text="FOUNDED").parent.parent.find(class_="metadata-description").text.strip()
        except:
            year_founded = not_found
        year_founded_list.append(year_founded)

        # Get number of employees
        try:
            employees_list.append(company_profile_card.find(text="EMPLOYEES").parent.parent.find(class_="metadata-description").text.strip())
        except:
            employees_list.append(not_found)

        # Get funding stage
        try:
            funding_stage_list.append(company_profile_card.find(text="FUNDING STAGE").parent.parent.find(class_="metadata-description").text.strip())
        except:
            funding_stage_list.append(not_found)

        # Get product stage
        try:
            product_stage_list.append(company_profile_card.find(text="PRODUCT STAGE").parent.parent.find(class_="metadata-description").text.strip())
        except:
            product_stage_list.append(not_found)

        # Get funding raised so far
        try:
            funds_raised_list.append(company_profile_card.find(text="RAISED").parent.parent.find(class_="metadata-description").text.strip())
        except:
            funds_raised_list.append(not_found)
        
        # Get company website url
        try:
            company_website_list.append(side_bar.find(class_="js-external-link-item general-info-regular-text").text.strip())
        except:
            company_website_list.append(not_found)
        
        # Get tags
        try:
            tags = specific_soup.find(class_="tags-wrapper").findAll(class_="tag-name")
            tags = ([tag.text for tag in tags])
            tags_list.append(tags)
        except:
            tags_list.append(not_found)

        # Get verticals
        try:
            verticals = specific_soup.findAll(class_="tags-wrapper")[1].findAll('a')
            verticals = ([vertical.text for vertical in verticals])
            verticals_list.append(verticals)
        except:
            verticals_list.append(not_found)

        # Collet and get team Linkedin profiles
        try:
            team_members = []
            team_members_soup = specific_soup.find(class_="team-member-cards-wrapper js-team-member-carousel")
            for member in team_members_soup.findAll(class_="card-wrapper"):
                member_name = member.find(class_="card-title").text.strip()
                member_title = member.find(class_="card-subtitle").text.strip()
                try:
                    member_linkedin_url = member.find('a')['href']
                except:
                    member_linkedin_url = '-'
                member_full_credits = (member_name, member_title, member_linkedin_url)
                team_members.append(member_full_credits)
            team_list.append(team_members)
        except:
            team_list.append(not_found)

        # Get sectors
        try:
            sectors = row_bar.find(lambda tag:tag.name=="div" and "Sector" in tag.text).findAll('a')
            sectors = ([sector.text.strip() for sector in sectors])
            sectors_list.append(sectors)
        except:
            sectors_list.append(not_found)

        # Get target industries
        try:
            target_industries = row_bar.find(lambda tag:tag.name=="div" and "Target Industry" in tag.text).findAll('a')
            target_industries = ([target_industry.text.strip() for target_industry in target_industries])
            target_industries_list.append(target_industries)
        except:
            target_industries_list.append(not_found)

        # Get core technologies
        try:
            core_technologies = row_bar.find(lambda tag:tag.name=="div" and "Core Technology" in tag.text).findAll('a')
            core_technologies = ([core_technology.text.strip() for core_technology in core_technologies])
            core_technologies_list.append(core_technologies)
        except:
            core_technologies_list.append(not_found)

    # Iterate over lists and make each list item into an singelton array for stacking
    print("Convert to lists")
    for feature_list in tqdm(list_of_feature_lists):
        for index, feature in enumerate(feature_list):
            feature_list[index] = [feature_list[index]]

    # Stack features and convert features to dataframe
    data_matrix = np.hstack([name_list, page_url_list, business_model_list, year_founded_list, about_list,
                            employees_list, funds_raised_list, funding_stage_list, product_stage_list, 
                            company_website_list,tags_list,verticals_list,sectors_list, target_industries_list, core_technologies_list])
    df = pd.DataFrame(data_matrix)
    df.columns = headers_for_excel

    # Create excel spreadsheet
    df.to_excel(excel_writer="results/excel/result.xlsx")

    print("Done")
