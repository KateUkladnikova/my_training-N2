my_dict = {"Вера": 1939, "Ира": 1963, "Сергей": 1988}
print(my_dict)
print(my_dict["Ира"])
print(my_dict.get("Катя"))
my_dict["Гоша"] = 1996
my_dict["Kирилл"] = 2004
print(my_dict)
del my_dict["Ира"]
print(my_dict)