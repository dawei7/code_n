# Eliminate Maximum Number of Monsters

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/eliminate-maximum-number-of-monsters/) |
| Frontend ID | 1921 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are defending a city from $N$ monsters. Monster `i` begins `dist[i]` kilometers away and approaches at the constant rate `speed[i]` kilometers per minute.

Your weapon destroys one monster whenever it is fully charged. It is ready at minute zero, and each shot requires one minute before the next shot. If any surviving monster reaches the city, you immediately lose. Arrival at the exact instant the weapon becomes ready still counts as a loss, so that shot cannot be fired.

Choose the firing order that eliminates as many monsters as possible. Return that maximum count, or $N$ when every monster can be destroyed in time.

### Function Contract

**Inputs**

- `dist`: an array of $N$ positive initial distances.
- `speed`: an array of $N$ positive constant speeds corresponding by index to `dist`.
- $1 \le N \le 10^5$ and $1 \le \texttt{dist[i]}, \texttt{speed[i]} \le 10^5$.

**Return value**

- Return the greatest number of monsters that can be eliminated before any surviving monster reaches the city.

### Examples

**Example 1**

- Input: `dist = [1, 3, 4], speed = [1, 1, 1]`
- Output: `3`

Their arrival times are one, three, and four minutes, allowing shots at minutes zero, one, and two.

**Example 2**

- Input: `dist = [1, 1, 2, 3], speed = [1, 1, 1, 1]`
- Output: `1`

After the first shot, another monster reaches the city exactly at minute one.

**Example 3**

- Input: `dist = [3, 2, 4], speed = [5, 3, 2]`
- Output: `1`

Two monsters arrive before or at minute one, so only the initial shot is available.

### Required Complexity

- **Time:** $O(N \log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Convert arrival times into integer firing deadlines**

Monster `i` reaches the city after $\texttt{dist[i]}/\texttt{speed[i]}$ minutes. A shot at integer minute $m$ is safe only when

$$
m < \frac{\texttt{dist[i]}}{\texttt{speed[i]}}.
$$

Its latest safe integer firing minute is therefore `((dist[i] - 1) // speed[i])`. This integer formulation handles both fractional arrivals and the rule that an exact-minute arrival happens before a shot.

**Schedule the earliest deadlines first**

Sort all latest-safe minutes. Try to shoot the monster at sorted position `minute` at that same minute. If its deadline is smaller than `minute`, it has already arrived and the game ends; return `minute`, the number previously eliminated.

This order is optimal by exchange. If a schedule shoots a later-deadline monster before an earlier-deadline one, swapping them cannot make the later monster late and can only help the urgent monster. Repeating such swaps produces sorted deadline order without reducing the number of feasible shots. Consequently, the first failed sorted deadline proves that no schedule can eliminate more monsters.

#### Complexity detail

Computing $N$ integer deadlines takes $O(N)$ time. Sorting them costs $O(N\log N)$ time, and the final feasibility scan is $O(N)$. The deadline array occupies $O(N)$ space.

#### Alternatives and edge cases

- **Repeatedly choose the next arrival:** Scanning all remaining monsters before every shot implements the same greedy choice in $O(N^2)$ time.
- **Sort floating-point arrival times:** This can work but introduces unnecessary precision concerns at exact integer boundaries.
- **Use floor division without subtracting one:** `dist // speed` is wrong when the quotient is exact because arrival at that minute prevents firing.
- **Several deadline-zero monsters:** Only one can be destroyed at minute zero.
- **Tied later deadlines:** At most one monster can be assigned to each minute, so a tie may still cause failure.
- **All deadlines feasible:** Return $N$ after the scan completes.

</details>
