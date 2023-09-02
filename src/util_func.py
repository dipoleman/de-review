from pg8000.native import Connection, identifier
from os import environ
from pprint import pprint
import datetime

# manipulate features and maipulate stock data
def select_all_data_from_tables():
    db_user = environ.get('PGUSER')
    db_database = 'nc_sells_fridges_og'

    conn = Connection(db_user, database=db_database)
    query = f'SELECT * FROM items;'
    rows = conn.run(query)
    items = []
    for row in rows:
        items.append({'item_name':row[0],'features':row[1],'department':row[2],'amount_in_stock':row[3]})

    query = f'SELECT * FROM staff;'
    rows = conn.run(query)
    staff = []
    for row in rows:
        staff.append({'staff_id':row[0],'first_name':row[1],'last_name':row[2],'department':row[3]})

    query = f'SELECT * FROM sales;'
    rows = conn.run(query)
    sales = []
    for row in rows:
        sales.append({'sale_code':row[0],'item_name':row[1],'salesperson':row[2],'price':float(row[3]),
                      'quantity':row[4],'created_at':row[5].strftime('%Y-%m-%d %H:%M:%S')})

    return (items,staff,sales)
