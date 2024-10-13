def fill(arr, method=0):
    if len(arr) <= 1:
        return arr

    if all(x == None for x in arr):
        return arr

    if method == -1:
        replacer = None
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != None:
                replacer = arr[i]
            else:
                arr[i] = replacer
    elif method == 1:
        replacer = None
        for i in range(len(arr)):
            if arr[i] != None:
                replacer = arr[i]
            else:
                arr[i] = replacer
    elif method == 0:
        nums = dict()
        for i, x in enumerate(arr):
            if x != None:
                nums[i] = x

        arr2 = []
        for i, x in enumerate(arr):
            dists = {}
            for y in nums:
                if abs(i - y) in dists:
                    dists[abs(i - y)] = min(dists[abs(i - y)], nums[y])
                else:
                    dists[abs(i - y)] = nums[y]
            arr2.append(dists[min(dists)])

        arr = arr2

    return arr