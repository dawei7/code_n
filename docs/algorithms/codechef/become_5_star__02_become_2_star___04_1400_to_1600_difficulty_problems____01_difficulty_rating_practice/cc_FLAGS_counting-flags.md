# Counting Flags

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLAGS |
| Difficulty Rating | 1446 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [FLAGS](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/FLAGS) |

---

## Problem Statement

Mike is a famous traveler. He visits about 100 countries a year and buys the flag of each country he has been to.

Mike knows, that there are some flags, that correspond to one pattern, but colored in different ways. E.g. the flag of Ireland([link](http://en.wikipedia.org/wiki/File:Flag_of_Ireland.svg)) and the flag of Belgium([link](http://en.wikipedia.org/wiki/File:Flag_of_Belgium.svg)). In this problem we consider only **five** 2,2cm✕1,1cm patterns of flags:

There are **N** different colors available to paint the flags and the colors are denoted by integers from 1 to **N**.

Mike wants you to count the number of different well-painted flags. We call a flag well-painted if it's made according to the following algorithm:

- Pick up one of the flag patterns considered above;

- Paint each one-colored polygon on the pattern in a color encoded by an integer from **1** to **N**. Different colors are encoded with different integers. If two different one-colored polygons share a common side(not corner), than they must be painted in different colors. In any other case they can be painted in both equal and different colors.

Two flags are different, if they look different(have at least one pixel painted with different color).

Help Mike!

### Text version of the pictures:

**Picture 1**

112233

112233

112233

111111

222222

333333

112222

112222

113333

122223

111333

144443

111222

333222

333444

**Picture 2**

112211

112211

112211

221122

221122

221122

111111

222222

111111

222222

111111

222222

### Input

The first line of the input contains integer **T**, denoting the number of testcases. The description of **T** testcases follows.

The only line of each test case contains integer **N**, denoting the number of different colors, that can be used while painting a flag pattern.

### Output

For each testcase, output a single line containing an integer - the answer for the corresponding query.

### Constraints

1 ≤ **T** ≤ 10 000;

1 ≤ **N** ≤ 10 000 for each testcase.

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
0
4
42
```

**Explanation**

There are **four** different well-painted flags for **N** = 2 different colors :

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
42
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/FLAGS)

[Contest](http://www.codechef.com/COOK47/problems/FLAGS)

**Author:** [Konstantin Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Tasnim Imran Sunny](http://www.codechef.com/users/rustinpiece)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

simple combinatorics.

### PROBLEM:

Given following 5 patterns of a flag.

112233

112233

112233

111111

222222

333333

112222

112222

113333

122223

111333

144443

111222

333222

333444

Your need to count the number of different well-painted flags. We call a flag well-painted if it’s made according to the following algorithm:

- Pick up one of the flag patterns considered above;

- Paint each connected component in an color encoded by an integer from 1 to N. Different colors are encoded with different integers.

If two different connected components share a common side(not corner), than they must be painted in different colors.

In any other case they can be painted in both equal and different colors.

### QUICK EXPLANATION

- For each flag, we can find out the number of different well painted flags. The flags are given in such a way that no two flags in the 5 flags

will be similar to each other. So you can solve the problem independently for each flag.

- For a single flag, find number of ways of painting that flag using N colors.

### EXPLANATION

For each flag, we can find out the number of different well painted flags independently because the shape of the flags are in such a way

that no two flags in the above given 5 flags will be similar to each other in any possible painting.

So you can solve the problem independently for each flag.

**Flag 1**

112233

112233

112233

We can use minimum 2 colors to make the flag well painted.

112211

112211

112211

So here we can paint the first connected component by using any of the N possible colors. Then for second connected component, total possible

colors available will be N - 1 because we can not use the color of first connected component. Then for third connected component, total

possible colors available will also be N - 1 because we can not use color of second connected component.

Hence number of ways = N * (N - 1) * (N - 1).

**Flag 2**

111111

222222

333333

We can use minimum 2 colors to make the flag well painted.

111111

222222

111111

So here we can paint the first connected component by using any of the N possible colors. Then for second connected component, total possible

colors available will be N - 1 because we can not use the color of first connected component. Then for third connected component, total

possible colors available will also be N - 1 because we can not use color of second connected component.

Hence number of ways = N * (N - 1) * (N - 1).

**Flag 3**

112222

112222

113333

We can use minimum 3 colors to make the flag well painted.

112222

112222

113333

So here we can paint the first connected component by using any of the N possible colors. Then for second connected component, total possible

colors available will be N - 1 because we can not use the color of first connected component. Then for third connected component, total

possible colors available will also be N - 2 because we can not use color of first and second connected component.

Hence number of ways = N * (N - 1) * (N - 2).

**Flag 4**

122223

111333

144443

We can use minimum 3 colors to make the flag well painted.

122223

111333

122223

So here we can paint the first connected component by using any of the N possible colors. Then for second connected component, total possible

colors available will be N - 1 because we can not use the color of first connected component. Then for third connected component, total

possible colors available will also be N - 2 because we can not use color of first and second connected component. Then for the fourth connected

component, total numbers of colors available will be N - 2 because we can not use first and thrid connected component.

Hence number of ways = N * (N - 1) * (N - 2) * (N - 2).

**Flag 5**

111222

333222

333444

We can use minimum 3 colors to make the flag well painted.

111222

333222

333111

So here we can paint the first connected component by using any of the N possible colors. Then for second connected component, total possible

colors available will be N - 1 because we can not use the color of first connected component. Then for third connected component, total

possible colors available will also be N - 2 because we can not use color of first and second connected component. Then for the fourth connected

component, total numbers of colors available will be N - 2 because we can not use second and thrid connected component.

Hence number of ways = N * (N - 1) * (N - 2) * (N - 2).

**Final answer**

- For flag 1: N * (N - 1) * (N - 1).

- For flag 2: N * (N - 1) * (N - 1).

- For flag 3: N * (N - 1) * (N - 2).

- For flag 4: N * (N - 1) * (N - 2) * (N - 2)

- For flag 5: N * (N - 1) * (N - 2) * (N - 2)

**Pseudo code**

``long long n;
read n
long long ans = 2*n*(n-1)*(n-1) + n*(n-1)*(n-2) + 2*n*(n-1)*(n-2)*(n-2);
print ans
``

**Complexity**

We just need constant amount of addition and multiplication operations. Hence the time complexity will be O(1).

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK47/Setter/FLAGS.cpp)

[Tester’s solution](https://codechef_shared.s3.amazonaws.com/download/Solutions/COOK47/Tester/FLAGS.cpp)

</details>
