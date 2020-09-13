import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

with open(cereal_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    headers = next(csv_reader)
    print(headers)

    for x in csv_reader:
        fiber = x[7]
        print(float(fiber), type(float(fiber)))
        # if float(fiber) >= 5:
        #     print(row)