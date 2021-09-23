new_dict = {"key1": "Hello World",
            12: "hiken wooorld"}



def lst():
    for key, value in new_dict.items():
        if isinstance(key, str):
            new_lst = []
            new_lst.append(value)
            print(new_lst)

lst()





