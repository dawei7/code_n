# Angle Between Hands of a Clock

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1344 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/angle-between-hands-of-a-clock/) |

## Problem Description

### Goal

An analog clock is showing the time described by an integer `hour` and an integer `minutes`. The hour hand moves continuously as the minutes advance; it is not restricted to the numbered hour marks. The minute hand points to the position for the given whole minute.

Return the smaller angle, measured in degrees, between the two hands. Either direction around the clock may describe an angle between them, so the requested result is never greater than $180$ degrees. Floating-point answers within $10^{-5}$ of the exact value are accepted.

### Function Contract

**Inputs**

- `hour`: an integer from $1$ through $12$.
- `minutes`: an integer from $0$ through $59$.

**Return value**

- Return the smaller nonnegative angle in degrees between the hour and minute hands.

### Examples

**Example 1**

- Input: `hour = 12, minutes = 30`
- Output: `165.0`
- Explanation: The minute hand is at $180$ degrees while the hour hand has advanced to $15$ degrees.

**Example 2**

- Input: `hour = 3, minutes = 30`
- Output: `75.0`

**Example 3**

- Input: `hour = 3, minutes = 15`
- Output: `7.5`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Convert both hands to positions on one circle.** A full turn contains $360$ degrees and twelve hour marks, so adjacent hour marks are $30$ degrees apart. The hour hand also advances by half a degree per minute. Its position is therefore `(hour % 12) * 30 + minutes * 0.5`; the remainder maps twelve o'clock to zero degrees without changing its physical position.

There are sixty minute marks, so the minute hand's position is `minutes * 6`. Let the absolute difference of these two positions be `difference`. This describes one route between the hands. The route in the opposite direction measures `360 - difference`, and `min(difference, 360 - difference)` is exactly the requested smaller angle.

#### Complexity detail

The method performs a fixed number of arithmetic operations regardless of the displayed time, so it uses $O(1)$ time and $O(1)$ auxiliary space. The complete legal domain has only $12 \cdot 60 = 720$ times; the bounded-domain certificate replaces an artificial runtime-scaling benchmark with exhaustive comparison against an independent exact-arithmetic oracle.

#### Alternatives and edge cases

- **Relative angular speed:** Starting from the hour mark, compute the hands' relative displacement using $5.5$ degrees per minute. This is equivalent but still needs normalization to the smaller circular angle.
- **Discrete hour hand:** Treating the hour hand as fixed on an hour mark is incorrect because it moves continuously throughout the hour.
- **Twelve o'clock:** Applying `hour % 12` makes `12` and `0` share the same angular origin.
- **Opposite hands:** A raw difference of $180$ degrees is already the smaller angle and must remain $180$.
- **Near the wraparound:** Times close to twelve can have positions near both $0$ and $360$ degrees; taking the complementary angle handles this boundary.

</details>
