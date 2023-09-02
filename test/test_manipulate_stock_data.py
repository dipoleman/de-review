import pytest
from src.manipulate_stock_data import format_stock, BadInputError

def test_output_is_a_list():
    output = format_stock([
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        },
        {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 10
        }
    ])
    assert type(output) == list

def test_returns_expected_result():
    output = format_stock([
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear',
            'amount_in_stock': 5
        },
        {
            'item_name': 'Eau de Fromage',
            'features': ['Fragrance', 'Designer'],
            'department': 'Beauty',
            'amount_in_stock': 10
        }
    ])
    expected = [['Louboutin Flip Flops', 5], ['Eau de Fromage', 10]]
    assert output == expected

def test_raises_error_if_not_passed_a_list():
    with pytest.raises(BadInputError, match="Invalid input: abc is not a list"):
        format_stock("abc")

def test_raises_error_if_dict_does_not_contain_required_keys():
    input = [
        {
            'item_name': 'Louboutin Flip Flops',
            'features': ['Designer', 'Faux-Faux-Leather'],
            'department': 'Footwear'
        }
    ]
    with pytest.raises(BadInputError, match="Invalid input: not a dictionary or does not contain correct key"):
        format_stock(input)
