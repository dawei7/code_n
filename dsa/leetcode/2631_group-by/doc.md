# Group By

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2631 |
| Difficulty | Medium |
| Category | JavaScript |
| Topics | Uncategorized |
| Supported Languages | javascript |
| Official Link | [LeetCode](https://leetcode.com/problems/group-by/) |

## Problem Description

### Goal

Enhance every JavaScript array with an `array.groupBy(fn)` method. Calling the method must partition the array's items according to a selector function and return the groups as an object.

For each element `arr[i]`, the callback `fn` produces a string key. The returned object's value at that key is an array containing every original item that generated the key. Items within each group must retain their relative order from the source array; the order in which the object's keys appear is irrelevant.

The array may contain values of any type. Implement the grouping behavior directly without using Lodash's `_.groupBy` helper.

### Function Contract

**Inputs**

- `fn`: A callback that accepts one array item and returns a string key.

The method receiver is an array of length $n$, where $0 \le n \le 10^5$.

For the app-local serializable adapter, `array` supplies the receiver values and `fnName` selects an authored callback. Benchmarks may use a `distinctRange` array plan instead of listing every value.

**Return value**

Return an object mapping every produced string key to the source items assigned to that key, in their original relative order. An empty receiver produces an empty object.

### Examples

**Example 1**

- Input: `array = [{"id":"1"}, {"id":"1"}, {"id":"2"}]`, `fn = item => item.id`
- Output: `{"1":[{"id":"1"},{"id":"1"}],"2":[{"id":"2"}]}`
- Explanation: The two items whose `id` is `"1"` share one group, and the remaining item belongs to key `"2"`.

**Example 2**

- Input: `array = [[1,2,3], [1,3,5], [1,5,9]]`, `fn = list => String(list[0])`
- Output: `{"1":[[1,2,3],[1,3,5],[1,5,9]]}`
- Explanation: Every nested array has the same first element, so all three remain together in one group.

**Example 3**

- Input: `array = [1,2,3,4,5,6,7,8,9,10]`, `fn = n => String(n > 5)`
- Output: `{"false":[1,2,3,4,5],"true":[6,7,8,9,10]}`
- Explanation: The selector separates values according to whether they exceed five.
