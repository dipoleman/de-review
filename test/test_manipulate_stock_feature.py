from src.manipulate_stock_feature import format_stock_feature


new_stock = [
    {
        'stock_id': 1,
        'item_name': 'Louboutin Flip Flops',
        'amount_in_stock':5
    }, {
        'stock_id': 2,
        'item_name': 'Eau de Fromage',
        'amount_in_stock': 10
    }
]

new_features = [
    {
        'feature_id':1,
        'feature_name':'Designer'
    },{
        'feature_id':2,
        'feature_name':'Faux-Faux-Leather'
    }
]

original_stock = [

    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }, {
        'item_name': 'Eau de Fromage',
        'features': ['Designer'],
        'department': 'Beauty',
        'amount_in_stock': 10
    }
]

def test_output_is_a_list():
    output = format_stock_feature(new_stock,new_features,original_stock)
    assert type(output) == list

def test_output_is_correct_value():
    output = format_stock_feature(new_stock,new_features,original_stock)
    expected = [[1, 1], [1, 2], [2, 1]]
    assert output == expected