# Chef and digits of a number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LONGSEQ |
| Difficulty Rating | 1209 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [LONGSEQ](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/LONGSEQ) |

---

## Problem Statement

Chef has a number **D** containing only digits 0's and 1's. It can have leading 0's. He wants to make the number to have all the digits same. For that, he will change **exactly** one digit, i.e. from 0 to 1 or from 1 to 0. If it is possible to make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "Yes", else print "No" (quotes for clarity)

### Input

 The first line will contain an integer **T** representing the number of test cases.

Each test case contain a number made of only digits 1's and 0's on newline

### Output

 Print T lines with a "Yes" or a "No", depending on whether its possible to make it all 0s or 1s or not.

### Constraints
**Subtask #1: (40 points)**

- **1** ≤ **T** ≤ **50**

- **1** ≤ **Length of the number D** ≤ **50**

**Subtask #2: (60 points)**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **Length of the number D** ≤ **105**

---

## Examples

**Example 1**

**Input**

```text
2
101
11
```

**Output**

```text
Yes
No
```

**Explanation**

**Example case 1.** In 101, the 0 can be flipped to make it all 1..

**Example case 2.** No matter whichever digit you flip, you will not get the desired string.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
101
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
11
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LONGSEQ)

[Contest](https://www.codechef.com/SEPT16/problems/LONGSEQ)

**Author:** [Chandan Boruah](http://www.codechef.com/users/chandubaba)

**Tester:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

**Editorialist:** [Ajay K. Verma](http://www.codechef.com/users/djdolls)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Ad-hoc, String

### PROBLEM:

Given a binary string, find if it is possible to make all its digits equal by flipping exactly one digit.

### QUICK EXPLANATION:

All the digits of the binary string can be made equal by flipping exactly one digit if and only if the original string has exactly one digit equal to zero, or exactly one digit equal to one.

### EXPLANATION:

Suppose that the input string has exactly one digit equal to one, and all other digits are zero, then we can flip this digit, which will result in a string with all digits equal to zero. Similarly, if the input string has exactly one digit equal to zero, and all other digits are one, then flipping this digit would result in a string with all digits equal to one.

On the other hand, if all digits of a string can be made identical by doing exactly one flip, that means the string has all its digits equal to one another except this one digit which has to be flipped, and this digit must be different than all other digits of the string. The value of this digit could be either zero or one. Hence, this string will either have exactly one digit equal to zero, and all other digits equal to one, or exactly one digit equal to one, and all other digit equal to zero.

Therefore, we only need to check whether the string has exactly one digit equal to zero/one, and if so, the answer is yes; otherwise the answer is no.

`
void f(string str) {
  int num_zeros = 0;
  int num_ones = 0;

  for (char ch : str) {
    if (ch == '0') {
      ++num_zeros;
    } else {
       ++num_ones;
    }
  }

  if (num_zeros == 1 || num_ones == 1) {
    print("Yes\n");
  } else {
    print("No\n");
  }
}
`

### TIME COMPLEXITY:

O (N), where N is the length of the string.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be uploaded soon.

Tester’s solution will be uploaded soon.

</details>
