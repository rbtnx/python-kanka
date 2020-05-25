from datetime import datetime
import pytest
from kanka.utils import to_datetime

def test_kanka_date_to_datetime():
    date = "2020-05-06T10:00:05.000000Z"

    converted_date = to_datetime(date)
    assert isinstance(converted_date, datetime)
    assert converted_date.year == 2020
    assert converted_date.month == 5
    assert converted_date.day == 6
    assert converted_date.hour == 10
    assert converted_date.minute == 0
    assert converted_date.second == 5

    with pytest.raises(Exception):
        converted_date = to_datetime(None)

    with pytest.raises(Exception):
        converted_date = to_datetime("No proper date string")
