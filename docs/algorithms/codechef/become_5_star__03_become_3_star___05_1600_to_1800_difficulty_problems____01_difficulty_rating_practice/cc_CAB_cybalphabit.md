# Cybalphabit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CAB |
| Difficulty Rating | 1771 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CAB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CAB) |

---

## Problem Statement

In the new world, we also have a new system called Cybalphabit system.
The system assigns points to each Latin lowercase alphabet as follows:-
'a' is assigned $2^0$ , 'b' is assigned $2^1$, 'c' $2^2$ and so on. Thus, finally 'z' is assigned $2^{25}$ points.

A Cyberstring is a sequence of lowercase Latin alphabets.

Now, the total score of a Cyberstring will be the sum of points of its characters.
You will be given two integers $N$ and $K$.
Construct a Cyberstring $X$ of length $N$ with total score $K$ or print $-1$ if it is not possible to form the Cyberstring ($X$).
If there are multiple answers, print any.

###INPUT:

- First line contains $T$, the number of test cases.
- Each of the next $T$ lines denotes a different test case :
- The ${(i+1)}^{th}$ line denotes the $i^{th}$ test case, and contains two integers $N$ and $K$, the length of the string that is to be constructed, and the score of the string respectively.

###OUTPUT:

- For each test case, provide the output on a different line.
- Output the required string $X$, if one exists, otherwise output $-1$.

###Constraints:-

- $1 \leq T \leq 10^5$
- $1 \leq n \leq 10^5$
- $1  \leq k  \leq 5*10^7$

The sum of $n$ over all test cases is less than $10^{5}$

---

## Examples

**Example 1**

**Input**

```text
4
2 2
2 5
4 5
3 2
```

**Output**

```text
aa
ac
baaa
-1
```

**Explanation**

In the first test case, $n=2$ and $k=2$. So,we have to construct a string of length $2$ with total score $2$. It can be easily seen that the only possible string is "aa". Its total score will be equal to $2^0 + 2^0 = 2$.

In the second case, "ac" will have score $2^0 + 2^2 = 5$. Obviously, "ca" will also have the same score and is also a possible answer.

In the fourth test case, it can be shown that there is no possible string which satisfies the conditions.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
aa
```



#### Test case 2

**Input for this case**

```text
2 5
```

**Output for this case**

```text
ac
```



#### Test case 3

**Input for this case**

```text
4 5
```

**Output for this case**

```text
baaa
```



#### Test case 4

**Input for this case**

```text
3 2
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CAB](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CAB)

### [](#problem-statement-1)Problem Statement:

Given two integers `n` (number of characters) and `k` (integer to be represented in character values), construct a string using exactly `n` characters with the smallest lexicographical order such that the sum of the character values equals `k`. The character value of ‘a’ is 2^0, ‘b’ is 2^1, …, and ‘z’ is 2^{25}. If it’s impossible to form such a string, print `-1`.

### [](#approach-2)Approach:

**Bit Representation**:

- Calculate the number of `1`s in the binary representation of `k`. This step ensures you understand the minimum distinct elements required.

- If `num > n` or `n > k`, output `-1` since it’s impossible to form the string.

**Frequency Array**:

- Create a `freq` array where `freq[i]` represents the number of times the character corresponding to value `2^i` should be used.

- Populate the `freq` array by iterating through the bits of `k` and setting `freq[25 - temp]` (to represent ‘z’ down to ‘a’).

**Redistribution Logic**:

- Redistribute bits to achieve exactly `n` characters. Start with lower bit positions and move excess bits to higher positions, doubling their value (e.g., moving two 'a’s to one ‘b’) until the count of characters reaches `n`.

**String Construction**:

- Construct the result string using the characters based on their frequencies, ensuring lexicographical order.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(n + log(k))`, where `n` is the maximum number of characters needed in the result, and `log(k)` is the number of bits in `k`.

- For typical integer limits (e.g., `k` up to 32 or 64 bits), the `log(k)` factor is constant, so the time complexity is dominated by `O(n)`.

- **Space Complexity:** `O(n)` for the string result, plus `O(1)` for the auxiliary `freq` array because of constant value.

</details>
