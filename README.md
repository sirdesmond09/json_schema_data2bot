This program is a utility for generating a JSON schema from a given JSON data object. It contains two functions: `get_schema` and `get_data_schema`.   

The get_schema function takes a JSON data object as input and returns a dictionary representing the high-level schema of the data and includes the required specifications for the project.  

The `get_data_schema` function, which is commented out, takes a JSON data object as input and returns a more detailed schema, including the types of all values within the object. Both functions also incudes provision for adding metadata such as tags and descriptions.    

The program contains a dictionary mapping Python data types to their corresponding JSON schema types, and uses this mapping to determine the schema types of the values in the input data object.

## get_schema() function
This function is used to get the schema of a given json data.

### Parameters
- `json_data (dict)`: The json data.
- `tag (str, optional)`: The tag of the json data. Default is an empty string.
- `desc (str, optional)`: The description of the json data. Default is an empty string.

### Returns
The schema of the json data.

### Example
```
json_data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "is_human": true
}

schema = get_schema(json_data)
print(schema)

# Output: {
#   "name": {
#     "type": "string",
#     "tag": "",
#     "description": "",
#     "required": False
#   },
#   "age": {
#     "type": "integer",
#     "tag": "",
#     "description": "",
#     "required": False
#   },
#   "city": {
#     "type": "string",
#     "tag": "",
#     "description": "",
#     "required": False
#   },
#   "is_human": {
#     "type": "boolean",
#     "tag": "",
#     "description": "",
#     "required": False
#   }
# }
```


## How to run the program

- Clone the git repository using `git clone` command
- Make the project directory your current working directory in your terminal
- Run `python3 solution.py`

Note: In the section that says `if __name__ == '__main__':`, you should change the file paths to correspond to your file name.
