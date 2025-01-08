import re
from datetime import datetime

class File:
    def __init__(self, name: str, creation_date: str, size: int):
        self.name = name
        self.creation_date = datetime.strptime(creation_date, "%Y.%m.%d")
        self.size = size

    def __repr__(self):
        return f"File(name='{self.name}', creation_date='{self.creation_date.strftime('%Y.%m.%d')}', size={self.size} bytes)"

def parse_object(input_str: str):
    pattern = r"(\w+)\s+\"(.*?)\"\s+(\d{4}\.\d{2}\.\d{2})\s+(\d+)"
    match = re.match(pattern, input_str)

    if not match:
        raise ValueError("Input string format is invalid.")

    object_type = match.group(1)
    name = match.group(2)
    creation_date = match.group(3)
    size = int(match.group(4))

    if object_type.lower() == "tarea":
        return File(name, creation_date, size)
    else:
        raise ValueError(f"Unknown object type: {object_type}")

if __name__ == "__main__":
    input_string = "tarea \"example_file.txt\" 2024.10.30 1025"
    try:
        obj = parse_object(input_string)
        print(obj)
    except ValueError as e:
        print(f"Error: {e}")
