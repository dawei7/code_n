# Chef Generates Letter Combinations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WEGUW01 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [WEGUW01](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/WEGUW01) |

---

## Problem Statement

Chef has found an old phone keypad and wants to explore all the possible letter combinations that can be generated from a given string of digits. \
Each digit from 0 to 9 maps to a set of letters just like on a traditional telephone keypad

0: "" \
1: "" \
2: "abc" \
3: "def" \
4: "ghi" \
5: "jkl" \
6: "mno" \
7: "pqrs" \
8: "tuv" \
9: "wxyz"

Chef wants to generate every possible string by replacing each digit with one of its corresponding letters.

Help Chef by writing a function that takes the input digits $inputDigits$ and returns all possible letter combinations that the number could represent. If Chef provides an empty string, then no combinations should be returned.

## Function Declaration

### Function Name
$getLetterCombinations$ - This function generates all possible letter combinations that the input digits could represent on a phone keypad.

### Parameters
- $inputDigits$ : A string containing digits from $0$ to $9$ inclusive. Each digit maps to a set of letters as on a traditional phone keypad.

### Return Value
- Returns a string containing all possible letter combinations.
- Each string in the array represents one valid letter combination.
- The output vector is empty if $inputDigits$ is empty.

## Constraints
- $1 \leq T \leq 10^5$
- $1 \leq |\text{inputDigits}| \leq 4$
- Each character in `inputDigits` is a digit in the range $['0', '9']$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases.
- Each test case consists of a single line containing the string $inputDigits$.

---

## Output Format

- For each test case, print all possible letter combinations that the input digits could represent.
- Print the combinations separated by spaces in any order.
- If there are no combinations, print an empty line.

---

## Examples

**Example 1**

**Input**

```text
3
2
23
234
```

**Output**

```text
a b c
ad ae af bd be bf cd ce cf
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
```

**Explanation**

- For input "2": digit '2' maps to letters a, b, c; output all single letters.
- For input "23": digit '2' -> a,b,c and '3' -> d,e,f; combine each letter of '2' with each of '3'.
- For input "234": digits map to '2'-> a,b,c, '3' -> d,e,f, '4' -> g,h,i; output all combinations picking one letter from each digit in order.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
a b c
```



#### Test case 2

**Input for this case**

```text
23
```

**Output for this case**

```text
ad ae af bd be bf cd ce cf
```



#### Test case 3

**Input for this case**

```text
234
```

**Output for this case**

```text
adg adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg cdh cdi ceg ceh cei cfg cfh cfi
```



**Example 2**

**Input**

```text
2
79
9
```

**Output**

```text
pw px py pz qw qx qy qz rw rx ry rz sw sx sy sz
w x y z
```

**Explanation**

- t=1: Digits "79" map to "pqrs" and "wxyz". Output is all combinations of letters from these two sets in order.
- t=2: Digit "9" maps to "wxyz". Output is each letter alone as single combinations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
79
```

**Output for this case**

```text
pw px py pz qw qx qy qz rw rx ry rz sw sx sy sz
```



#### Test case 2

**Input for this case**

```text
9
```

**Output for this case**

```text
w x y z
```



**Example 3**

**Input**

```text
1
8
```

**Output**

```text
t u v
```

**Explanation**

- For input digit '8', the corresponding letters on a phone keypad are 't', 'u', and 'v'. Hence, the output is "t u v".

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Summary

You are given a string of digits, each between 2 and 9. Each digit corresponds to a set of letters on a traditional phone keypad. The task is to generate all possible letter combinations that can be formed by replacing each digit with any of its corresponding letters.

For example:

* Digit 2 → a, b, c
* Digit 3 → d, e, f
* Digit 7 → p, q, r, s
* Digit 9 → w, x, y, z

Given a digit string, we must output every possible string formed by choosing one letter for each digit in order.

If the input string is empty, no combinations exist.

Multiple test cases are processed independently.

---

## Key Observations

1. Each digit independently maps to a fixed set of letters.
2. For a digit string of length n, the number of combinations is the product of the number of letters for each digit.

   * Maximum digits allowed is 4.
   * Worst case: digits like "7799" produce 4×4×4×4 = 256 combinations.
3. A natural way to explore all possibilities is depth-first search (DFS) with backtracking.
4. Order of output is not important unless specified, so any correct traversal order is acceptable.

---

## Approach

### 1. Mapping Digits to Letters

We establish a mapping of digits to their respective letter groups:

* 2 → "abc"
* 3 → "def"
* 4 → "ghi"
* 5 → "jkl"
* 6 → "mno"
* 7 → "pqrs"
* 8 → "tuv"
* 9 → "wxyz"

Digits 0 and 1 are not included since they have no letters.

### 2. Backtracking Strategy

We build combinations character by character.

Define a recursive function:

* Parameters: current index in the input string, current partial combination.
* Each step:

  1. Look at the current digit.
  2. Iterate over all letters mapped to that digit.
  3. Append a letter to the partial string.
  4. Move recursively to the next index.
  5. Remove the letter afterward (backtrack).

When the index reaches the length of the input digit string, a complete combination is formed, and it is added to the result list.

### 3. Handling Edge Cases

* If the input digit string is empty, return an empty list.
* If a test case has only one digit, return the letters corresponding to that digit.
* Ensure each test case starts fresh, and results do not overlap between test cases.

### 4. Output

For each test case:

* Print all generated combinations separated by spaces.
* If no combinations exist, simply print an empty line.

---

## Time Complexity

Let n be the length of the input digit string, and let k be the average number of letters per digit (typically between 3 and 4).

Total number of combinations: k^n
Maximum input length is 4, so absolute worst case is 4^4 = 256 combinations.

The time complexity is:
O(k^n × n)
because each combination takes O(n) time to store or print.

Given constraints (T up to 10^5, n up to 4), this is manageable because each test case is very small.

---

## Space Complexity

O(n) for the recursion stack and temporary string, and
O(k^n × n) for storing results per test case if stored before printing.

Since n ≤ 4, this is small.

---

## Summary

The problem is a classic application of backtracking:

* Map each digit to its letters.
* Use recursion to explore all letter choices at each position.
* Generate all possible strings in a depth-first manner.
* Print combinations for each test case.

This method ensures complete and correct enumeration of all phone keypad letter combinations.

</details>
