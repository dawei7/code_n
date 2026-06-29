# Lucky Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LUCKY3 |
| Difficulty Rating | 1875 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [LUCKY3](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/LUCKY3) |

---

## Problem Statement

Chef loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits **4** and **7**. For example, numbers **47**, **744**, **4** are lucky and **5**, **17**, **467** are not.

 Chef also use term **"lucky sum"**. Lucky sum is an operation between two integers. Let the first integer is **A**, **A[i]** equals **i-th** digit of **A** (0-base numeration, from right to left) and the second integer is **B**, **B[i]** equals to **i-th** digit of **B**. Then the lucky sum of **A** and **B** is equal to **C**, **C[i] = max(A[i], B[i])**. If **i** is greater than or equal to size of integer, the **i-th** digit is equal to **0**. For example, the lucky sum of **47** and **729** equals **749**, the lucky sum of **74** and **92** and **477** equals **497**.

 Chef has an array **W** of integers. Find a number of non-empty subsequences of **W** such that the lucky sum of integers in that subsequences is a lucky number.

 Subsequence of **W** is created by erasing some number (probably zero) elements from **W**.

### Input

First line contains one number **T**, number of test cases. Each test is formed as follows: first line contains integer **n** - number of integers in **W**, next line contains **n** integers - array **W** for corresponding test.

### Output

For each **T** test cases print one integer - result for the corresponding test.

### Constraints

1 <= **T** <= 10

1 <= **n** <= 50

1 <= **Wi** < 10^9

---

## Examples

**Example 1**

**Input**

```text
2
2
4 7
3
43 87 44
```

**Output**

```text
3
2
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
4 7
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
43 87 44
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/LUCKY3/)

[Contest](http://www.codechef.com/JAN12/problems/LUCKY3/)

### DIFFICULTY

MEDIUM

### EXPLANATION

First of all, notice that there are exactly 1022 lucky number of length between 1 and 9. We can solve problem for each lucky number independently, then sum up all results and get total result.

Now we need to solve problem for some lucky number L (L[i] - i-th digit if number L, starting from right). If there is some number W[i] in input array W that has some digit on some postion which is greater than corresponding digit in L (i. e. there exits some j, that W[i][j] > L[j]), then we can delete W[i] from W (because if we pick that number to subsequence then we’ll never get lucky number L).

Now we should think about dynamic programming approach to solve problem for current lucky number L. You can read about this method here: [http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg](http://community.topcoder.com/tc?module=Static&d1=tutorials&d2=dynProg)

Lets start think about what information we need to handle in DP state. Here we need 2-dimensional state space. Of course, we need to review all numbers of W, so first dimension of DP sate must be [pos], pos = [0; n) (0-based numberation of array W, n - size of W). State [pos] means that we already have reviewed all numbers up to position pos in array W and have picked some to our set. But what set? We don’t know that. We need some more information to know whenever we will achieve current lucky number in current set (using lucky sum operation). If we already have some set of numbers (with indexes up to pos) and some digits of lucky sum of all numbers in that set are already lucky, we need to now that. To achieve that we need to handle bitmask ( [http://en.wikipedia.org/wiki/Mask_(computing)](http://en.wikipedia.org/wiki/Mask_(computing)) ) of digits that are already the same like in current lucky L, i. e. j-th bit of bitmask must be turned on if j-th digit of lucky sum of current selected set is equal to L[j] (it can not be greater than L[j], because of second paragraph). So, now we have new state of DP, now it is [pos][mask].

Now we should think about transitions of DP. If we are on state [pos][mask] we can do two things. First - do not choose W[pos] to current set. Then mask, of course, will not changes (because we do not change out current set) and we go to the sate [pos+1][mask]. If we choose W[pos], then we go to the state [pos+1][new_mask]. What is new_mask? This is new_mask created by turning on some bit of musk, which are corresponding to the positions of digits of W[pos] that are equal to L (i. e. if for some j W[pos][j] = L[j] and j-th bit is not turned on in mask, then new_mask should have j-th bit turned on. All bits that were turned on in mask must be also turned on in new_mask).

So, considering 2D DP approach we can handle all possible states which will include all subsequences. Please, read setters solution for further understanding of DP approach.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/January/Setter/LUCKY3.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/January/Tester/LUCKY3.c).

</details>
