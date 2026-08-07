[TOC]

## Solution

--- 

### Overview

In this problem, we are given an integer `num` where every digit is either `6` or `9`, we can change up to 1 digit (from `6` to `9` or vice versa).

The task is to return the largest integer we can get.

After observation, we can get these conclusions as follows:

- We can only increment `num` by converting a digit `6` to `9`. 
- We should always convert the **highest** digit `6`. Suppose `num = 669`, it has multiple digits `6`, we must convert the first one to make it `969` rather than `699`. 
- If every digit of `num` is `9`, we only need to return `num` since it already stands for the largest integer.

More examples:

![img](images/1323-1.png)

Hence, the task equals finding the highest digit `6` (if it exists) and replacing it with `9`.

---

### Approach 1: Convert the integer to an iterable object

#### Intuition   

The most intuitive method to find the first digit `6` is to traverse through each digit of `num` from high to low, as we discussed in the overview section. 

However, we can't traverse over an integer in C++, Java, or Python, nor can we modify it. Hence, we can first convert it to an iterable and mutable object, such as a string in C++, a string builder in Java, or a list in Python, and traverse over the object to locate the first occurrence of `6`.


<br>

#### Algorithm

1) Convert the input integer `num` to an iterable and mutable object `num_obj`.
2) Iterate over `num_obj`, if we find a digit `6`, replace it with `9` and stop the iteration.
3) Return the integer converted from the modified `num_obj`.

#### Implementation


```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the input 'num' to a list of character 'num_char_list'.
        num_char_list = list(str(num))
        
        # Iterate over the list (from high to low).
        for i, cur_char in enumerate(num_char_list):
            # If we find the first '6', replace it with '9' and break the loop.
            if cur_char == '6':
                num_char_list[i] = '9'
                break
        
        # Convert the modified char list to integer and return it.
        return int("".join(num_char_list))
```



#### Complexity Analysis

Let $$L$$ be the maximum number of digits `nums` can have ($$L = 4$$ in this problem).

* Time complexity: $$O(L)$$

    - Since the input number `num` has up to most $$L$$ digits, it requires $$O(L)$$ time to convert it to an equivalent object and vice versa.
    - To sum up, the time complexity is $$O(L)$$.
    

* Space complexity: $$O(L)$$
    - We create an object of length $$L$$.

<br/>



---

### Approach 2: Use built-in function

#### Intuition   

Similar to the previous approach, but with some built-in features. We don't need to manually traverse through the converted object. 

Although this solution is concise, it is not necessarily the best approach for interviews.

<br>

#### Algorithm

- Convert the input number `num` to the string `num_string`.
- Use the built-in function to replace the first `6` to `9` if it exists.
- Return the integer converted from the modified `num_string`.

#### Implementation


```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert the input 'num' to the string 'num_string'.
        num_string = str(num)

        # Use the built-in function to replace the first '6' with '9'.
        # Return the integer converted from the modified 'num_string'.
        return int(num_string.replace('6', '9', 1))
```



#### Complexity Analysis

Let $$L$$ be the maximum number of digits `nums` can have ($$L = 4$$ in this problem).

* Time complexity: $$O(L)$$
    - We need to look for the first occurrence of digit `6` and make at most one replacement, which takes $$O(L)$$ time.

* Space complexity: $$O(L)$$
    - We convert `num` to a string of length $$L$$, therefore, the space complexity is $$O(L)$$.

<br/>



---

### Approach 3: Check the remainder

#### Intuition   

Can we locate the highest digit of `6` without converting `num` to string? The answer is Yes! 

We can always get the last digit of a non-negative integer by taking the remainder of `num` divided by $$10$$, for example, to get the last digit of `613`: 

$$613\ \%\ 10 = 3$$

How about the second last digit? We can 'remove' the last digit by taking the quotient of `num` and $$10$$.

$$613\ /\ 10 = 61$$


Therefore, we can check every digit of `num` from low to high and record the highest digit `6`. Assume that it is the `k-th` digit (`0` based), 'converting' this digit from `6` to `9` equals adding $$3 \cdot 10^{k}$$ to the original integer `num`! As shown in the picture below, we find the highest `6` is the **2nd** digit and increment `9669` by $$3\ \cdot \ 10^{2}$$ to make the answer `9969`!

![img](images/1323-2.png)

Take the picture below as an example.

![img](images/1323-3.png)

<br>

#### Algorithm

1) Initialize an integer `num_copy = num` for checking digits.
2) Get the remainder of `num_copy` and $$10$$.
3) If the remainder is $$6$$, record the current digit as the first (highest) digit of `6`.
4) Divide `num_copy` by $$10$$ using integer division.
    - If `num_copy = 0`, go to step 5.
    - Otherwise, repeat step 2.
5) If we find the first digit of `6`, let's say `index_first_six`, increment `num` by $$3 \cdot 10^{index\_first\_six}$$ and return `num`. Otherwise, just return `num`. 


#### Implementation


```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        # Since we start with the lowest digit, initialize curr_digit = 0.
        curr_digit = 0
        index_first_six = -1
        num_copy = num
        
        # Check every digit of 'num_copy' from low to high.
        while num_copy:
            # If the current digit is '6', record it as the highest digit of 6.
            if num_copy % 10 == 6:
                index_first_six = curr_digit
            
            # Move on to the next digit.
            num_copy //= 10
            curr_digit += 1
        
        # If we don't find any digit of '6', return the original number,
        # otherwise, increment 'num' by the difference made by the first '6'.
        return num if index_first_six == -1 else num + 3 * 10 ** index_first_six
```



#### Complexity Analysis

Let $$L$$ be the maximum number of digits `nums` can have ($$L = 4$$ in this problem).

* Time complexity: $$O(L)$$
    - We need to make at most $$L$$ time of integer divisions, which takes $$O(L)$$ time.

* Space complexity: $$O(1)$$
    - We only need to update several variables, which takes $$O(1)$$ space.



<br/>