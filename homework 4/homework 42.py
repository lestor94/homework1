new_dict = {"key1":"Hello World",
            "key2":"Helloo World",
            "key3":"Hell World",
            12:"Helloo woorld"}

new_lst = []

def s():
    for key, value in new_dict.items():
        if isinstance(key, str):
            new_lst.append(value)
            print(new_lst)
s()