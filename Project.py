"""
URL: https://saida0.github.io/Data-Science-Project/
TITLE: Changes in Precipitation Levels in NYC and Its Correlation With Global Land Temperature as Indicators of Climate Change

TABLE OF CONTENTS:
1. DATA ACQUISITION AND CLEANING:.............................................. Line 27
    A. Retrieving and Saving NYC Precipitation Data from the NOAA API.......... Line 29
    B. Cleaning Datasets....................................................... Line 64
    C. Combining Datasets...................................................... Line 87

2.  DATA ANALYSIS/VISUALIZATION:............................................... Line 109
    A. Plotting Daily NYC Precipitation Data....................................Line 111
    B. Plotting Monthly NYC Precipitation Data..................................Line 128
    C. Plotting Global Land Temperature Data....................................Line 200
    D. Plotting Combined Monthly Precipitation/Global Land Temperature Data.....Line 214

3. RESOURCES................................................................... Line 237
"""

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from datetime import datetime

# 1. DATA ACQUISITION AND CLEANING:

# A. Retrieving and Saving NYC Precipitation Data from the NOAA API:
"""
# saving access token generated from NOAA and NYC Central Park weather station ID
token = '' # insert api key
station_id = 'GHCND:USW00094728'

# arrays to store the data from the API response
precip_dates = []
precip = []

# requesting precipitation data within the specified year range
print('Retrieving data from 1900 to 2022. Please wait.')
for year in range(1900, 2022):
    year = str(year)
    print('Working on year: ' + year)
    request = requests.get('https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=PRCP&limit=1000&stationid=GHCND:USW00094728&startdate='+year+'-01-01&enddate='+year+'-12-30', headers={'Token':token})
    data = json.loads(request.text)

    precipitation = [item for item in data['results'] if item['datatype'] == 'PRCP']

    # saving the date and value fields into the precip_dates and precip arrays
    precip_dates += [item['date'] for item in precipitation]
    precip += [item['value'] for item in precipitation]

# converting API response into a dataframe and saving it as a CSV file
df = pd.DataFrame()
df['Date'] = [datetime.strptime(d, "%Y-%m-%dT%H:%M:%S") for d in precip_dates]
df['Precipitation'] = [float(v)/10.0*1.8 + 32 for v in precip]
df.to_csv('NOAA-NYC-PRCP.csv', index=False)
"""





# B. Cleaning Datasets:

# reading CSV datasets
precipitation = pd.read_csv('NOAA-NYC-PRCP.csv') 
land_temp = pd.read_csv('NOAA-Land.csv', skiprows=[0,1,2,3])

# renaming columns in land_temp and changing the 'Date' column formatting ('Year': 190001 -> 'Date': 1900-01-01) 
land_temp = land_temp.rename(columns={'Year':'Date', 'Value':'Temperature'})
land_temp['Date'] = [datetime.strptime(str(s), '%Y%m') for s in land_temp['Date']] 

# converting 'Date' column in precipitation to datetime
precipitation['Date'] = pd.to_datetime(precipitation['Date'])

# making seperate columns for 'Year', 'Month', and 'Day' for land_temp dataset
land_temp[['Year', 'Month', 'Day']] = land_temp['Date'].astype(str).str.split("-", expand = True)

# dropping 'Day' column from land_temp because the datset only shows monthly averages and day numbers are always "01"
land_temp = land_temp.drop('Day', axis=1) 





# C. Combining Datasets

# making a seperate precipitation dataframe which will hold monthly values instead of daily values
# this new dataframe will be used to combine with the land_temp data
precipitation_monthly = pd.DataFrame()
precipitation_monthly = precipitation[['Precipitation']]
precipitation_monthly[['Year', 'Month', 'Day']] = precipitation['Date'].astype(str).str.split("-", expand = True)
#print(precipitation_monthly)


# averaging by year in both datasets
precipitation_monthly = precipitation_monthly.groupby(['Year','Month']).Precipitation.mean().reset_index(name='Precipitation')
land_temp = land_temp.groupby(['Year','Month']).Temperature.mean().reset_index(name='Temperature')

# merging datasets with an inner join and using 'Year' and 'Month' as join key values
land_prcp_monthly = pd.merge(precipitation_monthly, land_temp, how='inner', on=('Year', 'Month'))
#print(land_prcp_monthly)





# 2. DATA ANALYSIS/VISUALIZATION:

# A. Plotting Daily NYC Precipitation 
"""
# plotting a line graph for daily NYC precipitation
precipitation.plot('Date', 'Precipitation')
plt.ylabel("Precipitation (millimeters)")
plt.title('NYC Daily Precipitation Levels (1900-2021)')
plt.savefig("PRCP_Daily.png")
plt.show()

# statistics for daily precipitation levels
print(precipitation['Precipitation'].describe())
"""





# B. Plotting Monthly NYC Precipitation Data
"""
fig, axs = plt.subplots(3, 4, figsize = (17,10))
fig.suptitle('Average Monthly Temperatures from 1900 to 2021', fontsize=16)
jan = precipitation_monthly[precipitation_monthly['Month'] == '01']
axs[0, 0].plot(jan['Year'],jan['Precipitation'],'tab:blue')
axs[0, 0].set_title('January')
axs[0, 0].xaxis.set_major_locator(plt.MaxNLocator(4))

feb = precipitation_monthly[precipitation_monthly['Month'] == '02']
axs[1, 0].plot(feb['Year'],feb['Precipitation'],'tab:blue')
axs[1, 0].set_title('February')
axs[1, 0].xaxis.set_major_locator(plt.MaxNLocator(4))

mar = precipitation_monthly[precipitation_monthly['Month'] == '03']
axs[2, 0].plot(mar['Year'],mar['Precipitation'],'tab:blue')
axs[2, 0].set_title('March')
axs[2, 0].xaxis.set_major_locator(plt.MaxNLocator(4))

apr = precipitation_monthly[precipitation_monthly['Month'] == '04']
axs[0, 1].plot(apr['Year'],apr['Precipitation'],'tab:pink')
axs[0, 1].set_title('March')
axs[0, 1].xaxis.set_major_locator(plt.MaxNLocator(4))

may = precipitation_monthly[precipitation_monthly['Month'] == '05']
axs[1, 1].plot(may['Year'],may['Precipitation'],'tab:pink')
axs[1, 1].set_title('May')
axs[1, 1].xaxis.set_major_locator(plt.MaxNLocator(4))

jun = precipitation_monthly[precipitation_monthly['Month'] == '06']
axs[2, 1].plot(jun['Year'],jun['Precipitation'],'tab:pink')
axs[2, 1].set_title('June')
axs[2, 1].xaxis.set_major_locator(plt.MaxNLocator(4))

jul = precipitation_monthly[precipitation_monthly['Month'] == '07']
axs[0, 2].plot(jul['Year'],jul['Precipitation'],'tab:orange')
axs[0, 2].set_title('July')
axs[0, 2].xaxis.set_major_locator(plt.MaxNLocator(4))

aug = precipitation_monthly[precipitation_monthly['Month'] == '08']
axs[1, 2].plot(aug['Year'],aug['Precipitation'],'tab:orange')
axs[1, 2].set_title('August')
axs[1, 2].xaxis.set_major_locator(plt.MaxNLocator(4))

sep = precipitation_monthly[precipitation_monthly['Month'] == '09']
axs[2, 2].plot(sep['Year'],sep['Precipitation'],'tab:orange')
axs[2, 2].set_title('September')
axs[2, 2].xaxis.set_major_locator(plt.MaxNLocator(4))

octo = precipitation_monthly[precipitation_monthly['Month'] == '10']
axs[0, 3].plot(octo['Year'],octo['Precipitation'],'tab:purple')
axs[0, 3].set_title('October')
axs[0, 3].xaxis.set_major_locator(plt.MaxNLocator(4))

nov = precipitation_monthly[precipitation_monthly['Month'] == '11']
axs[1, 3].plot(nov['Year'],nov['Precipitation'],'tab:purple')
axs[1, 3].set_title('November')
axs[1, 3].xaxis.set_major_locator(plt.MaxNLocator(4))

dec = precipitation_monthly[precipitation_monthly['Month'] == '12']
axs[2, 3].plot(dec['Year'],dec['Precipitation'],'tab:purple')
axs[2, 3].set_title('December')
axs[2, 3].xaxis.set_major_locator(plt.MaxNLocator(4))

plt.savefig("PRCP_Monthly.png")
plt.show()
"""





# C. Plotting Global Land Temperature Data
"""
# plotting a line graph for land_temp from 1900 to 2021
land_temp.plot('Year', 'Temperature', color='orange')
plt.ylabel("Temperature (C)")
plt.title('Monthly Avg. Global Land Temperature (1900-2021)')
plt.savefig("Land_Temp_Monthly.png")
plt.show()
"""





# D. Plotting Combined Monthly Precipitation/Global Land Temperature Data
"""
plt.figure(figsize=(15, 9))
land_prcp_monthly = land_prcp_monthly.set_index(['Year'])
ax1 = land_prcp_monthly['Temperature'].plot(color='orange', grid=True, label='Avg. Monthly Global Land Temp. (C)')
ax2 = land_prcp_monthly['Precipitation'].plot(color='blue', grid=True, secondary_y=True, label='Avg. Monthly NYC Precip. (mm.)')

ax1.set_ylabel('Temperature (C)')
ax2.set_ylabel('Precipitation (mm.)')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

plt.legend(h1+h2, l1+l2, loc=2)
plt.title('NYC Precip. and Global Land Temp. Monthly Averages (1900-2021)', fontsize=16)
plt.savefig('Comparing_Monthly_PRCP_Land.png')
plt.show()
"""





# 3. Resources:
"""
Datasets:
(1) NOAA Daily Precipitation Levels for NYC: https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094728/detail
(2) NOAA Global Land Temperature: https://www.ncdc.noaa.gov/cag/global/time-series/globe/ocean/all/1/1900-2021

Other Links:
(3) https://towardsdatascience.com/getting-weather-data-in-3-easy-steps-8dc10cc5c859
(4) https://www.tutorialspoint.com/how-to-plot-two-pandas-time-series-on-the-same-plot-with-legends-and-secondary-y-axis-in-matplotlib
(5) https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
"""
