# Count Artist Occurrences on Spotify Ranking List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2669 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database, Aggregation |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/) |

## Problem Description

### Goal

The `Spotify` table contains ranked tracks. Every row has a unique `id`, a `track_name`, and the `artist` credited for that occurrence. The same artist may appear on multiple rows, whether for different tracks or repeated ranked entries.

Count how many table rows belong to each artist. Return the artist name beside that count under the column name `occurrences`. Order artists by decreasing occurrence count; when two artists have equal counts, order their names in ascending lexicographic order. Every artist present in the table must appear exactly once.

### Function Contract

**Inputs**

- `Spotify`: Rows `(id, track_name, artist)`, with unique integer `id` values and text track and artist names.

**Return value**

- Return columns `artist` and `occurrences`, grouped by artist and ordered by `occurrences` descending and then `artist` ascending.

### Examples

#### Example 1

- **Input:** Two rows credit DJ Khalid, two credit Ed Sheeran, and one credits Sia.
- **Output:** `DJ Khalid, 2`; `Ed Sheeran, 2`; `Sia, 1`.
- **Explanation:** The two tied leaders are alphabetized before the artist with one occurrence.
