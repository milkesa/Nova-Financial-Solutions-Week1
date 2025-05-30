# src/explore.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

STOCK_FILES = [
    "AAPL_historical_data.csv", "AMZN_historical_data.csv", "GOOG_historical_data.csv",
    "META_historical_data.csv", "MSFT_historical_data.csv", "NVDA_historical_data.csv",
    "TSLA_historical_data.csv"
]

def load_data(path):
    return pd.read_csv(path)

def explore_stock_data(file_path, output_dir="outputs/stocks"):
    os.makedirs(output_dir, exist_ok=True)
    df = load_data(file_path)
    stock_name = os.path.basename(file_path).split("_")[0]
    
    # Summary
    print(f"\n🟢 {stock_name} Summary:")
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.isnull().sum())
    
    # Price distribution
    if 'Close' in df.columns:
        plt.figure()
        sns.histplot(df['Close'], kde=True)
        plt.title(f"{stock_name} Closing Price Distribution")
        plt.savefig(f"{output_dir}/{stock_name}_close_dist.png")
        plt.close()

def explore_analyst_ratings(file_path, output_dir="outputs/ratings"):
    os.makedirs(output_dir, exist_ok=True)
    df = load_data(file_path)
    
    print("\n🟣 Analyst Ratings Summary:")
    print("Shape:", df.shape)
    print(df.dtypes)
    print(df.isnull().sum())
    print(df.describe(include='all'))
    
    if 'rating' in df.columns:
        plt.figure(figsize=(8,4))
        sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index)
        plt.title("Rating Counts")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"{output_dir}/rating_distribution.png")
        plt.close()

if __name__ == "__main__":
    raw_data_dir = "data/raw"

    for file in STOCK_FILES:
        explore_stock_data(os.path.join(raw_data_dir, file))

    explore_analyst_ratings(os.path.join(raw_data_dir, "raw_analyst_ratings.csv"))
