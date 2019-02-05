from google.cloud import bigquery
import sys
import csv
import os, errno

def get_data(client, dataset, table, limit):
    hn = client.get_table(dataset.table(table))

    # CSV file will be saved
    with open(f'{limit}/{table}.csv', 'w', newline='\n') as csvfile:
        head = []
        for sc in hn.schema:
            head.append(sc.name)
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(head)
        rows =[x for x in client.list_rows(hn, max_results=limit)]
        for r in rows:
            writer.writerow(r)

def main(argv):
    client = bigquery.Client()
    so_dataset_ref = client.dataset('stackoverflow', project='bigquery-public-data')
    limit = int(argv[1])

    # try to create folder by limit if it does not exist.
    try:
        os.makedirs(argv[1])
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    # get data
    for table in argv[2:]:
        get_data(client, so_dataset_ref, table, limit)

if __name__ == "__main__":
    main(sys.argv)