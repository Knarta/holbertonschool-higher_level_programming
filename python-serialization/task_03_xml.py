#!/usr/bin/python3

"""
Module that defines functions to serialize and deserialize data to/from XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(data, filename):
    """
    Serializes data to an XML file
    """
    root = ET.Element("data")
    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = value

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserializes data from an XML file
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
