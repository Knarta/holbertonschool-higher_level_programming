#!/usr/bin/python3

"""
Module that defines a serialization/deserialization function
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes data to a JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Deserializes data from a JSON file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
