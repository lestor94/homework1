new_dict = {"key1":"Hello World",
            12:"Helloo woorld"}

def s():
    for key, value in new_dict.items():
        new_lst = []
        if isinstance(key, str):
            new_lst.append(value)
            print(new_lst)
s()
