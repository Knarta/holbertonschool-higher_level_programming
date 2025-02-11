#!/usr/bin/python3
"""
Module that defines a function to convert a CSV file to a JSON file
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Converts a CSV file to a JSON file
    """
    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open("data.json", "w") as file:
            json.dump(data, file)

            return True

    except FileNotFoundError:
        print("File not found")
        return False
