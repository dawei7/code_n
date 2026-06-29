# Chef and Prime Divisors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHAPD |
| Difficulty Rating | 1720 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CHAPD](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CHAPD) |

---

## Problem Statement

You are given two positive integers – **A** and **B**. You have to check whether **A** is divisible by all the prime divisors of **B**.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

For each test case, you are given two space separated integers – **A** and **B**.

### Output

For each test case, output "Yes" (without quotes) if **A** contains all prime divisors of **B**, otherwise print "No".

### Constraints

- **1** ≤ **T** ≤ **104**

- **1** ≤ **A, B** ≤ **1018**

### Subtasks

- **Subtask 1 (20 points):****1** ≤ **B** ≤ **107**

- **Subtask 2 (30 points):****1** ≤ **A** ≤ **107**

- **Subtask 3 (50 points):** Original constraints

---

## Examples

**Example 1**

**Input**

```text
3
120 75
128 16
7 8
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Example case 1.** In the first case 120 = 23*3*5 and 75 = 3*52. 120 is divisible by both 3 and 5. Hence, we will print "Yes"

**Example case 2.** In the second case both 128 and 16 are powers of two. Hence, the answer is "Yes"

**Example case 3.** In the third case 8 is power of two and 7 is not divisible by 2. So, the answer is "No"

**Separated test cases**

#### Test case 1

**Input for this case**

```text
120 75
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
128 16
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
7 8
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/MAY15/problems/CHAPD)

[Contest](http://www.codechef.com/MAY15/problems/CHAPD)

**Author:** [Vitalij Kozhukhivskij](http://www.codechef.com/users/witalij_hq)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Editorialist:** [Ajay K. Verma](http://www.codechef.com/users/djdolls)

**Russian Translator:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Mandarian Translator:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

### DIFFICULTY:

Easy

### PREREQUISITES:

Basic maths, greatest common divisor (gcd)

### PROBLEM:

Given two numbers, determine if the first number is divisible by all prime divisors of the second number.

### EXPLANATION:

We are given two integers A and B, and we want to determine whether there exist a prime number which divides B, but not A.

If B = 1, then clearly there is no such prime, as B has no prime divisors.

Now assume that B > 1. Let us say d = \gcd (A, B). If any prime number divides both A and B, then it must also divide d. In other words, d contains all common prime divisors of A and B.

If d = 1, that means, there is no common prime divisor between A and B. In this case, clearly, B has a prime divisor which does not divide A, in fact all prime divisors of B fall in this category.

On the other hand, if d > 1, then B = d * (B / d). Since d contains only those primes which divide A as well, hence, B will have a prime divisor not dividing A, if and only if (B/d) has such a prime divisor. So now we have reduced the task for pair (A, B) to the pair (A, B/d). Using this we can implement an easy recursive approach as shown below.

`
bool HasUniquePrime(int A, int B) {
  if (B == 1) return false;

  int d = gcd(A, B);
  if (d == 1) return true;
  return HasUniquePrime(A, B/d);
}
`

Since each step reduces B by a factor greater than one, the recursion will terminate at most after (\log B) steps. Also, in each step we are calculating gcd, which takes O (\log \min (A, B)) time. Hence, the overall complexity of this approach is O (\log^2 B)

#### Time Complexity:

O (\log^2 B)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/MAY15/Setter/CHAPD.py)

[Tester’s solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/MAY15/Tester/CHAPD.py)

</details>
