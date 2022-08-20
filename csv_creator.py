
import csv


def create_csv(data: dict, csv_name: str):

    csv_file = f"{csv_name}.csv"

    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(data.keys())
        writer.writerow(data.items())

    return
