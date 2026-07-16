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

### Required Complexity

- **Time:** $O(S + n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Describe the whole address, not merely its suffix**

The verified MySQL query uses one anchored, case-sensitive regular expression. `^` fixes the match at the beginning, `[A-Za-z]` requires the first prefix character to be a letter, and `[A-Za-z0-9_.-]*` permits exactly the remaining prefix alphabet. The literal suffix `@leetcode[.]com` then consumes the rest of the address, and `$` prevents trailing characters.

Case sensitivity is material. Without it, a database collation may treat `@LEETCODE.COM` as equal to the required lowercase domain even though the contract rejects that address. The native predicate therefore requests case-sensitive matching explicitly.

**Express the same contract in SQLite**

The app-local engine uses SQLite, whose built-in `GLOB` matching is case-sensitive. The first condition requires a leading letter and the exact lowercase terminal suffix. Because a glob `*` can otherwise consume arbitrary characters, a second condition isolates the prefix with `substr(mail, 1, length(mail) - 13)` and rejects it if it contains any character outside `[A-Za-z0-9_.-]`.

Together, the two conditions are equivalent to the accepted regular expression: the first proves a nonempty letter-led prefix and exact domain placement; the second proves every prefix character belongs to the permitted alphabet. Selecting the original columns preserves the qualifying rows without transformation.

#### Complexity detail

Each predicate inspects a mail value in time proportional to its length, using $O(S)$ filtering time across the table. The native query may return rows in any order. The app-local query adds deterministic ordering, which gives the conservative total bound $O(S + n\log n)$; an engine that can scan the integer primary key in order may avoid an explicit sort.

Filtering itself needs only constant-sized pattern and substring state. The deterministic sort may retain up to $n$ qualifying rows, so the conservative auxiliary-space bound is $O(n)$, excluding the returned table.

#### Alternatives and edge cases

- **Suffix-only `LIKE`:** `mail LIKE '%@leetcode.com'` accepts prefixes beginning with digits or punctuation and permits forbidden characters, so it is insufficient alone.
- **Case-insensitive regular expression:** relying on a default collation may incorrectly accept uppercase or mixed-case domains; force case-sensitive matching.
- **Character-by-character conditions:** a recursive CTE can validate every prefix position but is more complicated and may add avoidable overhead.
- **Minimal prefix:** `a@leetcode.com` is valid because one initial letter is enough and the remaining-prefix repetition may be empty.
- **Allowed punctuation:** underscore, period, and dash are permitted only after the first prefix letter.
- **Forbidden punctuation:** characters such as `#`, `+`, spaces, and a second `@` invalidate the prefix.
- **Lookalike suffix:** missing dots, extra trailing text, subdomains, and different domains must fail even if they contain the word `leetcode`.
- **Domain case:** `@LEETCODE.COM` and other case variants are invalid.

</details>
