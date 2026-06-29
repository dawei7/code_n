# Chef and Rainbow Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RAINBOWA |
| Difficulty Rating | 1467 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [RAINBOWA](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/RAINBOWA) |

---

## Problem Statement

Chef likes all arrays equally. But he likes some arrays more equally than others. In particular, he loves Rainbow Arrays.

An array is Rainbow if it has the following structure:

- First **a1** elements equal **1**.

- Next **a2** elements equal **2**.

- Next **a3** elements equal **3**.

- Next **a4** elements equal **4**.

- Next **a5** elements equal **5**.

- Next **a6** elements equal **6**.

- Next **a7** elements equal **7**.

- Next **a6** elements equal **6**.

- Next **a5** elements equal **5**.

- Next **a4** elements equal **4**.

- Next **a3** elements equal **3**.

- Next **a2** elements equal **2**.

- Next **a1** elements equal **1**.

- **ai** can be any non-zero positive integer.

- There are no other elements in array.

Help Chef in finding out if the given array is a Rainbow Array or not.

### Input

- The first line of the input contains an integer **T** denoting the number of test cases.

- The first line of each test case contains an integer **N**, denoting the number of elements in the given array.

- The second line contains **N** space-separated integers **A1**, **A2**, ..., **AN** denoting the elements of array.

### Output

- For each test case, output a line containing "yes" or "no" (without quotes) corresponding to the case if the array is rainbow array or not.

### Constraints

- 1 ≤ **T** ≤ 100

- 7 ≤ **N** ≤ 100

- 1 ≤ **Ai** ≤ 10

### Subtasks

- **Subtask 1** (100 points) : Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
19
1 2 3 4 4 5 6 6 6 7 6 6 6 5 4 4 3 2 1
14
1 2 3 4 5 6 7 6 5 4 3 2 1 1
13
1 2 3 4 5 6 8 6 5 4 3 2 1
```

**Output**

```text
yes
no
no
```

**Explanation**

The first example satisfies all the conditions.

The second example has **1** element of value **1** at the beginning and **2** elements of value **1** at the end.

The third one has no elements with value **7** after elements with value **6**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
19
1 2 3 4 4 5 6 6 6 7 6 6 6 5 4 4 3 2 1
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
14
1 2 3 4 5 6 7 6 5 4 3 2 1 1
```

**Output for this case**

```text
no
```



#### Test case 3

**Input for this case**

```text
13
1 2 3 4 5 6 8 6 5 4 3 2 1
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RAINBOWA)

[Contest](https://www.codechef.com/AUG17/problems/RAINBOWA)

[Video Editorial](https://www.youtube.com/watch?v=HqLpVbEVHgM)

**Author:** [Dmytro Berezin](https://www.codechef.com/users/berezin)

**Primary Tester** [Prateek Gupta](https://www.codechef.com/users/prateekg603)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### PROBLEM EXPLANATION

A rainbow array of **n** elements follows the form

**{** **1** (repeated **a1**  times), **2** (**a2** times), **3** (**a3** times), **4** (**a4** times), **5** (**a5** times), **6** (**a6** times), **7** (**a7** times), **6** (**a6** times), **5** (**a5** times), **4** (**a4** times), **3** (**a3** times), **2** (**a2** times), **1** (**a1** times) **}**

2*(a_1+a_2+a_3+a_4+a_5+a_6)+a_7 = n

Given an array consisting of **n** elements, check if it’s a rainbow array or not.

### DIFFICULTY:

cakewalk

### PREREQUISITES:

None

### EXPLANATION:

This problem is similar to checking if a given string is a palindrome or not. The simplest and most effective way to check if the array is rainbow, is by maintaining 2 pointers one iterating through elements starting from the beginning of our array, and the other one iterating through the elements in the reversed direction.

Both of the first and the last element of the array must be ones. In fact, there must be two blocks consisting of the same number of **consecutive** ones **(1)** one of them located at the beginning of the array, and the other one at the end.

Figuring out the number of consecutive ones at the beginning of our array can be done easily by moving our first pointer forward, and stopping when encountering a number not equal to 1 or reaching the end of our array. We can do the same on the other side by moving our second pointer backwards. After that, we should check that we had processed the same number of **ones** on both sides.

After processing elements equal to **one**, you can observe that we are still solving the same problem (in fact, it’s a subproblem now). Both of our pointers must be referring to elements equal to **2**. Moving our pointers is equivalent to dropping elements, so if we consider that we have dropped processed **ones**, there must be two blocks consisting of the same number of **consecutive** twos **(2)** one of them located at the beginning of the array, and the other one at the end. Of course instead of using 2 pointers, maintaining a data structure which supports dropping elements from both ends of the array (Like C++ Deque) does the job perfectly.

After repeating the same procedure for **{1,2,3,4,5,6}** (considering that none of our conditions was violated, in case that happened we can report that our array is not rainbow and break) we would be finishing with a single block consisting **only** of elements equal to seven **7**. Reaching this point confirms that our array is rainbow.

You can check my implementation for better understanding.

### AUTHOR’S AND TESTER’S SOLUTIONS:

**AUTHOR’s solution**: Can be found [here](http://www.codechef.com/download/Solutions/AUG17/Setter/RAINBOWA.cpp)

**TESTER’s solution**: Can be found [here](http://www.codechef.com/download/Solutions/AUG17/Tester2/RAINBOWA.cpp)

**EDITORIALIST’s solution**: Can be found [here](http://www.codechef.com/download/Solutions/AUG17/Editorialist/RAINBOWA.cpp)

### Video Editorial

</details>
