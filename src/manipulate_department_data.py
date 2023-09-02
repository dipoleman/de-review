
class BadInputError(Exception):
    """Raised when a function receives a bad input."""
    pass

def format_departments(list_dict):
    """Extracts department names from a list of dictionaries.

    Args:
        arr_dict (list): A list of dictionaries, where each dictionary represents
            a staff member and contains a 'department' key with the department name.

    Returns:
        list: A list of lists, where each inner list contains a single department name.

    Raises:
        BadInputError: If the input is not a list or if any dictionary in the input
            list does not contain a 'department' key.
    """
    if not isinstance(list_dict, list):
        raise BadInputError(f"Invalid input: {list_dict} is not a list")

    department_names = []
    for dep in list_dict:
        if not isinstance(dep, dict) or 'department' not in dep:
            raise BadInputError(f"Invalid input: not a dictionary or does not contain a 'department' key")
        department_names.append([dep['department']])
    return department_names
