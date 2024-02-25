# This file contains the code to clean the data and save it to a new file

'''The column indices for the crime data:
    0: 'X' : float, 
    1: 'Y' : float, 
    2: 'RowID' : int, 
    3: 'CCNumber' : string, 
    4: 'CrimeDateTime' : string, 
    5: 'CrimeCode' : string, 
    6: 'Description' : string, 
    7: 'Inside/Outside' : I or O, 
    8: 'Weapon' : string including 'NA', 
    9: 'Post' : int, 
    10: 'Gender' : M, F, or U,
    11: 'Age' : int, 
    12: 'Race' : string, 
    13: 'Ethnicity' : string,, 
    14: 'Location' : string, 
    15: 'Old_District' : string, 
    16: 'New_District' : string, 
    17: 'Neighborhood' : string, 
    18: 'Latitude' : float, 
    19: 'Longitude' : float, 
    20: 'GeoLocation' : string, 
    21: 'PremiseType' : string, 
    22: 'Total_Incidents' : int
'''

'''The column indices for the 311 data:
    0: 'OBJECTID'
    1: 'SRRecordID'
    2: 'ServiceRequestNum'
    3: 'SRType'
    4: 'MethodReceived'
    5: 'CreatedDate'
    6: 'SRStatus'
    7: 'StatusDate'
    8: 'DueDate'
    9: 'CloseDate'
    10: 'Agency'
    11: 'LastActivity'
    12: 'LastActivityDate'
    13: 'Outcome'
    14: 'Address',
    15: 'ZipCode',
    16: 'Neighborhood',
    17: 'CouncilDistrict',
    18: 'PoliceDistrict',
    19: 'PolicePost',
    20: 'Latitude',
    21: 'Longitude',
    22: 'GeoLocation',
    23: 'NeedsSync',
    24: 'IsDeleted',
    25: 'HashedRecord'
'''

import pandas as pd

# Function to return a cleaned version of the crime data
def clean_crime_data(crimeData):

    # Focus on the following columns: 'CrimeDateTime', 'Description', 'Neighborhood', 'Latitude', 'Longitude'
    crimeData = crimeData.iloc[:, [4, 6, 17, 18, 19]]

    # Function to remove rows with dates that are not in 2020 and 2021
    def remove_invalid_dates(data):
        # remove rows with dates that are not in 2020 and 2021
        cleaned_data = data[data['CrimeDateTime'].str.contains('2020|2021')]
        return cleaned_data
    
    # Function to combine similar descriptions
    def combine_similar_descriptions(data):
        # change 'LARCENY FROM AUTO' to 'LARCENY'
        cleaned_data = data.replace('LARCENY FROM AUTO', 'LARCENY')
        # change 'ROBBERY - CARJACKING' to 'ROBBERY'
        cleaned_data = cleaned_data.replace('ROBBERY - CARJACKING', 'ROBBERY')
        # change 'ROBBERY - COMMERCIAL' to 'ROBBERY'
        cleaned_data = cleaned_data.replace('ROBBERY - COMMERCIAL', 'ROBBERY')
        return cleaned_data
    
    # Function to clean the neighborhood column
    def clean_neighborhood_column(data):
        # remove rows with NaN values in the 'Neighborhood' column
        cleaned_data = data.dropna(subset=['Neighborhood'])

        # make the neighborhood values uppercase
        cleaned_data['Neighborhood'] = cleaned_data['Neighborhood'].str.upper()
        return cleaned_data
    
    # Function to remove rows with NaN and 0 values in the 'Longitude' and 'Latitude' column
    def delete_invalid_location_rows(data):
        # delete rows with NaN values in the 'Longitude' and 'Latitude' column
        cleaned_data = data.dropna(subset=['Longitude', 'Latitude'])
        # delete rows with 0 values in the 'Longitude' and 'Latitude' column
        cleaned_data = cleaned_data[cleaned_data['Longitude'] != 0]
        cleaned_data = cleaned_data[cleaned_data['Latitude'] != 0]
        return cleaned_data
    
    # Call the functions
    crimeData = remove_invalid_dates(crimeData)
    crimeData = combine_similar_descriptions(crimeData)
    crimeData = clean_neighborhood_column(crimeData)
    crimeData = delete_invalid_location_rows(crimeData)

    return crimeData




# Function to return a cleaned version of the 311 data
def clean_311_data(serviceData):

    # Focus on the following columns: 'SRType', 'CreatedDate', 'SRStatus', 'CloseDate', 'Neighborhood', 'Latitude', 'Longitude'
    serviceData = serviceData.iloc[:, [3, 5, 6, 9, 16, 20, 21]]

    # Function to remove rows with dates that are not in 2020 and 2021
    def remove_invalid_dates(data):
        # remove rows with created dates that are not in 2020 and 2021
        cleaned_data = data[data['CreatedDate'].str.contains('2020|2021')]
        
        # remove rows with close dates that are not in the year 2020 and 2021 or are NaN
        cleaned_data = cleaned_data[cleaned_data['CloseDate'].str.contains('2020|2021') | cleaned_data['CloseDate'].isna()]
        return cleaned_data
    
    # Function to clean the neighborhood column
    def clean_neighborhood_column(data):
        # remove rows with NaN values in the 'Neighborhood' column
        cleaned_data = data.dropna(subset=['Neighborhood'])

        # make the neighborhood values uppercase
        cleaned_data['Neighborhood'] = cleaned_data['Neighborhood'].str.upper()
        return cleaned_data
    
    # Function to remove rows with NaN and 0 values in the 'Longitude' and 'Latitude' column
    def delete_invalid_location_rows(data):
        # delete rows with NaN values in the 'Longitude' and 'Latitude' column
        cleaned_data = data.dropna(subset=['Longitude', 'Latitude'])
        # delete rows with 0 values in the 'Longitude' and 'Latitude' column
        cleaned_data = cleaned_data[cleaned_data['Longitude'] != 0]
        cleaned_data = cleaned_data[cleaned_data['Latitude'] != 0]
        return cleaned_data
    
    # Call the functions
    serviceData = remove_invalid_dates(serviceData)
    serviceData = clean_neighborhood_column(serviceData)
    serviceData = delete_invalid_location_rows(serviceData)

    return serviceData



# create a new cleaned file for the crime data
# _________________________________________________________________________
# crimeData = pd.read_csv("Part_1_Crime_Data.csv")
# crimeData = clean_crime_data(crimeData)
# crimeData.to_csv("Cleaned_Part_1_Crime_Data.csv", index=False)
# _________________________________________________________________________



# create a new cleaned file for the 311 data
# _________________________________________________________________________
# serviceData = pd.read_csv("311_Customer_Service_Request.csv")
# serviceData = clean_311_data(serviceData)
# serviceData.to_csv("Cleaned_311_Customer_Service_Request.csv", index=False)
# _________________________________________________________________________