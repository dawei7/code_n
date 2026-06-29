# Movie Weekend

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MOVIEWKN |
| Difficulty Rating | 1175 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MOVIEWKN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MOVIEWKN) |

---

## Problem Statement

Little Egor is a huge movie fan. He likes watching different kinds of movies: from drama movies to comedy movies, from teen movies to horror movies. He is planning to visit cinema this weekend, but he's not sure which movie he should watch.

There are **n** movies to watch during this weekend. Each movie can be characterized by two integers **Li** and **Ri**, denoting the length and the rating of the corresponding movie. Egor wants to watch *exactly* one movie with the maximal value of **Li × Ri**. If there are several such movies, he would pick a one with the maximal **Ri** among them. If there is still a tie, he would pick the one with the minimal index among them.

Your task is to help Egor to pick a movie to watch during this weekend.

### Input

The first line of the input contains an integer **T** denoting the number of test cases.

The first line of the test case description contains an integer **n**.

The second line of the test case description contains **n** integers **L1, L2, ...,Ln**. The following line contains **n** integers **R1, R2, ..., Rn**.

### Output

For each test case, output a single integer **i** denoting the index of the movie that Egor should watch during this weekend. Note that we follow 1-based indexing.

### Constraints

- **1 ≤ T ≤ 5**

- **1 ≤ n ≤ 100**

- **1 ≤ Li, Ri ≤ 100**

---

## Examples

**Example 1**

**Input**

```text
2
2
1 2
2 1
4
2 1 4 1
2 4 1 4
```

**Output**

```text
1
2
```

**Explanation**

In the first example case, both films have the same value of **L × R**, but the first film has a better rating.

In the second example case, the second and the fourth movies are equally good, but the second movie has a smaller index.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 1 4 1
2 4 1 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/MOVIEWKN)

[Contest](http://www.codechef.com/COOK69/problems/MOVIEWKN)

**Author:** [Constantine Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Pavel Sheftelevich](http://www.codechef.com/users/pavel1996)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

cakewalk

### PREREQUISITES:

None

### PROBLEM:

You want to select a movie to watch on the weekend. There are n movies in cinema : i-th of them has rating R_i and length (duration) L_i. You want to select a movie according to following criterions applied in order.

- First you choose a movie with highest value of L_i * R_i.

- If there are more than one such movies, you select the one with the highest rating R_i.

- If still, there are more than one such movies, you select the one with the minimum index i.

You have to output the index of movie (1-based) that you are going to watch.

### QUICK EXPLANATION:

Just implement what is said in the problem statement.

### EXPLANATION:

Let us iterate over i from 1 to n. Let max_{LR} denote the the maximum value of L_j * R_j till now (i.e. for all j < i). Similarly, let maxR denote the maximum rating R_j among all the movies such that L_j * R_j = max_{LR}, j < i. Also, let ans denote the index corresponding to the movie you should select till now to watch. Now, we want to consider the i-th movie and want to find the what would be the best movie you select to watch after considering i-th movie.

There are following possible scenarios.

- If L_i * R_i < max_{LR}, then this movie can not be the best movie to watch. So you skip this movie.

- If L_i * R_i > max_{LR}, then this movie will be the best movie to watch till now. Update max_{LR} to  L_j * R_j and maxR to R_i.

- If L_i * R_i = max_{LR}, then it means that current movie might be a possible best movie to watch. We should now check the second criteria : i.e., whether the rating of current movie is strictly greater than max_R or not. If yes, then we will select this movie to be the best movie till now. Otherwise, if rating R_i of this movie is equal to max_R, then we will go to third criteria and check whether the index of this movie is less than ans or not. Note that this can never be possible, because we are going in increasing order of indices. So, we don’t even need to consider this case.

At the end of the iteration, ans will be the index of best movie to watch.

**Pseudo Code**

``
long maxLR = 0;
long maxR = 0;
int ans = 0;
for (int i = 1; i <= L.length; i++) {
    if (L[i] * (long) R[i] > maxLR) {
        maxLR = L[i] * (long) R[i];
        maxR = R[i];
        ans = i;
    } else if (L[i] * (long) R[i] == maxLR) {
        if (R[i] > maxR) {
            maxR = R[i];
            ans = i;
        }
    }
}
print ans

``

### Time complexity:

We iterate over the arrays L, R only once. Hence time complexity is \mathcal{O}(n).

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK69/Setter/MOVIEWKN.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK69/Tester/MOVIEWKN.cpp).

</details>
