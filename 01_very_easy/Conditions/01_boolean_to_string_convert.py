def bool_to_string(flag: bool) -> str:
    if flag == True:
        return "True"
    elif flag == False:
        return "False"


print(bool_to_string(True))
print(bool_to_string(False))