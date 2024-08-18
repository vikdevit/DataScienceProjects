# JapTokElecIbp - a program that imports, explores, cleans and analyzes data
# of electricity market in Tokyo region across 2022-2024 from a csv file
# giving imbalance prices in Japanese electricity market.
# Source : https://www.kaggle.com/datasets/mitsuyasuhoshino/japan-imbalance-prices
# Date : Monday 12 August 2024
#
# Importing, exploring and cleaning data with pandas
#
import pandas as pd
#
# Loading the dataset
#
column_names = ['date','time_code','Hokkaido_ibprice','Tohoku_ibprice','Tokyo_ibprice',
                'Chubu_ibprice','Hokuriku_ibprice','Kansai_ibprice','Chugoku_ibprice',
                'Shikoku_ibprice','Kyushu_ibprice']
#
# Importing imbalance prices of Japanese electricity market, creating dataframe and displaying the first five rows.
#
jap_ibp_data = pd.read_csv(r"C:\Users\vkhat\OneDrive\Documents\DataProjects\Electricity\Japan_ImbalancePrice2.csv", sep=',', names = column_names,
                           parse_dates= None,date_format={'date':'%Y-%m-%d'},header = 0)
#
## Converting date column to datetime using pd.to_datetime
#
jap_ibp_data['date'] = pd.to_datetime(jap_ibp_data['date'])
#
## Creating dataframe with all data
#
df_jap_ibp_data = pd.DataFrame(jap_ibp_data)
print(df_jap_ibp_data.head())
#
# Exploring the dataset
#
## Getting overall structure
#
print(df_jap_ibp_data.info())
#
## Generating descriptive statistics
#
## Creating a second dataframe that contains subset of imbalance prices' columns
#
dfstat_jap_ibp_data = pd.DataFrame(df_jap_ibp_data,columns=['Hokkaido_ibprice','Tohoku_ibprice',
                                                            'Tokyo_ibprice','Chubu_ibprice',
                                                            'Hokuriku_ibprice','Kansai_ibprice',
                                                            'Chugoku_ibprice','Shikoku_ibprice',
                                                            'Kyushu_ibprice'])
#
## Generating descriptive statistics for these columns
#
print(dfstat_jap_ibp_data.describe())
#
# Cleaning the dataset
#
## Identifying and removing duplicate records, if needed
#
## Identifying duplicates
#
print("Number of duplicates: ",df_jap_ibp_data.duplicated().sum())
#
## Removing duplicates, if needed and resetting index in the dataframe
#
df_jap_ibp_data.drop_duplicates(inplace=True, ignore_index=True)
#
## Seeing if all duplicates have been successfully removed
#
print("Number of duplicates after removing redundant rows: ",df_jap_ibp_data.duplicated().sum())
#
# Using set_index method to assign the values of the date column to the index in the current dataframe.
# Date column is dropped to not duplicate dates.
#
df_jap_ibp_data.set_index("date",drop=True,inplace=True)
print(df_jap_ibp_data)
#
# Analyzing data with pandas, matplotlib and numpy
#
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
#
## Setting plot background
#
plt.style.use('bmh')
plt.grid(color='black',linestyle='--',alpha=0.3)
#
## Plotting electricity imbalance prices in Tokyo region from March 2022 to August 2024.
#
## Creating a new dataframe
#
tok_ibp_2203_2408 = df_jap_ibp_data["2022-03-01":"2024-08-01"]
#
## Creating figure and plot space
#
fig1, ax1 = plt.subplots(figsize=(22,12))
#
## Creating plot
#
ax1.plot(tok_ibp_2203_2408.index.values,
        tok_ibp_2203_2408['Tokyo_ibprice'],
        linewidth = 0.5,
        color ='r')
#
## Setting plot title and labels for x-axis and y-axis
#
ax1.set(xlabel="date",
       ylabel="imbalance price (Yen/kWh)",
       title= "Electricity market imbalance prices\n for Tokyo region across 2022-2024"
       )
#
## Defining the date format of x-axis
#
date_form = mdates.DateFormatter("%Y-%m-%d")
ax1.xaxis.set_major_formatter(date_form)
#
## Ensuring a major tick for each three-month period and aligning labels with their respective xticks
#
ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
plt.xticks(rotation=45,ha='right')
#
## Specifying the start and end of the labels.
#
ax1.set_xlim(np.datetime64("2022-03-01"),np.datetime64("2024-08-01"))
#
## Enabling end of program execution after creating plot.
#
plt.show(block=False)
#
## Saving plot to a file
#
file_name = "Tok_Ibp_032022_To_082024"
extension = ".png"
full_file_name = file_name + extension
plt.savefig(full_file_name)
#
## Creating a dataframe storing mean,std,min and max values of imbalance prices in Tokyo region for each month across 2022-2024
#
tok_ibp_destats = jap_ibp_data.groupby([jap_ibp_data['date'].dt.to_period('M')]).agg(({"Tokyo_ibprice":['mean','std','min','max']}))
print(tok_ibp_destats.head())
#
## Naming returned columns after using pandas aggregate function
#
tok_ibp_destats.columns = ["_".join(x) for x in tok_ibp_destats.columns.ravel()]
print(tok_ibp_destats.head())
#
## Creating a date column to store date frequencies from the index and convert them to date format
#
tok_ibp_destats["date"] = tok_ibp_destats.index
tok_ibp_destats["date"] = tok_ibp_destats.date.values.astype('datetime64[M]')
print(tok_ibp_destats.info())
#
## Creating figure and plot space
#
fig2,(ax1,ax2,ax3,ax4) = plt.subplots(4,1, figsize=(22,12))
fig2.suptitle('Descriptive statistics of imbalance prices\n for Tokyo region by month across 2022-2024')
#
ax1.plot(tok_ibp_destats["date"],tok_ibp_destats["Tokyo_ibprice_mean"],linewidth = 0.5,color ='b')
ax1.set_ylabel('Mean value (Yen/kWh)')
#
ax2.plot(tok_ibp_destats["date"],tok_ibp_destats["Tokyo_ibprice_std"],linewidth = 0.5,color ='b')
ax2.set_ylabel('Std value (Yen/kWh)')
#
ax3.plot(tok_ibp_destats["date"],tok_ibp_destats["Tokyo_ibprice_min"],linewidth = 0.5,color ='b')
ax3.set_ylabel('Min value (Yen/kWh)')
#
ax4.plot(tok_ibp_destats["date"],tok_ibp_destats["Tokyo_ibprice_max"],linewidth = 0.5,color ='b')
ax4.set_ylabel('Max value (Yen/kWh)')
ax4.set(xlabel="month")
#
## Enabling end of program execution after creating plot.
#
plt.show(block=False)
#
## Saving plot to a file
#
file_name = "Tok_Ibp_Destats_032022_To_082024"
extension = ".png"
full_file_name = file_name + extension
plt.savefig(full_file_name)
#
# END OF PROGRAM.