# Find All Unique Email Domains

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3059 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-all-unique-email-domains/) |

## Problem Description

### Goal

Each row contains one lowercase email address. Its domain is the portion after
the `@` separator, and several individuals may share the same domain.

Find every distinct domain whose name ends with the exact suffix `.com`, and
count how many email rows belong to it. Domains with another ending, even if
they contain `com` elsewhere, are excluded. Return one row per qualifying
domain, ordered by the domain text ascending.

### Function Contract

**Inputs**

- `Emails(id, email)`: each unique `id` identifies one lowercase email
  address.

Let $n$ be the number of rows, $S$ the total number of characters across all
email addresses, and $g$ the number of qualifying distinct domains.

**Return value**

- An ordered table with columns `email_domain` and `count`, containing each
  qualifying `.com` domain and its number of associated individuals.

### Examples

**Example 1**

The supplied rows contain two addresses at `outlook.com` and one at
`yahoo.com`. The `.edu` and `.org` domains are ignored, so the two `.com`
domains are returned alphabetically with counts `2` and `1`.

**Example 2**

Different local parts do not create different groups: `a@site.com` and
`b@site.com` both contribute to the count for `site.com`.

**Example 3**

`shop.com.org` is excluded because the complete domain ends in `.org`, not
`.com`.
