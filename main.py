import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
from pandas import to_datetime


#Fetch data from World Bank API
def get_world_bank_data(indicator, country_code, start_year, end_year):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator}?date={start_year}:{end_year}&format=json"
    response = requests.get(url)
    data = response.json()[1]  # Data is in the second part of the response

    # Extract relevant data into a dataframe
    df = pd.DataFrame(data)
    return df[['date', 'value']].rename(columns={'date': 'year', 'value': indicator})

# Get GDP and Inflation data for United States (USA) (I will add more in the future)
df_gdp = get_world_bank_data('NY.GDP.MKTP.CD', 'USA', 2000, 2025)
df_inflation = get_world_bank_data('FP.CPI.TOTL.ZG', 'USA', 2000, 2025)

# Merge dataframes on 'year'
df_combined = pd.merge(df_gdp, df_inflation, on='year')

# Data Processing/Tansformation (Handling Missing Values and Normalization)
# Handling missing values - drop rows with missing data
df_combined = df_combined.dropna()

# Normalize GDP and Inflation values
scaler = MinMaxScaler()
df_combined[['NY.GDP.MKTP.CD', 'FP.CPI.TOTL.ZG']] = scaler.fit_transform(
    df_combined[['NY.GDP.MKTP.CD', 'FP.CPI.TOTL.ZG']])

# Exploratory Data Analysis (EDA)
# Correlation heatmap
corr = df_combined.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Economic Indicators')
plt.show()

# Visualizing Trends - Plot GDP and Inflation over time
plt.figure(figsize=(10, 5))
plt.plot(df_combined['year'], df_combined['NY.GDP.MKTP.CD'], label='GDP', color='b')
plt.plot(df_combined['year'], df_combined['FP.CPI.TOTL.ZG'], label='Inflation Rate', color='r')
plt.xlabel('Year')
plt.ylabel('Normalized Value')
plt.title('GDP and Inflation Over Time (Normalized)')
plt.legend()
plt.show()

##########################################    Forecasting using ARIMA for GDP      ###############################################
# Convert 'year' to datetime
df_combined['year'] = pd.to_datetime(df_combined['year'], format='%Y')
df_combined.set_index('year', inplace=True)

# ARIMA model for forecasting GDP (assuming stationary data)
model = ARIMA(df_combined['NY.GDP.MKTP.CD'], order=(5, 1, 0))  # Adjust order for ARIMA
model_fit = model.fit()

# Forecasting the next 5 years
forecast = model_fit.forecast(steps=5)
print("Forecasted GDP for next 5 years:")
print(forecast)

# Linear Regression to Analyze Relationship between GDP and Inflation
X = df_combined[['FP.CPI.TOTL.ZG']]  # Predictor: Inflation
y = df_combined['NY.GDP.MKTP.CD']  # Response: GDP

# Linear regression model
lin_reg_model = LinearRegression()
lin_reg_model.fit(X, y)

# Predict GDP based on Inflation
df_combined['predicted_gdp'] = lin_reg_model.predict(X)

# Plot Predicted GDP vs Actual GDP
plt.figure(figsize=(10, 5))
plt.plot(df_combined.index, df_combined['NY.GDP.MKTP.CD'], label='Actual GDP', color='b')
plt.plot(df_combined.index, df_combined['predicted_gdp'], label='Predicted GDP', color='g', linestyle='--')
plt.xlabel('Year')
plt.ylabel('Normalized GDP')
plt.title('Actual vs Predicted GDP based on Inflation')
plt.legend()
plt.show()

# Alert if inflation exceeds a certain threshold (e.g., 10% inflation)
inflation_threshold = 0.10  # 10% inflation threshold after normalization
high_inflation_years = df_combined[df_combined['FP.CPI.TOTL.ZG'] > inflation_threshold]

# Print years where inflation exceeded the threshold
if not high_inflation_years.empty:
    print("High inflation years (greater than 10%):")
    print(high_inflation_years[['year', 'FP.CPI.TOTL.ZG']])
else:
    print("No years with inflation greater than 10%.")
