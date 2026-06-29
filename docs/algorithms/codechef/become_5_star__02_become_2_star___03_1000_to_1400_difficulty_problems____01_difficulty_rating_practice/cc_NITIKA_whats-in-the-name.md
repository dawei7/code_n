# Whats in the Name

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NITIKA |
| Difficulty Rating | 1299 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [NITIKA](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/NITIKA) |

---

## Problem Statement

Nitika was once reading a history book and wanted to analyze it. So she asked her brother to create a list of names of the various famous personalities in the book. Her brother gave Nitika the list. Nitika was furious when she saw the list. The names of the people were not properly formatted. She doesn't like this and would like to properly format it.

A name can have at most three parts: first name, middle name and last name. It will have at least one part. The last name is always present. The rules of formatting a name are very simple:

- **Only** the first letter of each part of the name should be capital.

- All the parts of the name except the last part should be represented by only two characters. The first character should be the first letter of the part and should be capitalized. The second character should be ".".

Let us look at some examples of formatting according to these rules:

- gandhi -> Gandhi

- mahatma gandhI -> M. Gandhi

- Mohndas KaramChand ganDhi -> M. K. Gandhi

### Input

The first line of the input contains an integer **T** denoting the number of test cases.

The only line of each test case contains the space separated parts of the name.

### Output

For each case, output the properly formatted name.

### Constraints

- 1 ≤ **T** ≤ 100**

- 2 ≤ Length of each part of the name ≤ 10

- Each part of the name contains the letters from lower and upper case English alphabets (i.e. from 'a' to 'z', or 'A' to 'Z')

### Subtasks

**Subtask #1 (40 points)**

- There is exactly one part in the name.

**Subtask #2 (60 points)**

- Original constraints.

---

## Examples

**Example 1**

**Input**

```text
3
gandhi
mahatma gandhI
Mohndas KaramChand gandhi
```

**Output**

```text
Gandhi 
M. Gandhi 
M. K. Gandhi
```

**Explanation**

The examples are already explained in the problem statement.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
gandhi
```

**Output for this case**

```text
Gandhi
```



#### Test case 2

**Input for this case**

```text
mahatma gandhI
```

**Output for this case**

```text
M. Gandhi
```



#### Test case 3

**Input for this case**

```text
Mohndas KaramChand gandhi
```

**Output for this case**

```text
M. K. Gandhi
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/JULY17/problems/NITIKA)

[Contest](https://www.codechef.com/problems/NITIKA)

**Author:** [Abhinav Jain](https://www.codechef.com/users/iamabjain)

**Primary Tester:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Hussain Kara Fallah](https://www.codechef.com/users/deadwing97)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

Given names of people. Each name may consist of at least one and at most three parts. You are asked to show the name with replacing the first two parts (if they exist) with the first letter of each (abbreviation) and followed by the last part (last name). Abbreviations should be upper case letters. **Only** the first letter of the last name should be in uppercase.

### EXPLANATION:

This problem is straight forward implementation (string manipulation). Each name will be given on a separate line, so we should read each line completely (one by one). We have to find the parts of each name and separate them from each other. Since each two consecutive parts are separated by a space,we should be looking for spaces in each line. The first space (if it exists) separates between the 1st and the 2nd part, the second space (if it exists) separates between the 2nd and the 3rd part. Finding spaces on each line would make us able to break our full name into parts (This can be done manually by a loop).

My solution uses stringstream (C++ class) which is very useful for parsing input and solves this problem easily. A brief explanation can be found here :[stringstream](https://www.eecis.udel.edu/~breech/progteam/stringstream.html)

After breaking the name into parts we should capitalize the first letter of each part. We should output **only** the first letter of each part capitalized (except the last part). As for the last part, we must set its first letter to uppercase, and the rest of its letters to lowercase. After that, we can print it.

### AUTHOR’S AND TESTER’S SOLUTIONS:

**AUTHOR’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Setter/NITIKA.java)

**TESTER’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Tester/NITIKA.cpp)

**EDITORIALIST’s solution**: Will be found [here](https://s3.amazonaws.com/codechef_shared/download/Solutions/JULY17/Editorialist/NITIKA.cpp)

</details>
