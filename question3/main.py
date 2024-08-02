#A

def mergingDict(*args):
    merged_dict = {}
    for dictionary in args:
        for i in dictionary:
            if (i not in merged_dict.keys()):
                merged_dict[i] = [dictionary[i]]
            else:
                merged_dict[i].append(dictionary[i])
    return merged_dict

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"b": 5}

merged = mergingDict(dict1, dict2, dict3)
print(merged)

#b

def commonKeys(*args):
    common_keys = set(args[0].keys())
    for dictionary in args:
        common_keys = common_keys.intersection(set(dictionary.keys()))
    return list(common_keys)
common_keys = commonKeys(dict1,dict2,dict3)
print(common_keys)

#c

def invertDictionary(dictin):
    result= {}
    for i in dictin:
        if (dictin[i] not in result.keys()):
            result[dictin[i]] = [i]
        else:
            result[dictin[i]].append(i)
    return result

fruitPrice = {"orange": 100, "apple" : 200, "berry" : 100}
fruitGroup = invertDictionary(fruitPrice)
print(fruitGroup)

#d
def commonKeyValue(*args):
    common_pairs = {(x, args[0][x]) for x in args[0]}
    for dictionary in args:
        temp = {(x, dictionary[x]) for x in dictionary}
        common_pairs = common_pairs.intersection(temp)
    return common_pairs
dict4 = {"a": 1, "b": 2}
dict5 = {"b": 3, "a": 1}
dict6 = {"a": 1}
print(commonKeyValue(dict4,dict5,dict6))