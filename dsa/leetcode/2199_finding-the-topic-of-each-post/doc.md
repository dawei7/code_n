# Finding the Topic of Each Post

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2199 |
| Difficulty | Hard |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/finding-the-topic-of-each-post/) |

## Problem Description

### Goal

The `Keywords` table associates topic IDs with words that express those topics. A topic may have several keywords, and the same word may belong to several topics. The `Posts` table stores each post's ID and text, which contains only English letters and spaces.

A post has a topic when one of that topic's keywords appears as a complete word in the post, compared case-insensitively. A shared prefix is not enough: for example, `war` does not match the word `warning`.

For every post, produce its distinct matching topic IDs in ascending numeric order, joined by commas. If no keyword matches, use the literal string `Ambiguous!`. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Keywords(topic_id, word)`: `(topic_id, word)` is the composite primary key.
- `Posts(post_id, content)`: `post_id` is the primary key.

Let $p$ be the number of posts, $k$ the number of keyword rows, $L$ the maximum post length, and $t$ the number of distinct matched post-topic pairs.

**Return value**

Return one row per post with columns `post_id` and `topic`. `topic` is either the sorted comma-separated topic IDs without duplicates or `Ambiguous!`.

### Examples

**Example 1**

With keywords `(1, handball)`, `(1, football)`, `(3, WAR)`, and `(2, Vaccine)`, a post containing `football` receives topic `1`.

**Example 2**

A post containing both `war` and `handball` receives `1,3`, with topic IDs sorted and deduplicated.

**Example 3**

A post containing `warning` but none of the complete keyword words receives `Ambiguous!`; `war` is not a complete word inside `warning`.
