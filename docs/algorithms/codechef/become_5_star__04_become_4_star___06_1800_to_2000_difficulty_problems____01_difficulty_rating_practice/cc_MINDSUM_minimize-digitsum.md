# Minimize Digitsum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINDSUM |
| Difficulty Rating | 1862 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MINDSUM](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MINDSUM) |

---

## Problem Statement

You are given positive integers $N$ and $D$. You may perform operations of the following two types:
- add $D$ to $N$, i.e. change $N$ to $N+D$
- change $N$ to $\mathop{\mathrm{digitsum}}(N)$

Here, $\mathop{\mathrm{digitsum}}(x)$ is the sum of decimal digits of $x$. For example, $\mathop{\mathrm{digitsum}}(123)=1+2+3=6$, $\mathop{\mathrm{digitsum}}(100)=1+0+0=1$, $\mathop{\mathrm{digitsum}}(365)=3+6+5=14$.

You may perform any number of operations (including zero) in any order. Please find the minimum obtainable value of $N$ and the minimum number of operations required to obtain this value.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $D$.

### Output
For each test case, print a single line containing two space-separated integers — the minimum value of $N$ and the minimum required number of operations.

### Constraints
- $1 \le T \le 10$
- $1 \le N, D \le 10^{10}$

### Subtasks
**Subtask #1 (30 points):** $1 \le N, D \le 100$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 1
9 3
11 13
```

**Output**

```text
1 9
3 2
1 4
```

**Explanation**

**Example case 1:** The value $N=1$ can be achieved by 8 successive "add" operations (changing $N$ to $10$) and one "digit-sum" operation.

**Example case 2:** You can prove that you cannot obtain $N=1$ and $N=2$, and you can obtain $N=3$.
The value $N=3$ can be achieved by one "add" and one "digitsum" operation, changing $9$ to $12$ and $12$ to $3$.

**Example case 3:** $N=1$ can be achieved by operations "add", "add", "digitsum", "digitsum": $11 \rightarrow 24 \rightarrow 37 \rightarrow 10 \rightarrow 1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1 9
```



#### Test case 2

**Input for this case**

```text
9 3
```

**Output for this case**

```text
3 2
```



#### Test case 3

**Input for this case**

```text
11 13
```

**Output for this case**

```text
1 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Link :

[Division 1](https://www.codechef.com/OCT18A/problems/MINDSUM)

[Division 2](https://www.codechef.com/OCT18B/problems/MINDSUM)

[Practice](https://www.codechef.com/problems/MINDSUM)

### Author : [pekempey](https://www.codechef.com/users/pekempey)

### Tester : [Misha Chorniy](https://www.codechef.com/users/mgch)

### Editorialist : [Anand Jaisingh](https://www.codechef.com/users/anand20)

### Pre-Requisites :

Properties of digital roots

### Explanation :

Digital Sums and properties of digital sums may be common to some participants. Let’s establish 2 very important properties of digital sums required to solve this problem.

Let Dr(x) be a function defined for integer x as :

Dr(x)= x,  if  0 \le x \le 9 ,

else

Dr(x)=Dr(Sum-of-digits(x))

This function Dr(x) is called the digital root of a number x. Now,

Dr(a+b) = Dr(Dr(a)+Dr(b)),

Dr(ab) = Dr(Dr(a)\cdot Dr(b))

These are well known properties, and you can find proofs of them [here](https://en.m.wikipedia.org/wiki/Digital_root). It is very clear that the minimum value we are trying to find is a single digit number.

**Claim 1 :** : The minimum value is always the minimum over :  Dr(N+kD) for some non-negative integer k.

Proof :

 Dr(N+kD)=Dr(Dr(N)+Dr(kD)) ... (1)

Now, Dr(kd) = Dr(Dr(k) \cdot Dr(D)) .

Possible values of Dr(k) are  0,1,2...9  , given by numbers  k=0,1,2...9

Now, Dr(x)=Dr(Sum-of-digits(x)) ... (2)

So, the minimum value for N is obviously equal to the minimum value for Sum-of-digits(N). Reducing the answer once and then adding D **does not affect** the minimum possible value that can be reached. If any any place, we have a reduce operation followed by an add operation, the we can do the add operation and then the reduce operation without affecting the possible roots we can reach. This is proved as a combination of formulae (1) and (2)

Doing a reduce operation followed by an add operation can be replaced by doing an add operation followed any further operations and we can still reach the same set of roots. In short, we can do all add operations first, all reduce operations later, and reach any number that can be possibly reached by any set of operations

So, using these two claims, we can prove the minimum possible value is the minimum of Dr(N+kD)  where  0 \le k \le 9

Now, to find the minimum number of steps, we must first note that the relative order of the add and Sum-of-digits operations **does affect the answer**. However, we can note that the Sum-of-digits function is an extremely fast decreasing function.

Any number  \le 10^{10} goes to a number  \le 90, any number  \le 90  goes to something  \le 18  and so on. In short , any number can be reduced to its digital root in  \le 3-5  steps.

Via this, we can prove that the value of the minimum steps can never be greater than 15. This is a loose upper bound, not the exact one. Let’s prove this via contradiction : If some process takes  > 15  steps, we can always take N to the value of N+kD, k \le 9  that provides the minimum possible value, and then reduce it in 5-6 steps. Using this fact, we can now in-fact construct a brute force algorithm.

We can follow a complete brute force recursion algorithm, that at each step branches in 2 different directions, one x=Sum-of-digits(x), the other being x=x+D, but only until a recursion depth of 15. In this way, we stop after exploring 2^{15} different ways.

After reading all proofs mentioned above, understanding the code should be trivial. Also note that the greedy nature of this problem permits many other solutions too, and you can read about some of them using the comments below.

Overall time complexity  O(T \cdot 2^{15} \cdot log_{10} N )

### Tester’s Code : : [Link](https://www.ideone.com/uq9plQ)

### My Code :  : [Link](https://www.ideone.com/WZN3xu)

</details>
