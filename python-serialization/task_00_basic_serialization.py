#!/usr/bin/python3

"""
Module that defines a serialization/deserialization function
"""

from os import path
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to a JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        serialization = json.dumps(data)
        file.write(serialization)


def load_from_file_and_deserialize(filename):
    """
    Deserializes data from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.loads(file.read())
    return data
