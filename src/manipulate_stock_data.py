class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def format_stock(list_dict):
    """Extracts item names and stock amounts from a list of dictionaries.

    Args:
        list_dict (list): A list of dictionaries, where each dictionary represents
            an item and contains 'item_name' and 'amount_in_stock' keys.

    Returns:
        list: A list of lists, where each inner list contains an item name and
            the corresponding stock amount.

    Raises:
        BadInputError: If the input is not a list or if any dictionary in the input
            list does not contain 'item_name' or 'amount_in_stock' keys.
    """
    if not isinstance(list_dict, list):
        raise BadInputError(f"Invalid input: {list_dict} is not a list")

    stock = []
    for item in list_dict:
        if not isinstance(item, dict) or 'item_name' not in item or 'amount_in_stock' not in item:
            raise BadInputError(f"Invalid input: not a dictionary or does not contain correct key")
        stock.append([item['item_name'], item['amount_in_stock']])
    return stock
