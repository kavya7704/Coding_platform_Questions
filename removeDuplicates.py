def removeDuplicates(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    i = 0
    for key in d:
        nums[i] = key
        i += 1

    return len(d)
