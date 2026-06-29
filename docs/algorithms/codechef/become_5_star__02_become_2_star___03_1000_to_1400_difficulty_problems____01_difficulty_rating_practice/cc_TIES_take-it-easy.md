# Take it Easy

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TIES |
| Difficulty Rating | 1289 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [TIES](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/TIES) |

---

## Problem Statement

*Believe nothing you hear, and only one half that you see*

On a Halloween evening, young Tim embarks on a candy-filled quest with his friends, dressed as ghouls and witches.
There are $N$ friends, initially the $i$-th of them has $A_i$ candies.

To truly savor the spooky spirit, Tim wishes for everyone to have an **equal** number of candies.
To achieve this, he is armed with a magical operation which is as follows:
- First, Tim chooses two integers $i$ and $j$  ($1 \leq i, j \leq N$), denoting the indices of two of his friends.
- Next, he chooses an integer $k$ that's **at least $1$**, while also satisfying $2^k \leq A_i$.
That is, the inequality $2 \leq 2^k \leq A_i$ should hold.
- Finally, Tim takes away $2^k$ candies from friend $i$ and gives them to the friend $j$.
That is, their candy counts change to $(A_i - 2^k)$ and $(A_j + 2^k)$ respectively.

Determine whether all of Tim's friends can have an equal number of candies in the end, after some (possibly zero) operations are performed.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the number of friends.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the initial number of candies each friend has.

---

## Output Format

For each test case output the answer on a new line — `"Yes"` (without quotes) if it is possible to perform operations such that in the end all friends have same number of candies, and `"No"` (without quotes) otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, `"Yes"`, `"YES"`, and `"yEs"` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq  10^5 $
- $1 \leq A_i \leq 10^3$
- The sum of $N$ over all  test cases does not exceed $3 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
4 4
3
2 4 12
2
4 6
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Test case $1$:** No operations are required, everyone already has an equal number of candies.

**Test case 2:** Consider the following sequence of operations:
- Move $2^2 = 4$ candies from friend $3$ to friend $1$. The candy counts are now $[6, 4, 8]$.
- Move $2^1 = 2$ candies from friend $3$ to friend $2$. The candy counts are now $[6, 6, 6]$.

Everyone has an equal number of candies now, as required.

**Test case $3$:** There is no way to perform operations to have all friends with same number of candies

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
4 4
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
2 4 12
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
2
4 6
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TIES)

[Contest: Division 1](https://www.codechef.com/START105A/problems/TIES)

[Contest: Division 2](https://www.codechef.com/START105B/problems/TIES)

[Contest: Division 3](https://www.codechef.com/START105C/problems/TIES)

[Contest: Division 4](https://www.codechef.com/START105D/problems/TIES)

***Author:***  [still_me](https://www.codechef.com/users/still_me)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1289

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You have an array A.

In one move, you can choose an integer k \geq 1 and two indices i and j, and move 2^k from A_i to A_j. However, the elements of A must remain non-negative at all times.

Can all the elements of A be made equal?

# [](#explanation-5)EXPLANATION:

First, observe that performing an operation doesn’t change the overall sum of the array, since we’re just moving values around a bit.

Let S = A_1 + A_2 + \ldots + A_N be the sum of the array elements.

Suppose we’re able to make all the elements equal, say to y.

Then, the sum of the final array is just N\cdot y, which should equal S.

This uniquely fixes y = \frac{S}{N}.

In particular, N must divide S — if it doesn’t, the answer is immediately `No`.

Next, we need to check if everything can indeed be made equal to y = \frac{S}{N}.

We’re allowed to move any powers of 2 other than 2^0 = 1.

Notice that since we have unlimited moves, we can just move **exactly** 2 at each step (do you see why?)

In other words, our operation is just “move 2 from one element to another”.

For an element A_i to be able to reach y at all using this operation, we must have |y - A_i| be even, since each element can only be increased/decreased by 2.

We now have two conditions:

- N should divide S.

- For every i, |A_i - y| should be even (where y = \frac{S}{N}).

Equivalently, every A_i should have the same parity as y.

These two conditions are sufficient for the answer to be `Yes`!

How?

The argument to show this is quite simple.

Consider a situation where not all the A_i are equal to y = \frac{S}{N}.

Since their sum is S, this means some element has to be strictly greater than y *and* some other element has to be strictly less than y.

Now, just move 2 from the larger element to the smaller one.

Repeat this till all the A_i become equal.

This gives us a solution in \mathcal{O}(N): check the above two conditions; if they’re both satisfied the answer is `Yes`, otherwise it’s `No`.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    S = sum(a)
    if S%n != 0: print('No')
    else:
        target = S//n
        ans = 'Yes'
        for i in range(n):
            if a[i]%2 != target%2: ans = 'No'
        print(ans)
``

</details>
