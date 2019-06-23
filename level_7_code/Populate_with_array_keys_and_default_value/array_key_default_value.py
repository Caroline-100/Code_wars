def populate_dict(keys,default):
    element = [keys,default]
    for e in element:
        print(e)
    d = {}
    d[element[0]]= e
    return d 

print(populate_dict("draft","d"))


# assert populate_dict(["draft", "completed"],0) =={"completed": 0, "draft": 0}
# assert populate_dict(["a", "b", "c"], None)== {"c": None, "b": None, "a": None}
# assert populate_dict([1, 2, 3, 4], "OK")== {1: "OK", 2: "OK", 3: "OK", 4: "OK"}


