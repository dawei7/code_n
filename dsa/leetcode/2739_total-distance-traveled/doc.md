# Total Distance Traveled

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2739 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/total-distance-traveled/) |

## Problem Description

### Goal

A truck begins with `mainTank` liters in its main fuel tank and `additionalTank` liters in a reserve tank. It travels $10$ kilometers for every liter consumed from the main tank; reserve fuel cannot power the truck directly.

Immediately after each cumulative block of $5$ liters has been consumed from the main tank, transfer $1$ liter from the reserve into the main tank when reserve fuel remains. Transfers happen only at these discrete consumption events, including events made possible by earlier transfers. Determine the maximum total distance the truck can travel before its main tank becomes empty.

### Function Contract

**Inputs**

- `mainTank`: The initial liters in the main tank, where $1 \le \texttt{mainTank} \le 100$.
- `additionalTank`: The initial reserve liters, where $1 \le \texttt{additionalTank} \le 100$.

**Return value**

Return the maximum distance in kilometers after consuming every usable liter from the main tank and all reserve liters that can be transferred under the five-liter rule.

### Examples

#### Example 1

- **Input:** `mainTank = 5, additionalTank = 10`
- **Output:** `60`
- **Explanation:** Consuming the first five liters triggers one transfer, so six liters are ultimately burned.

#### Example 2

- **Input:** `mainTank = 1, additionalTank = 2`
- **Output:** `10`
- **Explanation:** The main tank empties before a transfer event can occur.

#### Example 3

- **Input:** `mainTank = 9, additionalTank = 2`
- **Output:** `110`
- **Explanation:** The first transfer allows another five-liter consumption milestone, so both reserve liters become usable.
