# Churu and Balls

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CBALLS |
| Difficulty Rating | 1697 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [CBALLS](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/CBALLS) |

---

## Problem Statement

Little Churu is a naughty child, who likes to play with balls. He has **N** buckets. Each bucket contains one or more balls. He has numbered his buckets **1** to **N** (both inclusive). He has an infinite supply of extra balls, apart from the ones already in the buckets. He wants to add zero or more number of balls to each of the buckets in such a way, that number of balls in the buckets are in a non-decreasing order, and their [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) is strictly greater than 1.

He wants to do it using the minimum number of extra balls. As he is too young to solve the problem, please help him with the solution.

### Input

- First line of input contains an integer **T** denoting the number of test cases.

- For each test case, first line contains an integer **N** denoting the number of buckets.

- Second line of each test case contains **N** space separated integers, where the **ith** denotes the number of balls in the **ith** bucket.

### Output
For each test case, output a line containing a single integer — the answer for that test case.

### Constraints

**Subtask #1: 20 points**

- **1 ≤ T  ≤ 10, 1 ≤ N  ≤ 1000, 1 ≤ number of balls in a bucket  ≤ 1000**

**Subtask #2: 80 points**

- **1 ≤ T  ≤ 10, 1 ≤ N  ≤ 10000, 1 ≤ number of balls in a bucket  ≤ 10000**

---

## Examples

**Example 1**

**Input**

```text
1
3
11 13 15
```

**Output**

```text
3
```

**Explanation**

Add one ball to each of the buckets.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CBALLS)

[Contest](http://www.codechef.com/JAN16/problems/CBALLS)

**Author:** [Amit Pandey](https://www.codechef.com/users/amitpandeykgp)

**Tester:** [Antoniuk Vasyl](https://www.codechef.com/users/antoniuk1) and [Misha Chorniy](https://www.codechef.com/users/mgch)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Easy

### PREREQUISITES:

Primes, Sieve of Eratosthenes

### PROBLEM:

Given is an array A of numbers. We need to increase each number by a certain amount such that the numbers form a non-decreasing sequence and the GCD of all of them is strictly greater than 1.

### EXPLANATION:

**Subtask 1**

For this subtask, we have been given that the elements in the array are positive integers smaller than or equal to 10^3. Also, the size of the array is at max 10^3. We just need to increase each element such that the array forms a non-decreasing subsequence and at the same time has GCD greater than 1. We can try each number between 1 and 10^3 as a potential GCD and change the array elements to its multiples in non-decreasing order. Here is the pseudocode of the algorithm:

``let ans = infinity //variable which will store global minima

for i = 1 to 10^4
{
    let current_multiple = 0
    //current_multiple stores that multiple of i which the element
    //under consideration must be increased to. it is initially set to 0

    let temp_ans = 0
    //temp_ans stores the total increase if multiples of i are used

    for j = 1 to N
    {
        if(A[j] > current_multiple)
        {
            //if A[j] is greater than the current multiple of i
            //then we need to take a bigger multiple. This is because we need
            //a non-decreasing sequence.

            current_multiple = ((A[j] + i - 1)/i) * i;
        }

        //accumulating the change
        temp_ans += current_multiple - A[j];
    }

    //calculating minimum over all possible primes
    ans = minimum(ans, temp_ans);
}

return ans;
``

**Subtask 2**

For this subtask, we have to make an important observation. We have been given that the elements in the array are positive integers smaller than or equal to 10^4. Also, the size of the array is at max 10^4. The \mathcal{O}(N^2) algorithm will time out.

The crucial observation is that for the numbers to have GCD greater than 1, all of them should be divisible by at least one common prime. That gives us a big reduction: we only have to check for each prime smaller than 10^4 that which prime’s multiples yield the best possible result. Since there are only 1229 primes smaller than 10^4, this method works within time limits for the given constraints. The only change from the above pseudocode is that we skip all composite i. Marking all primes under 10^4 can be done as preprocessing using [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes). Check editorialist’s program for implementation. Here is the pseudocode of the algorithm:

``prime[i] = 1 if i is prime else 0 //marked using sieve
let ans = infinity //variable which will store global minima

for i = 1 to 10^4
{
    if (prime[i] != 1)
        skip and go on to next i;

    let current_multiple = 0
    //current_multiple stores that multiple of i which the element
    //under consideration must be increased to. it is initially set to 0

    let temp_ans = 0
    //temp_ans stores the total increase if multiples of i are used

    for j = 1 to N
    {
        if(A[j] > current_multiple)
        {
            //if A[j] is greater than the current multiple of i
            //then we need to take a bigger multiple. This is because we need
            //a non-decreasing sequence.

            current_multiple = ((A[j] + i - 1)/i) * i;
        }

        //accumulating the change
        temp_ans += current_multiple - A[j];
    }

    //calculating minimum over all possible primes
    ans = minimum(ans, temp_ans);
}

return ans;
``

The editorialist’s program follows the editorial. Please see for implementation details.

### OPTIMAL COMPLEXITY:

\mathcal{O}(NP) per test case where P is the number of primes less than equal to 10^4.

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/JAN16/Setter/CBALLS.cpp)

[Tester](http://www.codechef.com/download/Solutions/JAN16/Tester/CBALLS.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/JAN16/Editorialist/CBALLS.cpp)

</details>
