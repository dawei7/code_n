# Maximum Candies You Can Get from Boxes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1298 |
| Difficulty | Hard |
| Topics | Array, Breadth-First Search, Graph Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/) |

## Problem Description
### Goal
There are $n$ boxes labeled from $0$ through $n-1$. Each box has an open or closed status, contains some candies, may provide keys for other boxes, and may physically contain other boxes. Opening a box lets you collect all of its candies, take every key inside it, and gain possession of every contained box.

You initially possess the boxes listed in `initialBoxes`. A box can be opened only when you both possess it and either it was already open or you have obtained its key. Keys may be found before or after their corresponding boxes, and either order must eventually make the box usable. Return the maximum total number of candies obtainable by repeatedly applying these rules.

### Function Contract
**Inputs**

Let $n$ be the common length of the first four arrays, let

$$
K = \sum_{i=0}^{n-1} \lvert \texttt{keys[i]} \rvert,
\qquad
B = \sum_{i=0}^{n-1} \lvert \texttt{containedBoxes[i]} \rvert,
$$

and define $S=n+K+B$.

- `status`: an array of $n$ values from $\{0,1\}$; `status[i] = 1` means box $i$ is initially open.
- `candies`: an array of $n$ positive candy counts, each at most $1000$.
- `keys`: `keys[i]` lists distinct box labels whose keys are found when box $i$ is opened.
- `containedBoxes`: `containedBoxes[i]` lists distinct box labels obtained from box $i$; each box is contained in at most one other box.
- `initialBoxes`: the labels of the boxes initially possessed.
- The constraints satisfy $1 \le n \le 1000$, while every referenced box label is between $0$ and $n-1$.

**Return value**

The greatest total number of candies that can be collected from boxes that become both possessed and openable.

### Examples
**Example 1**

- Input: `status = [1,0,1,0]`, `candies = [7,5,4,100]`, `keys = [[],[],[1],[]]`, `containedBoxes = [[1,2],[3],[],[]]`, `initialBoxes = [0]`
- Output: `16`
- Explanation: Box 0 yields boxes 1 and 2; box 2 supplies the key for box 1. Box 3 remains locked.

**Example 2**

- Input: `status = [1,0,0,0,0,0]`, `candies = [1,1,1,1,1,1]`, `keys = [[1,2,3,4,5],[],[],[],[],[]]`, `containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]`, `initialBoxes = [0]`
- Output: `6`
- Explanation: Opening box 0 provides both every remaining box and every required key.

**Example 3**

- Input: `status = [0,1]`, `candies = [10,20]`, `keys = [[],[]]`, `containedBoxes = [[],[0]]`, `initialBoxes = [1]`
- Output: `20`
- Explanation: Box 0 is obtained but cannot be opened because its key is never found.
