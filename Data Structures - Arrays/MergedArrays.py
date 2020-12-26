# Problem: Merge Sorted Arrays
#   Input: arr1 = [0,3,4,31], arr2 = [4,6,30]
#  Output: [0,3,4,4,30,31]  


arr1 = [0,3,4,31]
arr2 = [4,6,30]

def mergeSortedArrays(arr1, arr2):
  mergedArray = []
  x = 0
  i = 0
  while x < len(arr1) and i < len(arr2):
    if arr1[x] <= arr2[i]:
      mergedArray.append(arr1[x])
      x += 1
    elif arr2[i] < arr1[x]:
      mergedArray.append(arr2[i])
      i += 1
  return mergedArray+arr1[x:]+arr2[i:]

def mergeSortedArrays2(arr1,arr2):
  x = arr1 + arr2
  x.sort()
  return x


print(mergeSortedArrays(arr1,arr2))
print(mergeSortedArrays2(arr1,arr2))
