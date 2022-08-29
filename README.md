# Webscraping Project 
## Introduction 
This project is a code block to scrape miscellaneous data about smartphones from a retail e-commerce web store. The code is created on 06/16/2022.  
I utilized **requests and BeautifulSoup** libraries in the project. 
The original code extracts about 1000 products in the web store.

It might be subject to anti-scripting protection measurements by the servers if used excessively in a small period of time.

I have a medium post that I explained the process in more detailed here:

[![image](https://user-images.githubusercontent.com/105684729/187313917-49de41fb-8eea-4a37-9563-18cc234de4fc.png)](https://yusufgulcan.medium.com/how-to-collect-data-using-python-beautifulsoup-library-b9c025668a58)



## Step by step project 

- Navigate to the page to be scraped.

- Send requests order for the url

- Parse the text response with BeautifulSoup 'html.parser'

- Detect the directory of the desired information pieces on the html format of the page.

- Store the data in different groups

- Create a data frame and save it to csv

![image](https://user-images.githubusercontent.com/105684729/187313488-0d658d73-adcd-44d3-b871-1c3e0ef4fa96.png)


## References

[BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/en/latest/#)

[Regular Expressions](https://docs.python.org/3/library/re.html)
