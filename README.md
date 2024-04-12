## Project Title
Exploratory Data Analysis - Online Shopping in Retail

## Table of Contents
   - A description of the project
   - Installation instructions
   - File structure of the project
   - Table columns
     
## A description of the project
You currently work for a large retail company where you have the task to conduct exploratory data analysis on a dataset of online shopping website activity. 
With the increasing popularity of online shopping, this dataset provides valuable insights into consumer behaviour.
We will use various statistical and visualisation techniques to explore the data and draw meaningful insights. 
This analysis will not only provide a better understanding of customer behaviour but also help the business optimise marketing strategies and improve their customer experience.
The data contains information about the website activity of users over one year. 
Each sample represents the user interacting with the website during a shopping session.
Overall, this project will showcase the power of exploratory data analysis in uncovering valuable insights from large datasets and how to leveraged these insights to drive business success.

## Installation instructions
Before you start using this project, ensure that you have the following prerequisites installed or created accounts.
   - Python
   - GitHub
   - Pandas
   - Numpy
   - Matplotlib
   - seaborn
   - PyYAML
   - SQLalchemy

## File structure of the project
   - Setup GitHub
     We will use GitHub to track changes to our code and save them online in a GitHub repo.
     
   - db_utils.py
     This Python script contain our code to extract the data from the database.Within the script,we create a       new class called RDSDatabaseConnector. This class will contain the methods which we will use to extract       data from the RDS database.
     
   - credentials.yaml
     Created this file to store the database credentials.Added this file to our .gitignore file in our      repository, as we don't want our credentials being pushed to GitHub for security reasons.

   - customer_activity.csv
     The data is stored in a table called customer_activity.

   - DataTransform.py
     If there are columns should be converted into a different format, a DataTransform class to handle these      conversions. Within the DataTransform class we add methods which we can apply to our DataFrame columns      to perform any required conversions.

   - DataFrameInfo.py
     
## Table columns
   Below columns of the database to help you understand their meaning.

   - administrative:
     Columns which indicate which administrative activity the user was performing on their
     account
   - administrative_duration: 
     How long a user performed administrative tasks in that session
   - informational: 
     Indicates which informational activity the user was performing on the website
   - informational_duration: 
     How long a users performed informational tasks in seconds during that session
   - product_related: 
     Indicates which product the user was viewing on the website
   - product_related_duration: 
     How long a user browsed products during that session
   - bounce_rates: 
     Historical bounce rate of that particular page for all users (that visited the website and immediately        exited)
   - exit_rates:
     Historical exit rate of the users from that particular page.
   - page_values: 
     The average value contribution of a page to a customer sale
   - month: 
     The month the user's activity took place
   - operating_systems: 
     The operating system the user was using
   - browser: 
     The browser the user was using
   - region: 
     The region the user originated from
   - traffic_type: 
     How the user was redirected to the site
   - visitor_type: 
     Whether a customer was new, returning or other
   - weekend: 
     Whether the activity only took place during the weekend
   - revenue`: 
     Whether the customer purchased anything during that session
  
