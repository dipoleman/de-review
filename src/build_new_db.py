# order of tables:
# 1 dim_features
# 2 stock_feature_junc
# 3 dim_stock
# 4 dim_department
# 5 dim_staff
# 6 sales
from pg8000.native import Connection, identifier
from src.util_func import select_all_data_from_tables
from src.manipulate_feature_data import format_features
from src.manipulate_stock_feature import format_stock_feature
from os import environ
from pprint import pprint
import datetime

#  ------ dim_features -------

#  feature_id | feature_name 
# ------------+--------------
# (0 rows)

items,staff,sales = select_all_data_from_tables()

features = sorted(format_features(items))
feature_name = []
for i in range(len(features)):
    feature_name.append((features[i][0]))
    
print(feature_name)



def populate_dim_features():
    db_user = environ.get('PGUSER')
    db_database = 'nc_sells_fridges_new'
    conn = Connection(db_user, database=db_database)

    for feature in feature_name:
        conn.run("INSERT INTO dim_features (feature_name) VALUES (:title)", title=feature)

    conn.close()

def populate_stock_feature_junction():
    db_user = environ.get('PGUSER')
    db_database = 'nc_sells_fridges_new'
    conn = Connection(db_user, database=db_database)

    features = conn.run('SELECT * FROM dim_features')
    new_features = [{'feature_id':feature[0],'feature_name':feature[1]} for feature in features]
    
    # print(new_features)
    item_ids_list = []
    # list of item_id,item_name
    for i in range(len(items)):
        item_ids_list.append({'stock_id':i+1,
                              'item_name':items[i]['item_name'],
                              'amount_in_stock':[item['amount_in_stock'] for item in items if items[i]['item_name'] == item['item_name']][0]})
    print(item_ids_list)
    stock_features = format_stock_feature(item_ids_list,new_features,items)
    print(items)
    print(stock_features)
    # for stock in stock_features:
        # print(stock[0],stock[1])
        # conn.run("INSERT INTO stock_feature_junc (stock_id,feature_id) VALUES (:stock_id, :feature_id)", stock_id=stock[0],feature_id=stock[1])
    # print(table)
    # conn.close()
# populate_dim_features()
populate_stock_feature_junction()