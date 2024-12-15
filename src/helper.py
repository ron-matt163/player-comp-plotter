import json

def write_dict_to_json(data, file_path):
    """
    Writes a dictionary to a JSON file.

    Args:
        data (dict): The dictionary to write.
        file_path (str): The path to the JSON file.
    """
    try:
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")