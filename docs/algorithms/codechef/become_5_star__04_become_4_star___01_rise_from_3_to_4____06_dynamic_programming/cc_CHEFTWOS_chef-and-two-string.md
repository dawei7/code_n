# Chef and Two String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFTWOS |
| Difficulty Rating | 2233 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [CHEFTWOS](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/CHEFTWOS) |

---

## Problem Statement

Chef's loves his dog so much! Once his dog created two strings **a** and **b** each of length **n** consisting of digits **1** and **2**, and even a problem about them!

Chef's Dog will tell by barking if a string **x** (also containing only digits **1** and **2** and with length **N**) is **good** or not by performing the following actions.

- It starts at first digit of the string, i.e. at **i = 1**.

- It can move from digit **i** to either **i - 1** or **i + 1** if **xi** equals **1** and the corresponding digits exist.

- It can move from digit **i** to either **i - 2** or **i + 2** if **xi** equals **2** and the corresponding digits exist.

- It **must** visit each digit **exactly** once.

- It **must** finish at the last digit (**XN**).

Chef's dog wants to make both the strings **a** and **b** *good* by choosing some subset **S** (possibly empty) of indices of set **{1, 2, ..., n}** and swapping each index **i ϵ S** between string **a** and **b**, i.e. swapping **ai** and **bi**. Can you find how many such subsets **S** exist out there? As the answer could be large, output it modulo **109 + 7**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line contains string **a**.

The second line contains string **b**.

### Output

For each test case, output a single line containing answer of the problem.

### Constraints

- **1** ≤ **T** ≤ **20**

- **1** ≤ **|a| = |b|** ≤ **105**

- **'1'** ≤ **ai, bi** ≤ **'2'**

### Subtasks

- Subtask #1 (30 points) **|a|, |b|** ≤  **10**

- Subtask #2 (70 points) **original constraints**

---

## Examples

**Example 1**

**Input**

```text
2
1111
2211
222
111
```

**Output**

```text
8
0
```

**Explanation**

**Test case 1.**
Possible subsets are:
**{}**, **{1, 2}**, **{1, 2, 3}**, **{1, 2, 4}**, **{1, 2, 3, 4}**, **{3}**, **{4}**, **{3, 4}**.

**Test case 2.** There are no possible sets **S** which can make both the strings good.
`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1111
2211
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
222
111
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CHEFTWOS)

[Contest](http://www.codechef.com/OCT16/problems/CHEFTWOS)

### DIFFICULTY

easy

### PREREQUISITES

observation, dp

### PROBLEM

A string s is called good if you start at the first character and can reach the last character by applying the below moves repeatedly, visiting each character **exactly** once in the process. When you are at character ‘1’, you can move one step to the left or to the right, similarly at character ‘2’, two steps left or right. The string consists of only 1’s and 2’s.

In the problem, you are given two string a, b, each of length n. You have to find number of ways of swapping some subset of indices among them such that the resulting strings a and b both are good.

### QUICK EXPLANATION

A string s will be good if it contains 2’s, then they should occur as a pair. Also, the string should not end up with 22

This observation can be used to get a dynamic programming solution.

### EXPLANATION

#### Characterization of good string

Let us take some examples.

Trivially, any string of length 1 is good, i.e. “1” and “2”.

String “11” is also good, as you start from first character, you have a character ‘1’ at this position, so you can move one step to the right and end up at the last character. During this process, you visited both first and second characters exactly once.

The string “12” is also good.

However the string “21” is not good, as you can’t go anywhere from the first character, so the second character will never be visited.

The string 22 is not good.

Now let us first make some observations.

Last character of the string does not matter in the deciding whether it is good or not. As for a good string, we want to end up at the last character,  i.e. after landing at last character, we won’t be making any more moves. So the last character of string will be unused in making any decision about moves.

Assume currently you are position i, and if consecutive two or more of positions i, i + 1, i + 2 \dots  are visited. In that case, you can not move in the right direction from position i. This is due to the fact that in each move, you can take at most two steps.

The character set of the string is very limited, it contains either ‘0’ or ‘1’. This restricts our movement a lot. Imagine you are at some character, and you were not able to visit a position that is two or more steps left to it. You will never be able to visit it, along with satisfying all the conditions for a string to be good. The idea is if you go back, you won’t be able to come back again without revisiting some characters. This can be understood from the observation stated in the previous paragraph.

This motivates us to think that our movement should be almost going from left to right, with a few deviations if possible, but all those deviations will be at most one position to the left. This deviation is only possible in the case when you have come from position i - 2 (s.t. s_{i - 2} = '2') to position i with s_i = '1' and s_{i - 1} = '2', so that you after landing at i - 1, you can go position i + 1 from there.

This leads to us to make a speculation - A string will be a good if it does not contain more than two consecutive 2’s. Also, there will a separate case to consider when the string ends up two 2’s. In that case also, the string won’t be good.

This is indeed true. It is easy to see that if the string satisfies this property then string will be good. From the previous discussion, we can see that in all other cases, the string will be bad. These cases are namely, if the string contains groups of single 2’s and more than one 2’s. We have already proved that string will be bad in both these scenarios.

**A string s will be good if it contains 2’s, then they should occur as a pair. Also, the string should not end up with 22.**

#### Final Solution

Finding number of ways of swapping subsets of indices in string a and b to make both of them good can solve using dynamic programming and the above definition of good string.

We iterate over both a and b simultaneously in order from left to right. Suppose we are at index i and till now the parts of both the strings a, b are good (i.e. a[0, i - 1], b[0, i - 1] are good). Now, we have two choices for position i. We make a swap of a_i, b_i or we don’t. What information should we keep as a part of state in the dp solution, so that after processing position i, we can ensure that the strings a[0, i], b[0, i] are good.

According to definition of good string, it should not contain more than two consecutive 2’s. So, we should maintain that count of 2’s that are at the end of strings a[0, i - 1] and b[0, i - 1]. As we know that both of these strings are good, so the count of 2’s can be either 0 or 1 at max.

So our dp state will be dp[i][cntTwosInA][cntTwosInB].

The transitions of this dp can be done easily. At position i, we have two possibilities, to swap or not to swap. For both of these possibilities, we check that for a and b, if the character at position i is ‘2’, then the corresponding cntTwos should be 1. If it is ‘1’, then we should make sure that current character is not ‘2’.

Don’t forget to check that in the end, there should not be two 2’s in either a or b.

Time complexity of this solution will be \mathcal{O}(n * 2 * 2) (for states) \times * \mathcal{O}(1) (for transitions) = \mathcal{O}(n).

### EDITORIALIST’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Editorialist/CHEFTWOS.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Tester/CHEFTWOS.cpp).

</details>
