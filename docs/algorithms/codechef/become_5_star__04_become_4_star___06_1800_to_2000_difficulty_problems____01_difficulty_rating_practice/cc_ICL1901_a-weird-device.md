# A Weird Device

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ICL1901 |
| Difficulty Rating | 1810 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ICL1901](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ICL1901) |

---

## Problem Statement

You were strolling outside the restaurant at the end of the universe. On a metaspiral path you stumble upon a weird device which takes a three-digit number as input and processes it. The Hitchhiker's guide to the galaxy explains that it processes the input in the following manner:

- Multiplies it with 13, followed by 11 and then 7
- Outputs all the distinct three-digit numbers possible from the digits of the new number (each digit can only be used once)

Your friend Zaphod is in a playful mood, and does the following with the device-
- Given a three-digit positive number $K$, he feeds it to the device for processing.
- He then takes the numbers it gives as output, and send each of them through the device and again collect all the numbers sent out.
- Repeats the above step $N$ times.

To test your wit, he challenges you to find the number of distinct 3-digit numbers which the device outputs over the $N$ steps. Can you?

### Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $K, N$.

### Output:
For each testcase, output a single integer denoting the number of distinct 3-digit numbers which the device outputs over the $N$ steps.

### Constraints
- $1 \leq T \leq 1000$
- $5 \leq N \leq 10^9$
- Each digit of $K$ is non-zero

---

## Examples

**Example 1**

**Input**

```text
1
123 5
```

**Output**

```text
27
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK:** [https://www.codechef.com/ICL2019/problems/ICL1901](https://www.codechef.com/ICL2019/problems/ICL1901)

**DIFFICULTY:** EASY

**PROBLEM**

Given a 3-digit number K whose all digits are non-zero and a number N.The number K is fed to a machine which performs the following operation: Take in a 3-digit number, multiply it by 7,11 and 13 consecutively and use the digits of the product to form all possible 3-digit numbers. All these 3-digit numbers are again fed to the machine and this process is done for N iterations. Over all these steps, how many different 3-digit numbers are output by the machine?

**EXPLANATION**

Note that 13*11*7=1001=1000+1. Now consider any three digit number ABC. Any such number multiplied by 1001 will give ABCABC as output. Now, any of the numbers that can be output by the machine consists of the digits of ABCABC which are the same as the digits of the original number,i.e., A,B and C.

The number may go through the machine any number of times, but each time the numbers output by the machine contain only the digits A,B and C. Also, by observation, we may see that after 5(N>=5) iterations, all possible 3-digit numbers that can be generated would have been generated. So, the required answer is the number of 3-digit numbers that can be formed by using the digits A, B and C only.

Suppose all three digits of K are different. Then, all 3 places can have any 3-digits and  answer=3*3*3=27. If any two digits of K are the same, then the answer is 2*2*2=8.If all the three digits are the same, then the answer is 1*1*1=1.

</details>
