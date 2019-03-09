from google.cloud import bigquery
import sys
import csv
import os, errno


def get_users(client, query, query_params):
    job_config = bigquery.QueryJobConfig()
    job_config.query_parameters = query_params
    query_job = client.query(
        query,  # Location must match that of the dataset(s) referenced in the query.
        location='US',
        job_config=job_config)  # API request - starts the query
    for row in query_job:
        print('{}: \t{}'.format(row.name, row.count))


def main(argv):
    client = bigquery.Client()
    posts_answers = argv[1]

    owners = []
    posts = []
    with open(posts_answers, "rt") as postf:
        for line in postf:
            cols = line.split(",")
            try:
                owners.append(int(cols[2]))
                posts.append(int(cols[3]))
            except:
                continue

    print(owners)
    print(posts)
    print(len(posts))
    query = f"SELECT id, reputation, up_votes, down_votes, views FROM `bigquery-public-data.stackoverflow.users` WHERE id in ({owners})"
    query_params = [
        bigquery.ArrayQueryParameter(
            'ids', 'int', owners)
    ]
    get_users(client, query, query_params)


if __name__ == "__main__":
    main(sys.argv)
