
_names = []

def initialize (names_file):

    with open (names_file, "r") as file:

        global _names
        _names = [ name [ :-1 ].lower () for name in file.readlines () ]

def change_name (original_name):

    lower_original_name = original_name.lower()

    for name in _names:
        if name in lower_original_name:
            print ("--- changed {} into {} ---".format(original_name, name))
            return name
        
    return original_name


if __name__ == "__main__":
    print('ran name_handler.py')
