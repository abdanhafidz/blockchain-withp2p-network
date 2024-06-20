import json

import json

class DictObj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)
    
    def __getitem__(self, key):
        return self.__dict__[key]
    
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    
    def __delitem__(self, key):
        del self.__dict__[key]
    
    def __repr__(self):
        return f"{self.__dict__}"

# Contoh data
data = {
    "greeting": "hi",
    "test": True
}

# Konversi dictionary ke DictObj menggunakan object_hook
data_obj = json.load(json.dumps(data), object_hook=DictObj)

# Mengakses data sebagai atribut objek
print(data_obj.greeting)  # Output: hi
print(data_obj.test)      # Output: True

# Mengakses data sebagai dictionary
print(data_obj['greeting'])  # Output: hi
print(data_obj['test'])      # Output: True

# Mengubah data menggunakan atribut objek
data_obj.greeting = "hello"
print(data_obj.greeting)  # Output: hello

# Mengubah data menggunakan dictionary
data_obj['test'] = False
print(data_obj.test)      # Output: False