from solution import get_schema

def test_get_schema():
    
    # Test input that is a dictionary
    json_data = {'key1': 'value1', 'key2': 'value2',}
    
    expected_output = {
        'key1': {
            'type': 'string', 
            'tag': 'test', 
            'description': 'testing the data', 
            'required': False}, 
        
        'key2': {
            'type': 'string', 
            'tag': 'test', 
            'description': 'testing the data', 
            'required': False
            }
        }
    assert get_schema(json_data, tag="test", desc="testing the data") == expected_output

    # Test input that the value is a list of strings
    json_data = {"key1" :['value1', 'value2']}
    expected_output = {
        "key1": {
            'type': 'enum', 
            'tag': '', 
            'description': '', 
            'required': False
            }
        }
    assert get_schema(json_data) == expected_output

    # Test input that the value is a list of dictionaries
    json_data = {"data": [{'key1': 'value1'}, {'key2': 'value2'}]}
    
    expected_output = {
        "data":{
            'type': 'array', 
            'tag': '', 
            'description': '', 
            'required': False
            }
        }
    assert get_schema(json_data) == expected_output
    
    
test_get_schema()