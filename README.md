## daily-news-collecting

## Introduction
- This program selects for latest news articles at the time of initializing the program to summarize and store in database

## Instructions
- Start program from ./app/main.py
- Input links of desired webpages and it will search these links and ask GPT to summarize the information (sample is included in /search/search.py package)

## GPT-API
- Allows for full code automation (with out this, the work around is using opencv and pyautogui)

## Future improvements
1. Create API to transfer data between GPT and program
    - Create an API endpoint or a webhook receiver.
    - Input the data received from gpt into this endpoint.
    - With Python script make requests to the API endpoint or listens to the webhook to receive the data.

2. Figure out appropriate way to request data from news pages
3. Expand database with more entities (Author, Company, Brand, etc)
4. Automate link acquiring feature
5. Find ways to separate this into 2 systems that allow for more secure local storing of data