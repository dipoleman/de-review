class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def format_features(list_dict):
    """Extracts unique feature names from a list of dictionaries.

    Args:
        list_dict (list): A list of dictionaries, where each dictionary represents
            an item and contains a 'features' key with a list of feature names.

    Returns:
        list: A list of lists, where each inner list contains a single unique feature name.
    """
    features = [feature for item in list_dict for feature in item['features']]
    unique_features = sorted([[feature] for feature in set(features)])
    return unique_features
