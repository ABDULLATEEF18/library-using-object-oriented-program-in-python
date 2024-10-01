### testing
### assert can be used to check if something is true

##code twttr
name = input("name: ")
dei = ['a', 'e', 'i', 'o', 'u']
for i in name:
    if i.casefold() not in dei:
        print(i, end="")