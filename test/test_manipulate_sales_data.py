from src.manipulate_sales_data import format_sales

new_stock_data = [
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
new_staff_data =[
    {
        'staff_id': 1,
        'first_name': 'Duncan',
        'last_name': 'Crawley',
        'department_id': 1
    },
    {
        'staff_id': 4,
        'first_name': 'Jim',
        'last_name': 'Nibbly',
        'department_id': 1
    }
]
original_sales_data = [
    {
        'sale_code': 'guiiljnevn',
        'item_name': 'Louboutin Flip Flops',
        'salesperson': 'Duncan Crawley',
        'price': 22.49,
        'quantity': 1,
        'created_at': '2023-01-03 10:34:56'
    },
    {
        'sale_code': 'guiiljnevn',
        'item_name': 'Eau de Fromage',
        'salesperson': 'Jim Nibbly',
        'price': 2.49,
        'quantity': 3,
        'created_at': '2023-01-03 12:34:56'
    }
]


def test_output_is_a_list():
    output = format_sales(new_stock_data,new_staff_data,original_sales_data)
    assert type(output) == list

def test_function_works_as_it_should():
    output = format_sales(new_stock_data,new_staff_data,original_sales_data)
    expected = [[1, 1, 22.49, 1, '2023-01-03 10:34:56'], [2, 4, 2.49, 3, '2023-01-03 12:34:56']]
    assert output == expected