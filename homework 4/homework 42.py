new_dict = {"key1":"Hello World",
            "key2":"Helloo World",
            "key3":"Hell World",
            12:"Helloo woorld"}


def s():
    for key, value in new_dict.items():
        if isinstance(key, str):
            values = new_dict.values()
            print(list(values))
s()
