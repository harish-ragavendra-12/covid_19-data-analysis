import pandas as pd
import matplotlib.pyplot as plt

#Load data
patients = pd.read_csv("../data/covid_data.csv")

#clean column names
patients.columns = patients.columns.str.replace("\r\n", " ", regex=True)
print(patients.columns)

print("Dataset:\n")
print(patients.head())

print("\nDataset Info")
patients.info()

#Convert text columns into numeric
columns = [
    "Total Cases",
    "Total Deaths",
    "Total Recovered",
    "Active Cases",
    "Population"
]

for col in columns:
    patients[col] = (
        patients[col]
        .str.replace(",", "",regex=False)
    )

    patients[col] = pd.to_numeric(
        patients[col],
        errors="coerce"
    )

print("\nMissing Values")
print(patients.isnull().sum())

print("\nStatistics")
print(patients.describe())

#Cases by Country
top_cases = patients.sort_values(by="Total Cases",ascending=False).head(10)

plt.figure(figsize=(10,5))

plt.bar(
    top_cases["Country, Other"],
    top_cases["Total Cases"]
)

plt.xticks(rotation=45)

plt.title("Top 10 Countries by Total Cases")

plt.xlabel("Country")

plt.ylabel("Cases")

plt.tight_layout()

plt.savefig("../visuals/cases_by_country.png")

plt.show()

#Death Rate Analysis
patients["Death Rate"] = (
    patients["Total Deaths"] /
    patients["Total Cases"]
) * 100


top_death = patients.sort_values(
    by="Death Rate",
    ascending=False
).head(10)


plt.figure(figsize=(10,5))

plt.bar(
    top_death["Country, Other"],
    top_death["Death Rate"]
)

plt.xticks(rotation=45)

plt.title("Top Death Rate Countries")

plt.ylabel("Death Rate %")

plt.tight_layout()

plt.savefig("../visuals/death_rate.png")

plt.show()

#Trends over Time
top_trend = patients.head(10)

plt.figure(figsize=(10,5))

plt.plot(
    top_trend["Country, Other"],
    top_trend["Total Cases"],
    label="Cases"
)

plt.plot(
    top_trend["Country, Other"],
    top_trend["Total Recovered"],
    label="Recovered"
)

plt.xticks(rotation=45)

plt.legend()

plt.title("Cases vs Recovery Trend")

plt.tight_layout()

plt.savefig("../visuals/trends.png")

plt.show()

#Top affected country
top_affected = patients.loc[
    patients["Total Cases"].idxmax()
]

print("\nTop affected country:\n")

print(
    top_affected[
        ["Country, Other","Total Cases"]
    ]
)