## Solution

---

### Approach 1: Using Separate Space

#### Intuition

We are required to find the running sum of numbers $\text{nums}[i]$ in the input array where `i` ranges from `0` to `n-1` and `n` is the size of the input array. We can see that the running sum is the sum of all of the elements from index `0` to index `i` inclusive. Since we start building our output array at index `0`, at each index `i` we have already calculated the sum of all numbers up to and including index `i-1`. Thus, instead of recalculating the sum, we can get the result for index `i` by simply adding the element at index `i` to the previously calculated running sum for index `i-1`.

#### Algorithm

1. Define an array `result`.
2. Initialize the first element of `result` with the first element of the input array.
3. At index `i` append the sum of the element $\text{nums}[i]$ and previous running sum $result[i - 1]$ to the `result` array.
4. We repeat step 3 for all indices from `1` to `n-1`.

#### Implementation

```cpp
class Solution {
public:
    vector<int> runningSum(vector<int> &nums) {
        // Initialize result array with first element in nums.
        vector<int> result = {nums[0]};

        for (int i = 1; i < nums.size(); i++) {
            // Result at index `i` is sum of result at `i-1` and element at `i`.
            result.push_back(result.back() + nums[i]);
        }
        return result;
    }
};
```

#### Complexity Analysis

* Time complexity: $O(n)$ where $n$ is the length of the input array. This is because we use a single loop that iterates over the entire array to calculate the running sum.

* Space complexity: $O(n)$ We declare an array `result` of size `n` to store the running sum and access the previous value to calculate the next value. Although output space is not considered when calculating space complexity, our `result` array is used for calculating the answer, so its space is considered.

<br />

---

### Approach 2: Using Input Array for Output

#### Intuition

In the previous approach we created an extra array to store our results. However, we do not actually need to do so. We can obtain the same result without using extra space by performing the same operations on the input array instead.

#### Algorithm

1. Increase $\text{nums}[i]$ by the previous index's running sum.  The previous index's running sum is stored at index `i-1` in the input array.
2. We repeat step 1 for all indices from `1` to `n-1`.

#### Implementation

```cpp
class Solution {
public:
    vector<int> runningSum(vector<int> &nums) {
        for (int i = 1; i < nums.size(); i++) {
            // Result at index `i` is sum of result at `i-1` and element at `i`.
            nums[i] += nums[i - 1];
        }
        return nums;
    }
};
```

#### Complexity Analysis

* Time complexity: $O(n)$ where $n$ is the length of input array.

* Space complexity: $O(1)$ since we don't use any additional space to find the running sum. _Note_ that we do not take into consideration the space occupied by the output array.

</br>