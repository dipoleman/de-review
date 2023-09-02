import pytest
from src.manipulate_department_data import format_departments,BadInputError

def test_output_is_a_list():
    output = format_departments([
        {
            'staff_id': 1,
            'first_name': 'Duncan',
            'last_name': 'Crawley',
            'department': 'Beauty'
        },
        {
            'staff_id': 2,
            'first_name': 'Cat',
            'last_name': 'Hoang',
            'department': 'Footwear'
        }
    ])
    assert type(output) == list

def test_returns_expected_departments():
    output = format_departments([
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
])
    expected = [['Beauty'], ['Footwear']]
    assert output == expected 

def test_raises_error_if_not_passed_a_list():
    with pytest.raises(BadInputError, match="Invalid input: abc is not a list"):
        format_departments("abc")

def test_raises_error_if_not_passed_a_list():
    input = [
    {
        'staff_id': 1,
    },
]
    with pytest.raises(BadInputError, match="Invalid input: not a dictionary or does not contain a 'department' key"):
        format_departments(input)