[TOC]

## Solution

--- 

### Overview

The problem involves analyzing an integer array `nums` to count the number of subarrays in which the maximum element of `nums` appears at least `k` times, where `k` is given as an input.

> A **subarray** is a contiguous sequence of elements within an array.

Algorithmically, solving this problem involves traversing the array and tracking the frequency of the maximum element in a dynamic range. The algorithm should efficiently update the frequency as it progresses through the array.

This problem is similar to scenarios where we need to find the frequency of occurrence of a particular event or condition within a given time frame or sequence. 
- For instance in financial data analysis, one might be interested in identifying periods where a stock's price reaches its maximum value at least a certain number of times within a given timeframe. This can provide insights into potential trends or patterns.
- Similarly, in network traffic analysis, identifying subintervals where the network experiences maximum data transfer rates beyond a certain threshold can be crucial for optimizing network performance or identifying potential issues.

---

### Approach 1: Sliding Window

#### Intuition

Since we are concerned with contiguous sequences and the frequency of a specific element, the sliding window algorithm emerges as a potentially effective approach. The sliding window algorithm is useful when handling contiguous segments within an array.

> A sliding window is maintained by two indices, one of which indicates the start of the window, and the other the end of the window.

As we traverse the array, we should maintain the frequency of the maximum element within the window. Whenever we encounter the maximum element, we increment the frequency. The objective is to count the windows where this frequency is greater than or equal to the given threshold, `k`.

To achieve this objective, whenever the frequency of the maximum element in the window is greater than `k`, we initiate a process to shrink the window. This involves adjusting the starting point of the window (let's track this by index variable `start`) until the frequency of the maximum element in the window is exactly `k` to identify subarrays that have the maximum element appear at least `k` times.

The index variable `start` accounts for multiple starting positions for valid subarrays (where the frequency of the maximum is at least `k`) at the current ending position (let's track this by index variable `end`). By adding `start` to the answer, we ensure that we account for all valid subarrays ending at the current index `end`. This is because of the fact that for a given ending position `end`, there exist `start + 1` possible starting positions, each contributing to a valid subarray.

As we traverse the array and execute these steps, we accumulate the count of valid subarrays. The final result is the total count of such subarrays.



![Slide 1](images/slideshow_2962-1_2962_fix-1.png)

![Slide 2](images/slideshow_2962-1_2962_fix-2.png)

![Slide 3](images/slideshow_2962-1_2962_fix-3.png)

![Slide 4](images/slideshow_2962-1_2962_fix-4.png)

![Slide 5](images/slideshow_2962-1_2962_fix-5.png)

![Slide 6](images/slideshow_2962-1_2962_fix-6.png)

![Slide 7](images/slideshow_2962-1_2962_fix-7.png)

![Slide 8](images/slideshow_2962-1_2962_fix-8.png)

![Slide 9](images/slideshow_2962-1_2962_fix-9.png)

![Slide 10](images/slideshow_2962-1_2962_fix-10.png)

![Slide 11](images/slideshow_2962-1_2962_fix-11.png)

![Slide 12](images/slideshow_2962-1_2962_fix-12.png)

![Slide 13](images/slideshow_2962-1_2962_fix-13.png)

![Slide 14](images/slideshow_2962-1_2962_fix-14.png)

![Slide 15](images/slideshow_2962-1_2962_fix-15.png)

![Slide 16](images/slideshow_2962-1_2962_fix-16.png)

![Slide 17](images/slideshow_2962-1_2962_fix-17.png)



#### Algorithm

1. **Initialization:**
   - Initialize variables `max_element`, `ans`, `start`, and `max_elements_in_window`.
   - `max_element` stores the maximum element in the given array `nums`.
   - `ans` will be the final count of subarrays meeting the condition.
   - `start` is a pointer for the start of the window.
   - `max_elements_in_window` stores the frequency of the `max_element` within the current window.

2. **Iterating through the array:**
   - Iterate through each element in the array using a `for` loop with index `end` ranging from 0 to the length of `nums`.

3. **Counting frequency of `max_element` in the current window:**
   - Check if the current element `nums[i]` is equal to `max_element`.
   - If true, increment `max_elements_in_window` as it represents the frequency of `max_element` in the current window.

4. **Sliding window to meet the condition:**
   - Use a `while` loop to shrink the window (`start` pointer) until `max_elements_in_window` is equal to `k`.
   - Inside the `while` loop, decrement `max_elements_in_window` if the element at the window's start (`nums[start]`) is equal to `max_element`.
   - Increment `start` to move the window to the right.

5. **Counting subarrays:**
   - Add `start` to the `ans` variable. This is done inside the `for` loop, so it accumulates the count of subarrays meeting the condition.

6. **Returning the result:**
   - After the loop completes, return the final count stored in the `ans` variable.

#### Implementation


```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        ans = start = max_elements_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                max_elements_in_window += 1
            while max_elements_in_window == k:
                if nums[start] == max_element:
                    max_elements_in_window -= 1
                start += 1
            ans += start
        return ans
```


#### Complexity Analysis

Let $N$ be the length of `nums`.

* Time complexity: $O(N)$.
  - Finding the maximum element in `nums` requires linear traversal of the array, taking $O(N)$ computational time.
  - The outer `for` loop iterates through each element in the array exactly once, as indicated by the range from $0$ to $N - 1$.
  - Inside this loop, the `while` loop with the `start` pointer performs a sliding window operation. However, note that the `start` pointer is increased, and `max_elements_in_window` is decreased within this loop. The `start` pointer is never decreased after it is increased in the while loop. Hence, once an element is processed in the `while` loop, it will not be revisited. Therefore, each element is processed at most twice: once during the outer loop and at most once during the `while` loop.
  - In the worst case, the `while` loop could iterate through the entire length of the array during its lifetime. However, since each element is processed at most twice, the total number of iterations across all elements is linear, making the time complexity of the algorithm $O(N)$.

* Space complexity: $O(1)$. The space complexity is $O(1)$ as the algorithm uses a constant amount of extra space regardless of the size of the input array.

---

### Approach 2: Track Indexes of Max Element

#### Intuition

In the previous approach, the variable `start` was used to monitor potential starting positions corresponding to a given ending position within the array `nums`. We can also observe that for each valid subarray that began at an index `r` that contains a max element and ended at some index `p`, all subarrays starting at any index before `r` and ending at `p` are also valid subarrays. Upon examining the code, we can see that after the `while` loop completes, `start` consistently points to the index following the index containing a `max_element`. With this understanding, we can store all indexes where a `max_element` is found in an array. If there are more than `k` maximum elements within the array at any given point, we can identify the index of the `max_element` that appeared `k` maximum elements ago.

```
For example:

nums = [1,3,2,3,3], k = 2
max_element = 3
indexes_of_max_elements = [1, 3, 4]

-------------------
For the index 3,
       ↓
[1,3,2,3,3]
index of the max element that appeared k maximum elements ago is  1
   ⌄   ↓
[1,3,2,3,3]
Add one to the index to find the number of possible starting positions:
1 + 1 = 2.
This indicates that the possible starting positions for the ending
position 3 are [0, 1].

-------------------
For the index 4,
         ↓
[1,3,2,3,3]
the index of the max element that appeared k maximum elements ago is 3
       ⌄ ↓
[1,3,2,3,3]
Add one to the index to find the number of possible starting positions:
1 + 3 = 4.
This indicates that the possible starting positions for the ending
position 4 are [0, 1, 2, 3].

```

Therefore, for any `index` where we've observed more than `k` maximum elements, the number of potential starting positions equals 1 plus the index where we encountered the `max_element` `k` maximum elements ago.

#### Algorithm

1. **Initialization:**
   - Initialize variables `max_element`, `indexes_of_max_elements`, and `ans`.
   - `max_element` stores the maximum element in the given array `nums`.
   - `indexes_of_max_elements` is a list that stores the indexes of occurrences of the maximum element.
   - `ans` will be the final count of subarrays meeting the condition.

2. **Iterating through the array:**
   - Iterate through each element in the array along with its index.

3. **Finding indexes of maximum element:**
   - Check if the current element is equal to `max_element`.
   - If true, append the index of the current element to the `indexes_of_max_elements` list.

4. **Counting frequency of maximum element:**
   - Calculate the frequency of occurrences of the maximum element by finding the length of the `indexes_of_max_elements` list.

5. **Checking condition for subarrays:**
   - Check if the frequency of the maximum element is greater than or equal to `k`.
   - If true, increment `ans` by the index of the `(len(indexes_of_max_elements) - k)`-th occurrence of the maximum element plus 1.
   - This step counts the number of subarrays ending at the current index where the maximum element appears at least `k` times.

6. **Returning the result:**
   - After iterating through all elements, return the final count stored in the `ans` variable, which represents the total count of subarrays meeting the given condition.

#### Implementation


```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        indexes_of_max_elements = []
        ans = 0

        for index, element in enumerate(nums):

            if element == max_element:
                indexes_of_max_elements.append(index)

            freq = len(indexes_of_max_elements)
            if freq >= k:
                ans += indexes_of_max_elements[-k] + 1

        return ans
```


#### Complexity Analysis

Let $N$ be the length of `nums`.

* Time complexity: $O(N)$. Initializing `max_element` incurs a time complexity of $O(N)$ since each element of `nums` is checked. The `for` loop used to count subarrays also incurs a time complexity of $O(N)$.

* Space complexity: $O(N)$. In the worst case all the elements in `nums` are equal to `max_element`. In this case, the final length of `indexes_of_max_elements` will be `N`. Hence, the worst-case space complexity is $O(N)$.

---