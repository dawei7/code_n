[TOC]

## Video Solution

---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/537935313" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>
</div>

</br>

## Solution Article

---

### Approach 1: Linear search

**Intuition**

Let's try to find the missing number by linearly scanning the array from start to end.
Since we are given that the first and the last numbers cannot be removed, we can use them to get the required difference between each pair of consecutive elements.

$\text{difference} = \dfrac{\text{last value} - \text{first value}}{\text{number of values}}$

Once we have the difference we can use it to know what the value at each index is supposed to be. Using the `difference` as calculated above, and defining `initial` to be the value at index 0, we have the following:

$$\text{index 0} = \text{initial} \\
  \text{index 1} = \text{initial} + \text{difference} \\
  \text{index 2} = \text{initial} + 2 \cdot  \text{difference} \\
  \text{index 3} = \text{initial} + 3 \cdot  \text{difference} \\
  \dots \\
  \text{index n} = \text{initial} + \text{n} \cdot \text{difference}$$

Let's use this to figure out the first missing value in the Arithmetic Progression.

**Algorithm**

1. Get the value of `difference` using first and the last element, $difference = \text{last}_{value} - \text{first}_{value} / number_{of\_values}$.
2. Start with the first element as expected value $expected = \text{first}_{element}$
3. Run a loop from the first value to the last while checking if the current value is equal to `expected`. If it is not, then increase `expected` by `difference` for the next iteration.
4. Return the first `expected` value that doesn't match value in the array`.

```cpp
class Solution {
public:
    int missingNumber(vector<int> &arr) {
        int n = arr.size();

        // 1. Get the difference `difference`.
        int difference = (arr.back() - arr.front()) / n;

        // 2. The expected element equals the starting element.
        int expected = arr.front();

        for (int &val : arr) {
            // Return the expected value that doesn't match val.
            if (val != expected) return expected;

            // Next element will be expected element + `difference`.
            expected += difference;
        }
        return expected;
    }
};
```

**Complexity Analysis**

* Time complexity : $O(n)$. Where $n$ is the length of array `arr` since in the worst case we iterate over the entire array.

* Space complexity : $O(1)$. Algorithm requires constant space to execute.

<br />

---

### Approach 2: Binary Search

**Intuition**

In the previous approach we saw that we can get the value required at any index. Let's try to use that property to binary search for the missing value.

We know that there is only one missing number in the given progression. At any index `i` we can figure out if the value at index `i` is at the correct position by adding `difference` times `i` to the first value in the list, and then comparing it with the value at index `i`. if they match it means the missing value is in an index on the right of `i` else it's on the left of `i` or at `i`.

This fact can be used to find the index which has the first incorrect number using binary search because if `i` is the first index with an incorrect number all indices following `i` would be at incorrect positions (they should be present at 1 position further, since one number is missing) and all numbers before index `i` will be at correct position. This property is required for binary search to be possible.

**Algorithm**

1. Get the value of `difference` using first and the last element, $difference = \text{last}_{value} - \text{first}_{value} / number_{of\_values}$.
2. Start with left index $lo = 0$ and right index $hi = \text{arr.size}() - 1$.
3. Pick a mid point index $mid = (lo + hi) / 2$.
4. If $\text{arr}[mid] = \text{first}_{element} + mid * difference$. Binary search on the right of `mid` else binary search on left side of `mid` including `mid` itself.
5. End when there is a single index left as this would be the first index with incorrect value.
6. Return the value supposed to be at this index which would be $\text{first}_{element} + difference * index$.

```cpp
class Solution {
public:
    int missingNumber(vector<int> &arr) {
        int n = arr.size();

        // Get the difference `difference`.
        int difference = (arr.back() - arr.front()) / n;
        int lo = 0;
        int hi = n - 1;

        // Basic binary search template.
        while (lo < hi) {
            int mid = (lo + hi) / 2;

            // All numbers upto `mid` have no missing number, so search on the right side.
            if (arr[mid] == arr.front() + mid * difference) {
                lo = mid + 1;
            }

            // A number is missing before `mid` inclusive of `mid` itself.
            else {
                hi = mid;
            }
        }

        // Index `lo` will be the position with the first incorrect number.
        // Return the value that was supposed to be at this index.
        return arr.front() + difference * lo;
    }
};
```

**Complexity Analysis**

* Time complexity : $O(\log n)$.Where $n$ is the length of array `arr` since we cut the search space in half at every iteration.

* Space complexity : $O(1)$. Algorithm requires constant space to execute.

</br>