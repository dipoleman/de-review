from src.util_func import select_all_data_from_tables

def test_data_from_util_func():
    output = select_all_data_from_tables()
    expected = {'item_name': 'Louboutin Flip Flops', 'features': ['Designer', 'Faux-Faux-Leather'], 'department': 'Footwear', 'amount_in_stock': 50}
    assert output[0][0] == expected