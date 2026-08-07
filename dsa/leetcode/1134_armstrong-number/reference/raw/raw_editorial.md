[TOC]

## Solution

---

### Approach 1: Calculate k by Converting to String

**Intuition**

Per the definition of an Armstrong number, once we have the value of `k` all we need to do is add the **k'th** power of each digit and compare the final result to the original number. A simple way to calculate the length of an integer (number of digits in `n`) is by converting the integer to a string and then getting the length of the string.

**Algorithm**

1. Get the number of digits in `n` by converting it to a string and getting the `length`. Pass these values into the function created below.
2. Let's create a function `getSumOfKthPowerOfDigits()` that takes in the parameters `n` and `k` and returns the sum of taking the k'th power of each digit. The function works as explained further.
   1. Create a variable `result` which will store the final result of the operations to be applied on `n`.
   2. Get the `last_digit` of `n` by using the formula `n % 10`.
   3. Add `last_digit` raised to the power of `k` to the result.
   4. Remove the `last_digit` of `n` by using the formula `n /= 10`.
   5. Repeat steps 1 - 4 until `n != 0`.
3. Return `true` if `result` equals the original number `n`.


```cpp
class Solution {
public:
    int getSumOfKthPowerOfDigits(int n, int k) {
       // `result` stores the result of sum of k'th power of each digit.
       int result = 0;

       // Run until n is not 0
       while (n != 0) {
           // Modulo 10 gives us the last digit
           // Add digit ^ k to the result
           result += pow(n % 10, k);

           // Remove the last digit.
           n /= 10;
       }
       return result;
    }
    bool isArmstrong(int n) {
        // Get length of the number by converting to string.
        int length = to_string(n).length();

        // Return true if Sum of k'th power of digits equals original number.
        return getSumOfKthPowerOfDigits(n, length) == n;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(M)$$, where $$M$$ is the number of digits in integer `n`. Since we need to iterate through all digits in `n`.

* Space complexity : $$O(1)$$


<br />

---

### Approach 2: Calculate k by Using Log

**Intuition**

In the previous approach we saw that we can get the value of `k` by converting `n` to a string. Let's look at a mathematical way to get this value.

Recall that in math, the `log` function can be used to get the number of digits in a number.

Let's see how $${\log_{10}}$$ works:

$$
  {\log_{10} 1} = 0 \\
  {\log_{10} 2} = 0.301 \\
  {\log_{10} 9} = 0.954 \\
  {\log_{10} 10} = 1 \\
  {\log_{10} 99} = 1.995 \\
  {\log_{10} 100} = 2 \\
  \dots \\
  {\log_{10} 1000} = 3
$$

Thus, we can see that we need the value of $$\text{floor}(\log_{10} n) + 1$$ which will be the number of digits in `n`. Below, we have implemented this intuition.

**Algorithm**

1. Get the number of digits in `n` by calculating $$\text{floor}(\log_{10} n) + 1$$ and adding $$1$$.
2. Call `getSumOfKthPowerOfDigits()` (as defined in Approach 1) with `n` and `length` as `k`.
3. Return `true` if `result` of this function equals the original number `n`.


```cpp
class Solution {
public:
    int getSumOfKthPowerOfDigits(int n, int k) {
       // `result` stores the result of sum of k'th power of each digit.
       int result = 0;

       // Run until n is not 0
       while (n != 0) {
           // Modulo 10 gives us the last digit
           // Add digit ^ k to the result
           result += pow(n % 10, k);

           // Remove the last digit.
           n /= 10;
       }
       return result;
    }
    bool isArmstrong(int n) {
        // Get length of the number by getting floor of log10 and adding 1.
        int length = log10(n) + 1;

        // Return true if Sum of k'th power of digits equals original number.
        return getSumOfKthPowerOfDigits(n, length) == n;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(M)$$, where $$M$$ is the number of digits in integer `n`. Since we need to iterate through all digits in `n`.

* Space complexity : $$O(1)$$

</br>

---

### Approach 3: Calculate k Without Built-in Methods

**Interview Tip:** Often for simple problems such as this one, the interviewer will ask you to solve it *without using any built-in or library functions*. It is important for you to practice solving problems with this constraint.

**Intuition**

In the previous solutions, we used built-in methods to get the number of digits in `n`. Now let's try to get this value manually. We can use the idea from the previous solutions of dividing `n` by `10` to remove the last digit. All we need to do is keep on dividing `n` by `10` and increasing a `length` counter until `n` is `0`. This will give us the exact number of digits in `n`.

**Algorithm**

1. Store `n` in a temporary variable `tempN`; we'll use this to find the length of `n`.
2. Initialize the `length` counter to `0`.
3. Remove the last digit of `tempN` by dividing `tempN` by `10`.
4. Increment the `length` counter.
5. Repeat steps 3 and 4 while `tempN != 0`.
6. `length` should now contain the number of digits in `n`.
8. Call `getSumOfKthPowerOfDigits()` with `n` and `length` as `k`.
9. Return `true` if the `result` of this function equals the original number `n`.


```cpp
class Solution {
public:
    int getSumOfKthPowerOfDigits(int n, int k) {
       // `result` stores the result of sum of k'th power of each digit.
       int result = 0;

       // Run until n is not 0
       while(n != 0) {
           // Modulo 10 gives us the last digit
           // Add digit ^ k to the result
           result += pow(n % 10, k);

           // Remove the last digit.
           n /= 10;
       }
       return result;
    }
    bool isArmstrong(int n) {
        // Initilize length counter to 0.
        int length = 0;

        // Store `n` in a temporary variable to find the length.
        int tempN = n;

        // Get the number of digits in integer `n`.
        while (tempN) {
            length++;
            tempN /= 10;
        }

        // Return true if Sum of k'th power of digits equals original number.
        return getSumOfKthPowerOfDigits(n, length) == n;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(M)$$, where $$M$$ is the number of digits in integer `n`. Since we need to iterate through all digits in `n`.

* Space complexity : $$O(1)$$