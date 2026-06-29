# Prime Generator

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRIME1 |
| Difficulty Rating | 1069 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PRIME1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PRIME1) |

---

## Problem Statement

Ram wants to generate some prime numbers for his cryptosystem. Help him please!
Your task is to generate all prime numbers between two given numbers.

`
**Warning: large Input/Output data, be careful with certain languages (though most should be OK if the algorithm is well designed)**

---

## Input Format

The first line contains t, the number of test cases (less then or equal to 10).

Followed by t lines which contain two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

---

## Output Format

For every test case print all prime numbers p such that m <= p <= n,
one number per line.  Separate the answers for each test case by an empty line.

---

## Constraints

(1 <= m <= n <= 1000000000, n-m<=100000)

---

## Examples

**Example 1**

**Input**

```text
2
1 10
3 5
```

**Output**

```text
2
3
5
7


3
5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Prime Generator Practice Problem in 1000 to 1400 difficulty problems](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PRIME1)

### [](#problem-statement-1)Problem Statement:

Ram wants to generate some prime numbers for his cryptosystem. Help him please! Your task is to generate all prime numbers between two given numbers.

### [](#approach-2)Approach:

**Primality Check Function**:

- The function checks if a given number `n` is prime using a trial division up to \sqrt{n}

- If `n≤1`, it immediately returns `false` as numbers less than or equal to `1` are not prime.

- It iterates from `2` to \sqrt{n} If `n` is divisible by any of these numbers, it returns `false` (indicating `n` is not prime). Otherwise, it returns `true` (indicating `n` is prime).

**Generating Primes in the Given Range**:

- For each test case, iterate from `m` to `n` and use the Prime function to check if each number in this range is prime.

- If a number is prime, it is printed to the output, each on a new line.

### [](#complexity-3)Complexity:

- **Time Complexity:** The Prime function has a time complexity of O(\sqrt{n}). the code iterates over the range from `m to n`. If the range size is `R=n−m+1`, the main loop runs `O(R)` times. Total time complexity is O(R . \sqrt{n}).

- **Space Complexity:** `O(1)` No extra space required.

</details>
