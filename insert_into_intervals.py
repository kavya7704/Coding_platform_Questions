 def insert(intervals,newInterval):
      merge = []
      i = 0
      while i < len(intervals) and intervals[i][1] < newInterval[0]:
          merge.append(intervals[i])
          i += 1

      while i < len(intervals) and intervals[i][0] <= newInterval[1]:
          newInterval[0] = min(newInterval[0],intervals[i][0])
          newInterval[1] = max(newInterval[1],intervals[i][1])
          i += 1
      merge.append(newInterval)

      while i < len(intervals):
          merge.append(intervals[i])
          i += 1

      return merge
