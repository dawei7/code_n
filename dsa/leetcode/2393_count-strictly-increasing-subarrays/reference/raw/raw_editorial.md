[TOC]

## Solution

---

### Approach 1: Dynamic Programming

**Intuition**

We are given an array of $N$ positive integers; we need to return the number of subarrays that are strictly increasing. A straightforward way to do this is to iterate over every possible subarray and then check if the subarray is strictly increasing or not. To do this, we would need to iterate over every pair of indices and then iterate over the elements between these indices to check if the elements are in the required order or not; hence this would be an $O(N^3)$ approach which is not very efficient.


Let's try to solve this problem by breaking it into subproblems; let's say the number of increasing subarrays between indices `0` and `x - 1` is `k`. Now, we consider the element at index `x`.

If we have `nums[x] > nums[x - 1]`, then we could take all `k` subarrays and simply append `nums[x]` to it. We also consider `nums[x]` as its own subarray, thus we have found `k + 1` new increasing subarrays ending at index `x`.

Otherwise, if `nums[x] <= nums[x - 1]`, adding this new element will invalidate any previous subarrays. Thus we only gain one new increasing subarray, the one consisting of only `nums[x]`.

Therefore, we keep the length of the current subarray `currSubarray`, which is strictly increasing, and for each new element that we iterate over, we will check if it's greater than the last element. If it is, we will increment `currSubarray`; otherwise, we will reset it to `1`. After each element, we will add `currSubarray` to the total count of subarrays we have found so far `subarrayCount`.



![Slide 1](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393A.png)

![Slide 2](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393B.png)

![Slide 3](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393C.png)

![Slide 4](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393D.png)

![Slide 5](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393E.png)

![Slide 6](images/slideshow_2393_Count_Strictly_Increasing_Subarrays_2393F.png)

 <br>


**Algorithm**

1. Initialize `currSubarray` and `subarrayCount` to `1`; This is because we will start from the element at index `1`, and hence the initial subarray is `[nums[0]]`.
2. Iterate over the elements from index `1` to the last index; For each index `i`:
    1. Check if `nums[i] > nums[i - 1]`, if true then increment `currSubarray`
    2. If the above condition is false, reset `currSubarray` to `1`.
    3. Add `currSubarray` to `subarrayCount`.
3. Return `subarrayCount`.

**Implementation**


```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums) {
        long long currSubarray = 1;
        long long subarrayCount = 1;
        
        for (int i = 1; i < nums.size(); i++) {
            // If the current element is greater, increase the subarrays.
            if (nums[i] > nums[i - 1]) {
                currSubarray++;
            } else {
                // Otherwise, reset the subarray size to 1.
                currSubarray = 1;
            }
            // Add the number of subarrays to the total count.
            subarrayCount += currSubarray;
        }
        
        return subarrayCount;
    }
};
```


**Complexity Analysis**

Here, $N$ is the number of elements in the array `nums`.

* Time complexity: $O(N)$

  We iterate over the array `nums` once, and hence the total time complexity is equal to $O(N)$.

* Space complexity: $O(1)$

  We don't require any extra space apart from the two variables `currSubarray` and `subarrayCount`, and hence the space complexity is constant.
  <br/>

---

### Approach 2: Greedy

**Intuition**

If we observe the previous approach closely, we will observe that for every additional element in the strictly increasing subarray, we are adding the updated length to the final answer. So, if the subarray length is `5`, that means we have added `{1, 2, 3, 4, 5}` to the answer during the previous 5 iterations. Hence, an increasing subarray with size `5` would contribute `1 + 2 + 3 + 4 + 5 = 15` increasing subarrays to the answer.

As per the above observation, we will just find the length of each strictly increasing subarray, and for each subarray of length `K`, we can add $\frac{K \cdot (K + 1)}{2}$ to the final answer. This is the formula [for the first K natural numbers](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF#Partial_sums).

**Algorithm**

1. Initialize  `subarrayCount` to `0`.
2. Iterate over the elements from index `0` to the last index; For each index `i`:
    1. Keep iterating over the elements while `nums[i] < nums[i + 1]`, i.e. elements are in strictly increasing order.
    2. Store the length of this subarray in the variable `currSubarray`. It should be initialized to `1` before the while loop.
    3. Add the value `(currSubarray * (currSubarray + 1)) / 2` to `subarrayCount`.
3. Return `subarrayCount`.

**Implementation**


```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums) {
        // Variable to store the total number of subarrays.
        long subarrayCount = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            // Length of the current subarray.
            long currSubarray = 1;
            
            while (i + 1 < nums.size() && nums[i] < nums[i + 1]) {
                currSubarray++;
                i++;
            }
            
            // Add the total number of different subarrays possible from this length.
            subarrayCount += (currSubarray * (currSubarray + 1)) / 2;
        }
        
        return subarrayCount;
    }
};
```


**Complexity Analysis**

Here, $N$ is the number of elements in the array `nums`.

* Time complexity: $O(N)$

  Despite the nested loop, each element is only iterated over once as `i` is strictly increasing, and hence the total time complexity is equal to $O(N)$.

* Space complexity: $O(1)$

  We don't require any extra space apart from the two variables `currSubarray` and `subarrayCount`, and hence the space complexity is constant.
  <br/>

---