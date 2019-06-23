def boolean_to_string(b):
    if b:
        return str(True)
    return str(False)

    
assert boolean_to_string(True) == "True", 'When we pass in true, we want the string "true" as output'
assert boolean_to_string(False) =="False", 'When we pass in false, we want the string "false" as output'
