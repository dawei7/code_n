# Two City Scheduling

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1029 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/two-city-scheduling/) |

## Problem Description

### Goal

A company plans to interview `2n` people. For person `i`, `costs[i] = [aCost_i, bCost_i]` gives the price of flying that person to city A and city B, respectively.

Fly every person to exactly one city so that exactly `n` people arrive in city A and exactly `n` arrive in city B. Return the minimum possible total flight cost under this balance requirement.

### Function Contract

**Inputs**

- `costs`: an array containing $N=2n$ pairs `[aCost, bCost]`.
- $2 \le N \le 100$, $N$ is even, and every flight cost is between $1$ and $1000$, inclusive.

**Return value**

- The minimum total cost of assigning exactly $N/2$ people to each city.

### Examples

**Example 1**

- Input: `costs = [[10,20],[30,200],[400,50],[30,20]]`
- Output: `110`
- Explanation: Send the first two people to A for `10 + 30` and the other two to B for `50 + 20`.

**Example 2**

- Input: `costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]`
- Output: `1859`

**Example 3**

- Input: `costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]`
- Output: `3086`

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Measure the relative cost of city A:** For each person, `aCost - bCost` is the change in total cost if that person is sent to A instead of B. A smaller difference means choosing A is more favorable relative to choosing B.

**Choose exactly half by that difference:** Sort the people in ascending order of `aCost - bCost`. Send the first $N/2$ people to A and the remaining people to B. Summing the corresponding entries produces a balanced schedule by construction.

**Why this greedy split is optimal:** Suppose a proposed balanced assignment sends person `i` to B and person `j` to A even though `i` has a smaller difference. Swapping their cities changes the cost by
$$
(\texttt{aCost}_i-\texttt{bCost}_i)-(\texttt{aCost}_j-\texttt{bCost}_j) \le 0.
$$
The swap preserves the city counts and never increases the total. Repeating it removes every inversion, yielding exactly the sorted split, so no balanced assignment can be cheaper.

#### Complexity detail

Sorting $N$ cost pairs takes $O(N\log N)$ time. A sorted copy stores $N$ references and uses $O(N)$ auxiliary space; the two summations take $O(N)$ additional time.

#### Alternatives and edge cases

- **Start with everyone in city B:** Add every B cost, then apply the $N/2$ smallest values of `aCost - bCost`. This is the same greedy argument written as savings.
- **Dynamic programming by people and A slots:** Track the minimum cost after each prefix and number sent to A. It takes $O(N^2)$ time and $O(N)$ space, which is unnecessary for two cities.
- **Quadratic selection:** Repeatedly search for the next smallest difference. It remains correct but takes $O(N^2)$ time.
- **Equal differences:** Tied people are interchangeable because swapping them changes the total by zero.
- **Everyone prefers one city:** Exactly half must still go to each city; absolute preference does not override the balance constraint.
- **Minimum input:** With two people, compare the only two balanced assignments.

</details>
