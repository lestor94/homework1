class Storage():

    def save_data(self):
        raise NotImplementedError

    def get_data(self):
        raise NotImplementedError

class FileStorage(Storage):
    pass

class PickleStorage(Storage):
    pass

class DBStorage(Storage):
    pass