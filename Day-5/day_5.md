#  Day 5 Dictionaries (Hash Maps) 
## Theory: Hash Tables 
A Dictionary is a Key-Value store. It is optimized for O(1) Lookup. 
When you search a List, Python scans left-to-right (O(N)). When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in memory. It is instant, even with 1 million items.

```
user = {"id" : 1, "name" : "Admin"}
# Safe Access (.get) 
# Returns None if key missing, prevents crash 
email = user.get("email","No Email Found")

# Iteration
for key, val in user.items(): 
    print (f"{key}: {val}") 

```
## Goals:
1. List Search (O(N)): Python must scan item 1, item 2, item 3... until the end.  
Dict/Set Search (O(1)): Python runs hash (-1), gets a memory address (e.g., 0x99), and looks only at that spot. It is instant. 
2.  Direct access user ["key"] raises a KeyError if the key is missing, crashing the script. The method user.get("key", "Default") checks the Hash Table. If the bucket is empty.
3. Create a dictionary that counts the frequency of each letter.
4. Marge teo dictionary using  the update operator | or .update()