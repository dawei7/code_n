# Firecracker - Optimal Approach

## 1. Problem Essence & Formal Mathematical Formulation

A firecracker explodes at a height of $h = 100\text{ m}$ above level ground.
Fragments fly in all directions with initial speed $v = 20\text{ m/s}$.
Assuming constant gravitational acceleration $g = 9.81\text{ m/s}^2$ and no air resistance:
Find the volume of the region through which the fragments move before hitting the ground, rounded to $4$ decimal places.

---

## 2. The Naive Approach & Fundamental Bottlenecks

### 3D Numerical Grid Discretization
A naive approach discretizes 3D space into voxel cells and traces thousands of parabolic trajectories:
- Achieving 4 decimal places of volume accuracy requires sub-millimeter voxel resolutions with billions of grid points.
- Numerical integration introduces truncation and discretization errors.

---

## 3. Core Intuition & Mathematical Structure

### The Paraboloid of Safety (Bounding Envelope)
For projectiles launched from $(0, 0, h)$ with speed $v$ at angle $\theta$ to the horizontal:

$$
r(t) = (v \cos \theta) t, \quad z(t) = h + (v \sin \theta) t - \frac{1}{2} g t^2
$$

Eliminating $t = \frac{r}{v \cos \theta}$:

$$
z = h + r \tan \theta - \frac{g r^2}{2 v^2} (1 + \tan^2 \theta)
$$

This is a quadratic in $T = \tan \theta$:

$$
-\frac{g r^2}{2 v^2} T^2 + r T + \left( h - z - \frac{g r^2}{2 v^2} \right) = 0
$$

The envelope (bounding boundary) occurs when the discriminant $\Delta = 0$:

$$
r^2 - 4 \left( -\frac{g r^2}{2 v^2} \right) \left( h - z - \frac{g r^2}{2 v^2} \right) = 0 \iff 1 + \frac{2g}{v^2} \left( h - z - \frac{g r^2}{2 v^2} \right) = 0
$$

Solving for $z(r)$:

$$
\mathbf{z = h + \frac{v^2}{2g} - \frac{g r^2}{2 v^2}}
$$

This envelope is a **solid of revolution (circular paraboloid)** with apex at height $H = h + \frac{v^2}{2g}$ and base radius at $z = 0$ of $R = \frac{v}{g} \sqrt{v^2 + 2gh}$.

---

## 4. Rigorous Mathematical Breakthrough & Derivations

### Exact Volume of a Circular Paraboloid
The volume bounded by the paraboloid $z = H - c r^2$ from the ground $z = 0$ to its apex $z = H$ is given by the integral of circular cross-sections:

$$
V = \int_0^H \pi r^2(z) \, dz = \int_0^H \pi \frac{H - z}{c} \, dz = \frac{\pi}{2c} H^2
$$

Substituting $c = \frac{g}{2 v^2}$ and $H = h + \frac{v^2}{2g}$:

$$
\mathbf{V = \frac{\pi v^2}{g} \left( h + \frac{v^2}{2g} \right)^2}
$$

---

## 5. Concrete Step-by-Step Example Walkthrough

### Numerical Evaluation for $h = 100, v = 20, g = 9.81$:
1. $v^2 / (2g) = 400 / 19.62 \approx 20.3873598$.
2. $H = 100 + 20.3873598 = 120.3873598\text{ m}$.
3. $H^2 \approx 14\,493.1164$.
4. $\frac{\pi v^2}{g} = \frac{400 \pi}{9.81} \approx 128.09756$.
5. Volume $V = 128.09756 \times 14\,493.1164 \approx \mathbf{1\,856\,532.8455}\text{ m}^3$.

---

## 6. Implementation Architecture & Algorithmic Blueprint

### Algorithmic Execution Pipeline

| Stage | Operation | Formula Action | Complexity |
| :---: | :--- | :--- | :---: |
| **Stage 1** | **Apex Height** | $H = h + v^2 / (2g)$ | $\mathcal{O}(1)$ |
| **Stage 2** | **Paraboloid Volume** | $V = \frac{\pi v^2}{g} H^2$ | $\mathcal{O}(1)$ |
| **Stage 3** | **Formatting** | Format as 4-decimal float string `f"{V:.4f}"` | $\mathcal{O}(1)$ |

---

## 7. Mathematical Complexity & Edge Case Invariants

| Dimension | Complexity | Performance / Resource Bounds |
| :--- | :--- | :--- |
| **Time Complexity** | $\mathcal{O}(1)$ | $< 0.0001\text{ s}$ execution in pure Python |
| **Space Complexity** | $\mathcal{O}(1)$ | Scalar float arithmetic |
| **Implementation Standard** | $100\%$ Pure Python | Uses `math.pi` |

### Critical Invariants & Edge Cases Handled:
1. **Envelope Maximality:** Paraboloid of safety strictly encloses all possible launch angles $\theta \in [-\pi/2, \pi/2]$.
2. **Ground Boundary:** Truncation at $z = 0$ corresponds to ground level.
3. **Exact Constant $g = 9.81$:** Preserved with standard IEEE 754 float precision.
