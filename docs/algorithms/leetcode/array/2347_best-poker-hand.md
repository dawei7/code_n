# Best Poker Hand

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2347 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [best-poker-hand](https://leetcode.com/problems/best-poker-hand/) |

## Problem Description & Examples
### Goal
Given five cards, represented by their ranks and suits, determine the strongest possible poker hand among "Flush", "Three of a Kind", "Pair", or "High Card". The task is to return a string indicating the best hand found according to the standard poker hand hierarchy.

### Function Contract
**Inputs**

- `ranks`: A list of 5 integers, where `ranks[i]` represents the rank of the i-th card. Ranks are typically in the range 1-13.
- `suits`: A list of 5 characters, where `suits[i]` represents the suit of the i-th card. Suits are represented by 'a', 'b', 'c', or 'd'.

**Return value**

A string: "Flush", "Three of a Kind", "Pair", or "High Card", corresponding to the strongest hand present in the given five cards.

### Examples
**Example 1**

- Input: `ranks = [13,2,3,1,9]`, `suits = ['a','a','a','a','a']`
- Output: `"Flush"`
- Explanation: All five cards share the same suit ('a'), which constitutes a Flush, the strongest hand in this problem's hierarchy.

**Example 2**

- Input: `ranks = [4,4,2,4,9]`, `suits = ['a','b','c','d','e']`
- Output: `"Three of a Kind"`
- Explanation: Three cards have the rank 4. Since the suits are not all identical, it's not a Flush. The next strongest hand is Three of a Kind.

**Example 3**

- Input: `ranks = [10,10,2,12,9]`, `suits = ['a','b','c','d','e']`
- Output: `"Pair"`
- Explanation: Two cards have the rank 10. It is neither a Flush nor Three of a Kind. The next strongest hand is a Pair.

**Example 4**

- Input: `ranks = [1,2,3,4,5]`, `suits = ['a','b','c','d','e']`
- Output: `"High Card"`
- Explanation: There is no Flush, Three of a Kind, or Pair. All card ranks are distinct, and suits are mixed, resulting in a High Card hand.

---

## Underlying Base Algorithm(s)
The solution primarily leverages **frequency counting** and **set operations** to efficiently determine the poker hand.
1.  **Set for Suit Check**: A `set` data structure is used to store the unique suits present in the hand. By checking the size of this set, it can be quickly determined if all five cards share the same suit (set size of 1), indicating a "Flush".
2.  **Hash Map (Frequency Counter) for Rank Check**: A hash map (or dictionary in Python, often implemented with `collections.Counter`) is employed to count the occurrences of each card rank. This frequency information is then used to identify "Three of a Kind" (any rank count of 3 or more) or "Pair" (any rank count of 2 or more). The checks are performed in the specified order of hand strength (Flush first, then Three of a Kind, then Pair). If none of these conditions are met, the hand defaults to "High Card".

---

## Complexity Analysis
- **Time Complexity**: `O(1)`
    The input size (number of cards) is fixed at 5.
    - Checking for a Flush involves iterating through 5 suits to populate a set, which is a constant time operation.
    - Counting rank frequencies involves iterating through 5 ranks and updating a hash map, also a constant time operation.
    - Iterating through the at most 5 unique rank counts in the hash map is also a constant time operation.
    Therefore, the overall time complexity is constant, as all operations are bounded by the fixed input size.
- **Space Complexity**: `O(1)`
    The auxiliary space used is for storing the set of suits (at most 4 distinct suits) and the hash map of rank frequencies (at most 5 distinct ranks). Both require a constant amount of space, independent of any variable input size (as the input size is fixed).
