# Changes in Precipitation Levels in NYC and Its Correlation With Land/Ocean Temperatures as Global Indicators of Climate Change
<p align="center">
  <img src="https://static01.nyt.com/images/2021/08/07/us/07xp-elsalandfall-2/07xp-elsalandfall-2-superJumbo.jpg" />
</p>

### Overview:
Studies indicate that extreme weather conditions are likely to become more frequent with the global rise in climate change. Given the recent heavy rainfall we have experienced in NYC over the summer, the purpose of this project is to explore whether or not these changes in NYC's precipitation levels show any observable correlations with global land temperature changes from 1900 to 2021. My underlying hypothesis was that the frequency of precipitation in New York would not show any observable increase on an annual basis, but more on a seasonal basis. In order to prove this hypothesis, I applied various time-series analysis/plotting techniques on my datasets.


### Data:
Both of the datasets used for this project are from the National Oceanic and Atmospheric Administration (NOAA).
- **[Daily NYC Precipitation (1900-2021)](https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/stations/GHCND:USW00094728/detail)**: Contains daily precipitation values taken from the NYC Central Park weather station. The weather station provides records starting from 1869, however, for this project only the records starting from 1900 were used. Precipitation values are measured in millimeters (mm.). The base value of 32mm. is used instead of 0mm., even for days with no rainfall (dataset documentation does not specify why). In order to access and downlaod this dataset, the [NOAA API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) has to be utilized. 

- **[Monthly Global Land Temperature (1900-2021)](https://www.ncdc.noaa.gov/cag/global/time-series/globe/ocean/all/1/1900-2021)**: Contains monthly global land temperature values from 1900 to 2021. **The temperature values are based on land temperature** ***anomalies*** (i.e. a description of how the overall average temperature of the surface of the Earth deviates from what is expected) with the base periods being 1901-2000. This dataset is available for direct download. 

### Technique:
- #### Part 1: Retrieving and Cleaning Datasets
  - For retrieving the NYC precipitation dataset, I first had to generate an API key and then choose a weather station ID (GHCND:USW00094728) from the NOAA website. Then I had to make a JSON API call using the key and station ID to download and save the data as a CSV file. The data download portion took a while since I was working with a large time frame. The global land temperature dataset was directly downloadable as a CSV file. 
  - For cleaning the datasets, the datetime module was mainly utilized. 
- #### Part 2: Combining Datasets 
  - Although both of the datasets used the same year range (1900-2021), the precipitation dataset gave **daily measurements** while the land temperature dataset gave **monthly average measurements**. In order to ensure this would not be a problem when combining the datasets, I had to make a seperate dataframe of monthly precipitation averages. 
  - The land temperature and new monthly precipitation datasets were then merged using an inner join based on their values of month and year and saved to a new combined dataframe.
- #### Part 3: Data Analysis/Visualization
  - See **[Analysis](#analysis)**

### Analysis:
(coming soon)

![image](https://raw.githubusercontent.com/Saida0/Data-Science-Project/main/PRCP_Daily.png)

![image](https://raw.githubusercontent.com/Saida0/Data-Science-Project/main/PRCP_Monthly.png)

![image](https://raw.githubusercontent.com/Saida0/Data-Science-Project/main/Land_Temp_Monthly.png)

![image](https://raw.githubusercontent.com/Saida0/Data-Science-Project/main/Comparing_Monthly_PRCP_Land.png)

### Conclusion:
- #### What were the results? Was my hypothesis correct?
- #### What would I have done differently?







