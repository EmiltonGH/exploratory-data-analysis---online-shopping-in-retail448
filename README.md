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
   - Setup GitHub:
     We will use GitHub to track changes to our code and save them online in a GitHub repo.
     
   - db_utils.py:
     This Python script contain our code to extract the data from the database.Within the script,we create a       new class called RDSDatabaseConnector. This class will contain the methods which we will use to extract       data from the RDS database.
     
   - credentials.yaml:
     Created this file to store the database credentials.Added this file to our .gitignore file in our           repository, as we don't want our credentials being pushed to GitHub for security reasons.

   - customer_activity.csv:
     The data is stored in a table called customer_activity.

   - DataTransform.py:
     If there are columns should be converted into a different format, a DataTransform class to handle these       conversions. Within the DataTransform class we add methods which we can apply to our DataFrame columns        to perform any required conversions.

   - DataFrameInfo.py:
     After converting our columns to a more appropriate format, we develop a class to extract information         from the DataFrame and its columns. Created a DataFrameInfo class which will contain methods that            generate useful information about our DataFrame.

   - plottingdata.py:
     An important EDA task is to impute or remove missing values from the dataset. Missing values can occur       due to a variety of reasons such as data entry errors or incomplete information.
     We create two classes at this stage:
     A Plotter class to visualise insights from the data
     A DataFrameTransformclass to perform EDA transformations on your data

   - Skewed_columns.py:
     Skewed data can lead to biased models and inaccurate results, so it's important to address this issue      before proceeding with any analysis.
     Firstly we need to identify the skewed columns in the data. This can be done using standard Pandas           methods. We then need to determine a threshold for the skewness of the data, over which a column will        be considered skewed. We should also visualise the data using your Plotter class to analyse the skew.
     Once the skewed columns are identified, we should perform transformations on these columns to determine      which transformation results in the biggest reduction in skew. We created the the method to transform        the columns in our DateFrameTransform class.

   - remove_outliers.py:
     Removing outliers from the dataset will improve the quality and accuracy of the analysis as outliers         can distort the analysis results. First we identify the outliers and then use a method to remove them.
     First visualise our data using our Plotter class to determine if the columns contain outliers.
     Once identified use a method to transform or remove the outliers from the dataset. With the outliers         transformed/removed re-visualise our data with our Plotter class to check that the outliers have been      correctly removed.

   - dropping_overly_correlated_columns.py:
     Highly correlated columns in a dataset can lead to multicollinearity issues, which can affect the           accuracy and interpretability of models built on the data. We will identify highly correlated columns       and remove them to improve the quality of the data.
     First compute the correlation matrix for the dataset and visualise it.Then identify which columns are        highly correlated. We need to decide on a correlation threshold and to remove all columns above this         threshold.

   - customers_doing.py:
     Our manager would like a general overview of the performance of the website.We use pandas to find the      answers for the following questions answered:
     Are sales proportionally happening more on weekends?
     Which regions are generating the most revenue currently?
     Is there any particular website traffic that stands out when generating sales?
     What percentage of time is spent on the website performing administrative/product or informational      related tasks?
     Are there any informational/administrative tasks which users spend time doing most?
     What is the breakdown of months making the most sales?

   - customers_and_softwares.py:
     The company would like to know what systems our users are using to visit the website. To answer this      question we created visualisations of the following:
     The count of the operating systems used to visit the site and the percentage of the total
     The amount of users visiting the site using mobile operating system and desktop operating systems
     The most commonly used browsers and their breakdown on mobile versus desktop
     Based on this analysis of what are the most popular operating system, are there any regions where there is a      discrepancy in what is popular? This could be an indication that users in that region are having technical      issues that the tech team might want to investigate.

   - effective_marketing.py:
     The company whats to investigate the traffic coming to the website to see if the marketing team can make any      improvements to their existing strategy. They would like the following information so that they can make      better decisions about what is/isn't working. We created visualisations of the following data:
     Visualise what traffic is currently generating the most revenue broken down by region
     What traffic has the highest bounce rate? This could indicate that the marketing channels advertisement       isn't enticing enough for the customers. Conversely a low bounce rate can indicate that the strategy is      highly effective. Break down this data by region.
     Check what months have generated the most sales from ads traffic

   - revenue_generated.py:
     We have been asked to determine where the website revenue is being generated and identifying any problematic      areas in the data. Therefore we created visualisations and generate reports for the following queries:
     Which region is currently generating the most/least revenue?
     What percentage of our returning/new customers are making a purchase when they visit the site?
     Are sales being made more on weekends comparatively to weekdays?
     Which months have been the most effective for generating sales?
     Is direct/social or advertising traffic contributing heavily to sales?
     
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
  
