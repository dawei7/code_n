# Reversing directions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIRECTI |
| Difficulty Rating | 1426 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [DIRECTI](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/DIRECTI) |

---

## Problem Statement

Chef recently printed directions from his home to a hot new restaurant across the town, but forgot to print the directions to get back home. Help Chef to transform the directions to get home from the restaurant.

A set of directions consists of several instructions. The first instruction is of the form "Begin on XXX", indicating the street that the route begins on. Each subsequent instruction is of the form "Left on XXX" or "Right on XXX", indicating a turn onto the specified road.

When reversing directions, all left turns become right turns and vice versa, and the order of roads and turns is reversed. See the sample input for examples.

### Input

Input will begin with an integer **T**, the number of test cases that follow. Each test case begins with an integer **N**, the number of instructions in the route. **N** lines follow, each with exactly one instruction in the format described above.

### Output

For each test case, print the directions of the reversed route, one instruction per line. Print a blank line after each test case.

### Constraints

- 1 ≤ **T** ≤ 15

- 2 ≤ **N** ≤ 40

- Each line in the input will contain at most 50 characters, will contain only alphanumeric characters and spaces and will not contain consecutive spaces nor trailing spaces. By alphanumeric characters we mean digits and letters of the English alphabet (lowercase and uppercase).

---

## Examples

**Example 1**

**Input**

```text
2
4
Begin on Road A
Right on Road B
Right on Road C
Left on Road D
6
Begin on Old Madras Road
Left on Domlur Flyover
Left on 100 Feet Road
Right on Sarjapur Road
Right on Hosur Road
Right on Ganapathi Temple Road
```

**Output**

```text
Begin on Road D
Right on Road C
Left on Road B
Left on Road A

Begin on Ganapathi Temple Road
Left on Hosur Road
Left on Sarjapur Road
Left on 100 Feet Road
Right on Domlur Flyover
Right on Old Madras Road
```

**Explanation**

In the first test case, the destination lies on Road D, hence the reversed route begins on Road D. The final turn in the original route is turning left from Road C onto Road D. The reverse of this, turning right from Road D onto Road C, is the first turn in the reversed route.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Link

[Practice](http://www.codechef.com/problems/DIRECTI)

[Contest](http://www.codechef.com/COOK29/problems/DIRECTI)

# Difficulty

CAKEWALK

# Pre-requisites

Ad-hoc programming

# Problem

Chef has printed directions from home to his new restaurant. You need to take these “printed directions” as input, and output printed directions from the restaurant back to his home.

# Explanation

This was just a problem of parsing a little input and giving a good formatted output. Indeed, the problem statement itself described what to do: “When reversing directions, all left turns become right turns and vice versa, and the order of roads and turns is reversed.”

To illustrate the solution, let us consider the first Sample Input:

Begin on Road A

Right on Road B

Right on Road C

Left on Road D

Consider the input in the following 2 sequence manner. Sequence 1 is the set of directions: “Begin”, “Right”, “Right”, “Left”. Lets abbreviate this as BRRL. Sequence 2 is the set of Roads traversed: “Road A”, “Road B”, “Road C”, “Road D”.

Your output should just take sequence 1, put a “Begin” at the beginning, and flip L/R’s in reverse order, and concatenate it with the reverse of sequence 2. That means, reversing sequence 1 gives you: “LRRB”, which when you bring begin to the beginning, and flip L/Rs, gives you “BRLL”. Reversing Sequence 2 gives you: “Road D”, “Road C”, “Road B”, “Road A”.

Finally concatenating the 2 sequences gives you:

Begin on Road D

Right on Road C

Left on Road B

Left on Road A

which is the required output.

# Implementation

The best way to implement this would be to (a) store the sequence of L/R values as seen in order, along with (b) an array of Strings determining the roads used (incl. of spaces). A nice trick to use here is to include the word “on” in the road name, so in the example, you would store “on Road A”, “on Road B”, “on Road C”, “on Road D”.

Then traverse the arrays in reverse direction and flip left/right values of the first array and concatenate it with that of the second array.

# Author’s Solution

Can be found [here](http://www.codechef.com/download/Solutions/COOK29/Setter/DIRECTI.cpp)

# Tester’s Solution

Can be found [here](http://www.codechef.com/download/Solutions/COOK29/Tester/DIRECTI.cpp)

</details>
