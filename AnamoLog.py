# -*- coding: utf-8 -*-
"""
Created on Sat May 20 01:18:26 2023

@author: Kashish
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r"C:\Users\Kashish\Downloads\Chitkara_Anomaly_Detection\Chitkara_Anomaly_Detection\Login_Data.csv")
print(df.info())
# Handling missing values
# Remove rows with missing values
df.dropna(inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

# Data type conversion
# Convert User ID to string
df['User ID'] = df['User ID'].astype(str)
# Convert Login Timestamp column to datetime type
df['Login Timestamp'] = pd.to_datetime(df['Login Timestamp'])

# Data transformation (example: extract date and time from Login Timestamp)
df['Date'] = df['Login Timestamp'].dt.date
df['Time'] = df['Login Timestamp'].dt.time

# Pattern 1: Daily login activity
daily_logins = df.groupby(df['Login Timestamp'].dt.date).size().head(5)
print("Daily login activity:")
print(daily_logins)

# Pattern 2: Popular browsers
popular_browsers = df['Browser Name and Version'].value_counts().head(5)
print("Popular browsers:")
print(popular_browsers)

# Pattern 3: Login success rate
login_success_rate = df['Login Successful'].mean() * 100
print("Login success rate: {:.2f}%".format(login_success_rate))
# Pattern 4: Distribution by device type
device_distribution = df['Device Type'].value_counts()
print("Distribution by device type:")
print(device_distribution)

# Pattern 5: Top countries with the most logins
top_countries = df['Country'].value_counts().head(5)
print("Top countries with the most logins:")
print(top_countries)



threshold = 10 
threshold = pd.to_datetime('yyyy-mm-dd hh:mm:ss', format='%Y-%m-%d %H:%M:%S')  # Replace with the actual datetime threshold
ip_counts = df['IP Address'].value_counts()
potentially_anomalous_ip = ip_counts[ip_counts > threshold]

# Country
country_counts = df['Country'].value_counts()
potentially_anomalous_country = country_counts[country_counts < threshold]

# Region
region_counts = df['Region'].value_counts()
potentially_anomalous_region = region_counts[region_counts < threshold]

# City
city_counts = df['City'].value_counts()
potentially_anomalous_city = city_counts[city_counts < threshold]

# Browser Name and Version
browser_counts = df['Browser Name and Version'].value_counts()
potentially_anomalous_browser = browser_counts[browser_counts < threshold]

# Device Type
device_counts = df['Device Type'].value_counts()
potentially_anomalous_device = device_counts[device_counts < threshold]

# Login Timestamp
#login_timestamps = pd.to_datetime(df['Login Timestamp'])
#potentially_anomalous_timestamps = login_timestamps[login_timestamps < threshold]

# Print the potentially anomalous data
print("Potentially Anomalous IP Addresses:")
print(potentially_anomalous_ip)

print("\nPotentially Anomalous Countries:")
print(potentially_anomalous_country)

print("\nPotentially Anomalous Regions:")
print(potentially_anomalous_region)

print("\nPotentially Anomalous Cities:")
print(potentially_anomalous_city)

print("\nPotentially Anomalous Browsers:")
print(potentially_anomalous_browser)

print("\nPotentially Anomalous Devices:")
print(potentially_anomalous_device)

#print("\nPotentially Anomalous Timestamps:")
#print(potentially_anomalous_timesta
for column in df.columns:
    unique_patterns = df[column].value_counts()
    print(f"Unique Patterns for {column}:")
    print(unique_patterns)
    print()
import sklearn
from sklearn.ensemble import IsolationForest
import pickle

# Assuming your DataFrame is named 'df'
# Replace 'column_names' with the actual column names from your dataset

# Prepare the data and perform any necessary preprocessing
# ...

# Train the anomaly detection model
model = IsolationForest(contamination=0.01)  # Adjust the contamination parameter as needed
model.fit(df['Login Timestamp','User ID ','IP Address','Country','Region ',' City ','Browser Name and Version',' Device Type ','Login Successful '])

# Save the trained model to disk using pickle
pickle.dump(model, open('anomaly_model.pkl', 'wb'))




