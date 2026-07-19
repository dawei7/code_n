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
