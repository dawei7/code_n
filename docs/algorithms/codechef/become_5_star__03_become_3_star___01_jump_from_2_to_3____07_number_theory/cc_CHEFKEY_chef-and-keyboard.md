# Chef and Keyboard

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFKEY |
| Difficulty Rating | 1323 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [CHEFKEY](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/CHEFKEY) |

---

## Problem Statement

Chef is a well known programmer. He owns a brand new Android phone of screen size of dimension **n × m** (**n** denotes the height of the phone and **m** denotes the width). Chef wants to design a program for painting the screen. He figured out **c** colors, which he will use to paint the screen. He wants to paint some rectangular section of pixels of the screen each with different color. Also Chef would like to use all of his **c** colors in painting.

Can you help Chef in finding number of different dimensions of rectangular section he can paint? In other words, find number of pairs **x, y** such that Chef can paint a rectangular section of dimension **x × y** (**x** denotes height, **y** denotes width) on the screen. Please note that Chef uses a fix orientation of his phone and is not allowed to rotate it, i.e. height always stays **n** and width always stays **m** and not the other way around.

### Input

First line of the input contains an integer **T** denoting the number of test cases. **T** test cases follow.

Only line of each test case contains three space separated integers **n, m, c**.

### Output

For each test case, output a single line containing the answer for the test case.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **n, m** ≤ **106**

- **1** ≤ **c** ≤ **106**

### Subtasks

- Subtask #1: (40 points) **1** ≤ **n, m** ≤ **100**, **1** ≤ **c** ≤ **104**

- Subtask #2: (60 points) **original constraints**

---

## Examples

**Example 1**

**Input**

```text
2
4 6 12
3 3 10
```

**Output**

```text
3
0
```

**Explanation**

**Test case 1.** Possible pairs of dimensions are **(2, 6)**, **(3, 4)** and **(4, 3)**. Note that the rectangular section of dimension **(1, 12)** can't be painted as it can't fit into the screen, because 12 > 6.

**Test case 2.** There does not exist any rectangle of desired dimensions which can have 10 different pixels painted.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 6 12
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 3 10
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CHEFKEY)

[Contest](http://www.codechef.com/OCT16/problems/CHEFKEY)

### DIFFICULTY

Cakewalk

### PREREQUISITES

loops, simple maths

### PROBLEM

Find number of (x, y) pairs such that 1 \leq x \leq H, 1 \leq y
\leq W and x * y = K.

### QUICK EXPLANATION

Iterate over x and you can check if there exists a valid y in the desired range satisfying x \cdot y = K or not.

### EXPLANATION

##\mathcal{O}(H * W) bruteforce solution

Constraints on H and W are quite small. We can exploit these to get a

simple bruteforce solution. We iterate over all (x, y) pairs and check

whether their product x * y is equal to K or not. We can count such

valid pairs in \mathcal{O}(W * H) time.

**Pseudo Code:**

``ans = 0
for x = 1 to H:
  for y = 1 to W:
    if x * y == K:
      ans++
``

##\mathcal{O}(K log K) solution

Let us make a simple change in the last solution? What if we you stop iterating over y when the value

of x * y exceeds K. Will that improve time complexity?

``ans = 0
for x = 1 to H:
  for y = 1 to W:
    if x * y > K:
      break;
    if x * y == K:
      ans++
``

Yes, it will. Let us estimate it. From a casual look, it looks that

its time complexity will still be \mathcal{O}(H * W). But it’s not. Let us

delve into depth.

For each x, the inner loop over y will run at most \frac{K}{x} times. So,

total number of iterations the program will be run will be given by

\frac{K}{1} + \frac{K}{2} + \dots + \frac{K}{H}

\leq \frac{K}{1} + \frac{K}{2} + \dots + \frac{K}{K}

\leq K \cdot (\frac{1}{1} + \frac{1}{2} + \dots + \frac{1}{K})

The expression

\frac{1}{1} + \frac{1}{2} + \dots + \frac{1}{n}

is also known as harmonic sum H_n. One can prove that H_n = \mathcal{O}(log \, n).

Hence, the time complexity will be \mathcal{O}(K log K).

##\mathcal{O}(H) solution

Let us exploit the condition x * y = K. For a fixed x, do we really need to iterate

over all y's to check how many of them satisfy x * y = K. It turns out, no. Firstly there will be at most a single y. If K is not divisible by x, then there can’t exist such y. Otherwise y will be \frac{K}{x}.

In summary, we iterate over only

x values and find the corresponding y (if it exists), and

check whether the y is \geq 1 and \leq H.

Time complexity of this method will be \mathcal{O}(H), as are iterating over x values only once.

#### Factorization based solutions

If x \cdot y = K, then both x and y should divide K. So we can find all the divisors of the K. Let x be one such divisor, then y will be \frac{K}{x}.

You can find all the divisors of K in \mathcal{O}(sqrt(K)) time.

### EDITORIALIST’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Editorialist/CHEFKEY.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/OCT16/Tester/CHEFKEY.cpp).

</details>
