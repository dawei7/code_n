# Snake Procession

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SNAKPROC |
| Difficulty Rating | 1014 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Strings |
| Official Link | [SNAKPROC](https://www.codechef.com/practice/course/1to2stars/LP1TO203/problems/SNAKPROC) |

---

## Problem Statement

The annual snake festival is upon us, and all the snakes of the kingdom have gathered to participate in the procession. Chef has been tasked with reporting on the procession, and for this he decides to first keep track of all the snakes. When he sees a snake first, it'll be its Head, and hence he will mark a 'H'. The snakes are long, and when he sees the snake finally slither away, he'll mark a 'T' to denote its tail. In the time in between, when the snake is moving past him, or the time between one snake and the next snake, he marks with '.'s.

Because the snakes come in a procession, and one by one, a valid report would be something like "..H..T...HTH....T.", or "...", or "HT", whereas "T...H..H.T", "H..T..H", "H..H..T..T" would be invalid reports (See explanations at the bottom).

Formally, a snake is represented by a 'H' followed by some (possibly zero) '.'s, and then a 'T'. A valid report is one such that it begins with a (possibly zero length) string of '.'s, and then some (possibly zero) snakes between which there can be some '.'s, and then finally ends with some (possibly zero) '.'s.

Chef had binged on the festival food and had been very drowsy. So his report might be invalid. You need to help him find out if his report is valid or not.

### Input

- The first line contains a single integer, $R$, which denotes the number of reports to be checked. The description of each report follows after this.
- The first line of each report contains a single integer, $L$, the length of that report.
- The second line of each report contains a string of length $L$. The string contains only the characters '.', 'H', and 'T'.

### Output

- For each report, output the string **Valid** or **Invalid** in a new line, depending on whether it was a valid report or not.

### Constraints

- $1 \le R \le 500$
- $1 \le L \le 500$

---

## Examples

**Example 1**

**Input**

```text
6
18
..H..T...HTH....T.
3
...
10
H..H..T..T
2
HT
11
.T...H..H.T
7
H..T..H
```

**Output**

```text
Valid
Valid
Invalid
Valid
Invalid
Invalid
```

**Explanation**

- "H..H..T..T" is invalid because the second snake starts before the first snake ends, which is not allowed.

- ".T...H..H.T" is invalid because it has a 'T' before a 'H'. A tail can come only after its head.

- "H..T..H" is invalid because the last 'H' does not have a corresponding 'T'.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
18
..H..T...HTH....T.
```

**Output for this case**

```text
Valid
```



#### Test case 2

**Input for this case**

```text
3
...
```

**Output for this case**

```text
Valid
```



#### Test case 3

**Input for this case**

```text
10
H..H..T..T
```

**Output for this case**

```text
Invalid
```



#### Test case 4

**Input for this case**

```text
2
HT
```

**Output for this case**

```text
Valid
```



#### Test case 5

**Input for this case**

```text
11
.T...H..H.T
```

**Output for this case**

```text
Invalid
```



#### Test case 6

**Input for this case**

```text
7
H..T..H
```

**Output for this case**

```text
Invalid
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINKS:

[Contest](https://www.codechef.com/SNCKQL17/problems/SNAKPROC)

[Practice](https://www.codechef.com/problems/SNAKPROC)

**Author**: Praveen Dhinwa

**Primary Tester**: Hasan Jaddouh

**Editorialist**: Aulene De

## DIFFICULTY:

Cakewalk

## PREREQUISITES:

None

## PROBLEM:

A string is given in the form of ‘H’, ’T’ and ‘.’ characters, where H denotes the head, T denotes the tail and ‘.’ denotes the time between a snake passing or a the time between one snake and another. Given a string, check if it is a valid sequence of ordering of snakes.

**EXPLANATION:**

Let’s see… the ‘.’ characters don’t look useful. Do they? Nah. They’re just signifying empty spaces… which doesn’t help us at all. Ignore them.

Now, we have a string made up entirely of ‘H’ and ’T’ characters. This string denotes the ordering of the snakes. Alright, so when is a string invalid?

So, like most animals, a snake can’t have two heads or tails. Thus, we can’t have two ‘H’ or ’T’ characters together. What else?

Let’s see, we can’t have a tail appearing before a head, that’s preposterous! Similarly, we can’t have a head without a tail. Could these two cases appear anywhere in our string?

Sadly, they can. The first case will appear only at the beginning of the string. The second will appear towards the end.

Thus, we can simply check if any of the above conditions is true, thus making our answer ‘Invalid’. Otherwise, our answer is ‘Valid’. We have a cute solution.

Simply put, the only way a string is valid is when it is of the form “HTHTHTHT”. Starts with an ‘H’, ends with a ’T’ and no character should repeat right after itself.

PS: Finding edge cases is always important. Take whatever is in a problem statement at face-value and don’t assume that a case isn’t possible. To put it in Sherlock’s words - “If you eliminate the improbable, whatever remains must be the truth”. Always be on the lookout for cases where your code could fail.

## SOLUTIONS:

Editorialist’s solution - [https://pastebin.com/LEfk2hsy](https://pastebin.com/LEfk2hsy)

</details>
