# Find Longest Calls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3124 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-longest-calls/) |

## Problem Description

### Goal

The `Contacts` table identifies people by `id` and stores each person's first and last names. The `Calls` table records a contact, whether the call was `incoming` or `outgoing`, and its duration in seconds. Each call belongs to the contact whose `Contacts.id` equals its `contact_id`.

Find the three longest calls in each direction. Report the contact's `first_name`, the call `type`, and the duration converted from seconds to the fixed `HH:MM:SS` form. The final result must be sorted by `type`, raw `duration`, and `first_name`, with all three keys in descending order.

### Function Contract

**Inputs**

The query reads two tables:

- `Contacts(id, first_name, last_name)`: one row per contact; `id` is unique.
- `Calls(contact_id, type, duration)`: call records whose composite key is `(contact_id, type, duration)`. The `type` value is either `incoming` or `outgoing`, and `duration` is measured in seconds.

**Return value**

Return up to three rows for each call type with columns `first_name`, `type`, and `duration_formatted`. Format every selected duration as `HH:MM:SS`, and order the rows by `type`, duration, and first name in descending order.

### Examples

#### Example 1

- **Input:** `Contacts = [[1,"John","Doe"],[2,"Jane","Smith"],[3,"Alice","Johnson"],[4,"Michael","Brown"],[5,"Emily","Davis"]]`, `Calls = [[1,"incoming",120],[1,"outgoing",180],[2,"incoming",300],[2,"outgoing",240],[3,"incoming",150],[3,"outgoing",360],[4,"incoming",420],[4,"outgoing",200],[5,"incoming",180],[5,"outgoing",280]]`
- **Output:** `[["Alice","outgoing","00:06:00"],["Emily","outgoing","00:04:40"],["Jane","outgoing","00:04:00"],["Michael","incoming","00:07:00"],["Jane","incoming","00:05:00"],["Emily","incoming","00:03:00"]]`
- **Explanation:** The result retains the three greatest durations within each direction, then places `outgoing` before `incoming` under descending type order.
