def add_char(string,char):
    old_size = len(string)
    new_size = old_size + 1
    new_string = ['']*new_size

    for i in range(old_size):
        new_string[i] = string[i]

    new_string[old_size] = char
    return "".join(new_string)

string = ""
for i in range(10000):
    string = add_char(string,'a')
print(string)