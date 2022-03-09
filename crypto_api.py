import requests
import json
import pandas as pd
import pandas_datareader.data as web
import csv
import pickle
# matplotlib or pylab for graph
# numpy too?

#####################################
### connect to sample crypto APIs ###
#####################################

# aapl.csv us some sample price data I've downloaded. Saved as pickle and CSV, also uploaded those
# general framework for working with historical data

pd.set_option('display.max.columns', None)
pd.set_option('display.precision', 2)

def getAPIdata(url):
    """Connect to API and retrieve JSON data. Convert to pandas DF."""
    json_data = requests.get(url).json()
    df = pd.DataFrame.from_dict(json_data)
    return df

def csv_to_df(csv_file):
    """Convert CSV file to Pandas dataframe."""
    df = pd.read_csv(csv_file)
    return df

def getLastDays(df, days):
    """Get last num of days' data"""
    return df.tail(days)

# aapl_df = csv_to_df('aapl.csv')  # loaded from CSV, don't need now since data is pickled
def readPickle(file_name):
    """Read file and return. Why doesn't the exception handling work?"""
    return pd.read_pickle(file_name)
    # except FileNotFoundError:
    #     print('Specified file path not found.')
    # else:
    #     return df

def test():
    ### AAPL DATAFRAME STORED IN PICKLE
    aapl_df = readPickle('aapl.pkl')
    print('* entire dataframe *')
    print(aapl_df)
    print()
    print('* last 7 days data *')
    last_7 = getLastDays(aapl_df, 7)
    print(last_7)
    print()
    print(f'* dataframe.info() *')
    print(aapl_df.info())
    print()
    print(f'* dataframe.describe() *')
    print(aapl_df.describe())
    ### track historical close data column
    ### plot graph

test()
