# Maximum Energy Boost From Two Drinks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3259 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/) |

## Problem Description

### Goal

Two equal-length arrays give the energy available from drinks A and B during each of the next $n$ hours. In an hour when you keep consuming the same drink, you gain that drink's listed energy. You may begin with either drink.

Switching from one drink to the other requires one complete cleansing hour. During that intervening hour you consume neither drink and gain no energy; the new drink can be consumed in the following hour. Choose when to stay or switch so that the total energy gained over all $n$ hours is as large as possible.

### Function Contract

**Inputs**

- \`energyDrinkA\`: Drink A's positive energy values for $n$ hours.
- \`energyDrinkB\`: Drink B's positive energy values for the same $n$ hours.

The common length satisfies $3 \le n \le 10^5$, and every energy value is between 1 and $10^5$.

**Return value**

- The maximum total energy obtainable while respecting the one-hour cleansing requirement for each switch.

### Examples

#### Example 1

- **Input:** \`energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]\`
- **Output:** \`5\`

Staying with either one drink for all three hours yields 5.

#### Example 2

- **Input:** \`energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]\`
- **Output:** \`7\`

Drink A in hour 0, cleanse during hour 1, and drink B in hour 2.

#### Example 3

- **Input:** \`energyDrinkA = [5,5,5], energyDrinkB = [1,1,1]\`
- **Output:** \`15\`

Drink A throughout; switching cannot improve the result.
