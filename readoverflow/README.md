# ETL Process

According to [Stackoverflow Dataset](https://www.kaggle.com/stackoverflow/stackoverflow), we can use BigQuery API to get data. Stackoverflow's data is bigdata, we might not be able to process all data, so limit is provided to limit rows will be fetched. [read_stackoverlow.py](./read_stackoverflow.py) will read data into a folder by given limit.

![stackoverflow ETL process](./stackoveflow.png "stackoverflow.tfl")