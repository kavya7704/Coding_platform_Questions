class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        zero_count = arr.count(0)
        if zero_count > 1:
            arr = [0] * len(arr)
            return arr
        p = 1
        for i in arr:
            if i != 0:
                p *= i
        for i in range(len(arr)):
            if zero_count == 0:
                arr[i] = p // arr[i]
            elif arr[i] == 0:
                arr[i] = p
            else:
                arr[i] = 0
        return arr
