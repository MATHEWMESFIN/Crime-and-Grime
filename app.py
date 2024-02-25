import streamlit as st
import pandas as pd

st.title("Crime and Grime")

# Read the data from the clean csv files

# 'SRType', 'CreatedDate', 'SRStatus', 'CloseDate', 'Neighborhood', 'Latitude', 'Longitude'
serviceData = pd.read_csv('Cleaned_311_Customer_Service_Request.csv')

# CrimeDateTime', 'Description', 'Neighborhood', 'Latitude', 'Longitude'
crimeData = pd.read_csv('Cleaned_Part_1_Crime_Data.csv')

# print the number of unique values
st.write("serviceData unique values")
st.write(serviceData.nunique())

st.write("crimeData unique values")
st.write(crimeData.nunique())

# print the unique SRType values with their counts
st.write("SRType column")
st.write(serviceData['SRType'].value_counts())



