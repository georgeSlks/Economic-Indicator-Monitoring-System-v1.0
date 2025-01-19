# Economic-Indicator-Monitoring-System

The first part of this project retrieves economic data from the World Bank API, performs data preprocessing, and analyzes the relationship between key economic indicators, such as GDP and Inflation Rate for the United States. It uses statistical models(ARIMA) and linear regression to explore, visualize, and forecast trends. 

The analyses include:  
**Exploratory Data Analysis (EDA):** Visualizing and analyzing correlations between GDP and Inflation.  
**Forecasting:** Using ARIMA to forecast future GDP values.  
**Regression Analysis:** Using Linear Regression to analyze the relationship between GDP and Inflation.  
**Inflation Alerts:** Identifying years where inflation exceeds a specified threshold.  

**Required Libraries**  
**requests:** For fetching data from the World Bank API.  
**pandas:** For data manipulation and handling.  
**seaborn:** For creating visualizations, such as heatmaps.  
**matplotlib.pyplot:** For generating additional visualizations.  
**statsmodels:** For the ARIMA model (used for time series forecasting).  
**sklearn:** For linear regression and data normalization.  

**Plots:**  
Correlation heatmap showing the relationship between GDP and Inflation.  
![GDP_INFLATION_HEATMAP_USA](https://github.com/user-attachments/assets/dc5e64f7-d8f1-4bbe-89f3-bccf2bd414bc)  

Time series plot of normalized GDP and Inflation values over time.  
![GDP_INFLATION_graph_USA](https://github.com/user-attachments/assets/e45073f4-2049-4158-9f88-45868f4ed0bd)  

Actual vs. Predicted GDP plot based on Linear Regression.    
![ActualVSPredoctiveGDP](https://github.com/user-attachments/assets/2f9733a7-59f3-4438-91cc-6bd7bad9994b)

