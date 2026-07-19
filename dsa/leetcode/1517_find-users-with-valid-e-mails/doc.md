# Find Users With Valid E-Mails

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1517 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-users-with-valid-e-mails/) |

## Problem Description
### Goal

The `Users` table stores each website account's identifier, name, and e-mail address, but some stored addresses do not satisfy the site's required format. Select every row whose `mail` value consists of a valid prefix followed by the exact domain `@leetcode.com`.

The prefix must begin with an uppercase or lowercase English letter. Every remaining prefix character, if any, must be an English letter, a digit, underscore, period, or dash. The domain is case-sensitive and must appear exactly in lowercase at the end of the address. Return all three columns for qualifying users; the source contract permits any row order.

### Function Contract
**Inputs**

Let $n$ be the number of rows and define the total number of inspected e-mail characters as

$$
S = \sum_{u \in \texttt{Users}} \lvert u.\texttt{mail} \rvert.
$$

- `Users.user_id`: An integer primary key.
- `Users.name`: A `VARCHAR(30)` account name.
- `Users.mail`: A `VARCHAR(50)` candidate e-mail address.

**Return value**

Return `user_id`, `name`, and `mail` for exactly those rows whose mail matches a letter-led prefix over the alphabet `[A-Za-z0-9_.-]` followed by the lowercase suffix `@leetcode.com`. The app-local query orders rows by `user_id` for deterministic judging.

### Examples
**Example 1**

- Input rows include `winston@leetcode.com`, `jonathanisgreat`, and `.shapo@leetcode.com`.
- Output: the row containing `winston@leetcode.com`.
- Explanation: The first address has the required prefix and domain; the second has no domain, and the third prefix starts with a period.

**Example 2**

- Input rows include `bella-@leetcode.com` and `sally.come@leetcode.com`.
- Output: both rows.
- Explanation: A dash or period is permitted after the prefix's initial letter.

**Example 3**

- Input rows include `Ada_9@leetcode.com`, `a@LEETCODE.COM`, and `quarz#2020@leetcode.com`.
- Output: only the row containing `Ada_9@leetcode.com`.
- Explanation: The domain must remain lowercase, and `#` is not an allowed prefix character.
