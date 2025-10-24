import csv
from pathlib import Path


BASE_DIR = Path.cwd()
FILES_DIR = BASE_DIR / 'files'


def read_csv_files(file_path):
    """Чтение CSV файлов."""
    data = []
    for path in file_path:
        full_path = FILES_DIR/path
        with open(full_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data.extend(csv_reader)
    return data
