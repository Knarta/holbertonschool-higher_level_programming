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
    with open(filename, "w") as f:
        json.dump(data, f)


def load_from_file_and_deserialize(filename):
    """
    Deserializes a JSON file
    """
    with open(filename, "r") as f:
        return json.loadf
