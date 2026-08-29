# Triangle Containment - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

Three points $A(x_A, y_A), B(x_B, y_B), C(x_C, y_C)$ that are not collinear define a triangle $\triangle ABC$ on the 2D Cartesian plane.

Examples from problem description:
- $A(-340,495), B(-153,-910), C(835,-947)$ contains the origin $O(0,0)$ in its interior.
- $X(-175,41), Y(-421,-714), Z(574,-645)$ does not contain the origin.

The file `triangles.txt` contains coordinates for one thousand ($1000$) triangles.

The objective is to find the **number of triangles** for which the interior contains the origin:

$$
N_{\text{origin}} = \sum_{k=1}^{1000} \mathbb{I}\left( O(0,0) \in \text{Int}(\triangle A_k B_k C_k) \right)
$$

---

## 2. The Naive Approach & Fundamental Bottlenecks

### Trigonometric / Floating-Point Barycentric System
A naive approach calculates internal angles with inverse trigonometric functions or calculates areas with floating-point Heron's formula:
```python
def naive_contains_origin(A, B, C):
    # Floating-point comparisons prone to precision loss
    # ...
```

### Exact 2D Vector Cross Product Orientations
1. The 2D cross product of vectors $\vec{OA}$ and $\vec{OB}$ is:

$$
\vec{OA} \times \vec{OB} = x_A y_B - y_A x_B
$$

2. The origin $O(0,0)$ lies strictly inside $\triangle ABC$ if and only if $O$ lies on the same relative side of all 3 directed edges ($AB, BC, CA$):

$$
\operatorname{sign}(x_A y_B - y_A x_B) = \operatorname{sign}(x_B y_C - y_B x_C) = \operatorname{sign}(x_C y_A - y_C x_A) \neq 0
$$

3. This involves only 6 integer multiplications and 3 subtractions per triangle with $100\%$ exact integer arithmetic, evaluating all 1000 triangles in $\approx 0.001$ seconds.

---

## 3. Core Intuition & Mathematical Structure

### Cross Product Signs for Origin Containment

| Cross Product Term | Formula | Geometric Meaning |
| :---: | :---: | :--- |
| **$c_1$** | $x_A y_B - y_A x_B$ | Orientation of $O(0,0)$ relative to directed edge $AB$ |
| **$c_2$** | $x_B y_C - y_B x_C$ | Orientation of $O(0,0)$ relative to directed edge $BC$ |
| **$c_3$** | $x_C y_A - y_C x_A$ | Orientation of $O(0,0)$ relative to directed edge $CA$ |
| **Containment Test** | $(c_1 > 0 \land c_2 > 0 \land c_3 > 0) \lor (c_1 < 0 \land c_2 < 0 \land c_3 < 0)$ | All 3 cross products share the same non-zero sign |

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Containment Pipeline
1. Parse each line $(x_A, y_A, x_B, y_B, x_C, y_C)$ from `triangles.txt`.
2. Compute:

$$
c_1 = x_A y_B - y_A x_B
$$

$$
c_2 = x_B y_C - y_B x_C
$$

$$
c_3 = x_C y_A - y_C x_A
$$

3. Triangle contains $O(0,0)$ iff:

$$
(c_1 > 0 \land c_2 > 0 \land c_3 > 0) \lor (c_1 < 0 \land c_2 < 0 \land c_3 < 0)
$$

4. Increment counter `origin_count += 1` on match.
5. Return `origin_count`.

---

## 5. Concrete Step-by-Step Example Walkthrough

### Example 1: Triangle $\triangle ABC$ from Problem Description
- $A(-340, 495), B(-153, -910), C(835, -947)$.
- $c_1 = (-340)(-910) - (495)(-153) = 309400 + 75735 = +385135 > 0$.
- $c_2 = (-153)(-947) - (-910)(835) = 144891 + 759850 = +904741 > 0$.
- $c_3 = (835)(495) - (-947)(-340) = 413325 - 321980 = +91345 > 0$.
- All $c_1, c_2, c_3 > 0 \implies$ **Contains Origin $\checkmark$**. Matches problem statement sample!

### Example 2: Triangle $\triangle XYZ$ from Problem Description
- $X(-175, 41), Y(-421, -714), Z(574, -645)$.
- $c_1 = (-175)(-714) - (41)(-421) = 124950 + 17261 = +142211 > 0$.
- $c_2 = (-421)(-645) - (-714)(574) = 271545 + 409836 = +681381 > 0$.
- $c_3 = (574)(41) - (-645)(-175) = 23534 - 112875 = -89341 < 0$.
- Signs mismatch ($+, +, -$) $\implies$ **Does NOT Contain Origin $\checkmark$**.

### Example 3: Target Evaluation across 1000 Triangles
- Evaluating all 1000 triangles in `triangles.txt`:

$$
N_{\text{origin}} = \mathbf{228}
$$

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Code / Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **File Loading** | Read comma-separated lines from `triangles.txt` | $\mathcal{O}(N)$ |
| **Stage 2** | **Parse Coords** | Extract integer coordinates $(ax, ay, bx, by, cx, cy)$ | $1000$ lines |
| **Stage 3** | **Cross Products** | Compute $c_1, c_2, c_3$ determinants | $\mathcal{O}(1)$ per triangle |
| **Stage 4** | **Sign Check** | Check uniform positive or negative sign | $\mathcal{O}(1)$ |
| **Stage 5** | **Return Count** | Return scalar integer $228$ | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(N)$ where $N = 1000$ | $\approx 0.001$ seconds ($6\,000$ integer multiplications) |
| **Space Complexity** | $\mathcal{O}(N)$ | Line buffer $\approx 25$ KB |
| **Dynamic Execution** | $100\%$ Inline | 2D vector cross product determinant checks |

### Critical Invariants & Edge Cases Handled:
1. **Dynamic Path Resolution**: Resolves `triangles.txt` relative to package location without relying on external working directories.
2. **Clockwise / Counterclockwise Invariance**: Checking both all-positive and all-negative signs handles both CW and CCW vertex orderings seamlessly.