#!/usr/bin/env python3

def lengh_funk(a:str ) -> int: 
    if not isinstance(a, str):
        print("Enter str")
        return None
    elif a == '':
        print("empty string")
        return 0
    else:
        return len(a)


print(lengh_funk(8))


def union_funk(*args: str) -> str:
    try:
        return " ".join(args)
    except TypeError:
        return  ("Enter str")

print(union_funk('Hello','World','233'))


def square_number(a: int) ->int:
    try:
        return a**2
    except TypeError:
        print("Enter int")


print(square_number(3))


def multip_funk(*args: int) ->int:
    try:
        return sum(args)
    except TypeError:
        print("Enter int")

print(multip_funk(23,43,53,1,8,0))


def divide_funk(a: int, b: int) ->int:
    try:
        return a//b , a%b 
    except TypeError:
        print("Enter int")

print(divide_funk(11,2))



def avg_list_funk(num_list: list[int | float]) -> float:
    try:
        if not isinstance(num_list, list):
            raise TypeError("Enter list")
        
        if len(num_list) == 0:
            raise ValueError("List is empty")

        for i in num_list:
            if not isinstance(i,(int, float)):
                raise TypeError("Enter only int and float")

        return round(( sum(num_list) / len(num_list)), 2)

    except (TypeError, ValueError) as e:
        print(f"Error {e}")
        return None

print(avg_list_funk([7,2,3,4,5,7,9]))
print(avg_list_funk(["Hello"]))
print(avg_list_funk({"num" : 4}))


def cross_val_fun(list_1: list, list_2: list):
    if not isinstance(list_1, list) or not isinstance(list_2, list):
        print("Enter only list")
        return None
    if not list_1 or not list_2:
        print("Lists is empty")
        return []
    cross_el = list(set(list_1) & set(list_2))
    return cross_el

print(cross_val_fun([1,23,5,7,9,'hello'], [7,43,2,7,1,9,'hello']))    
print(cross_val_fun((1,23,5,7,9,'hello'), [7,43,2,7,1,9,'hello'])) 
print(cross_val_fun([1,23,5,7,9,'hello'], []))     


def dict_key_fun(my_dic: dict):
    try:
        if not isinstance(my_dic, dict):
            raise TypeError("Enter dict")
    except TypeError as e:
        print(f"Error - {e}")
        return None
    
    if not my_dic:
        print("dict is empty")
        return []
    return list(my_dic.keys())

print(dict_key_fun({}))
print(dict_key_fun([1,2,3,'hello']))
print(dict_key_fun({"name": "Bob", "age" : 10}))


def union_dict_fun(my_dict_1: dict, my_dict_2: dict) -> dict:
    if not isinstance(my_dict_1, dict) or not isinstance(my_dict_2, dict):
        raise TypeError("Only dict")
    
    union_dict = {}

    union_keys = set( my_dict_1.keys()) | set( my_dict_2.keys())
    for key in union_keys:
        val_1 = my_dict_1.get(key)
        val_2 = my_dict_2.get(key)

        if key in my_dict_1 and key in my_dict_2:
            if val_1 == val_2:
                union_dict[key] = [val_1 ]
            else:
                union_dict[key] = [val_1, val_2]
        elif key in my_dict_1:
            union_dict[key] = [val_1]
        else:
            union_dict[key] = [val_2]
    
    return union_dict

print(union_dict_fun({"name": "Bob", "age" : 10},{"city" : "Zmerinka" , "country" : "Ukraine"}))    
#print(union_dict_fun({"name": "Bob", "age" : 10},["city" , "Zmerinka" , "country" , "Ukraine"]))
print(union_dict_fun({"name": "Bob", "age" : 10},{"name": "Ivan", "age" : 20}))    


def union_set_fun(my_set_1: set, my_set_2: set) -> set:
    if not isinstance(my_set_1, set) or not isinstance(my_set_2, set):
        raise TypeError("Enter set")
    return  my_set_1 | my_set_2
    

print(union_set_fun({1,2,5,7,9,'hello'},{3,1,9,'hello'}))
##print(union_set_fun({1,2,5,7,9,'hello'},(3,1,8,9,'hello')))
print(union_set_fun({1,2,5,7,9,'hello'},set()))


def cheking_set_fun(set_3: set, set_4: set) -> bool:
    if not isinstance(set_3, set) or not isinstance(set_4, set):
        raise TypeError("Enter onle set")
    
    return set_3.issubset(set_4)

print(cheking_set_fun({1,2,3,4,5},{1,2,3,4,5}))
print(cheking_set_fun({0,1,2,3,4,5},{1,2,3,4,5,'hello'}))
#print(cheking_set_fun({1,2,3,4,5},(1,2,3,4,5,'hello')))


def numer_fun(a: int) -> str:
    if not isinstance(a , int):
        value = "only numeric value"
    elif a % 2 == 1:
        value = 'непарне'
    else:
        value = 'парне'
    
    return value

print(numer_fun(3))
print(numer_fun(0))
print(numer_fun('3'))


def number_check_fun(my_list: list) -> list:
    if not isinstance(my_list , list ):
        return ["enter only  list"]
    new_list = []
    for i in my_list:
        if isinstance(i,int):
            if i % 2 == 0:
                new_list.append(i)
        else:
            return ['enter only number']
    
    return new_list

print(number_check_fun([1,2,3,4,5,6,7]))
print(number_check_fun([1,2,'3',4,5,6,7]))
print(number_check_fun([]))

    
