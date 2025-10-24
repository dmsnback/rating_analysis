import pytest
from reports.average_ratings import average_rating


@pytest.fixture
def test_data():
    test_data = [
        {'brand': 'apple', 'rating': '4.9'},
        {'brand': 'apple', 'rating': '4.1'},
        {'brand': 'xiaomi', 'rating': '4.1'},
        {'brand': 'samsung', 'rating': '4.8'},
    ]
    return test_data


def test_average_rating_return_list(test_data):
    report = average_rating(test_data)
    assert isinstance(report, list)


def test_average_rating_no_repeat_brands(test_data):
    report = average_rating(test_data)
    assert len(report) == 3


def test_average_rating_correct_avg(test_data):
    report = average_rating(test_data)
    apple_rating = 0
    for i in report:
        if i['brand'] == 'apple':
            apple_rating += i['rating']
    assert apple_rating == 4.5


def test_average_rating_correct_sort(test_data):
    report = average_rating(test_data)
    test_sorted_report = sorted(
        report,
        key=lambda val: val['rating'],
        reverse=True)
    assert report == test_sorted_report
