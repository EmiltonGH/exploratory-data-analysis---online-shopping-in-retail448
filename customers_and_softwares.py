import matplotlib.pyplot as plt
import pandas as pd

# Load data into a DataFrame
customer_activity = pd.read_csv('customer_activity.csv')  # Replace 'customer_activity.csv' with your file path

# Drop rows with missing values in the 'operating_systems' column
customer_activity = customer_activity.dropna(subset=['operating_systems'])

# Count of operating systems used to visit the site and the percentage of the total
operating_system_counts = customer_activity['operating_systems'].value_counts()
operating_system_percentages = operating_system_counts / operating_system_counts.sum() * 100

plt.figure(figsize=(10, 6))
operating_system_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Operating Systems Used to Visit the Site')
plt.xlabel('Operating System')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
operating_system_percentages.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen', 'lightblue'])
plt.title('Percentage of Operating Systems Used to Visit the Site')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Amount of users visiting the site using mobile operating systems and desktop operating systems
mobile_os_counts = customer_activity[customer_activity['operating_systems'].str.contains('Mobile', na=False, case=False)]['operating_systems'].value_counts()
desktop_os_counts = customer_activity[~customer_activity['operating_systems'].str.contains('Mobile', na=False, case=False)]['operating_systems'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(['Mobile', 'Desktop'], [mobile_os_counts.sum(), desktop_os_counts.sum()], color=['lightgreen', 'skyblue'])
plt.title('Number of Users Visiting the Site by Operating System Type')
plt.xlabel('Operating System Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Most commonly used browsers and their breakdown on mobile versus desktop
browser_counts = customer_activity['browser'].value_counts()
mobile_browser_counts = customer_activity[customer_activity['operating_systems'].str.contains('Mobile', na=False, case=False)]['browser'].value_counts()
desktop_browser_counts = customer_activity[~customer_activity['operating_systems'].str.contains('Mobile', na=False, case=False)]['browser'].value_counts()

plt.figure(figsize=(12, 6))
plt.bar(browser_counts.index, browser_counts.values, color='skyblue', label='Total')
plt.bar(mobile_browser_counts.index, mobile_browser_counts.values, color='lightgreen', label='Mobile')
plt.bar(desktop_browser_counts.index, desktop_browser_counts.values, color='lightcoral', label='Desktop')
plt.title('Most Commonly Used Browsers by Operating System Type')
plt.xlabel('Browser')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Analysis of popular operating systems and discrepancies in regions
popular_os = operating_system_counts.idxmax()
region_os_counts = customer_activity.groupby('region')['operating_systems'].apply(lambda x: (x == popular_os).sum())
region_os_counts.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Count of ' + popular_os + ' Users by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
