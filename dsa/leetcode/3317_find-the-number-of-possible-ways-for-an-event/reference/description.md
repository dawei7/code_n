### 1. Description

You are given three integers `n`, `x`, and `y`.

An event is being held for `n` performers. When a performer arrives, they are **assigned** to one of the `x` stages. All performers assigned to the **same** stage will perform together as a band, though some stages *might* remain **empty**.

After all performances are completed, the jury will **award** each band a score in the range `[1, y]`.

Return the **total** number of possible ways the event can take place.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that two events are considered to have been held **differently** if **either** of the following conditions is satisfied:

- **Any** performer is *assigned* a different stage.

- **Any** band is *awarded* a different score.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** n = 1, x = 2, y = 3

**Output:** 6

**Explanation:**

- There are 2 ways to assign a stage to the performer.

- The jury can award a score of either 1, 2, or 3 to the only band.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 5, x = 2, y = 1

**Output:** 32

**Explanation:**

- Each performer will be assigned either stage 1 or stage 2.

- All bands will be awarded a score of 1.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 3, x = 3, y = 4

**Output:** 684

</div>

### 5. Constraints

- $1 \le n, x, y \le 1000$