def SubsetSum(array, n, val, sum):
    if (sum == 0) :
      for value in val :
       print(value, end=" ")
       print()
       return
    if (n == 0):
       return
    SubsetSum(array, n - 1, val, sum)
    v1 = [] + val
    v1.append(array[n - 1])
    SubsetSum(array, n - 1, v1, sum - array[n - 1])

def isSubsets(array, n, sum):
    val = []
    SubsetSum(array, n, val, sum)
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum = 23
n = len(array)

isSubsets(array, n, sum)