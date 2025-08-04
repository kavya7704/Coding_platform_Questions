def isValid(s):
    stack = []
    if len(s) == 1:
      return False
    for i in s:
      if i in "[{(":
          stack.append(i)
      else:
          if len(stack) == 0:
              return False
          x = stack.pop()
          if i == ")" and x == "(" or i == "}" and x == "{" or i == "]" and x == "[":
              continue
          else:
              return False
return len(stack) == 0
