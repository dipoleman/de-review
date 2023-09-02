from src.manipulate_staff_data import format_staff

def test_output_is_a_list():
    output = format_staff([
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
],
[
    {
        'department_id': 1,
        'department_name':'Beauty'
    }, {
        'department_id': 2,
        'department_name':'Footwear'
    }
])
    assert type(output) == list

def test_returns_expected_result():
    output = format_staff([
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department': 'Beauty'
    }, {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
],[
    {
        'department_id': 1,
        'department_name':'Beauty'
    }, {
        'department_id': 2,
        'department_name':'Footwear'
    }
])
    expected = [['Duncan', 'Crawley', 1], ['Cat', 'Hoang', 2]]
    assert output == expected 