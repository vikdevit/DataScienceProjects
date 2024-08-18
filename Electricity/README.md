# 1-Project overview
This project aims to plot imbalance prices of Japanese electricity market using data store in a CSV file.
After cleaning and exploring data, dataframes will be created to get :

- Imbalance prices for Tokyo region across 2022-2024 period
- Descriptive statistics for the same region and period

This repository contains the whole script written in Python as well as graphs obtained when running the program and giving aforementioned information.
File names of the script and graphs are listed below:
- JapTokElecIbp.py
- Tok_Ibp_032022_To_082024 for imbalance prices
- Tok_Ibp_Destats_032022_To_082024 for descriptive statistics

# 2-Data source
CSV file was downloaded from Kaggle website and can be obtained using the url below:
https://www.kaggle.com/datasets/mitsuyasuhoshino/japan-imbalance-prices

# 3-Cleaning, exploring and analyzing data
Pandas library has been used to remove duplicate rows and make sure that data formats -especially dates- are appropriate.

Matplotlib library has also been imported to create figures and graphs.

# 4-What can be done to go further in data exploration ?
Data source provides imbalance prices for each region in Japan from the north to the south.

Therefore comparisons can be drawn between regions.

In addition, we can compute daily statistics and look for correlation existence to figure out possible role played  by seasonality. 

