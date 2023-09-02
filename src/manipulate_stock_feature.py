
def format_stock_feature(new_stock,new_features,original_stock):
    """Maps stock IDs to feature IDs based on item names and feature names.

    Args:
        new_stock (list): A list of dictionaries representing new stock data,
            where each dictionary contains 'stock_id' and 'item_name' keys.
        new_features (list): A list of dictionaries representing new feature data,
            where each dictionary contains 'feature_id' and 'feature_name' keys.
        original_stock (list): A list of dictionaries representing original stock data,
            where each dictionary contains 'item_name' and 'features' keys.

    Returns:
        list: A list of lists, where each inner list contains a stock ID and a
            corresponding feature ID.
    """
    stock_id_features = [[stock['stock_id'],
                      [o_stock['features'] for o_stock in original_stock 
                       if stock['item_name']==o_stock['item_name']]] 
                      for stock in new_stock]
    
    stock_features_ids = []

    for stock in stock_id_features:
        stock_id = stock[0]
        for feature in stock[1][0]:
            feature_id = [new_feature['feature_id'] for new_feature in new_features 
                          if new_feature['feature_name'] == feature][0]
            stock_features_ids.append([stock_id,feature_id])

    return stock_features_ids
    





