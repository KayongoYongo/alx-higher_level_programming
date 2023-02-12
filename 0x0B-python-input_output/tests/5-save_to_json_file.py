#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """An function that writes an object to a text file,
    using json representation.
    """
    with open(filename, 'w+', encoding='utf-8') as f:
        """We use dump to serialize the object to a text file"""
        json.dump(my_obj, f)


