from csv import DictReader

with open("demolist.csv", 'r') as f:
    list_of_dict = list(DictReader(f))
    print(list_of_dict)