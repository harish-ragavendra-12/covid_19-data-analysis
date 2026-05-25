# COVID-19 Data Analysis Project

A beginner-friendly Data Science project that performs Exploratory Data Analysis (EDA) on COVID-19 data using Python, Pandas, and Matplotlib.

This project cleans real-world COVID dataset data, performs statistical analysis, identifies top affected countries, calculates death rates, and visualizes insights through charts.

---

## Project Objectives

The main goals of this project are:

- Load and analyze COVID-19 dataset
- Clean messy column names and data values
- Handle missing values
- Convert text columns into numeric format
- Analyze total cases and deaths
- Calculate death rate percentages
- Identify top affected countries
- Create visualizations for better understanding

---

## Dataset Features

The dataset contains information such as:

- Country
- Total Cases
- Total Deaths
- Total Recovered
- Active Cases
- Population

---

## Technologies Used

- Python
- Pandas
- Matplotlib

---

## Project Structure

```text
covid-data-analysis/
│
├── data/
│   └── covid_data.csv
│
├── src/
│   └── covid_analysis.py
│
├── visuals/
│   ├── cases_by_country.png
│   ├── death_rate.png
│   └── trends.png
│
├── requirements.txt
└── README.md
```

---

## Data Cleaning Steps

The following preprocessing steps were performed:

### Cleaned column names

Removed unwanted line breaks:

```python
patients.columns = patients.columns.str.replace(
    "\r\n|\n",
    " ",
    regex=True
)
```

### Converted text values into numeric format

Removed commas and converted values:

```python
patients[col] = (
    patients[col]
    .str.replace(",", "")
)

patients[col] = pd.to_numeric(
    patients[col],
    errors="coerce"
)
```

---

## Exploratory Data Analysis Performed

### 1. Dataset Information

- Displayed dataset preview
- Checked column types
- Identified missing values
- Generated summary statistics

### 2. Cases by Country Analysis

Analyzed countries with the highest number of COVID cases.

Visualization:

- Bar chart of Top 10 countries by total cases

---

### 3. Death Rate Analysis

Created a new feature:

```python
Death Rate =
(Total Deaths / Total Cases) * 100
```

Visualization:

- Top countries with highest death rates

---

### 4. Trend Analysis

Compared:

- Total Cases
- Total Recovered

Visualization:

- Line chart comparison

---

### 5. Top Affected Country

Identified the country with maximum total cases using:

```python
idxmax()
```

---

## Visualizations Generated

### Cases by Country

Shows top affected countries by total cases.

### Death Rate Analysis

Displays countries with highest death percentages.

### Cases vs Recovery Trend

Compares total cases and recoveries.

---

## Concepts Learned

This project covers:

- Exploratory Data Analysis (EDA)
- Data Cleaning
- Missing Value Analysis
- Data Type Conversion
- Feature Engineering
- Correlation of metrics
- Statistical Analysis
- Data Visualization
- Working with real-world datasets
- Project organization

---

## How to Run

Clone repository:

```bash
git clone https://github.com/harish-ragavendra-12/covid_19-data-analysis.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/covid_analysis.py
```

---

## Future Improvements

- Add heatmap visualization
- Add time-series COVID trends
- Build dashboard using Plotly
- Create machine learning prediction model
- Deploy as web app

---

## Author

Harish Ragavendra
