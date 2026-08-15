### 1. Description

You are given a binary array `nums` of length `n`, a **positive** integer `k` and a **non-negative** integer `maxChanges`.

Alice plays a game, where the goal is for Alice to pick up `k` ones from `nums` using the **minimum** number of **moves**. When the game starts, Alice picks up any index `aliceIndex` in the range `[0, n - 1]` and stands there. If $\text{nums}[aliceIndex] = 1$ , Alice picks up the one and $\text{nums}[aliceIndex]$ becomes `0`(this **does not** count as a move). After this, Alice can make **any** number of **moves** (**including** **zero**) where in each move Alice must perform **exactly** one of the following actions:

- Select any index $j \neq aliceIndex$ such that $\text{nums}[j] = 0$ and set $\text{nums}[j] = 1$. This action can be performed **at** **most** `maxChanges` times.

- Select any two adjacent indices `x` and `y` ($|x - y| = 1$) such that $\text{nums}[x] = 1$, $\text{nums}[y] = 0$, then swap their values (set $\text{nums}[y] = 1$ and $\text{nums}[x] = 0$). If $y = aliceIndex$, Alice picks up the one after this move and $\text{nums}[y]$ becomes `0`.

Return *the **minimum** number of moves required by Alice to pick **exactly ***`k` *ones*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).
- `maxChanges`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1

- **Output:** 3

- **Explanation:** Alice can pick up `3` ones in `3` moves, if Alice performs the following actions in each move when standing at $aliceIndex = 1$:

- At the start of the game Alice picks up the one and $\text{nums}[1]$ becomes `0`. `nums` becomes `[1,**<u>0</u>**,0,0,0,1,1,0,0,1]`.

- Select $j = 2$ and perform an action of the first type. `nums` becomes `[1,**<u>0</u>**,1,0,0,1,1,0,0,1]`

- Select $x = 2$ and $y = 1$, and perform an action of the second type. `nums` becomes `[1,**<u>1</u>**,0,0,0,1,1,0,0,1]`. As $y = aliceIndex$, Alice picks up the one and `nums` becomes `[1,**<u>0</u>**,0,0,0,1,1,0,0,1]`.

- Select $x = 0$ and $y = 1$, and perform an action of the second type. `nums` becomes `[0,**<u>1</u>**,0,0,0,1,1,0,0,1]`. As $y = aliceIndex$, Alice picks up the one and `nums` becomes `[0,**<u>0</u>**,0,0,0,1,1,0,0,1]`.

Note that it may be possible for Alice to pick up `3` ones using some other sequence of `3` moves.

#### Example 2

- **Input:** nums = [0,0,0,0], k = 2, maxChanges = 3

- **Output:** 4

- **Explanation:** Alice can pick up `2` ones in `4` moves, if Alice performs the following actions in each move when standing at $aliceIndex = 0$:

- Select $j = 1$ and perform an action of the first type. `nums` becomes `[**<u>0</u>**,1,0,0]`.

- Select $x = 1$ and $y = 0$, and perform an action of the second type. `nums` becomes `[**<u>1</u>**,0,0,0]`. As $y = aliceIndex$, Alice picks up the one and `nums` becomes `[**<u>0</u>**,0,0,0]`.

- Select $j = 1$ again and perform an action of the first type. `nums` becomes `[**<u>0</u>**,1,0,0]`.

- Select $x = 1$ and $y = 0$ again, and perform an action of the second type. `nums` becomes `[**<u>1</u>**,0,0,0]`. As $y = aliceIndex$, Alice picks up the one and `nums` becomes `[**<u>0</u>**,0,0,0]`.

### 4. Constraints

- $2 \le n \le 10^{5}$

- $0 \le \text{nums}[i] \le 1$

- $1 \le k \le 10^{5}$

- $0 \le maxChanges \le 10^{5}$

- $maxChanges + sum(nums) \ge k$
