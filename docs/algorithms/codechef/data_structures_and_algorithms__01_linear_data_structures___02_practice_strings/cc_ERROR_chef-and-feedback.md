# Chef and Feedback

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ERROR |
| Difficulty Rating | 1199 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [ERROR](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/ERROR) |

---

## Problem Statement

Lots of geeky customers visit our chef's restaurant everyday. So, when asked to fill the feedback form, these customers represent the feedback using a binary string (i.e a string that contains only characters **'0'** and **'1'**.

Now since chef is not that great in deciphering binary strings, he has decided the following criteria to classify the feedback as **Good** or **Bad** :

If the string contains the substring **"010"** or **"101"**, then the feedback is **Good**, else it is **Bad**. Note that, to be **Good** it is not necessary to have both of them as substring.

 So given some binary strings, you need to output whether according to the chef, the strings are **Good** or **Bad**.

### Input

 The first line contains an integer **T** denoting the number of feedbacks. Each of the next **T** lines contains a string composed of only **'0' ** and **'1'**.

### Output

 For every test case, print in a single line **Good** or **Bad** as per the Chef's method of classification.

### Constraints

- ** 1 **≤  **T** ≤ **  100 **

- ** 1 ** ≤ ** |S| **  ≤ ** 105**

Sum of length of all strings in one test file will not exceed **6*106**.

---

## Examples

**Example 1**

**Input**

```text
2
11111110
10101010101010
```

**Output**

```text
Bad
Good
```

**Explanation**

**Example case 1.**

The string doesn't contain **010** or **101** as substrings.

**Example case 2.**

The string contains both **010** and **101** as substrings.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
11111110
```

**Output for this case**

```text
Bad
```



#### Test case 2

**Input for this case**

```text
10101010101010
```

**Output for this case**

```text
Good
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ERROR)

[Contest](http://www.codechef.com/JAN14/problems/ERROR)

**Author:** [Vivek Hamirwasia](http://www.codechef.com/users/viv001)

**Tester:** [Mahbub](http://www.codechef.com/users/white_king)

**Editorialist:** [Jingbo Shang](http://www.codechef.com/users/shangjingbo)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Programming Language.

### PROBLEM:

Determine whether the given binary string contains the substring (consecutive) “010” or “101”.

### EXPLANATION:

You can use a loop and condition clauses to check directly. Also, you can use some built-in functions to solve this problem too.

For example, C++, we can use

``int position = strstr(s, "010") - s;
``

to get the first occurrence of “010” and check whether this position is in range. Or, if string is used in C++, then

``int position = s.find("010");
``

will work for string.

Similarly, Java, Python, etc… a lot of languages have such functions. Post your accepted solution and let’s find which one is the shortest! I think it will be interesting

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/January/Setter/ERROR.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2014/January/Tester/ERROR.cpp).

</details>
