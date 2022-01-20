target = 8
lst = [10,5,4,2,2]


def group_sum(target:int, values:list):

    if target == 0:
        return []
    if len(values) == 0:
        return None
    
    if target > values[0]:
        target -= values[0]
        if target == 0:
            return values[0:1]
        lst = group_sum(target, values[1:])
        if lst is not None:
            return values[0:1] + lst
    elif target < values[0]:
        return group_sum(target, values[1:])
        # if lst is not None:
        #     return values[0:1] + lst
    else:
        if values is not None:
            return values[0:1]

print(group_sum(target,lst))
