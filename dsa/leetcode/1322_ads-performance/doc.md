# Ads Performance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1322 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/ads-performance/) |

## Problem Description
### Goal
The `Ads` table records one user's action on one advertisement. Each action is `Clicked`, `Viewed`, or `Ignored`, and the pair `(ad_id, user_id)` is unique.

For every advertisement present in the table, calculate its click-through rate (CTR) as the number of clicks divided by the combined number of clicks and views, multiplied by 100. Ignored actions contribute to neither part of that fraction. When an advertisement has no clicks or views, its CTR is 0.

Round each CTR to two decimal places. Return `ad_id` and `ctr`, ordered by CTR descending and then by `ad_id` ascending when rates tie.

### Function Contract
**Inputs**

- `Ads(ad_id, user_id, action)`: distinct advertisement-user rows whose action is `Clicked`, `Viewed`, or `Ignored`.

Let $r$ be the number of rows and $a$ the number of distinct advertisements.

**Return value**

One row per advertisement containing its identifier and rounded percentage CTR, in the required descending-rate and ascending-identifier order.

### Examples
**Example 1**

- Input: ad 1 has two clicks, one view, and one ignored action
- Output: `(1, 66.67)`
- Explanation: Its CTR is $100\cdot2/(2+1)$.

**Example 2**

- Input: ad 5 has only ignored actions
- Output: `(5, 0.00)`
- Explanation: With no clicks or views, the defined rate is 0.

**Example 3**

- Input: one click and one view for the same ad
- Output: a CTR of `50.00`
- Explanation: One of the two counted interactions is a click.
