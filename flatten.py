res = []
def flatten(item):
    if isinstance(item, (list, tuple, set, range)):
        for i in item:
            flat(i)
    else:
        res.append(item)
flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(res) # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
