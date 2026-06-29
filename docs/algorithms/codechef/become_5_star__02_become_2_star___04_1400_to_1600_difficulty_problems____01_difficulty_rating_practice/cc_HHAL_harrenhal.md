# Harrenhal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HHAL |
| Difficulty Rating | 1495 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [HHAL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/HHAL) |

---

## Problem Statement

*Harrenhal is the largest castle in the Seven Kingdoms and is the seat of House Whent in the Riverlands, on the north shore of the Gods Eye lake. Since the War of Conquest, however, it has become a dark and ruinous place.*

(c) A Wiki of Ice and Fire

Now Harrenhal is too dangerous since it's a nice place for bandits to hide, or even for rebels to start planning overthrowing of the king. So, the current Lord of the Seven Kingdoms has decided, that it's time to completely ruin the castle. For that puposes, he's planning to send some military troops.

In this problem we assume, that Harrenhal can be described as a string **H**, which consists only of symbols *'a'* and *'b'*. Harrenhal is completely ruined if and only if the length of **H** is equal to zero.

So, how to make **H** empty? Send a military troop! When a military troop of the king reach the castle, they delete some palindromic subsequence **S** of **H**. For example, let **H** = *'abbabaab'*. Then the current military troop can choose **S** = *'ababa'*(Let's make symbols of **S** bold in **H**: *'**ab**b**ab**a**a**b'*). After deleting **S**, **H** will be equal to *'bab'*. Military troops are free to choose any possible palindromic subsequence of **H**.

Your task is pretty simple: determine the minimal number of military troops, that the Lord of the Seven Kingdoms has to send in order to ruin Harrenhal.

### Note

Maybe, some of you aren't familiar with definitions from the statement. Here're some articles that could help you to understand the problem correctly:

- Subsequence: [http://en.wikipedia.org/wiki/Subsequence](http://en.wikipedia.org/wiki/Subsequence)

- Palindrome: [http://en.wikipedia.org/wiki/Palindrome](http://en.wikipedia.org/wiki/Palindrome)

### Input

The first line of the input contains an integer **T**, denoting the number of test cases.

The next **T** lines contain a string **H** each, denoting the string, that describes the current state of Harrenhal for the corresponding test cases.

It's guaranteed, that each **H** consists only of symbols *'a'* and *'b'*.

### Output

The output should contain exactly **T** lines. **i**'th line of the output should contain the only integer: the minimal number of military troops, that the Lord of the Seven Kingdoms has to send in order to ruin Harrenhal for the corresponding test cases.

### Constraints

- 1 ≤ **|H|** ≤ 100000, for each **H**.

- Subtask 1(30 points): each **H** in the input is a palindrome, 1 ≤ **T** ≤ 6;

- Subtask 2(70 points): 1 ≤ **T** ≤ 9.

---

## Examples

**Example 1**

**Input**

```text
1
abbabaab
```

**Output**

```text
2
```

**Explanation**

There're multiple ways to ruin Harrenhal in the example test. Let's consider one of them.

The first troop can delete **S** = *'ababa'*(*'**ab**b**ab**a**a**b'*). After that, **H** = *'bab'*.

The second troop can delete **S** = *'bab'*(*'**bab**'*). After that, **H** is empty and that's it.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Problem link** : [contest](http://www.codechef.com/LTIME15/problems/HHAL) [practice](http://www.codechef.com/problems/HHAL)

**Difficulty** : CakeWalk

**Pre-requisites** : None

**Problem** :

You have a string H consisting only of ‘a’ and ‘b’. In one move you can remove one palindromic subsequence of string H. Find minimum number of moves to make H empty.

#### Explanation

### How to get 30 points

Since string is already a palindrome, we can choose whole string in one move(whole string is still a subsequence of the string) and make it zero. So answer is 1.

### How to get 100 points

If string is palindrome, we know answer is 1.

If string is not palindrome, then you can notice that string will consist characters ‘a’ and ‘b’ both. We will choose a subsequence such that all ‘a’ are present in it. This subsequence is a palindrome. What will be left after removal of all ‘a’ will be all ‘b’. In next move, we choose whole string. So we can do it in 2 moves.

**Solutions** : [setter](http://www.codechef.com/download/Solutions/LTIME15/Setter/HHAL.cpp) [tester](http://www.codechef.com/download/Solutions/LTIME15/Tester/HHAL.cpp)

</details>
