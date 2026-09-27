# Guided Example: Generate Random Point in a Circle

We trace the step-by-step 2D spatial probability density function (PDF), area element Jacobian scaling ($dA = r \, dr \, d\theta$), Inverse Transform Sampling for radial distance ($r = R\sqrt{u}$), angle sampling ($\theta \sim [0, 2\pi)$), and Cartesian coordinate translation on representative circle geometries:

- **Input:** $radius = 1.0, \quad x\_center = 0.0, \quad y\_center = 0.0$
- **Required output:** Points $(x, y)$ uniformly distributed across the disc $x^2 + y^2 \le 1.0$
- **Execution trace via Inverse Transform Sampling:**
  - **The Area Element Dilemma:**
    - A naive uniform choice of radius $r \sim [0, R]$ produces severe central clustering because the area of an annulus of radius $r$ is $dA = 2\pi r \, dr$, which grows linearly with $r$.
    - For uniform 2D area density, the probability density must satisfy:
      $$
      f_R(r) = \frac{2r}{R^2} \quad \text{for } r \in [0, R]
      $$
    - Integrating yields the Cumulative Distribution Function (CDF):
      $$
      F_R(r) = \int_0^r \frac{2t}{R^2} \, dt = \frac{r^2}{R^2}
      $$
    - Inverting the CDF for uniform $u \sim \text{Uniform}(0, 1)$:
      $$
      u = \frac{r^2}{R^2} \implies r = R \sqrt{u} = \sqrt{u \cdot R^2}
      $$
  - **Sample Generation Steps:**
    1. Draw area uniform variable: $u \in [0, 1)$
    2. Compute radial distance:
       $$
       length = R \sqrt{u}
       $$
    3. Draw angular direction:
       $$
       \theta = v \times 2\pi \quad \text{where } v \in [0, 1)
       $$
    4. Project onto Cartesian coordinates:
       $$
       \begin{aligned}
       x &= x\_center + length \cdot \cos(\theta) \\
       y &= y\_center + length \cdot \sin(\theta)
       \end{aligned}
       $$
- **Worked Draw 1 ($u = 0, v = 0$):**
  - $length = 1.0 \times \sqrt{0} = 0.0$
  - $\theta = 0 \times 2\pi = 0.0$
  - Coordinates: $(0.0 + 0 \cdot \cos(0), \; 0.0 + 0 \cdot \sin(0)) = \mathbf{(0.0, 0.0)}$ (Center)
- **Worked Draw 2 ($u = 0.25, v = 0$):**
  - $length = 1.0 \times \sqrt{0.25} = 0.5$
  - Coordinates: $(0.0 + 0.5 \cos(0), \; 0.0 + 0.5 \sin(0)) = \mathbf{(0.5, 0.0)}$
  - Notice: $u = 0.25$ (quarter of the area) produces $r = 0.5$ (half the radius), correctly reflecting that a circle of half-radius has one-quarter of the total area!
- **Worked Draw 3 ($u = 1.0, v = 0.25$):**
  - $length = 1.0 \times \sqrt{1.0} = 1.0$
  - $\theta = 0.25 \times 2\pi = \pi / 2$ ($90^\circ$)
  - Coordinates: $(0.0 + 1.0 \cos(\pi/2), \; 0.0 + 1.0 \sin(\pi/2)) = \mathbf{(0.0, 1.0)}$ (Top boundary)

This instance demonstrates continuous 2D transformation of random variables, mathematically proves why the square root transformation compensates for the Jacobian determinant, and derives strictly $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given the radius $R$ and center coordinates $(x_c, y_c)$ of a circle:
Generate a point $(x, y)$ chosen **uniformly at random** from within the circle (including the boundary).

```text
The Density Fallacy (Naive vs Correct):
  Naive (r = R * u):                 Correct (r = R * sqrt(u)):
    Points cluster densely near        Points spread uniformly across
    the center because inner rings     equal area patches across the
    receive too many samples!          entire disc.

Area Geometry:
  Radius r = R/2 encloses Area = pi * (R/2)^2 = (1/4) * Area(Circle)
  Therefore, only 25% of points should have r <= R/2.
  Formula r = R * sqrt(u) satisfies: r <= R/2 <=> sqrt(u) <= 1/2 <=> u <= 1/4!
```

### The Jacobian Area Correction
In polar coordinates:
The differential area element is:
$$
dA = dx \, dy = r \, dr \, d\theta
$$
Because of the factor $r$:
- An annulus of width $dr$ at radius $r = R$ has **twice the circumference and area** of an annulus of the same width at radius $r = R / 2$.
- If $r$ were chosen uniformly, equal radial increments would receive equal numbers of points, causing outer rings to be starved of points and inner rings to be overpopulated.
- To make probability proportional to area, the radial distribution must have density proportional to $r$: $f(r) \propto r$.

---

## 2. Conceptual Foundation & Invariants

### 1. Derivation of Inverse CDF:
- Total area of circle: $A = \pi R^2$.
- The probability that a uniformly chosen point has distance $\le r$ from the center is the ratio of areas:
  $$
  F_R(r) = P(\text{Distance} \le r) = \frac{\pi r^2}{\pi R^2} = \left(\frac{r}{R}\right)^2
  $$
- This is the Cumulative Distribution Function (CDF).
- To generate a random variable with this CDF from a standard uniform variable $u \sim \text{Uniform}(0, 1)$:
  We apply the **Inverse Transform Method**:
  $$
  u = F_R(r) = \frac{r^2}{R^2}
  $$
  Solving for $r$:
  $$
  r^2 = u \cdot R^2 \implies r = R \sqrt{u}
  $$

### 2. Angular Independence:
By circular symmetry, the direction angle $\theta$ is completely independent of the radius $r$ and is uniformly distributed over the circle's circumference $[0, 2\pi)$:
$$
\theta \sim \text{Uniform}(0, 2\pi)
$$

### 3. Cartesian Translation:
$$
x = x_c + r \cos(\theta), \quad y = y_c + r \sin(\theta)
$$

> **Uniform Density Invariant.** For any measurable region $S \subset \text{Disc}$, the probability of a generated point landing in $S$ equals $\frac{\text{Area}(S)}{\pi R^2}$.

---

## 3. Step-by-Step Worked Execution

We trace $R = 1.0, x_c = 0.0, y_c = 0.0$:

---

### Step 1: Draw Area and Angle Uniform Variables
- Draw area fraction $u \in [0, 1)$. Suppose $u = 0.25$.
- Draw angle fraction $v \in [0, 1)$. Suppose $v = 0.5$.

---

### Step 2: Compute Radial Distance
Apply the square-root inverse CDF transformation:
$$
r = R \sqrt{u} = 1.0 \times \sqrt{0.25} = \mathbf{0.5}
$$
Notice that even though $u = 0.25$ is only 25% of the total area, $r = 0.5$ is 50% of the radius. This correctly accounts for the quadratic scaling of area with radius.

---

### Step 3: Compute Angle
Map $v$ to radians:
$$
\theta = v \times 2\pi = 0.5 \times 2\pi = \pi \quad (180^\circ)
$$

---

### Step 4: Map to Cartesian Coordinates
$$
x = x_c + r \cos(\theta) = 0.0 + 0.5 \cos(\pi) = 0.0 + 0.5(-1) = \mathbf{-0.5}
$$
$$
y = y_c + r \sin(\theta) = 0.0 + 0.5 \sin(\pi) = 0.0 + 0.5(0) = \mathbf{0.0}
$$
Point generated: **$(-0.5, 0.0)$**.
Distance squared: $(-0.5)^2 + 0.0^2 = 0.25 \le 1.0^2$ (Strictly inside the circle).

---

## 4. Complete Execution Trace

| Trial | Uniform $u$ | Radial Distance $r = R\sqrt{u}$ | Uniform $v$ | Angle $\theta = 2\pi v$ | $\cos(\theta), \sin(\theta)$ | Cartesian Coordinate $(x, y)$ | Distance to Center |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | $0.00$ | $0.0$ | $0.00$ | $0$ | $(1, 0)$ | **$(0.0, 0.0)$** | $0.0 \le 1.0$ |
| **2** | $0.25$ | $0.5$ | $0.00$ | $0$ | $(1, 0)$ | **$(0.5, 0.0)$** | $0.5 \le 1.0$ |
| **3** | $0.25$ | $0.5$ | $0.50$ | $\pi$ | $(-1, 0)$ | **$(-0.5, 0.0)$** | $0.5 \le 1.0$ |
| **4** | $1.00$ | $1.0$ | $0.25$ | $\pi / 2$ | $(0, 1)$ | **$(0.0, 1.0)$** | $1.0 \le 1.0$ |
| **5** | $0.64$ | $0.8$ | $0.125$| $\pi / 4$ | $(\frac{\sqrt{2}}{2}, \frac{\sqrt{2}}{2})$ | **$(0.566, 0.566)$** | $0.8 \le 1.0$ |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Radius ($u = 0$):** Produces the center point $(x_c, y_c)$ directly.
- **Maximum Boundary ($u \to 1$):** Produces points lying directly on the circular perimeter.
- **Translated Center ($x_c = 10, y_c = -5$):** Vector addition translates the origin without altering radial or angular distributions.
- **Zero Radius ($R = 0$):** Returns center $(x_c, y_c)$ with probability 1.

---

## 6. Traps & Common Anti-Patterns

- **Linear Radius Sampling ($r = R \cdot u$):** The most common mistake in 2D random geometry. A linear radius over-samples the center by a factor of $\frac{1}{r}$, completely failing uniformity statistical tests (chi-square or Kolmogorov-Smirnov).
- **Angle in Degrees Instead of Radians:** Calling `math.cos(degree)` with degrees $[0, 360)$ produces invalid coordinates because standard trigonometric functions expect radians $[0, 2\pi)$.
- **Rejection Sampling vs Inverse Transform:** Rejection sampling in the bounding box $[-R, R] \times [-R, R]$ also produces uniform points, but has unbounded worst-case runtime (though expected calls is $4/\pi \approx 1.27$). Inverse transform sampling is deterministic $O(1)$ with zero rejected draws.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Generating two uniform random numbers takes $O(1)$ time.
  - Computing square root and trigonometric functions takes $O(1)$ hardware math operations.
  - Total Time: $\mathcal{O}(1)$ deterministic per call.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ using scalar floating-point variables.
