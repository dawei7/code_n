# Filter Restaurants by Vegan-Friendly, Price and Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1333 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/) |

## Problem Description
### Goal
Each row of `restaurants` describes one restaurant as `[id, rating, veganFriendly, price, distance]`. Select only records that satisfy the requested dietary, price, and distance filters.

The price and distance limits are inclusive. When the input flag `veganFriendly` is 1, a selected record must also have its own vegan-friendly field set to 1; when the flag is 0, either kind of restaurant is permitted.

Return the selected restaurant IDs ordered by decreasing rating. If two selected restaurants have equal ratings, put the larger ID first.

### Function Contract
**Inputs**

- `restaurants`: an array of $n$ five-integer records, where $1\le n\le10^4$. In each record, the distinct ID, rating, price, and distance are between 1 and $10^5$, and the vegan-friendly field is 0 or 1.
- `vegan_friendly`: either 0 to allow every restaurant or 1 to require a vegan-friendly record.
- `max_price`: an inclusive price limit between 1 and $10^5$.
- `max_distance`: an inclusive distance limit between 1 and $10^5$.

**Return value**

The IDs of all qualifying restaurants, sorted by rating descending and then ID descending.

### Examples
**Example 1**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 1`, `max_price = 50`, `max_distance = 10`
- Output: `[3,1,5]`

**Example 2**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 0`, `max_price = 50`, `max_distance = 10`
- Output: `[4,3,2,1,5]`

**Example 3**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 0`, `max_price = 30`, `max_distance = 3`
- Output: `[4,5]`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Filter before ordering**

Scan each record once. Reject it when its price exceeds `max_price`, its distance exceeds `max_distance`, or the caller requires vegan-friendly choices and the record's flag is 0. Store only the pair `(rating, id)` for every remaining record.

Sort these pairs in reverse lexicographic order. Python compares the rating first and the ID second, so reversing the pair order implements both required descending keys without a custom comparator. Project the sorted pairs to their IDs for the result.

Every returned ID passed all three filters because pairs are appended only after the checks. Conversely, every qualifying record is appended. The pair ordering then places a higher rating first and uses the higher ID exactly when ratings tie, so the output satisfies the complete ordering contract.

#### Complexity detail

Let $k$ be the number of qualifying restaurants. Filtering costs $O(n)$ time and sorting costs $O(k\log k)$, bounded by $O(n\log n)$. The filtered pairs and returned IDs require $O(k)$ space, bounded by $O(n)$.

#### Alternatives and edge cases

- **Sort every record first:** Sorting all $n$ records and filtering afterward is correct but may perform unnecessary comparisons when few records qualify.
- **Selection sort:** Repeatedly choosing the best remaining qualifying record avoids relying on a library sort but takes $O(k^2)$ time.
- **No qualifying restaurant:** Return an empty array.
- **Inclusive limits:** A restaurant whose price or distance equals its corresponding maximum remains eligible.
- **Vegan flag disabled:** A value of 0 does not require non-vegan restaurants; it permits both flag values.
- **Equal ratings:** Compare IDs descending rather than preserving input order.

</details>
