import argparse
import sys

import pandas as pd
from datetime import datetime, timedelta

from exchangerate_api import BaseAPI


def get_30d_data(conf_path):
    yesterday = datetime.now().date() - timedelta(days=1)
   
    last_30data = []
   # Generate a list of the last 30 days
    last_30_days = [(yesterday - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(2)]
    for dt in last_30_days:
        api = BaseAPI('HISTORICAL_API',conf_path, dt)
        data = api.get_hist()
        last_30data.append(data)

    return last_30data


def transform_data(data):
    df = pd.DataFrame(data)

    df['aud_rate'] = df['rates'].apply(lambda x: x['AUD'])
    df['nzd_rate'] = df['rates'].apply(lambda x: x['NZD'])
    
    df.drop('rates', axis=1, inplace=True)
    df = df[['date', 'aud_rate', 'nzd_rate']]
    df['aud_to_nzd'] = df['nzd_rate'] / df['aud_rate']

    return df


def main():

    conf_path = sys.argv[1]
    print(conf_path)

    data = get_30d_data(conf_path)
    df = transform_data(data)

    # Best conversion rate
    best_ratio_index = df['aud_to_nzd'].idxmax()
    best_date = df.loc[best_ratio_index, 'date']
    best_ratio = df.loc[best_ratio_index, 'aud_to_nzd']
    best_ratio_rounded = round(best_ratio, 5)
    print(f"Best conversion ratio is :: {best_ratio_rounded} on date :: {best_date}")

    # Worst conversion rate
    min_ratio_index = df['aud_to_nzd'].idxmin()
    min_date = df.loc[min_ratio_index, 'date']
    min_ratio = df.loc[min_ratio_index, 'aud_to_nzd']
    min_ratio_rounded = round(min_ratio, 5)
    print(f"Worst conversion ratio is :: {min_ratio_rounded} on date :: {min_date}")

    # Average rate
    average_ratio = df['aud_to_nzd'].mean()
    avg_ratio_rounded = round(average_ratio, 5)
    print("Average AUD to NZD Ratio:", avg_ratio_rounded)


# # Main function call
# if __name__ == "main":
main()