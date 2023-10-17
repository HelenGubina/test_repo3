# dict1 = {"name " : "Jane", "surname" : "Smith","age" : 32}
#
# dict2 = {"phone " : "0503342929", "email" : "Smith@gmail.com","sex" : "feminine"}
#
# dict3 = dict1|dict2
#
# print(dict3)

def dict_union(dict_par_1, dict_par_2):
    dict={}

    for key in dict_par_1.keys():
        if dict.get(key) == None:
            dict[key] = dict_par_1[key]
        else:
            dict[key] += dict_par_1[key]

    for key in dict_par_2.keys():
        if dict.get(key) == None:
            dict[key] = dict_par_2[key]
        else:
            dict[key] += dict_par_2[key]

    return dict


dict1 = {"apple":12, "orange":8, "plum":5, "banana":6, "mango":9}
dict2 = {"pineapple":18, "peach":4, "plum":6,  "mango":7}

print(dict_union(dict1, dict2))
print(dict1)