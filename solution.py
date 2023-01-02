import json


json_types = {'dict': 'object', 
              'list': 'array', 
              'tuple': 'array', 
              'str': 'string', 
              'int': 'integer', 
              'bool': 'boolean', 
              'None': 'null'}

def get_schema(json_data,tag="", desc=""):
    
    """This function is used to get the high level schema of a given json data. 

    args:
    
        json_data (dict): The json data.

        tag (str): The tag of the json data.

        desc (str): The description of the json data.

    returns:

        The schema of the json data.

    """

    schema = {}
            
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            
            #Check if the value is an array and all data is a string, then the program  maps the data type as an ENUM 
            if (type(value).__name__ == "list" or type(value).__name__ == "tuple") and all(isinstance(i, str) for i in value):
               
                schema_data = (("type","enum"),
                               ("tag", tag),
                               ("description", desc),
                               ("required", False))
                
            #Check if the value is an array and all data is a json/dict, then the program  maps the data type as an array 
            elif (type(value).__name__ == "list" or type(value).__name__ == "tuple") and all(isinstance(i, dict) for i in value):
               
                schema_data = (("type","array"),
                               ("tag", tag),
                               ("description", desc),
                               ("required", False))
            else:
                schema_data = (("type",json_types.get(str((type(value).__name__)))),
                               ("tag", tag),
                               ("description", desc),
                               ("required", False))
            
            schema[key] = dict(schema_data)
            
        
    #if the json is an array of objects, the program loops through and gets the schema
    elif isinstance(json_data, list) or isinstance(json_data,tuple):
        for data in json_data:
            return get_schema(data)
        
    return schema


    
# def get_data_schema(json_object,tag="", desc=""):
    
#     """This function is used to get in-depth schema of a given json data. 

#     args:
    
#         json_data (dict): The json data.

#         tag (str): The tag of the json data.

#         desc (str): The description of the json data.

#     returns:

#         The schema of the json data.

#     """
    
#     schema = {}
    
#     if isinstance(json_object, dict):
#         # If the object is a dictionary, we'll create a dictionary for the schema
#         # with the keys as the keys of the original dictionary and the values
#         # as the schemas of the values in the original dictionary
#         schema = {}
#         for key, value in json_object.items():
#             schema_data = get_data_schema(value)
            
#             schema[key] = schema_data
#         return schema
#     elif isinstance(json_object, list):
#         # If the object is a list, we'll create a list for the schema with the
#         # schema of the first element as the schema for the whole list
#         if len(json_object) > 0:
#             return [get_data_schema(json_object[0])]
#         else:
#             # If the list is empty, we'll return an empty list as the schema
#             return []
#     else:
#         # If the object is not a dictionary or a list, it must be a primitive type
#         # (e.g. string, number, boolean). We'll return the type of the object as
#         # the schema.
#         data =(("type",json_types.get(str((type(json_object).__name__)))),
#                ("tag", tag),
#             ("description", desc),
#             ("required", False))
#         return dict(data)
            
            
if __name__ == "__main__":
    with open("data/data_2.json") as json_file:
        data = json.load(json_file)

    message_data = data.get("message")
    schema = get_schema(message_data) #using function 1 to get the schema
    # schema = get_data_schema(message_data) #using function 2 to get the schema
    
    json_data = json.dumps(schema, indent=2)
    
    with open("schema/schema_2.json", "w") as output:
        output.write(json_data)
        print("successful")
    
    