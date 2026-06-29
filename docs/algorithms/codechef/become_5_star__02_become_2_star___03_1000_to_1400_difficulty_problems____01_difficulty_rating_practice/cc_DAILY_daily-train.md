# Daily Train

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DAILY |
| Difficulty Rating | 1222 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DAILY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DAILY) |

---

## Problem Statement

A daily train consists of **N** cars. Let's consider one particular car. It has 54 places numbered consecutively from 1 to 54, some of which are already booked and some are still free. The places are numbered in the following fashion:

The car is separated into 9 compartments of 6 places each, as shown in the picture. So, the 1st compartment consists of places 1, 2, 3, 4, 53 and 54, the 2nd compartment consists of places 5, 6, 7, 8, 51 and 52, and so on.

A group of **X** friends wants to buy tickets for free places, all of which are in one compartment (it's much funnier to travel together). You are given the information about free and booked places in each of the **N** cars. Find the number of ways to sell the friends exactly **X** tickets in one compartment (note that the order in which the tickets are sold doesn't matter).

### Input

The first line of the input contains two integers **X** and **N** (1 ≤ **X** ≤ 6, 1 ≤ **N** ≤ 10) separated by a single space. Each of the following **N** lines contains the information about one car which is a string of length 54 consisting of '0' and '1'. The **i**-th character (numbered from 1) is '0' if place **i** in the corresponding car is free, and is '1' if place **i** is already booked.

### Output

Output just one integer -- the requested number of ways.

---

## Examples

**Example 1**

**Input**

```text
1 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010
```

**Output**

```text
85
```

**Explanation**

In the first test case, any of the free places can be sold.

**Example 2**

**Input**

```text
6 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010
```

**Output**

```text
1
```

**Explanation**

In the second test case, the only free compartment in the train is compartment 3 in the first car (places 9, 10, 11, 12, 49 and 50 are all free).

**Example 3**

**Input**

```text
3 2
000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000
```

**Output**

```text
360
```

**Explanation**

In the third test case, the train is still absolutely free; as there are 20 ways to sell 3 tickets in an empty compartment, the answer is 2 * 9 * 20 = 360.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/DAILY/)

[Contest](http://www.codechef.com/COOK19/problems/DAILY/)

### EXPLANATION

It’s obvious that we can solve the problem for each compartment separately. Let’s find the number of free places in a particular compartment, say **Y**. If **Y** > **X** then our group of friends can’t be placed in this compartment. In the other case the number of ways to choose any **X** places out of given **Y** should be added to the answer – in other words, the number of **X**-[combinations](http://en.wikipedia.org/wiki/Combination) of **Y** elements should be added. This number (let’s call it **C(Y,X)**) can be calculated in many ways:

- using the formula **C(Y,X**) = **Y**! / ( **X**! * (**Y-X)**! ),

- using the relation **C(Y,X)** = **C(Y-1,X)** + **C(Y-1,X-1**),

- or even calculating all the required values by hand (both **X** and **Y** are very small).

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK19/Setter/DAILY.cpp)

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/COOK19/Tester/DAILY.cpp)

</details>
