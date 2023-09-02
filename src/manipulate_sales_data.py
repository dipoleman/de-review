
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

def format_sales(new_stock_data,new_staff_data,original_sales_data):

   
    item_names = [sale['item_name'] for sale in original_sales_data]

    item_ids = []
    for item in item_names:
        item_ids.append([stock_item['stock_id'] for stock_item in new_stock_data 
                         if stock_item['item_name'] == item][0])

    item_sales_persons = [sale['salesperson'] for sale in original_sales_data]

    item_sale_person_ids = []
    for person in item_sales_persons:
        first_name, last_name = person.split(' ')
        item_sale_person_ids.append([staff['staff_id'] for staff in new_staff_data
                                     if first_name == staff['first_name'] and last_name == staff['last_name']][0])

    item_prices = [sale['price'] for sale in original_sales_data]
    item_quantity = [sale['quantity'] for sale in original_sales_data]
    item_time = [sale['created_at'] for sale in original_sales_data]
    
    format_sales_data = []
    for i in range(len(original_sales_data)):
        format_sales_data.append([item_ids[i],item_sale_person_ids[i],item_prices[i],item_quantity[i],item_time[i]])
    
    return format_sales_data




print(format_sales(new_stock_data,new_staff_data,original_sales_data))

