import argparse


def configuure_arguument_parser(available_models):
    """Конфигурация парсера аргкментов командной строки"""
    parser = argparse.ArgumentParser(description='Анализ рейтинга брендов')
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help='Путь к CSV файлам'
    )
    parser.add_argument(
        '--report',
        required=True,
        help='Создание отчёта в формате таблицы'
    )
    return parser
