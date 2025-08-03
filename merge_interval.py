def merge(intervals):
      if not intervals:
          return []

      intervals.sort(key=lambda x: x[0])  

      merged = []
      i = 0

      while i < len(intervals) - 1:
          if intervals[i][1] < intervals[i+1][0]:  
              merged.append(intervals[i])
          else:
              
              intervals[i+1][0] = min(intervals[i][0], intervals[i+1][0])
              intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
          i += 1

      merged.append(intervals[i])  

      return merged
