def twoPositives(a, b, c):
  positiveCount = 0
  
  if a > 0:
    positiveCount += 1
  if b > 0:
    positiveCount += 1
  if c > 0: 
    positiveCount += 1
    
  return positiveCount == 2
  
# result = twoPositives(1, -15, 10)
print( twoPositives(1, -15, 10))
print (twoPositives(1, -15, 0))
print (twoPositives(1, 5, 2))