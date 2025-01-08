import re
from datetime import datetime


class File:
    """Clase que representa un archivo."""

    def __init__(self, name: str, creation_date: str, size: int):
        self.name = name
        self.creation_date = datetime.strptime(creation_date, "%Y.%m.%d")
        self.size = size

    def __repr__(self):
        return (
            f"File(name='{self.name}', "
            f"creation_date='{self.creation_date.strftime('%Y.%m.%d')}', "
            f"size={self.size} bytes)"
        )


def parse_input_string(input_str: str) -> tuple:
    """Valida y analiza la cadena de entrada.

    Args:
        input_str (str): La cadena que describe el archivo.

    Returns:
        tuple: Contiene tipo de objeto, nombre, fecha y tamaño.
    """
    pattern = r"(\w+)\s+\"(.*?)\"\s+(\d{4}\.\d{2}\.\d{2})\s+(\d+)"
    match = re.match(pattern, input_str)
    if not match:
        raise ValueError("Formato de entrada inválido.")
    return match.groups()


def create_object(object_type: str, name: str, creation_date: str, size: str):
    """Crea un objeto basado en el tipo de entrada.

    Args:
        object_type (str): El tipo del objeto (por ejemplo, 'tarea').
        name (str): Nombre del archivo.
        creation_date (str): Fecha de creación.
        size (str): Tamaño del archivo.

    Returns:
        File: Un objeto de la clase File.
    """
    size = int(size)
    if object_type.lower() == "tarea":
        return File(name, creation_date, size)
    else:
        raise ValueError(f"Tipo de objeto desconocido: {object_type}")


def main(input_str: str):
    """Función principal que coordina el flujo del programa."""
    try:
        object_type, name, creation_date, size = parse_input_string(input_str)
        obj = create_object(object_type, name, creation_date, size)
        print(obj)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_string = 'tarea "example_file.txt" 2023.12.25 1024'
    main(input_string)
