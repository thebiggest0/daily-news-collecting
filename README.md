# daily-news-collecting

# Introduction
- This program selects for latest news articles at the time of initializing the program to summarize and store in database

# Instructions
- Start program from ./app/main.py
- If applicable, allow access to IDE running code
- If writing to database, ensure __ is changed to True, default is set to False, ensure to fill out db info in ./database/SQL.py

# GPT-API
- Allows for full automation
- Include your own GPT api-key in both functions 
- To summarize links it will be 1 usage to pull 5 links and 5 usage to summarize each link resulting in 6 gpt usagges
- Using GPT-API is not free so for a cheaper option see "Work Around" section below

# Work Around
- Currently, requires the user to find the links (I am working on automating this aspect too)
- Use OpenCV and Automation to summarize news articles

# Future improvements
1. Create API to transfer data between GPT and program
    - Create an API endpoint or a webhook receiver.
    - Input the data received from gpt into this endpoint.
    - With Python script make requests to the API endpoint or listens to the webhook to receive the data.

2. Figure out appropriate way to request data from news pages
3. Expand database with more entities (Author, Company, Brand, etc)