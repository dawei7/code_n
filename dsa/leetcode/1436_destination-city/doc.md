# Destination City

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1436 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/destination-city/) |

## Problem Description

### Goal

Each entry in `paths` is a directed trip `[from_city, to_city]`. Together, the trips form one route with no cycle: every intermediate destination is also the starting city of another trip, while the route's final city has no outgoing trip.

Return that unique destination city. The path entries may be given in any order, so their array positions do not necessarily follow the travel sequence.

### Function Contract

**Inputs**

- `paths`: an array of $n$ pairs, where $1 \le n \le 100$.
- Each pair contains two different city names, and every city name contains between 1 and 10 English letters or spaces.
- The directed paths form one chain with no loop and exactly one city that never appears as a starting city.

**Return value**

- The name of the chain's final destination city.

### Examples

**Example 1**

- Input: `paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]`
- Output: `"Sao Paulo"`

**Example 2**

- Input: `paths = [["B","C"],["D","B"],["C","A"]]`
- Output: `"A"`

**Example 3**

- Input: `paths = [["A","Z"]]`
- Output: `"Z"`
