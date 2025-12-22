def add(num_1:str, num_2:str)->str:
    if num_1 and num_2:
        addition : int = int(num_1) + int(num_2)
        return str(addition)
    else:
        return "Invalid Operation"
    
print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
