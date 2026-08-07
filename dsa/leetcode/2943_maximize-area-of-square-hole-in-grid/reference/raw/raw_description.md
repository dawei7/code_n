## Description

You are given the two integers, `n` and `m` and two integer arrays, `hBars` and `vBars`. The grid has `n + 2` horizontal and `m + 2` vertical bars, creating 1 x 1 unit cells. The bars are indexed starting from `1`.

You can **remove** some of the bars in `hBars` from horizontal bars and some of the bars in `vBars` from vertical bars. Note that other bars are fixed and cannot be removed.

Return an integer denoting the **maximum area** of a *square-shaped* hole in the grid, after removing some bars (possibly none).

**Example 1:**

![](images/screenshot-from-2023-11-05-22-40-25.png)

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 1, hBars = [2,3], vBars = [2]</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span>

**Explanation:**

The left image shows the initial grid formed by the bars. The horizontal bars are `[1,2,3,4]`, and the vertical bars are `[1,2,3]`.

One way to get the maximum square-shaped hole is by removing horizontal bar 2 and vertical bar 2.

</div>

**Example 2:**

![](images/screenshot-from-2023-11-04-17-01-02.png)

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 1, m = 1, hBars = [2], vBars = [2]</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span>

**Explanation:**

To get the maximum square-shaped hole, we remove horizontal bar 2 and vertical bar 2.

</div>

**Example 3:**

![](images/unsaved-image-2.png)

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">n = 2, m = 3, hBars = [2,3], vBars = [2,4]</span>

**Output: **<span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span>

**Explanation:**

<span style="color: var(--text-secondary); font-size: 0.875rem;">One way to get the maximum square-shaped hole is by removing horizontal bar 3, and vertical bar 4.</span>

</div>

**Constraints:**

	- `1 <= n <= 10^9`

	- `1 <= m <= 10^9`

	- `1 <= hBars.length <= 100`

	- `2 <= hBars[i] <= n + 1`

	- `1 <= vBars.length <= 100`

	- `2 <= vBars[i] <= m + 1`

	- All values in `hBars` are distinct.

	- All values in `vBars` are distinct.
