# Superstar Dishes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAJORELE2 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MAJORELE2](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MAJORELE2) |

---

## Problem Statement

Chef recently organised a **Grand Feast** where he served $n$ **different dishes** to his friends.\
Each friend picked their favourite dish, and now Chef has a list of all the dishes chosen.

Chef is curious:

- Which dishes were so popular that they were chosen by more than $⌊n/3⌋$ friends? Print the dishes in increasing order of popularity of dish among the friends.

Can you help Chef find these **superstar dishes**?

## Function Declaration

### Function Name

$findSuperstarDishes$ – This function finds all dishes that appear more than ⌊n/3⌋ times.

### Parameters

* $a$ : An array representing the dishes chosen by friends.
* $n$ : The number of dishes.

### Return Value

* This function **returns the array in ascending order**.

## Constraints

* $1 \leq n \leq 5 \times 10^4$
* $−10^9 \leq a[i] \leq 10^9$
* The output may contain **at most two dishes** (by pigeonhole principle)

---

## Input Format

* The first line of each test case contains a single integer $n$ — the number of dishes.
* The next line contains $n$ space-separated integers $a[i]$ — the dishes chosen by friends.

---

## Output Format

* For each test case, print on a new line all dishes that were chosen by **more than ⌊n/3⌋ friends**, in **increasing order**.
* If no such dish exists, print nothing for that test case.

---

## Constraints

- $1 \le N \le 5 \times 10^4 $
- $-10^9 \le \text{Dish}[i] \le 10^9 $

---

## Examples

**Example 1**

**Input**

```text
6
2 2 1 1 1 2
```

**Output**

```text
1 2
```

**Explanation**

Here, **n = 6**, so `[n/3]` = 2.
- Dish `1` appears **3 times** -> more than 2
- Dish `2` appears **3 times** -> more than 2\
So, both `1` and `2` are superstar dishes.

**Example 2**

**Input**

```text
7
5 5 5 1 2 3 4
```

**Output**

```text
5
```

**Explanation**

Here, **n = 7**, so `[n/3]` = 2.
- Dish `5` appears **3 times** -> more than 2.
- Other dishes (`1,2,3,4`) appear only once -> not more than 2.
So, the answer is `5`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef served `N` dishes in a Grand Feast, and each friend picked their favorite dish.
We are given the list of chosen dishes `(Dish[i])`.

A dish is called a **superstar dish** if it was chosen by **more than ⌊N/3⌋ friend**s.

We need to print all superstar dishes in **increasing order** (if multiple).
If no dish qualifies, print nothing.

---

## Key Observations

A dish is superstar only if it occurs **strictly more than ⌊N/3⌋ times**.
- Example: `N = 6 → ⌊6/3⌋ = 2`, so count must be `> 2`.

At most **2 superstar dishes** can exist.

- Why?
- If 3 different dishes each appeared more than `N/3` times, then the total count would exceed `N`.

There are multiple ways to solve:
- **Sorting + Counting** (O(n log n))
- **Boyer–Moore Majority Voting (extended)** (O(n))

---

## Approach

### The Extended Boyer-Moore Majority Vote Algorithm

This algorithm is designed to find all elements that appear strictly more than $\lfloor N/3 \rfloor$ times in an array. Because it is mathematically impossible to have more than two elements hit this threshold, we only ever need to track two potential candidates.

---

### Phase 1: The Three-Way Elimination (Selection)

The goal of this phase is to aggressively eliminate groups of three **completely different** numbers. Think of it as a three-way standoff. If a number appears more than $\lfloor N/3 \rfloor$ times, it is mathematically impossible for it to be completely wiped out in these three-way eliminations. It will always have survivors at the end.

* Create two empty slots (`Candidate A` and `Candidate B`) and give them each a counter starting at zero.
*  As you iterate through the array, if the current number already matches Candidate A or Candidate B, simply increase that candidate's counter.
*  If the current number is new, but one of the candidate counters is currently at zero (meaning the slot is "empty"), assign the current number to that slot and set its counter to 1.
*  If the current number does not match Candidate A, does not match Candidate B, AND both candidates have active counts greater than zero, you have found three completely distinct numbers. Discard the current number, and decrease the counters for both Candidate A and Candidate B by 1.

 **Important Note:** Phase 1 does not guarantee that the surviving candidates are actually the majority elements. It only guarantees that **if** a majority element exists in the array, it will be one of these survivors.

---

### Phase 2: The Final Audit (Validation)

Because Phase 1 might leave us with "imposter" candidates (which frequently happens if the array doesn't actually contain any numbers that cross the $\lfloor N/3 \rfloor$ threshold), we must verify our survivors.

* **Reset:** Set the actual counters for Candidate A and Candidate B back to zero.
* **Recount:** Iterate through the original array one more time from the beginning. Count exactly how many times Candidate A and Candidate B actually appear.
* **Verify:** Finally, check if Candidate A's actual total count is strictly greater than $\lfloor N/3 \rfloor$. If yes, it is a valid superstar dish. Do the exact same verification for Candidate B.

---

## Complexity Analysis

- **Time Complexity**: O(n) → because the array is scanned twice (candidate selection + validation).
- **Space Complexity**: O(1) → because only a constant number of variables are used regardless of input size.

</details>
