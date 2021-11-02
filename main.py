def SubsetSum(array, no, val, sum):
    if (sum == 0) :
      for value in val :
       print(value, end=" ")
       print()
       return
    if (no == 0):
       return
    SubsetSum(array, no - 1, val, sum)
    v1 = [] + val
    v1.append(array[no - 1])
    SubsetSum(array, no - 1, v1, sum - array[no - 1])

def isSubsets(array, no, sum):
    val = []
    SubsetSum(array, no, val, sum)
array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum = 23
no = len(array)

isSubsets(array, no, sum)