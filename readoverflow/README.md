# ETL Process

According to [Stackoverflow Dataset](https://www.kaggle.com/stackoverflow/stackoverflow), we can use BigQuery API to get data. Stackoverflow's data is bigdata, we might not be able to process all data, so limit is provided to limit rows will be fetched. [read_stackoverlow.py](./read_stackoverflow.py) will read data into a folder by given limit.

![stackoverflow ETL process](./stackoverflow.png "stackoverflow.tfl")

Pre-processing includes

* Import data to Tableau Prep, change all date time type and remove most of null value
* Convert id as string
* Split tags into multiple keywords
* Group posts by different keywords