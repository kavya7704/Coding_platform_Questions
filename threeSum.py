def threeSum(nums): 
      res = set()
      nums.sort()
      n = len(nums)
      for i in range(0,n):
          if i > 0 and nums[i] == nums[i-1]:
              continue
          j = i + 1
          k = n - 1
          while j < k:
              Sum = nums[i] + nums[j] + nums[k]
              if Sum == 0:
                  curr = [nums[i],nums[j],nums[k]]
                  curr.sort()
                  res.add(tuple(curr))
                  j += 1
                  k -= 1
                  while j < k and nums[j] == nums[j-1]:
                      j += 1
                  while j < k and nums[k] == nums[k+1]:
                      k -= 1
              elif Sum > 0:
                  k -= 1
              else:
                  j += 1
      ans = []
      for i in res:
          ans.append(list(i))
      return ans
