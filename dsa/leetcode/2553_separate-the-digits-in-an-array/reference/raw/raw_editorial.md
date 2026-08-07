### Approach: Simulation

#### Intuition

The problem requires splitting each number in the array into its individual digits and then reassembling those digits in order to form a new array.

When splitting a number $x$ digit by digit:
1. Taking $x \bmod 10$ gives the digit in the units place, which we store in a temporary array.
2. Dividing $x$ by 10 removes the digit in the units place.

We repeat this process until $x$ becomes 0, which gives us the digits of $x$ in reverse order. Since all values of $x$ in the input are positive integers, we do not need to handle the case where $x$ starts as 0.

After that, we traverse the temporary array in reverse order and append each digit to the result array. Once done, we clear the temporary array and continue with the next number. Finally, we return the result array.

#### Implementation


```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10
            res.extend(tmp[::-1])
        return res
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $M$ be the maximum value in $\textit{nums}$.

- Time complexity: $O(n \log M)$.

- Space complexity: $O(\log M)$.
  
  The output array is not included in the space complexity.

### Approach 2: Reverse Traversal

#### Intuition

In Approach 1, we use a temporary array to store the digits and then append them in reverse order to the result array. Instead, we can traverse $\textit{nums}$ in reverse order and directly append each digit of $x$ to the result array as we extract it, without using a temporary array. Finally, we reverse the result array to obtain the correct order.

#### Implementation


```python
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            while x > 0:
                res.append(x % 10)
                x //= 10
        res.reverse()
        return res
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $M$ be the maximum value in $\textit{nums}$.

- Time complexity: $O(n \log M)$.

- Space complexity: $O(1)$.

---