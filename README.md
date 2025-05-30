# Nova-Financial-Solutions-Week1

# Week 1 Challenge: Predicting Price Moves with News Sentiment

## Overview
This project analyzes financial news headlines to explore their impact on stock prices using NLP, TA-Lib, and PyNance.

## Tasks
- EDA & Stats (Task 1)
- Technical Indicators (Task 2)
- Sentiment-Return Correlation (Task 3)

## Folder Structure
See the project structure for organized source, notebooks, tests, and scripts.

Nova-Financial-Solutions-Week1/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
│   ├── __init__.py
│   └── data_processing.py         # data cleaning, feature engineering
│   └── sentiment_analysis.py      # sentiment scoring
│   └── correlation_analysis.py    # correlation computation
├── notebooks/
│   ├── __init__.py
│   └── eda.ipynb                  # EDA and data understanding
│   └── indicators.ipynb          # Technical analysis
│   └── sentiment.ipynb           # NLP-based sentiment work
├── tests/
│   ├── __init__.py
│   └── test_data_processing.py
│   └── test_sentiment_analysis.py
├── scripts/
│   ├── __init__.py
│   └── run_all.py                # master script to run everything
