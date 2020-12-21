# Removing vowels from a given sentence

x = "hello world"
list1 = ["a","e","i","o","u"]

for y in x:
    if y in list1:
        x = x.replace(y, '')
print(x)

