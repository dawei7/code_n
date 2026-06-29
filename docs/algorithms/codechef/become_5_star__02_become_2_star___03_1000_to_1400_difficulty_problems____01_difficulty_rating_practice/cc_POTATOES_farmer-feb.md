# Farmer Feb

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POTATOES |
| Difficulty Rating | 1148 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [POTATOES](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/POTATOES) |

---

## Problem Statement

Farmer Feb has three fields with potatoes planted in them. He harvested **x** potatoes from the first field, **y** potatoes from the second field and is yet to harvest potatoes from the third field. Feb is very superstitious and believes that if the sum of potatoes he harvests from the three fields is a prime number ([http://en.wikipedia.org/wiki/Prime_number](http://en.wikipedia.org/wiki/Prime_number)), he'll make a huge profit. Please help him by calculating for him the minimum number of potatoes that if harvested from the third field will make the sum of potatoes prime. At least one potato should be harvested from the third field.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. Each of the next **T** lines contain 2 integers separated by single space: **x** and **y**.

### Output

For each test case, output a single line containing the answer.

### Constraints

- **1** ≤ **T** ≤ **1000**

- **1** ≤ **x** ≤ **1000**

- **1** ≤ **y** ≤ **1000**

---

## Examples

**Example 1**

**Input**

```text
2
1 3
4 3
```

**Output**

```text
1
4
```

**Explanation**

In example case 1: the farmer harvested a potato from the first field and 3 potatoes from the second field. The sum is 4. If he is able to harvest a potato from the third field, that will make the sum 5, which is prime. Hence the answer is 1(he needs one more potato to make the sum of harvested potatoes prime.)

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 3
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/POTATOES)

[Contest](http://www.codechef.com/APRIL14/problems/POTATOES)

**Author:** [Shalini Sah](http://www.codechef.com/users/mischievous_me)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu) and [Mahbubul Hasan](http://www.codechef.com/users/white_king)

**Editorialist:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

[Prime numbers](http://en.wikipedia.org/wiki/Prime_number)

### PROBLEM:

Given x(<=1000) and y(<=1000), find the smallest z(>0) such that (x+y+z) is prime.

### EXPLANATION:

Keep increasing i (starting from 1) until (x+y+i) is not prime. i will never exceed 40 since x+y <= 2000. So we can afford to check each number one by one.

To check if a number N is prime:

``def check_prime(N):
    for i=2 to sqrt(N):
        if N%i==0:
            return false
    return true
``

Alternatively, we can use sieve of eratosthenes to check primes.

Naive primality testing (checking if N is divisible by any number from 2 to N-1) could also pass if precomputation is done.

### AUTHOR’S AND TESTER’S SOLUTIONS:

To be updated soon.

</details>
