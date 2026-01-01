
class PyListObject:
    def __init__(self,ob_size):
        self.ob_size = ob_size

def get_length(list_obj):
    return list_obj.ob_size 

element = [None]*10000
List = PyListObject(len(element))
print(get_length(List))