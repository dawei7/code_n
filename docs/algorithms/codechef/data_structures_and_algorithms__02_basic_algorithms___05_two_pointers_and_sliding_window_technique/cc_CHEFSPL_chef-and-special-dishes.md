# Chef And Special Dishes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFSPL |
| Difficulty Rating | 1760 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [CHEFSPL](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/CHEFSPL) |

---

## Problem Statement

One day, Chef prepared **D** brand new dishes. He named the i-th dish by a string **Si**. After the cooking, he decided to categorize each of these **D** dishes as *special* or not.

A dish **Si** is called *special* if its name (i.e. the string **Si**) can be represented in the form of a *double* string by removing at most one (possibly zero) character from it's name from any position.

A string is called a *double* string if it can be represented as a concatenation of two identical, non-empty strings.
e.g. "abab" is a double string as it can be represented as "ab" + "ab" where + operation denotes concatenation.
Similarly, "aa", "abcabc" are double strings whereas "a", "abba", "abc" are not.

### Input

- First line of the input contains an integer **D** denoting the number of dishes prepared by Chef on that day.

- Each of the next **D** lines will contain description of a dish.

- The i-th line contains the name of i-th dish **Si**.

### Output

For each of the **D** dishes, print a single line containing "**YES**" or "**NO**" (without quotes) denoting whether the dish can be called as a *special* or not.

### Constraints

- **1** ≤ **D** ≤ **106**

- **1** ≤ **|Si|** ≤ **106**.

- Each character of string **Si** will be lower case English alphabet (i.e. from 'a' to 'z').

### Subtasks

**Subtask #1 : (20 points)**

- Sum of **|Si|** in an input file doesn't exceed **2 * 103**

**Subtask 2 : (80 points) **

- Sum of **|Si|** in an input file doesn't exceed **2 * 106**

---

## Examples

**Example 1**

**Input**

```text
3
aba
abac
abcd
```

**Output**

```text
YES
NO
NO
```

**Explanation**

**Example case 1.**
We can remove the character at position 1 (0-based index) to get "aa" which is a *double* string. Hence, it is a *special* dish.

**Example case 2.**
It is not possible to remove the character at any of the position to get the double string. Hence, it is not a *special* dish.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
aba
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
abac
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
abcd
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/MARCH16/problems/CHEFSPL)

[Practice](http://www.codechef.com/problems/CHEFSPL)

**Author:** [Prateek Gupta](http://www.codechef.com/users/prateekg603)

**Tester:** [Roman Furko](http://www.codechef.com/users/furko)

**Translators:** [Vasya Antoniuk](http://www.codechef.com/users/antoniuk1) (Russian), [Team VNOI](http://www.codechef.com/users/vnoi) (Vietnamese) and [Hu Zecong](http://www.codechef.com/users/huzecong) (Mandarin)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### DIFFICULTY:

Simple

### PREREQUISITES:

String processing

### PROBLEM:

Given a string S, can you remove at most one character so that the remaining string is a **double string**? A double string is a string of the form W + W for some non-empty string W.

### QUICK EXPLANATION:

The answer is `YES` iff |S| \ge 2 and one of the following is true:

- The first \lfloor \frac{|S|}{2} \rfloor characters is a subsequence of the last \lceil \frac{|S|}{2} \rceil characters, or

- The last \lfloor \frac{|S|}{2} \rfloor characters is a subsequence of the first \lceil \frac{|S|}{2} \rceil characters.

### EXPLANATION:

# Subtask 1

Let’s first try using the simplest solution possible: Try all possible characters to remove (possibly none), and see whether any resulting string is a double string. There are only |S|+1 cases to try, because there are only |S| locations to remove a character from, plus 1 for the “*do nothing*” scenario. For this to work, we need code that checks whether a string is a double string. Here’s a pseudocode that does that:

``def is_double_string(s):
    n = s.length
    if n == 0 or n % 2 != 0:
        return false
    h = n / 2
    for i = 0..h-1:
        if s[i] != s[i+h]:
            return false
    return true
``

(*Note:* We also return `false` when `n == 0` because W must be nonempty from the definition!)

With this function, we can now answer a single test case by trying all |S|+1 cases. The following is a pseudocode for this:

``def solve(s):
    n = s.length
    good = is_double_string(s)
    if not good:
        for i = 0..n-1:
            let t be s with the i'th character removed
            if is_double_string(t):
                good = true
                break
    print (if good then 'YES' else 'NO')
``

Unfortunately, checking whether a string is a double string takes O(|S|) time, so this runs in (|S|+1)O(|S|) = O(|S|^2) time, too slow for the second subtask.

# Subtask 2

Here are a few observations that will help us find a faster solution:

- Double strings are of even length, and

- Removing a letter from a string changes its parity.

This gives us the following clues on what we must do:

- If |S| is even, then we must not remove any letter.

- If |S| is odd, then we must remove exactly one letter.

In the first case, since we can’t remove any character, we simply need to check whether S is already a double string to begin with. This takes O(|S|) time so we’re good.

In the second case, we still have a problem because we don’t know which letter to remove. However, we can use the fact that in a double string, the first half is the same as the second half (by definition). Since we can only remove one character to turn S into a double string, the first “half” of S must already be nearly the same as the second “half” to begin with. (The word “half” here is a bit ambiguous because |S| is odd, but you sorta get the idea.) Specifically, the first and second “halves” must differ from each other by exactly one **deletion**. This means that the shorter “half” must be a **subsequence** of the longer “half”. Thus, we have reduced the problem to simply checking whether some string is a subsequence of another string!

Now, we still have a problem because we don’t know which “half” must be the shorter one. But there are only two possibilities to check (either the first or second half is the shorter one), so it’s no problem.

Finally, how do we quickly check whether some string, say A, is a subsequence of another string, say B? A simple greedy algorithm such as the following will do:

``def is_subsequence(a,b):
    j = 0
    for i in 0..a.length-1:
        // find where a[i] appears in b[j..]
        while j < b.length and a[i] != b[j]:
            j++
        if j == b.length:
            return false
        j++ // "consume" b[j]
    return true
``

This code runs in O(|A| + |B|) time, and since in our case |A| + |B| = |S|, and there are only two cases to check, our algorithm runs in 2\cdot O(|S|) = O(|S|).

To summarize, here is our algorithm:

``def solve(s):
    n = s.length
    good = false
    if n % 2 == 0:
        good = is_double_string(s)
    else if n > 1: // n == 1 is bad
        h = n / 2
        good = is_subsequence(s[0..h-1], s[h..n-1]) or is_subsequence(s[h+1..n-1], s[0..h])
    print (if good then 'YES' else 'NO')
``

### Time Complexity:

O(|S|)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter](https://www.codechef.com/download/Solutions/MARCH16/Setter/CHEFSPL.cpp)

[tester](https://www.codechef.com/download/Solutions/MARCH16/Tester/CHEFSPL.cpp)

[editorialist](https://www.codechef.com/download/Solutions/MARCH16/Editorialist/CHEFSPL.py)

</details>
