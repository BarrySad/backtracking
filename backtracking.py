##Testing out backtracking in python
def permute(list, s):
    if list == 1:
        return s
    else:
        return [y + x 
        for y in permute (1, s)
        for x in permute (list - 1, s)
        ]
print (permute (1, ["1", "2", "3", "4", "5"]))
print (permute (2, ["1", "2", "3", "4", "5"]))