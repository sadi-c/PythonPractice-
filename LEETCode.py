        #TwoSum
def two_sum(arr, target):

    values =dict()

    for i, elem in enumerate(arr):
        comp = target - elem

        if comp in values:
            return  [values[comp], i]

        values[elem] = i

    return []


