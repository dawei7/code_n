# Reverse String (Recursive)

| | |
|---|---|
| **ID** | `recursion_02` |
| **Category** | recursion |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 1/10 |
| **Interview relevance** | 2/10 |
| **LeetCode Equivalent** | [Reverse String](https://leetcode.com/problems/reverse-string/) |

## Problem statement

Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place.
*Constraint:* You must solve this problem using **Recursion**. (Do not use `while` or `for` loops).

**Input:** An array of characters `s`.
**Output:** None (modify the array in-place).

## When to use it

- Strictly as a pedagogical exercise to teach how variables and memory are passed down and modified through the Recursive Call Stack.
- Never use this in production. An iterative Two-Pointer approach takes $O(1)$ space, while this recursive approach takes $O(N)$ space and risks a Stack Overflow!

## Approach

**1. The Recursive Analogy (Two Pointers):**
To reverse a string iteratively, we place a `left` pointer at index 0, and a `right` pointer at the last index. We swap the characters at those two pointers. Then we increment `left` and decrement `right`. We keep doing this until `left >= right`.

How do we do this recursively?
Instead of a `while` loop updating the pointers, we just pass the updated pointers as arguments to the next recursive function call!

**2. The Recursive Function Structure:**
We need a helper function `recurse(left, right)`.
- **Base Case:** If `left >= right`, all pairs have been swapped! The middle of the string has been reached. Stop recursing and `return`.
- **Recursive Step:**
  1. Swap the characters at `s[left]` and `s[right]`.
  2. Make the recursive call: `recurse(left + 1, right - 1)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for recursion_02: Reverse String.

Two-pointer swap; swap s[left] and s[right] in place, recurse
on the inner substring. Stop when left >= right. O(n) time,
O(n) recursion stack space.
"""


def solve(s, n):
    chars = list(s)

    def helper(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        helper(left + 1, right - 1)

    helper(0, n - 1)
    return "".join(chars)
```

</details>

## Walk-through

`s = ['h', 'e', 'l', 'l', 'o']`. Length 5.
Start: `recurse(0, 4)`.

1. **`recurse(0, 4)`**:
   - `0 >= 4` is False.
   - Swap `s[0]` ('h') and `s[4]` ('o').
   - Array is now: `['o', 'e', 'l', 'l', 'h']`.
   - Call `recurse(0 + 1, 4 - 1)` -> `recurse(1, 3)`.
2. **`recurse(1, 3)`**:
   - `1 >= 3` is False.
   - Swap `s[1]` ('e') and `s[3]` ('l').
   - Array is now: `['o', 'l', 'l', 'e', 'h']`.
   - Call `recurse(1 + 1, 3 - 1)` -> `recurse(2, 2)`.
3. **`recurse(2, 2)`**:
   - `2 >= 2` is TRUE! Base Case Hit!
   - `return`.
4. The call stack unwinds. `recurse(1, 3)` finishes. `recurse(0, 4)` finishes.

Final Array: `['o', 'l', 'l', 'e', 'h']`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

The pointers start at the edges and move inward by 1 at each step. They will meet exactly in the middle. Therefore, there are exactly N/2 recursive calls made. Time complexity is bounded linearly $O(N)$.
Every recursive call is placed on the system's Call Stack in memory. Because there are N/2 calls simultaneously active before hitting the base case, the space complexity is strictly $O(N)$.
*(In languages without Tail-Call Optimization, an input of 100,000 characters will instantly crash the program with a Stack Overflow Error!)*

## Variants & optimizations

- **Iterative Two-Pointer (`two_pointers_02`):** By completely removing the recursion and simply putting the swap logic inside a `while (left < right)` loop, the space complexity drops instantly from $O(N)$ to $O(1)$ constant space!
- **Tail-Call Optimization (TCO):** In languages like C++ or Scheme (but NOT Python or Java), if the recursive call is the absolute final instruction in the function, the compiler optimizes away the Call Stack entirely, running the recursive code in $O(1)$ space exactly like a `while` loop!

## Real-world applications

- **Functional Programming Languages:** Pure functional languages (like Haskell or Erlang) literally do not have `for` or `while` loops! EVERY iteration must be written as recursion like this, relying entirely on the compiler's Tail-Call Optimization to prevent memory crashes.

## Related algorithms in cOde(n)

- **[two_pointers_02 - Valid Palindrome](../two_pointers/two_pointers_02_valid-palindrome.md)** — Uses the exact same Two-Pointer string-edge logic, but iteratively.
- **[linked_list_01 - Reverse Linked List](../linked_list/ll_01_reverse-linked-list.md)** — The iterative recursive approach applied to nodes instead of array indices.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
