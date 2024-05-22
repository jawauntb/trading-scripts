import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define base folder
folder = "/Users/jawaun/llm_fine_tuning/may21data/nvda_4_timescales_5_21"

# Define files and their properties
files = [
    {"filename": "NASDAQ_NVDA, 60_30245.csv", "timescale": "60",
        "title": "60-Minute Data", "abbreviation": "60m"},
    {"filename": "NASDAQ_NVDA, 30_b7e42.csv", "timescale": "30",
        "title": "30-Minute Data", "abbreviation": "30m"},
    {"filename": "NASDAQ_NVDA, 15_98832.csv", "timescale": "15",
        "title": "15-Minute Data", "abbreviation": "15m"},
    {"filename": "NASDAQ_NVDA, 5_67294.csv", "timescale": "5",
        "title": "5-Minute Data", "abbreviation": "5m"},
]

# Function to load and clean data


def load_and_clean_data(filepath):
    data = pd.read_csv(filepath)
    data_cleaned = data.dropna(axis=1, how='all')
    data_cleaned = data_cleaned.loc[:, (data_cleaned != 0).any(axis=0)]
    data_cleaned.fillna(method='ffill', inplace=True)
    data_cleaned.fillna(method='bfill', inplace=True)
    data_cleaned['datetime'] = pd.to_datetime(
        data_cleaned['time'], unit='s', utc=True).dt.tz_convert('US/Eastern')
    return data_cleaned


# Load and clean all datasets
datasets = {}
for file in files:
    filepath = folder + '/' + file["filename"]
    datasets[file["abbreviation"]] = load_and_clean_data(filepath)
    print(f"Cleaned and Timestamp-Converted {file['title']}:")
    print(datasets[file["abbreviation"]].head())

# Calculate and save summary statistics for each dataset
for file in files:
    abbreviation = file["abbreviation"]
    summary = datasets[abbreviation].describe()
    summary.to_csv(
        folder + f'/NVDA_{abbreviation}_summary_statistics_final.csv')

# Function to plot time series data
def plot_time_series(data, title, filename):
    plt.figure(figsize=(14, 7))
    plt.plot(data['datetime'], data['open'], label='Open')
    plt.plot(data['datetime'], data['high'], label='High')
    plt.plot(data['datetime'], data['low'], label='Low')
    plt.plot(data['datetime'], data['close'], label='Close')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.show()


# Plot and save time series for each dataset
for file in files:
    abbreviation = file["abbreviation"]
    plot_time_series(
        datasets[abbreviation], f'NVDA {file["title"]}', folder + f'/NVDA_{abbreviation}_time_series.png')

# Calculate and save the correlation matrix for each dataset
correlation_matrices = {}
for file in files:
    abbreviation = file["abbreviation"]
    corr_matrix = datasets[abbreviation].corr()
    correlation_matrices[abbreviation] = corr_matrix
    plt.figure(figsize=(16, 12))
    sns.heatmap(corr_matrix, cmap='coolwarm', annot=False, fmt=".2f")
    plt.title(f'Correlation Matrix - NVDA {file["title"]}')
    plt.savefig(folder + f'/NVDA_{abbreviation}_correlation_matrix.png')
    plt.show()
    corr_matrix.to_csv(
        folder + f'/NVDA_{abbreviation}_correlation_matrix_final.csv')

# Compare correlations across different timeframes
correlation_comparison = pd.DataFrame(
    {abbr: corr['close'] for abbr, corr in correlation_matrices.items()})
print(correlation_comparison)
correlation_comparison.to_csv(folder + '/NVDA_comparison_of_correlations.csv')


