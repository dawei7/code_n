# Malvika is peculiar about color of balloons

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHN09 |
| Difficulty Rating | 988 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [CHN09](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/CHN09) |

---

## Problem Statement

Little Malvika is very peculiar about colors. On her birthday, her mom wanted to buy balloons for decorating the house. So she asked her about her color preferences. The sophisticated little person that Malvika is, she likes only two colors — amber and brass. Her mom bought **n** balloons, each of which was either amber or brass in color. You are provided this information in a string **s** consisting of characters 'a' and 'b' only, where 'a' denotes that the balloon is amber, where 'b' denotes it being brass colored.

When Malvika saw the balloons, she was furious with anger as she wanted all the balloons of the same color. In her anger, she painted some of the balloons with the opposite color (i.e., she painted some amber ones brass and vice versa) to make all balloons appear to be the same color. As she was very angry, it took her a lot of time to do this, but you can probably show her the right way of doing so, thereby teaching her a lesson to remain calm in difficult situations, by finding out the minimum number of balloons needed to be painted in order to make all of them the same color.

---

## Input Format

- The first line of input contains a single integer **T**, denoting the number of test cases.

- The first and only line of each test case contains a string **s**.

---

## Output Format

- For each test case, output a single line containing an integer — the minimum number of flips required.

---

## Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **n** ≤ **100**, where **n** denotes to the length of the string **s**.

---

## Examples

**Example 1**

**Input**

```text
3
ab
bb
baaba
```

**Output**

```text
1
0
2
```

**Explanation**

**In the first example**,
you can change amber to brass or brass to amber. In both the cases, both the balloons will have same colors. So, you will need to paint 1 balloon. So the answer is 1.

**In the second example**,
As the color of all the balloons is already the same, you don't need to paint any of them. So, the answer is 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
ab
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
bb
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
baaba
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/ACM15CHN/problems/CHN09)

**Author:** [???](http://www.codechef.com/users/???)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo), [Jingbo Shang](http://www.codechef.com/users/shangjingbo)

**Editorialist:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

### PREREQUISITES:

Strings, loops

### PROBLEM:

Given a string consisting of `a`s and `b`s, what is the minimum number of letters to be changed so that all letters are the same?

### EXPLANATION:

Count the `a`s and `b`s, and print the smaller count. (There’s really nothing more to it.) To make all letters the same, they will either be all `a`s or all `b`s, so either all `b`s or all `a`s need to be changed. Since we want the minimum, the answer is the smaller one.

There are only very few non-AC verdicts for this problem, and the only mistakes are (1) compile errors and (2) failing to initialize the array (to contain the string) properly.

Compile errors are some of the most unproductive verdicts in a contest, because they can easily be discovered and fixed (by simply compiling the code!). Though there are no penalty points for compile errors, remember that this is a short contest, so saving a few units of time and effort helps.

Failing to initialize the array properly can happen in one of the following ways:

- By failing to initialize the array at all.

- By failing to allocate an array large enough to contain the input. Remember to look at the constraints to know how much you need to allocate. Remember that in C++, you need an array of length n+1 to store a string of length n, because strings should be terminated by a null character (’`\0`’).

This is mostly a C/C++ problem though. The simplest ways to take a string input in Java don’t involve allocating an array yourself, so this problem doesn’t happen.

This is the easiest problem in the contest, so you should try to spend little time to get this one AC’ed, to give you more time to solve the others.

### Time Complexity:

O(n)

### AUTHOR’S AND TESTER’S SOLUTIONS:

[setter][333]

[tester][444]

[editorialist][555]

[333]: The link is provided by admins after the contest ends and the solutions are uploaded on the CodeChef Server.

[444]: The link is provided by admins after the contest ends and the solutions are uploaded on the CodeChef Server.

[555]: The link is provided by admins after the contest ends and the solutions are uploaded on the CodeChef Server.

</details>
