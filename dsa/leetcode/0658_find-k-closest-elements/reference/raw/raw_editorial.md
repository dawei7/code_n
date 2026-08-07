[TOC]

## Solution

---

### Approach 1: Sort With Custom Comparator

**Intuition**

This first approach is the most intuitive one that most people probably think of first - check every number in `arr` for its distance from `x` and sort the numbers by this criterion. Then, the answer will be the first `k` elements of our new sorted array.

**Algorithm**

1. Create a new array `sortedArr`, that is `arr` sorted with a custom comparator. The comparator should be `abs(x - num)` for each `num` in `arr`. Sorting the array in ascending order means that the first `k` elements will be the `k` closest elements to `x`.

2. We also have to sort the "sorted" array, since the problem wants our output in ascending order. Return the first `k` elements of `sortedArr`, sorted by value, in ascending order.

**Implementation**


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Sort using custom comparator
        sorted_arr = sorted(arr, key = lambda num: abs(x - num))

        # Only take k elements
        result = []
        for i in range(k):
            result.append(sorted_arr[i])
        
        # Sort again to have output in ascending order
        return sorted(result)
```



**Complexity Analysis**

Given $$N$$ as the length of `arr`,

* Time complexity: $$O(N \cdot \log(N) + k \cdot \log(k))$$.

    To build `sortedArr`, we need to sort every element in the array by a new criteria: `x - num`. This costs $$O(N \cdot \log(N))$$. Then, we have to sort `sortedArr` again to get the output in ascending order. This costs $$O(k \cdot \log(k))$$ time since `sortedArr.length` is only `k`.

* Space complexity: $$O(N)$$.

    Before we slice `sortedArr` to contain only `k` elements, it contains every element from `arr`, which requires $$O(N)$$ extra space. Note that we can use less space if we sort the input in place.
    
<br/>

### Approach 2: Binary Search + Sliding Window

**Intuition**

Every time you see a problem that involves a sorted array, you should consider binary search. In the previous approach, we considered every single number from `arr` as a potential candidate for the final output. However, when `arr.length` is very large, and `k` is very small, we do not care about a vast majority of the numbers in `arr`, and we should avoid looking at them.

Let's start by finding the closest number to `x` in `arr`. Logically, the second closest number to `x` must be directly beside the first number, either to the left or right. Then, the third closest number to `x` must be either to the left of the first number or to the right of the second number. This pattern continues, and is true because the input is sorted.

Using two pointers, we can maintain a sliding window that will expand to contain the `k` closest elements to `x`. Let's use binary search to efficiently find the closest number to `x` in `arr`, and start our pointers there. Then, we should expand our window by moving the pointers either left or right depending on which number is closer to `x`.



![Slide 1](images/slideshow_658_K_Closest_1_658_1.png)

![Slide 2](images/slideshow_658_K_Closest_1_658_2.png)

![Slide 3](images/slideshow_658_K_Closest_1_658_3.png)

![Slide 4](images/slideshow_658_K_Closest_1_658_4.png)

![Slide 5](images/slideshow_658_K_Closest_1_658_5.png)

![Slide 6](images/slideshow_658_K_Closest_1_658_6.png)

![Slide 7](images/slideshow_658_K_Closest_1_658_7.png)

![Slide 8](images/slideshow_658_K_Closest_1_658_8.png)

![Slide 9](images/slideshow_658_K_Closest_1_658_9.png)



**Algorithm**

1. As a base case, if `arr.length == k`, return `arr`.

2. Use binary search to find the index of the closest element to `x` in `arr`. Initailize two pointers `left` and `right`, with `left` set equal to this index, and `right` equal to this index plus one.

3. While the window's size is less than `k`, check which number is closer to `x`: `arr[left]` or `arr[right]`. Whichever pointer has the closer number, move that pointer towards the edge to include that element in our output.

4. Return the elements inside `arr` contained within the window defined between `left` and `right`.

**Implementation**

In Python, the [bisect](https://docs.python.org/3/library/bisect.html) module provides super handy functions that does binary search for us.


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find the closest element and initialize two pointers
        left = bisect_left(arr, x) - 1
        right = left + 1

        # While the window size is less than k
        while right - left - 1 < k:
            # Be careful to not go out of bounds
            if left == -1:
                right += 1
                continue
            
            # Expand the window towards the side with the closer number
            # Be careful to not go out of bounds with the pointers
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Return the window
        return arr[left + 1:right]
```


Given $$N$$ as the length of `arr`,

**Complexity Analysis**

* Time complexity: $$O(\log(N) + k)$$.

    The initial binary search to find where we should start our window costs $$O(\log(N))$$. Our sliding window initially starts with size 0 and we expand it one by one until it is of size `k`, thus it costs $$O(k)$$ to expand the window.

* Space complexity: $$O(1)$$

    We only use integer variables `left` and `right` that are $$O(1)$$ regardless of input size. Space used for the output is not counted towards the space complexity.
    
<br/>

---

### Approach 3: Binary Search To Find The Left Bound

**Intuition**

We can actually find the bounds of our sliding window much faster - and independent of `k`! First of all, what is the biggest index the left bound could be? If there needs to be `k` elements, then the left bound's upper limit is `arr.length - k`, because if it were any further to the right, you would run out of elements to include in the final answer.

As demonstrated in Approach 2, binary search is typically used to find if an element exists or where an element belongs in a sorted array. The beauty of algorithms lies in how abstract they are - with some clever thinking, we can apply binary search in a unique way to move our `left` and `right` pointers closer and closer to the left bound of our answer.

Let's consider two indices at each binary search operation, the usual `mid`, and some index `mid + k`. The relationship between these indices is significant because **only one of them could possibly be in a final answer**. For example, if `mid = 2`, and `k = 3`, then `arr[2]` and `arr[5]` could not possibly both be in the answer, since that would require taking 4 elements `[arr[2], arr[3], arr[4], arr[5]]`.

This leads us to the question: how do we move our pointers `left` and `right`? If the element at `arr[mid]` is closer to `x` than `arr[mid + k]`, then that means `arr[mid + k]`, as well as every element to the right of it can never be in the answer. This means we should move our `right` pointer to avoid considering them. The logic is the same vice-versa - if `arr[mid + k]` is closer to `x`, then move the left pointer.



![Slide 1](images/slideshow_658_K_Closest_2_658_10.png)

![Slide 2](images/slideshow_658_K_Closest_2_658_11.png)

![Slide 3](images/slideshow_658_K_Closest_2_658_12.png)

![Slide 4](images/slideshow_658_K_Closest_2_658_13.png)



**Algorithm**

1. Initalize two variables to perform binary search with, `left = 0` and `right = len(arr) - k`.

2. Perform a binary search. At each operation, calculate `mid = (left + right) / 2` and compare the two elements located at `arr[mid]` and `arr[mid + k]`. If the element at `arr[mid]` is closer to `x`, then move the right pointer. If the element at `arr[mid + k]` is closer to `x`, then move the left pointer. Remember, the smaller element always wins when there is a tie.

3. At the end of the binary search, we have located the leftmost index for the final answer. Return the subarray starting at this index that contains `k` elements.

**Implementation**


```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
```



**Complexity Analysis**

Given $$N$$ as the length of `arr`,

* Time complexity: $$O(\log(N - k) + k)$$.

    Although finding the bounds only takes $$O(\log(N - k))$$ time from the binary search, it still costs us $$O(k)$$ to build the final output.

	Both the Java and Python implementations require $$O(k)$$ time to build the result.  However, it is worth noting that if the input array were given as a list instead of an array of integers, then the Java implementation could use the `ArrayList.subList()` method to build the result in $$O(1)$$ time.  If this were the case, the Java solution would have an (extremely fast) overall time complexity of $$O(\log(N - k))$$.

* Space complexity: $$O(1)$$.

    Again, we use a constant amount of space for our pointers, and space used for the output does not count towards the space complexity.

<br/>

---