res = []
def reverse(item, out = []):
    if isinstance(item, (list, tuple, set, range)):
        out.insert(0, [])
        for i in item:
            reverse(i, out[0])
    else:
        out.insert(0, item)
        
reverse([[1, 2], [3, 4], [5, 6, 7]], res)
print(res) # [[[7, 6, 5], [4, 3], [2, 1]]]
