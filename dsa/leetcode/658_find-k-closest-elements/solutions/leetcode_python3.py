class Solution:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k
        while left < right:
            middle = (left + right) // 2
            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle
        return arr[left:left + k]
