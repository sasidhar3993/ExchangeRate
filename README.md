# Exchange Rate Analysis

This script retrieves historical exchange rate data between AUD (Australian Dollar) and NZD (New Zealand Dollar) for the last 30 days, analyzes it, and prints out some key metrics.

## Prerequisites
- Python 3.x
- Pandas

## Installation
1. Clone or download the repository.
2. Install the required dependencies using pip: Pandas
3. Alternatively you can run this code from Juypter note book or Jupyterlab in git hub codespaces


## Usage
1. `conf/confi.ini` file is store base url of exchange rates api and access key(use your own access key if required)

![alt text](data/images/image.png)

2. `conf/properties.yaml` is to segregate different api call based on latest , historical , timeseries and takes api id 

![alt text](data/images/image-1.png)

3. Run the script `src/rate_mertics.py`.(Main function currently confgiured to run only historical fetches) 
4. The script will:
  - Fetch historical exchange rate data for the last 30 days.
  - Analyze the data to find:
  - Best conversion ratio and its corresponding date.
  - Worst conversion ratio and its corresponding date.
  - Average conversion ratio.
- Print out the analysis results.
## Script Overview
- `get_30d_data()`: Fetches historical exchange rate data for the last 30 days.
- `transform_data(data)`: Transforms the fetched data into a pandas DataFrame and calculates the AUD to NZD conversion ratio.
- `main()`: Main function that orchestrates the data retrieval, transformation, analysis, and printing.

5. Script `src/exchagerate_api.py` Initialize an instance of BaseAPI with your API ID ex:LATEST_API,HISTORICAL_API and optional parameters.
  - Call the appropriate methods to fetch exchange rate data:
## Script Overview
  - get_latest(): Fetches the latest exchange rates.
  - get_hist(hist_date): Fetches historical exchange rates for the specified date.
  - get_time_series(start_date, end_date): Fetches time series data within the specified date range.

## Running the Script
```bash
python rate_metrics.py
```


## Output
![alt text](data/images/image-2.png)

