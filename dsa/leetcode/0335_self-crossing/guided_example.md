# Guided Example: Self Crossing

We trace the step-by-step geometric spiral analysis, classification of the three canonical self-intersection topologies (4-segment crossing, 5-segment touch, 6-segment spiral transition), direction offset vector tracking, and in-place boundary inequality evaluation on representative path distance arrays:

- **Input:** $\text{distance} = [2, 1, 1, 2]$
- **Required output:** `true`
  - Moves from $(0, 0)$:
    - Move 0 (North): $(0, 0) \to (0, 2)$
    - Move 1 (West):  $(0, 2) \to (-1, 2)$
    - Move 2 (South): $(-1, 2) \to (-1, 1)$
    - Move 3 (East):  $(-1, 1) \to (1, 1)$
  - Segment 3 traverses horizontal interval $[-1, 1]$ at $y = 1$
  - Segment 0 traverses vertical line $x = 0$ from $y = 0$ to $y = 2$
  - Intersection occurs at point $(0, 1) \implies \text{true}$
- **Expanding Non-Crossing Spiral:** $\text{distance} = [1, 2, 3, 4] \implies \text{false}$
- **Five-Segment Overlap Touch:** $\text{distance} = [1, 2, 3, 2, 2] \implies \text{true}$ ($d[4] + d[0] \ge d[2]$)
- **Short Path Base Cases:** Any path of length $< 4$ cannot self-intersect ($N \le 3 \implies \text{false}$)

This instance demonstrates geometric invariant classification on orthogonal counter-clockwise movements, proves why the first self-crossing in an orthogonal spiral can only occur across 4, 5, or 6 moves, contrasts $O(N)$ inequality evaluation against $O(N^2)$ pairwise segment intersection, and operates in strictly $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given move distances $\text{distance} = [2, 1, 1, 2]$ ($N = 4$):
Starting at $(0, 0)$, move counter-clockwise:
1. North by $\text{distance}[0] = 2$
2. West by $\text{distance}[1] = 1$
3. South by $\text{distance}[2] = 1$
4. East by $\text{distance}[3] = 2$
Determine whether the resulting polyline intersects itself at any point:

```text
Coordinates Tracked:
           (-1, 2) ------ (0, 2)
              |              |
              |   (0, 1)     |
           (-1, 1) --X-------+---> (1, 1)
                             |
                           (0, 0)

Segment 0: (0, 0) -> (0, 2) [Vertical at x = 0]
Segment 1: (0, 2) -> (-1, 2) [Horizontal at y = 2]
Segment 2: (-1, 2) -> (-1, 1) [Vertical at x = -1]
Segment 3: (-1, 1) -> (1, 1)  [Horizontal at y = 1]

Self-Crossing at point (0, 1)!
Output: True
```

### The Geometry of 90-Degree Counter-Clockwise Spirals
- Turns occur in strict cyclic order: North $\to$ West $\to$ South $\to$ East $\to$ North $\dots$
- Adjacent segments share endpoints by definition.
- Parallel segments separated by one turn cannot intersect without an intervening reversal.
- **The Tripartite Crossing Theorem:**
  The *first* self-crossing in such a spiral can occur in exactly three geometric configurations:
  1. **Case 1 (4 Segments):** Segment $i$ crosses segment $i - 3$.
  2. **Case 2 (5 Segments):** Segment $i$ touches or overlaps segment $i - 4$.
  3. **Case 3 (6 Segments):** Segment $i$ crosses segment $i - 5$ as an outward expanding spiral transitions to an inward contracting spiral.

---

## 2. Conceptual Foundation & Invariants

Let $d[i] = \text{distance}[i]$:

### Case 1: Crosses Segment $i - 3$ ($i \ge 3$)
Occurs when the current segment is at least as long as the parallel segment two steps prior, and the preceding orthogonal segment was trapped inside the segment three steps prior:
$$
d[i] \ge d[i - 2] \quad \text{and} \quad d[i - 1] \le d[i - 3]
$$

### Case 2: Overlaps Segment $i - 4$ ($i \ge 4$)
Occurs when the path folds back onto the collinear line of segment $i - 4$:
$$
d[i - 1] == d[i - 3] \quad \text{and} \quad d[i] + d[i - 4] \ge d[i - 2]
$$

### Case 3: Crosses Segment $i - 5$ ($i \ge 5$)
Occurs when transitioning from an expanding spiral ($d[i-2] \ge d[i-4]$) to a contracting spiral:
$$
d[i - 2] \ge d[i - 4], \quad d[i - 1] \le d[i - 3], \quad d[i] \ge d[i - 2] - d[i - 4], \quad \text{and} \quad d[i - 1] + d[i - 5] \ge d[i - 3]
$$

> **Invariant.** For any index $i \ge 3$, if the prefix path $0 \dots i-1$ is non-self-crossing, the path at step $i$ crosses itself if and only if one of Case 1, Case 2, or Case 3 is satisfied.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{distance} = [2, 1, 1, 2]$:
Array length $N = 4$. Indices to evaluate: $i = 3$.

---

### Step 1: Evaluate $i = 3$ ($d[3] = 2$)
We examine segment 3 against previous segment lengths:
- $d[i] = d[3] = 2$ (Eastward move)
- $d[i - 1] = d[2] = 1$ (Southward move)
- $d[i - 2] = d[1] = 1$ (Westward move)
- $d[i - 3] = d[0] = 2$ (Northward move)

---

### Step 2: Test Case 1 Condition ($i \ge 3$)
1. **Parallel Length Comparison:**
   $$
   d[i] \ge d[i - 2] \iff d[3] \ge d[1] \iff 2 \ge 1 \quad (\mathbf{True!})
   $$
   *(The current eastward move of length 2 is long enough to cross the vertical line at $x = 0$ established by the westward shift of length 1).*

2. **Orthogonal Enclosure Comparison:**
   $$
   d[i - 1] \le d[i - 3] \iff d[2] \le d[0] \iff 1 \le 2 \quad (\mathbf{True!})
   $$
   *(The southward move of length 1 did not overshoot the original northward move of length 2, meaning segment 3 is at height $y = 1$, which lies within the vertical span $[0, 2]$ of segment 0).*

---

### Step 3: Intersection Confirmation
Both sub-conditions of Case 1 hold simultaneously:
$$
(2 \ge 1) \land (1 \le 2) = \mathbf{\text{True}}
$$
Segment 3 crosses segment 0 at point $(0, 1)$!
Immediately return:
$$
\mathbf{\text{True}}
$$

---

## 4. Complete Execution Trace

```text
distance = [2, 1, 1, 2]

i = 3:
  d[3] = 2, d[2] = 1, d[1] = 1, d[0] = 2
  Case 1 Check:
    d[3] >= d[1] (2 >= 1) -> TRUE
    d[2] <= d[0] (1 <= 2) -> TRUE
  Case 1 Satisfied!

Intersection Detected -> return True
```

| Step $i$ | Direction | Move $d[i]$ | Parallel $d[i-2]$ | Prior Orthogonal $d[i-1]$ | Base Orthogonal $d[i-3]$ | Case 1 Condition: $d[i] \ge d[i-2] \land d[i-1] \le d[i-3]$ | Crossing Detected? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | North | 2 | - | - | - | - | No |
| 1 | West | 1 | - | - | - | - | No |
| 2 | South | 1 | - | - | - | - | No |
| **3** | **East** | **2** | **1** | **1** | **2** | **$2 \ge 1 \land 1 \le 2 \implies \text{True}$** | **Yes (Crosses Seg 0)** |

---

## 5. Algorithmic Correctness

**Soundness.** Because each turn is fixed at 90 degrees counter-clockwise, the relative positions of segments $i, i-1, \dots, i-5$ can be represented as closed-form linear intervals along the $X$ and $Y$ axes. The three cases cover all possible relative positions where a horizontal and vertical line segment can touch or cross. If an equality or inequality holds, the corresponding segments mathematically share at least one point in $\mathbb{R}^2$.

**Completeness.** A path cannot self-intersect earlier than step 3. Furthermore, an expanding spiral that never satisfies any of the three conditions continues outward forever without intersecting. Once a spiral contracts, it must either remain strictly inside the previous turns or trigger one of the three boundary crossing conditions. Since every move $i \ge 3$ is tested, no intersection can be missed.

---

## 6. Traps This Instance Exposes

- **Endpoint Touch Counts as Crossing:** The problem specifies that touching at an endpoint or overlapping along a segment counts as crossing. Using strict inequalities ($>$ instead of $\ge$) fails on touching loops like $[1, 1, 1, 1]$ or $[1, 2, 3, 2, 2]$.
- **$O(N^2)$ Pairwise Segment Comparison:** Testing all pairs of segments $(i, j)$ takes $O(N^2)$ time, which TLEs for $N = 10^5$. Local checking over windows of size 6 runs in $O(N)$ time.
- **Spiral Transition (Case 3):** Case 3 requires checking 4 simultaneous inequalities. Missing the condition $d[i] \ge d[i-2] - d[i-4]$ creates false positives when the inward spiral turns before reaching segment $i - 5$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of elements in `distance`. The loop iterates from index $3$ to $N - 1$, performing at most 3 constant-time arithmetic checks per move.
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory using zero additional data structures.
