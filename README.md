# Economic-Indicator-Monitoring-System

This Python project retrieves economic data from the World Bank API, performs data preprocessing, and analyzes the relationship between key economic indicators, such as GDP and Inflation Rate for the United States. It uses statistical and machine learning models to explore, visualize, and forecast trends. 

The analyses include:
Exploratory Data Analysis (EDA): Visualizing and analyzing correlations between GDP and Inflation.
**Forecasting:** Using ARIMA to forecast future GDP values.
Regression Analysis: Using Linear Regression to analyze the relationship between GDP and Inflation.
Inflation Alerts: Identifying years where inflation exceeds a specified threshold.
Required Libraries
The following libraries are used in the script:

requests: For fetching data from the World Bank API.
pandas: For data manipulation and handling.
seaborn: For creating visualizations, such as heatmaps.
matplotlib.pyplot: For generating additional visualizations.
statsmodels: For the ARIMA model (used for time series forecasting).
sklearn: For linear regression and data normalization.
