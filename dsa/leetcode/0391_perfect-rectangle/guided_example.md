# Guided Example: Perfect Rectangle

We trace the step-by-step dual geometric verification: aggregate area conservation ($\sum \text{Area}_i = \text{Area}_{\text{bbox}}$), four bounding corner singularity ($cnt[(\text{corner})] == 1$), and interior/border vertex parity topology ($c \in \{2, 4\}$) on representative rectangular tiling sets:

- **Input:** $rectangles = [[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]]$
- **Required output:** `true`
  - Bounding box calculation:
    - $\text{minX} = 1, \text{minY} = 1, \text{maxX} = 4, \text{maxY} = 4$
    - Bounding area: $(4 - 1) \times (4 - 1) = 3 \times 3 = 9$
  - Rectangle areas:
    - $R_1 [1, 1, 3, 3] \implies 2 \times 2 = 4$
    - $R_2 [3, 1, 4, 2] \implies 1 \times 1 = 1$
    - $R_3 [3, 2, 4, 4] \implies 1 \times 2 = 2$
    - $R_4 [1, 3, 2, 4] \implies 1 \times 1 = 1$
    - $R_5 [2, 3, 3, 4] \implies 1 \times 1 = 1$
    - Total sum: $4 + 1 + 2 + 1 + 1 = 9$ (Exact match with bounding area!)
  - Corner counts:
    - Outer 4 corners $(1, 1), (1, 4), (4, 4), (4, 1)$ each have count exactly $1$
    - All remaining 8 non-corner vertices have count exactly $2$ (Valid edge interfaces)
  - Result: forms a perfect non-overlapping rectangular cover $\implies \mathbf{\text{True}}$
- **Area Deficit (Gap):** $rectangles = [[1,1,2,3], [1,3,2,4], [3,1,4,2], [3,2,4,4]] \implies$ area $6 \ne 9 \implies \text{false}$
- **Overlap Counterexample:** Overlapping pieces can match total area if a gap cancels the overlap, but interior vertex multiplicities violate $c \in \{2, 4\}$

This instance demonstrates combining measure theory (Lebesgue area additivity) with topological vertex Euler characteristics, mathematically proves why area equality alone cannot detect balanced overlap/gap defects, and derives $O(N)$ linear time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of axis-aligned rectangles where each $r = [x_1, y_1, x_2, y_2]$:
Determine whether all given rectangles together form an **exact cover** of a single large rectangle without overlaps or empty holes:

```text
Visual Layout:
y=4 +-------+---+-------+
    |  R4   |R5 |  R3   |
y=3 +-------+---+       |
    |           |       |
y=2 |    R1     +-------+
    |           |  R2   |
y=1 +-----------+-------+
   x=1         x=3     x=4

Bounding Box: [1, 1, 4, 4] (Width = 3, Height = 3, Area = 9)
Sum of Component Areas: 4 + 1 + 2 + 1 + 1 = 9 (Matches exactly!)
```

### Why Area Equality Alone Fails
Consider a scenario where rectangle A overlaps rectangle B by 2 units, and an empty hole of 2 units is left somewhere else in the bounding box.
The total area $\sum \text{Area}_i$ will still equal the bounding box area because the $+2$ overlap numerically cancels the $-2$ hole!
To be mathematically foolproof, an exact cover must satisfy **both**:
1. **Area Equality:** $\sum \text{Area}_i == (\text{maxX} - \text{minX}) \times (\text{maxY} - \text{minY})$
2. **Topological Vertex Parity:**
   - The 4 outer bounding corners must have multiplicity **exactly 1**.
   - Every other shared vertex must have multiplicity **2** (meeting along a seam) or **4** (meeting at an interior cross). Any count of 1, 3, or $> 4$ indicates a hole, notch, or illegal overlap!

---

## 2. Conceptual Foundation & Invariants

### 1. The Vertex Multiplicity Map:
For each rectangle $[x_1, y_1, x_2, y_2]$, record its 4 vertices in a frequency map `cnt`:
- Bottom-Left: $(x_1, y_1)$
- Top-Left: $(x_1, y_2)$
- Top-Right: $(x_2, y_2)$
- Bottom-Right: $(x_2, y_1)$

### 2. Validation Conditions:
1. **Bounding Box Calculation:**
   $$
   minX = \min x_1, \quad minY = \min y_1, \quad maxX = \max x_2, \quad maxY = \max y_2
   $$
2. **Area Consistency:**
   $$
   \sum (x_2 - x_1)(y_2 - y_1) == (maxX - minX) \cdot (maxY - minY)
   $$
3. **Four Outer Corner Condition:**
   $$
   cnt[(minX, minY)] == 1 \land cnt[(minX, maxY)] == 1 \land cnt[(maxX, maxY)] == 1 \land cnt[(maxX, minY)] == 1
   $$
4. **Internal Vertex Multiplicity Condition:**
   After deleting the 4 outer corners from `cnt`:
   $$
   \forall (x, y) \in cnt: \quad cnt[(x, y)] \in \{2, \; 4\}
   $$

> **Invariant.** A set of non-overlapping axis-aligned rectangles forms an exact cover of a bounding box if and only if total area matches and vertex multiplicities conform to the Euler boundary tiling theorem.

---

## 3. Step-by-Step Worked Execution

We trace the 5 rectangles:
1. $R_1 = [1, 1, 3, 3]$: Area $= (3 - 1)(3 - 1) = 4$. Corners: $(1, 1), (1, 3), (3, 3), (3, 1)$.
2. $R_2 = [3, 1, 4, 2]$: Area $= (4 - 3)(2 - 1) = 1$. Corners: $(3, 1), (3, 2), (4, 2), (4, 1)$.
3. $R_3 = [3, 2, 4, 4]$: Area $= (4 - 3)(4 - 2) = 2$. Corners: $(3, 2), (3, 4), (4, 4), (4, 2)$.
4. $R_4 = [1, 3, 2, 4]$: Area $= (2 - 1)(4 - 3) = 1$. Corners: $(1, 3), (1, 4), (2, 4), (2, 3)$.
5. $R_5 = [2, 3, 3, 4]$: Area $= (3 - 2)(4 - 3) = 1$. Corners: $(2, 3), (2, 4), (3, 4), (3, 3)$.

---

### Step 1: Area Summation and Bounding Box
- Cumulative Area:
  $$
  area = 4 + 1 + 2 + 1 + 1 = \mathbf{9}
  $$
- Bounding Box Dimensions:
  $$
  minX = 1, \quad minY = 1, \quad maxX = 4, \quad maxY = 4
  $$
- Bounding Box Expected Area:
  $$
  (4 - 1) \times (4 - 1) = 3 \times 3 = \mathbf{9}
  $$
- Area check: $9 == 9$ (**True**).

---

### Step 2: Vertex Multiplicity Aggregation
Count occurrences of every coordinate across all 5 rectangles:

| Vertex $(x, y)$ | Contributing Rectangles | Total Count $cnt[(x, y)]$ | Role in Cover |
|:---:|:---:|:---:|:---|
| $(1, 1)$ | $R_1$ | **1** | Outer Bottom-Left Corner |
| $(1, 4)$ | $R_4$ | **1** | Outer Top-Left Corner |
| $(4, 4)$ | $R_3$ | **1** | Outer Top-Right Corner |
| $(4, 1)$ | $R_2$ | **1** | Outer Bottom-Right Corner |
| $(3, 1)$ | $R_1, R_2$ | **2** | Bottom edge seam |
| $(1, 3)$ | $R_1, R_4$ | **2** | Left edge seam |
| $(3, 3)$ | $R_1, R_5$ | **2** | Interior seam |
| $(3, 2)$ | $R_2, R_3$ | **2** | Vertical seam |
| $(4, 2)$ | $R_2, R_3$ | **2** | Right edge seam |
| $(2, 4)$ | $R_4, R_5$ | **2** | Top edge seam |
| $(2, 3)$ | $R_4, R_5$ | **2** | Interior seam |
| $(3, 4)$ | $R_3, R_5$ | **2** | Top edge seam |

---

### Step 3: Four Outer Corners Validation
- Check:
  $$
  cnt[(1, 1)] == 1 \land cnt[(1, 4)] == 1 \land cnt[(4, 4)] == 1 \land cnt[(4, 1)] == 1
  $$
  All four equal 1 (**True**).
- Remove the four outer corners from the dictionary.

---

### Step 4: Interior / Boundary Multiplicity Verification
- Check all remaining 8 vertices:
  - Every vertex has $c = 2 \in \{2, 4\}$.
  - Zero vertices have count 1, 3, or $> 4$.
- All conditions satisfied!
- Return:
  $$
  \mathbf{\text{True}}
  $$

---

## 4. Complete Execution Trace

```text
rectangles = [[1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4]]

Pass 1: Accumulate areas and corner counts
  Total area = 4 + 1 + 2 + 1 + 1 = 9
  Bounding box = [1, 1, 4, 4] -> expected area = (4-1)*(4-1) = 9 -> OK
  Outer corners: (1,1):1, (1,4):1, (4,4):1, (4,1):1 -> all == 1 -> OK

Pass 2: Check remaining vertices
  Vertices: {(3,1):2, (1,3):2, (3,3):2, (3,2):2, (4,2):2, (2,4):2, (2,3):2, (3,4):2}
  All counts in {2, 4} -> TRUE

Result: True
```

| Phase | Check Performed | Value Computed | Target Constraint | Validation Status |
|:---:|:---:|:---:|:---:|:---:|
| 1 | Bounding Box Calculation | $[1, 1, 4, 4]$ | Encloses all pieces | Valid |
| 2 | Area Equality | $\sum = 9$ | $(4-1) \times (4-1) = 9$ | **Pass** ($9 == 9$) |
| 3 | Outer Corner Multiplicities | All 4 points | Multiplicity $== 1$ | **Pass** (All four are 1) |
| **4** | **Interior Vertex Parity** | **8 vertices** | **Multiplicity $\in \{2, 4\}$** | **Pass** (All are 2) |
| **Final**| **Tiling Cover Decision** | - | - | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** In any planar rectangular subdivision, interior corners where rectangles meet without overlapping must join either as a T-junction (2 rectangles meeting) or a cross-junction (4 rectangles meeting). The exterior boundary has 4 convex corners of angle $90^\circ$, each belonging to exactly one rectangle. If rectangles overlapped, some vertex count would exceed 4 or an odd multiplicity (like 3) would appear without matching space. Combined with strict area conservation, no gaps or overlaps can go undetected.

**Completeness.** Every rectangle contributes exactly 4 vertices and its precise area in a single pass. If any overlap or gap exists, either the total area will mismatch or a rogue vertex with multiplicity $\ne 2, 4$ will be present, guaranteeing that all invalid covers return `False`.

---

## 6. Traps This Instance Exposes

- **Overlapping Pieces with Equal Area:** Two rectangles overlapping by $k$ area combined with an internal gap of $k$ area will have $\sum \text{area} == \text{bbox\_area}$. Only the vertex multiplicity check catches this defect.
- **Corner Set XOR Simplification:** Some approaches toggle corners in a set (`s.remove(pt)` if present else `s.add(pt)`). However, an interior cross where 4 rectangles meet would toggle $1 \to 0 \to 1 \to 0$ and disappear, which is correct, but a double overlap of 2 corners could also falsely disappear! Tracking explicit counts and verifying $c \in \{2, 4\}$ is strictly more robust.
- **Large Coordinates:** Coordinates range up to $10^5$. Using integer multiplication prevents overflow and floating-point errors.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of rectangles.
  - A single loop processes each rectangle: computing area and inserting 4 coordinates into the hash table in $O(1)$ time.
  - Post-processing checks the 4 bounding corners and iterates over at most $4N$ unique vertices in $O(N)$ time.
  - Overall time is strictly linear $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space to store the coordinate counts in hash map `cnt` (at most $4N$ entries).
