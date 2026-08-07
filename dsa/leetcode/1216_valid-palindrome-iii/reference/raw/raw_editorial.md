[TOC]

## Solution

---

### Approach 1: Top-Down DP (2D)

**Intuition**

Let's try to find the minimum number of character that can be removed to make the string a palindrome. If we see that the minimum number is less than or equal to `k` we can conclude that it is indeed a K-Palindrome, else it is not.

**Similar Problems:**

* [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
* [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)


**Algorithm**

How do we find the minimum characters to be removed to make it a palindrome?
Let's imagine matching the characters of the string like a palindrome, from the beginning and the end with 2 pointers `i` and `j`.
We may encounter the following two scenarios:

1. The character at `i` matches character at `j`.
2. The characters don't match each other.

For case 1 we just increase the pointer `i` and decrease the pointer `j`, `i++` and `j--` respectively.

In the second case we have 2 options:

* Remove character at `j` and see if the previous character matches character at `i`.

Or

* Remove character at `i` and see if the next character matches character at `j`.

Since we are not actually removing the characters from the string but just calculating the number of characters to be removed,
in case 1 we decrement the pointer `j` by 1 and `i` stays as it is, as we still need a character to match character at `i`
and in case 2 we increment the pointer `i` by 1 and `j` stays as it is, as we still need a character to match character at `j`.
In both the cases we remove 1 character and thus it adds 1 to the cost.

We can then use these two different pairs of new `i` and `j` values (`i+1, j` and `i, j-1`) to again repeat the process and get the minimum result of them as our result for current pair `i, j`.

We can see that this is recursive and thus we can use recursion with caching to store the repeated values.


```cpp
class Solution {
public:
    vector<vector<int>> memo;
    int isValidPalindrome(string &s, int i, int j) {

        // Base case, only 1 letter remaining.
        if (i == j)
            return 0;

        // Base case 2, only 2 letters remaining.
        if (i == j - 1)
            return s[i] != s[j];

        // Return the precomputed value if exists.
        if (memo[i][j] != -1)
            return memo[i][j];

        // Case 1: Character at `i` equals character at `j`
        if (s[i] == s[j])
            return memo[i][j] = isValidPalindrome(s, i + 1, j - 1);

        // Case 2: Character at `i` does not equal character at `j`.
        // Either delete character at `i` or delete character at `j`
        // and try to match the two pointers using recursion.
        // We need to take the minimum of the two results and add 1
        // representing the cost of deletion.
        return memo[i][j] = 1 + min(isValidPalindrome(s, i + 1, j), isValidPalindrome(s, i, j - 1));
    }
    bool isValidPalindrome(string s, int k) {
        memo.resize(s.length(), vector<int>(s.length(), -1));

        // Return true if the minimum cost to create a palindrome by only deleting the letters
        // is less than or equal to `k`.
        return isValidPalindrome(s, 0, s.length() - 1) <= k;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Where `n` is the length of string `s`. This is due to the fact that we try to find result for all combinations of `i` and `j` where `i` and `j` range from `0` to `n`, to compute a combination we perform an $$O(1)$$ operation thus the final complexity is $$O(n^2)$$.

* Space complexity : $$O(n^2)$$. Where `n` is the length of string `s`. This is due to caching all the results in `memo` table. The recursion stack depth can reach at max $$O(n)$$ depth. Thus the complexity is dominated by the space required for `memo`.


<br />

---

### Approach 2: Bottom-Up DP (2D)

**Algorithm**

Instead of filing up our `memo` table from top to bottom, let's try filling it from bottom to top. All we need to do is fill all the combinations of `i` and `j` in the correct order so that we have all the results required for the next state (combination of `i`, `j`) before we move to the next state (combination of `i`, `j`).


```cpp
class Solution {
public:
    bool isValidPalindrome(string s, int k) {
        vector<vector<int>> memo(s.length(), vector<int>(s.length(), 0));

        // Generate all combinations of `i` and `j` in the correct order.
        for (int i = s.length() - 2; i >= 0; i--)
            for (int j = i + 1; j < s.length(); j++) {

                // Case 1: Character at `i` equals character at `j`
                if (s[i] == s[j])
                    memo[i][j] = memo[i + 1][j - 1];

                // Case 2: Character at `i` does not equal character at `j`.
                // Either delete character at `i` or delete character at `j`
                // and try to match the two pointers using recursion.
                // We need to take the minimum of the two results and add 1
                // representing the cost of deletion.
                else
                    memo[i][j] = 1 + min(memo[i + 1][j], memo[i][j - 1]);
            }

        // Return true if the minimum cost to create a palindrome by only deleting the letters
        // is less than or equal to `k`.
        return memo[0][s.length() - 1] <= k;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Where `n` is the length of string `s`. This is due to the fact that we try to find result for all combinations of `i` and `j` where `i` and `j` range from `0` to `n`, to compute a combination we perform an $$O(1)$$ operation thus the final complexity is $$O(n^2)$$.

* Space complexity : $$O(n^2)$$. Where `n` is the length of string `s`. This is due to the `memo` table which is completely filled in this case.

</br>

---

### Approach 3: Bottom-Up DP (1D)

**Algorithm**

On looking closely to both the approaches mentioned above you'll notice that for any combination of `i` and `j`, you essentially only need the `i+1`'th row and `j-1`'th column. Thus we know we can reduce the space complexity to only $$O(n)$$ from $$O(n^2)$$.

An efficient way of doing so is using the previous contained value in the `memo` which represents result for the previous state before storing the result for current state. This is better than the approach of managing two arrays (previous and current) and copying them after every calculation.


```cpp
class Solution {
public:
    bool isValidPalindrome(string s, int k) {
        vector<int> memo(s.length(), 0);

        // To store the previous required values from memo.
        int temp, prev;

        // Generate all combinations of `i` and `j` in the correct order.
        for (int i = s.length() - 2; i >= 0; i--) {
            // 'prev' stores the value at memo[i+1][j-1];
            prev = 0;
            for (int j = i + 1; j < s.length(); j++) {
                // Store the value of memo[i+1][j] temporarily.
                temp = memo[j];

                // Case 1: Character at `i` equals character at `j`
                if (s[i] == s[j])
                    memo[j] = prev;

                // Case 2: Character at `i` does not equal character at `j`.
                // Either delete character at `i` or delete character at `j`
                // and try to match the two pointers using recursion.
                // We need to take the minimum of the two results and add 1
                // representing the cost of deletion.
                else

                    // memo[j] will contain the value for memo[i+1][j]
                    // memo[j-1] will contain the value for memo[i][j-1]
                    memo[j] = 1 + min(memo[j], memo[j - 1]);

                // Copy the value of memo[i+1][j] to `prev`
                // For the next iteration when j=j+1
                // `prev` will hold the value memo[i+1][j-1];
                prev = temp;
            }
        }

        // Return true if the minimum cost to create a palindrome by only deleting the letters
        // is less than or equal to `k`.
        return memo[s.length() - 1] <= k;
    }
};
```


**Complexity Analysis**

* Time complexity : $$O(n^2)$$. Where `n` is the length of string `s`. This is due to the fact that we try to find result for all combinations of `i` and `j` where `i` and `j` range from `0` to `n`, to compute a combination we perform an $$O(1)$$ operation thus the final complexity is $$O(n^2)$$.

* Space complexity : $$O(n)$$. Where `n` is the length of string `s`. This is due to the `memo` table which stores result for only one row/`i` and all it's combination columns/`j`.

</br>