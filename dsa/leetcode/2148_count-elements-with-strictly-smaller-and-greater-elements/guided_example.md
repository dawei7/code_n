# Guided Example: Count Elements With Strictly Smaller and Greater Elements

We analyze and execute the global extremum exclusion algorithm on a representative problem instance, demonstrating how determining the array minimum and maximum reduces individual element checks to an open-interval boundary comparison.

- **Input:** `nums = [-3, 3, 3, 90]`
- **Output:** `2`

This instance illustrates strict inequality checking, duplicate intermediate value retention, and global extremum elimination.

---

## 1. Problem Overview & Representative Instance

Given an integer array `nums`, an element occurrence $x \in \text{nums}$ qualifies if and only if both of the following criteria hold simultaneously:
1. There exists at least one element $y \in \text{nums}$ such that $y < x$ (a strictly smaller element).
2. There exists at least one element $z \in \text{nums}$ such that $z > x$ (a strictly greater element).

We are tasked with computing the total count of qualifying element occurrences. Each occurrence of a duplicate value is evaluated and counted individually.

In our representative instance:
- `nums = [-3, 3, 3, 90]` of length $n = 4$.
- Distinct values present: $\{-3, 3, 90\}$.
- The value $3$ appears twice.

We must determine which occurrences strictly reside between other values in the array and return their count.

---

## 2. Mathematical & Algorithmic Principles

### Equivalence to Global Extremum Exclusion

Let the global minimum and maximum of the multiset `nums` be:
$$M_{\min} = \min_{i} \text{nums}[i] \quad \text{and} \quad M_{\max} = \max_{i} \text{nums}[i]$$

Consider any candidate element $x \in \text{nums}$:
1. **Existence of Strictly Smaller Element:**
   $$\exists y \in \text{nums} \text{ such that } y < x \iff x > M_{\min}$$
   If $x = M_{\min}$, no element in the array can be strictly smaller than $x$ by definition of the minimum. Conversely, if $x > M_{\min}$, the minimum element itself serves as a valid witness $y = M_{\min} < x$.
2. **Existence of Strictly Greater Element:**
   $$\exists z \in \text{nums} \text{ such that } z > x \iff x < M_{\max}$$
   If $x = M_{\max}$, no element in the array can be strictly greater than $x$ by definition of the maximum. Conversely, if $x < M_{\max}$, the maximum element itself serves as a valid witness $z = M_{\max} > x$.

### The Open Interval Criterion

An element $x \in \text{nums}$ qualifies if and only if:
$$M_{\min} < x < M_{\max}$$

Therefore, every element strictly inside the open interval $(M_{\min}, M_{\max})$ qualifies, while every element lying on the boundaries ($x = M_{\min}$ or $x = M_{\max}$) is disqualified.

If all elements in the array are equal ($M_{\min} = M_{\max}$), the interval $(M_{\min}, M_{\max})$ is empty, and zero elements qualify.

| Concept / Metric | Formal Condition | Concrete Role in Instance |
|---|---|---|
| Global Minimum $M_{\min}$ | $\min(\text{nums})$ | $-3$ (eliminates lower boundary) |
| Global Maximum $M_{\max}$ | $\max(\text{nums})$ | $90$ (eliminates upper boundary) |
| Qualification Window | $(M_{\min}, M_{\max})$ | $(-3, 90)$ |
| Witness for Lower Bound | $M_{\min} = -3 < x$ | Certifies existence of strictly smaller element |
| Witness for Upper Bound | $M_{\max} = 90 > x$ | Certifies existence of strictly greater element |
| Final Count | Count of $x \in (M_{\min}, M_{\max})$ | $2$ (both occurrences of $3$) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the two-pass linear evaluation on `nums = [-3, 3, 3, 90]`.

```
Array values:  [-3,  3,  3,  90]
Min = -3, Max = 90
Test interval: (-3, 90)

-3:  -3 > -3 is False  => Disqualified
 3:  -3 < 3 < 90 is True   => Qualified
 3:  -3 < 3 < 90 is True   => Qualified
90:  90 < 90 is False  => Disqualified
Total Count = 2
```

### Step 1: Pass 1 — Find Global Extremes
Scan `nums` to identify $M_{\min}$ and $M_{\max}$:
- Inspect `nums[0] = -3`: Initialize $M_{\min} = -3$, $M_{\max} = -3$.
- Inspect `nums[1] = 3`: $M_{\min} = \min(-3, 3) = -3$; $M_{\max} = \max(-3, 3) = 3$.
- Inspect `nums[2] = 3`: $M_{\min} = -3$; $M_{\max} = 3$.
- Inspect `nums[3] = 90`: $M_{\min} = \min(-3, 90) = -3$; $M_{\max} = \max(3, 90) = 90$.

Global extremes finalized:
$$M_{\min} = -3, \quad M_{\max} = 90$$

Boundary check: $M_{\min} < M_{\max}$ ($-3 < 90$). The open interval $(-3, 90)$ is non-degenerate.

### Step 2: Pass 2 — Evaluate Each Occurrence
Initialize counter: $\text{count} = 0$.

- **Index 0 ($x = -3$):**
  - Check $x > M_{\min}$: $-3 > -3$ is False.
  - Reason: No element in the array is smaller than the minimum.
  - Status: Disqualified. Counter remains $0$.
- **Index 1 ($x = 3$):**
  - Check $x > M_{\min}$: $3 > -3$ is True (witness: $-3$).
  - Check $x < M_{\max}$: $3 < 90$ is True (witness: $90$).
  - Status: Qualified. $\text{count} = 0 + 1 = 1$.
- **Index 2 ($x = 3$):**
  - Check $x > M_{\min}$: $3 > -3$ is True (witness: $-3$).
  - Check $x < M_{\max}$: $3 < 90$ is True (witness: $90$).
  - Status: Qualified. $\text{count} = 1 + 1 = 2$.
- **Index 3 ($x = 90$):**
  - Check $x < M_{\max}$: $90 < 90$ is False.
  - Reason: No element in the array is greater than the maximum.
  - Status: Disqualified. Counter remains $2$.

### Step 3: Emit Final Count
- All elements inspected.
- Qualifying count: $2$.

---

## 4. Comprehensive State Trace

The table below catalogs every element in `nums`, its evaluation against both extreme witnesses, and its contribution to the final count:

| Index $i$ | Element Value | Strictly Greater Than $M_{\min} = -3$? | Strictly Smaller Than $M_{\max} = 90$? | Satisfies Open Interval $(-3, 90)$? | Qualifying Status | Running Count |
|---|---|---|---|---|---|---|
| $0$ | $-3$ | No ($-3 \ngtr -3$) | Yes ($-3 < 90$) | No | Disqualified (Minimum) | $0$ |
| $1$ | $3$ | Yes ($3 > -3$) | Yes ($3 < 90$) | Yes | **Qualified** | $1$ |
| $2$ | $3$ | Yes ($3 > -3$) | Yes ($3 < 90$) | Yes | **Qualified** | $2$ |
| $3$ | $90$ | Yes ($90 > -3$) | No ($90 \nless 90$) | No | Disqualified (Maximum) | $2$ |

### Frequency Subtraction Alternative Verification

We can also express the answer by subtracting the frequencies of the boundary values:
- Total array size: $n = 4$.
- Frequency of minimum value ($-3$): $f(-3) = 1$.
- Frequency of maximum value ($90$): $f(90) = 1$.
- Total qualifying count:
$$\text{Count} = n - f(M_{\min}) - f(M_{\max}) = 4 - 1 - 1 = 2$$

Both the filtering scan and frequency subtraction yield the identical result of $2$.

---

## 5. Algorithmic Correctness & Soundness

### Biconditional Proof
1. **Sufficiency:** If $M_{\min} < \text{nums}[i] < M_{\max}$, then because $M_{\min}, M_{\max} \in \text{nums}$, there exist concrete indices $j_{\min}$ and $j_{\max}$ such that $\text{nums}[j_{\min}] = M_{\min} < \text{nums}[i]$ and $\text{nums}[j_{\max}] = M_{\max} > \text{nums}[i]$. Thus $\text{nums}[i]$ strictly satisfies both problem requirements.
2. **Necessity:** Suppose $\text{nums}[i]$ qualifies. Then there exists $y \in \text{nums}$ with $y < \text{nums}[i]$. Since $M_{\min} \le y < \text{nums}[i]$, we have $\text{nums}[i] > M_{\min}$. Similarly, there exists $z \in \text{nums}$ with $z > \text{nums}[i]$. Since $M_{\max} \ge z > \text{nums}[i]$, we have $\text{nums}[i] < M_{\max}$. Thus $M_{\min} < \text{nums}[i] < M_{\max}$.

The condition $M_{\min} < \text{nums}[i] < M_{\max}$ is both necessary and sufficient.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **All Elements Identical:** `nums = [7, 7, 7, 7]`. Here $M_{\min} = 7$ and $M_{\max} = 7$. No element can satisfy $7 < x < 7$. The algorithm returns $0$.
2. **Only Two Elements:** `nums = [2, 5]`. $M_{\min} = 2, M_{\max} = 5$. Neither element is in $(2, 5)$. The algorithm returns $0$.
3. **Multiple Copies of Minimum and Maximum:** `nums = [1, 1, 3, 5, 5]`. Here $f(M_{\min}) = 2$ and $f(M_{\max}) = 2$. Only $3$ qualifies. Formula $5 - 2 - 2 = 1$ correctly eliminates all copies of extremes.
4. **Negative Numbers:** Handled naturally by standard numerical ordering (e.g., $-100 < -3 < 0$).

### Common Anti-Patterns
- **Pairwise Comparison ($O(n^2)$):** For each element $i$, iterating through all elements $j$ to search for smaller and larger witnesses takes $O(n^2)$ operations. Two linear scans reduce this to $O(n)$.
- **Sorting Unnecessarily ($O(n \log n)$):** Sorting the entire array to trim the ends works, but incurs extra time and memory overhead compared to a direct $O(n)$ min-max scan.
- **Set De-duplication Error:** Deduplicating the array with a `Set` drops duplicate intermediate values. The problem demands counting each qualifying *occurrence*. If `3` appears five times between $-3$ and $90$, all five occurrences must be counted.

---

## 7. Complexity Analysis

### Time Complexity
- **Pass 1:** Finding the minimum and maximum of $n$ numbers takes $n - 1$ comparisons, running in $O(n)$ time.
- **Pass 2:** Counting elements satisfying $M_{\min} < \text{nums}[i] < M_{\max}$ takes $n$ comparisons, running in $O(n)$ time.
- Total time complexity is strictly $O(n)$, executing in under $1$ millisecond for $n \le 100$.

### Auxiliary Space Complexity
- The algorithm tracks only scalar variables ($M_{\min}$, $M_{\max}$, and the counter).
- No new collections, hash tables, or recursive call frames are created.
- Total auxiliary space complexity is $O(1)$.
