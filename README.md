# pyspark-sql-df
NYC TLC Trips [Records](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) February 2021 analysis using PySpark SQL and Dataframe.

## Info:
1. `docker compose up` on terminal (Assure you have docker installed).
2. Wait till you see something like this texts:
```
jupyter-spark  |     To access the server, open this file in a browser:
jupyter-spark  |         file:///home/jovyan/.local/share/jupyter/runtime/jpserver-8-open.html
jupyter-spark  |     Or copy and paste one of these URLs:
jupyter-spark  |         http://45857a074e0b:8888/lab?token=<AUTO_GENERATE_TOKEN_TO_ACCESS_THE_SERVER>
jupyter-spark  |      or http://127.0.0.1:8888/lab?token=<AUTO_GENERATE_TOKEN_TO_ACCESS_THE_SERVER>
```
3. Click that link on the terminal (_**http<nolink>://127.0.0.1:8888/lab**_ <-- I recommend you to choose the last one).
4. Go to **work** folder (click on the left pane).
5. Open the **trip_spark.ipynb** file there. Congrats! You are settled.

## For Upload to BigQuery:
* [spark/resources/jars](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) (Download the file and put it there, only if using the second of direct way - BQ Connector).
* [.google](https://github.com/zeenfts/pyspark-sql-df/tree/main/.google) <-- **creds.json** (For GCP BQ Permission).