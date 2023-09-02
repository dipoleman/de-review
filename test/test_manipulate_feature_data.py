import pytest
from src.manipulate_feature_data import format_features, BadInputError

def test_output_is_a_list():
    output = format_features([
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
    output = format_features([
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
    expected = [['Designer'], ['Faux-Faux-Leather'], ['Fragrance']]
    assert output == expected 


