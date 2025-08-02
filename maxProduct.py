class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        if not arr:
            return 0

        curr_max = arr[0]
        curr_min = arr[0]
        result = arr[0]

        for i in range(1, len(arr)):
            num = arr[i]

            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            result = max(result, curr_max)

        return result
