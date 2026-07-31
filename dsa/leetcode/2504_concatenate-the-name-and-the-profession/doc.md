# Concatenate the Name and the Profession

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2504 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/concatenate-the-name-and-the-profession/) |

## Problem Description
### Goal
The `Person` table stores one row per person, identified by the primary key `person_id`. Each row also contains the person's `name` and a `profession` chosen from `Doctor`, `Singer`, `Actor`, `Player`, `Engineer`, or `Lawyer`.

Report every person's identifier together with a formatted name. The formatted value must place the first letter of the profession inside parentheses immediately after the complete name, with no whitespace inserted between them. For example, a singer named `Alex` becomes `Alex(S)`.

Return the rows ordered by `person_id` in descending order. Name the formatted output column `name`.

### Function Contract
**Inputs**

- `Person(person_id, name, profession)`: `person_id` is unique; `name` is a string; `profession` is one of the six allowed profession values.

Let $r$ be the number of rows in `Person`.

**Return value**

A table with columns `person_id` and `name`, containing one output row per input row in descending `person_id` order. The output `name` is the original name followed by `(`, the profession's first letter, and `)`.

### Examples
**Example 1**

- Input: `Person = [(1,"Alex","Singer"),(3,"Alice","Actor"),(2,"Bob","Player"),(4,"Messi","Doctor"),(6,"Tyson","Engineer"),(5,"Meir","Lawyer")]`
- Output: `[(6,"Tyson(E)"),(5,"Meir(L)"),(4,"Messi(D)"),(3,"Alice(A)"),(2,"Bob(P)"),(1,"Alex(S)")]`

**Example 2**

- Input: `Person = [(42,"Ava","Doctor")]`
- Output: `[(42,"Ava(D)")]`

**Example 3**

- Input: `Person = [(7,"Mary Jane","Lawyer"),(12,"Bo","Engineer")]`
- Output: `[(12,"Bo(E)"),(7,"Mary Jane(L)")]`
