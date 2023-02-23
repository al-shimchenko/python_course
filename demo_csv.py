"""
CSV: comma separated value
"""

import csv

CARS_CSV_FILE = "cars.csv"
BIRTH_MONTHS_CSV_FILE = "birth_months.csv"


def read_csv_cars():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.reader(f, delimiter=",")

        for line in csv_reader:
            print(line)
            print(line[1], line[4])


def read_csv_as_dict():
    with open(CARS_CSV_FILE) as f:
        csv_reader = csv.DictReader(f, delimiter=",")

        print("headers:", csv_reader.fieldnames)  # all readers in list

        for row in csv_reader:  # print lines as dicts
            # print(row)
            print(row["Model"], row["Price"])  # print by keys


def write_csv_dict():
    NAME = "name"
    MONTH = "birth_month"
    DEPARTMENT = "department"
    fieldnames = [NAME, MONTH, DEPARTMENT]
    with open(BIRTH_MONTHS_CSV_FILE, 'w') as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()  # write the line with keys

        row = {
            NAME: "Sam",
            MONTH: "Jan",
            DEPARTMENT: "IT",
        }
        csv_writer.writerow(row)

        row2 = {
            NAME: "Kate",
            MONTH: "Mar",
            DEPARTMENT: "Accounting",
        }
        row3 = {
            NAME: "Jack",
            MONTH: "May",
            DEPARTMENT: "HelpDesk",
        }
        rows = [row2, row3]
        csv_writer.writerows(rows)


def main():
    # read_csv_cars()
    # read_csv_as_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
