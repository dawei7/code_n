### 1. Description

You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where $\text{spells}[i]$ represents the strength of the $i^{\text{th}}$ spell and $\text{potions}[j]$ represents the strength of the $j^{\text{th}}$ potion.

You are also given an integer `success`. A spell and potion pair is considered **successful** if the **product** of their strengths is **at least** `success`.

Return *an integer array *`pairs`* of length *`n`* where *$\text{pairs}[i]$* is the number of **potions** that will form a successful pair with the *$i^{\text{th}}$* spell.*

### 2. Function Contract

**Inputs**

- `spells`: Input parameter (`List[int]`).
- `potions`: Input parameter (`List[int]`).
- `success`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** $spells = [5,1,3], potions = [1,2,3,4,5], success = 7$
- **Output:** `[4,0,3]`
- **Explanation:** 
- 0^th spell: 5 * [1,2,3,4,5] = [5,<u>**10**</u>,<u>**15**</u>,<u>**20**</u>,<u>**25**</u>]. 4 pairs are successful.
- 1^st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2^nd spell: 3 * [1,2,3,4,5] = [3,6,<u>**9**</u>,<u>**12**</u>,<u>**15**</u>]. 3 pairs are successful.
Thus, [4,0,3] is returned.

#### Example 2

- **Input:** $spells = [3,1,2], potions = [8,5,8], success = 16$
- **Output:** `[2,0,2]`
- **Explanation:** 
- 0^th spell: 3 * [8,5,8] = [<u>**24**</u>,15,<u>**24**</u>]. 2 pairs are successful.
- 1^st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
- 2^nd spell: 2 * [8,5,8] = [**<u>16</u>**,10,<u>**16**</u>]. 2 pairs are successful.
Thus, [2,0,2] is returned.

### 4. Constraints

- $n = \text{spells.length}$

- $m = \text{potions.length}$

- $1 \le n, m \le 10^{5}$

- $1 \le \text{spells}[i], \text{potions}[i] \le 10^{5}$

- $1 \le success \le 10^{10}$
