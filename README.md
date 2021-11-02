# Remagine_webscraper

Web scraper that collects startup companies data from Startup Nation Central.

The data is collected, analyzed by AI21's Jurassic model and sent via email to Remagine.
# Remagine_webscraper
 
![Image of Remagine Logo](https://github.com/idanvidra/Remagine_webscraper/blob/main/logo/Remagine%20logo.png) 

This is the Remagine project github.
The goal is to collect Israeli sturtup data and display to the VC fund.
Posted here is the technology code base for that project.

Please notice the project and issues in the github for details on the progress.

## Getting Started

### Clone the project

The first thing you'll want to do, is 'git clone' this project.
Create an appropriate folder in your local machine, 
Then enter Git Bash (or any other Linux terminal)
and type:
```
git clone <clone url>
```

the "clone url" can be found on the the top right part of this github page.

### Prerequisites

The prerequisites are listed in the "requirements.txt" file.
Make sure you have a working virtual environment with all the packages downloaded in it.
If you want to make a new virtual environment, create it and make sure you run
```
pip install requirements.txt
```
when inside your venv.

### Running the app

To run the app, I recommend using VS Code.
Follow these steps:
* Open the project you've cloned in VS Code.
* Run the file 'app.py' or 'main.py'
* The data will be transfered to data.xlsx

## Built With
* [Beautiful soup](https://beautiful-soup-4.readthedocs.io/en/latest/) /
  A Python library for pulling data out of HTML and XML files.

## Importent links
* [Startup Nation Central](https://finder.startupnationcentral.org/startups/search?tab=recently_updated&list_1_action=and&list_2_action=and&list_3_action=and&list_4_action=and&list_5_action=and&list_6_action=and&list_7_action=and&list_8_action=and&list_9_action=and&list_10_action=and&list_11_action=and&list_12_action=and&list_13_action=and&list_14_action=and&list_15_action=and&list_16_action=and&list_17_action=and&list_18_action=and&list_19_action=and&list_20_action=and&funding_stage=Bootstrapped&funding_stage=Pre-Seed&funding_stage=Seed&founded_from_year=2020&founded_to_year=2021&status=Active&academia_based=0&time_range_code=2&time_range_from_date=2021-09-12)
  / The website we are currently scraping


<!-- CONTRIBUTING -->
## Contributing

Feel free to contribute your own knowledge so that others can enjoy it too !\
To do that, simply:

1. Clone the project.
2. Create your Feature Branch (`git checkout -b feature/new_section_name`)
3. Commit your Changes (`git commit -m 'Add some section'`)
4. Push to the Branch (`git push origin feature/new_section_name`)
5. Open a Pull Request
