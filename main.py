from random import choice
from string import ascii_letters as A_Z
import csv

CONDITION = [ "AR", "SV", "OH", "RD", "NS", "NE", "FN"]

def random_string(num):
    return_str = ""
    for _ in range(num):
        return_str += choice(A_Z)
    return return_str

for _ in range(100000):
    part = {
        "part number": random_string(10),
        "serial number": random_string(10),
        "description": random_string(200),
        "condition": choice(CONDITION),
        "quantity": 1,
        "price": 0
    }
    with open("andres.csv", "a") as csv_file:
        fieldnames = ["part number", "serial number", "description", "condition", "quantity", "price"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow(part)
