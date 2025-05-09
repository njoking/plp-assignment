import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


df = pd.read_csv("owid-covid-data.csv")
df['date'] = pd.to_datetime(df['date'])

df['death_rate'] = df['total_deaths'] / df['total_cases']



plt.style.use('ggplot')


print("\n📌 Column Names:")
print(df.columns)


print("\n🔍 First 5 Rows:")
print(df.head())


print("\n🚨 Missing Values per Column:")
print(df.isnull().sum())


countries = ['South Africa', 'United Kingdom', 'Australia']
df = df[df['location'].isin(countries)]


df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])


numeric_cols = df.select_dtypes(include='number').columns
df[numeric_cols] = df[numeric_cols].interpolate()


print("\n✅ Cleaned Data Preview:")
print(df.head())

print("\n📏 Remaining Missing Values:")
print(df.isnull().sum())

plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_cases'], label=country)

plt.title('📈 Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['total_deaths'], label=country)

plt.title('☠️ Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['new_cases'], label=country)

plt.title('🦠 Daily New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countries:
    country_df = df[df['location'] == country]
    plt.plot(country_df['date'], country_df['death_rate'], label=country)

plt.title('📉 COVID-19 Death Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.legend()
plt.tight_layout()
plt.show()


latest = df[df['date'] == df['date'].max()]
corr = latest.select_dtypes('number').corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('📊 Correlation Matrix (Latest Data)')
plt.tight_layout()
plt.show()

countries = ['South Africa', 'United Kingdom', 'Australia']
vaccine_df = df[df['location'].isin(countries)][['date', 'location', 'total_vaccinations', 'people_fully_vaccinated_per_hundred']]

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = vaccine_df[vaccine_df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.tight_layout()
plt.show()

latest_date = df['date'].max()
latest_vax = df[df['date'] == latest_date]
vax_percent = latest_vax[latest_vax['location'].isin(countries)]

plt.figure(figsize=(8, 5))
sns.barplot(data=vax_percent, x='location', y='people_fully_vaccinated_per_hundred')
plt.title('People Fully Vaccinated (% of Population)')
plt.ylabel('Percentage')
plt.tight_layout()
plt.show()

import plotly.express as px

latest = df[df['date'] == df['date'].max()]
choropleth_df = latest[['iso_code', 'location', 'total_vaccinations']].dropna()

fig = px.choropleth(
    data_frame=choropleth_df,
    locations="iso_code",
    color="total_vaccinations",
    hover_name="location",
    color_continuous_scale="Viridis",
    title="Global Total COVID-19 Vaccinations"
)

fig.show()
