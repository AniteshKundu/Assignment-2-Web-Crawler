This assignment involves creating a web crawler—a program that automatically navigates the web to collect specific information based on given parameters. The web crawler will be designed to find URLs from web pages that match specified criteria.

Breakdown of the Assignment
Expected Input
I create a program that takes in a JSON object with the following fields:

Primary Category: This specifies the type of content to search for, such as:
"Medical Journal"
"Blog"
"News"
Secondary Category: This further narrows down the search within the primary category, such as:
"Orthopedic"
"Gynecology"
Geography: This specifies the geographical focus of the search, such as:
"India"
"US"
"Europe"
"Latin America"
Date Range: This specifies the time period for the search, such as:
"2022"
"2022-23"
"Sep 22"
Expected Output
The output should be a CSV file containing the URLs that the web crawler has found. I can also include additional relevant data if it adds value, such as the page title, publication date, or a brief summary.

Goals of the Assignment
Data Collection: Develop a tool to gather URLs from web pages based on specific criteria.
Automation: Automate the process of web scraping to reduce manual effort in data collection.
Filtering: Ensure the collected URLs match the given parameters.
Output: Save the collected data in a structured format (CSV file) for easy analysis or further processing.


Technologies
The preferred technology stack is Python or JavaScript. Both languages have strong libraries and frameworks for web scraping and data processing:

Python: Libraries like requests for HTTP requests, BeautifulSoup for parsing HTML, and csv for writing to CSV files.
