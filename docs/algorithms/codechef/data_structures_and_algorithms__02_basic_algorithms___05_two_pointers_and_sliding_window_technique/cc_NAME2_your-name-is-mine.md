# Your Name is Mine

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NAME2 |
| Difficulty Rating | 1285 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [NAME2](https://www.codechef.com/practice/course/two-pointers/POINTERF/problems/NAME2) |

---

## Problem Statement

In an attempt to control the rise in population, **Archer** was asked to come up with a plan. This time he is targeting marriages. Archer, being as intelligent as he is, came up with the following plan:

A man with name **M** is allowed to marry a woman with name **W**, only if **M** is a [subsequence](http://en.wikipedia.org/wiki/Subsequence) of **W** or **W** is a subsequence of **M**.

**A** is said to be a subsequence of **B**, if **A** can be obtained by deleting some elements of **B** without changing the order of the remaining elements.

Your task is to determine whether a couple is allowed to marry or not, according to Archer's rule.

### Input

The first line contains an integer **T**, the number of test cases. **T** test cases follow. Each test case contains two space separated strings **M** and **W**.

### Output

For each test case print `"YES"` if they are allowed to marry, else print `"NO"`. (quotes are meant for clarity, please don't print them)

### Constraints

- **1 ≤ T ≤ 100**

- **1 ≤ |M|, |W| ≤ 25000 (|A| denotes the length of the string A.)**

- All names consist of lowercase English letters only.

---

## Examples

**Example 1**

**Input**

```text
3
john johanna
ira ira
kayla jayla
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Case 1:** Consider **S = "johanna"**. So, **S[0] = 'j', S[1] = 'o', S[2] = 'h'** and so on. If we remove the indices [3, 4, 6] or [3, 5, 6] from S, it becomes **"john"**. Hence **"john"** is a subsequence of **S**, so the answer is "YES".

**Case 2:** Any string is a subsequence of it self, as it is formed after removing **"0"** characters. Hence the answer is **"YES"**.

**Case 3:** **"jayla"** can not be attained from **"kayla"** as removing any character from **"kayla"** would make the string length smaller than **"jayla"**, also there is no **'j'** in **"kayla"**. Similar reasoning can be applied to see why **"kayla"** can't be attained from **"jayla"**. Hence the answer is "NO".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
john johanna
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
ira ira
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
kayla jayla
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/NAME2)

[Contest](http://www.codechef.com/MAY13/problems/NAME2)

### DIFFICULTY

CAKEWALK

### PREREQUISITES

Ad-Hoc

### PROBLEM

Given two strings, say **A** and **B**, find whether **A** is a sub-sequence of **B**, or whether **B** is a sub-sequence of **A**.

A sub-sequence is defined as a string obtained from another string, say **S**, by **deleting** **one** **or** **more** characters form **S**, and not changing the **order** of the remaining characters.

### QUICK EXPLANATION

If the length of **A** is more than the length of **B**, then **A** cannot be a sub-sequence of **B**. This is obvious because you cannot delete characters from B and end up with a string that has **more** characters than it did orginally.

Thus, if length of **A** is larger than length of **B** we can swap them. Now, it only needs to be checked whether **A** is a sub-sequence of **B**.

### EXPLANATION

Checking whether **A** is a sub-sequence of **B** can be done greedily.

Let us find the **first** occurence of the first character of **A** in **B**.

`
for i = 1 to B.length
    if B[i] == A[1]
        break
    i++
`

If we find that **i** is larger than **B.length**, then of course the very first character of **A** doesn’t exist in **B**. This would mean that it is impossible for **A** to be a sub-sequence of **B**.

On the other hand, we have found that the the first character of **A** occurs in **B** at position **i**, first. Now, we can start looking for the **second** character of **A**. But, any occurance of the second character of **A** that occurs before **i** in **B** is irrelevant because we cannot perform any operation that **changes** **the** **order** of characters in **A** (or **B** for that matter).

Thus, we can resume searching for the second character of **A** in **B**, after position **i**.

`
for j = i+1 to B.length
    if B[j] == A[2]
        break
    j++
`

Using the same arguments as above, if **j** is not more than **B.length**, we have to resume searching for the third character of **A** in **B**, after position **j**.

When we have found all the characters of **A** in **B**, we can safely end the algorithm as well (with a **positive**). Otherwise we will run out of characters in **B** and we must return with a **negative**.

The above algorithm will look like the following pseudo code.

`
j = 1

for i = 1 to A.length
    while j < B.length
        if B[j] == A[i]
            break
        j++
    if j > B.length
        return false
    i++
    j++

return true
`

The complexity of the algorithm is **O(|A| + |B|)**, where **|S|** is the length of **S**. If it is not obvious to you why the algorithm isn’t **O(|A| * |B|)** note that we never decrement the value of **j**. In every iteration of the above algorithm we always increment **i** as well as **j**, and probably increment **j** more so. Thus, the algorithm must terminate in at most **O(|A|)** iterations of the outer loop and not more than **O(|B|)** iterations of the inner loop.

Note how this problem differs from the standard Dynamic Programming problem of finding the **largest common sub-sequence** between two strings. We could of course solve this problem by finding the longest commong sub-sequence between **A** and **B** as well, but doing so requires **O(|A| * |B|)** which is too slow for the limits set for length of the strings **A** and **B**.

### SETTER’S SOLUTION

Setter’s solution will be updated soon.

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/May/Tester/NAME2.cpp).

</details>
