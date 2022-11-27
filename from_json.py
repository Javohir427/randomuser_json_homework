import json


def read_json(filename:str) -> dict:
    """Reads a JSON file and returns the data as a dictionary

    Args:
        filename (str): The name of the JSON file
    return:
        dict: The data in the file
    """

    # Read the data from the file
    f = open('user.json').read()

    # Parse the JSON data
    data = json.loads(f)
    print(type(data))
    return data
print(read_json('diyor'))  


     
