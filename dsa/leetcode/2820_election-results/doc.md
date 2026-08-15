# Election Results

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2820 |
| Difficulty | Medium |
| Category | Database |
| Topics | Uncategorized |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/election-results/) |

## Problem Description

### Goal

The `Votes` table records the candidates selected by each voter. Every voter owns one vote. A voter who selects several candidates divides that vote equally among all of those candidates, while a row whose candidate is `NULL` represents an abstention and contributes nothing.

Add the fractional contributions received by every candidate. Return every candidate whose total is the largest; a tie may therefore produce several rows. Sort the candidate names in ascending order.

### Function Contract

**Tables**

- `Votes(voter, candidate)`: the pair `(voter, candidate)` identifies a recorded selection. A voter can have several rows, one per chosen candidate. A `NULL` candidate means that voter did not vote for anyone.

Let $R$ be the number of rows in `Votes`.

**Return value**

Return one column:

- `candidate`: the name of a candidate tied for the greatest total vote allocation.

Include all tied winners and order the rows by `candidate` ascending. Abstentions never appear as candidates.

### Examples

#### Example 1

Suppose Charles selects Ryan, Christine, and Kathy, so each receives one third of his vote. Benjamin and Arthur each give a full vote to Christine; Anthony and Edward each give a full vote to Ryan; Evelyn gives a full vote to Kathy; Kathy and Terry abstain.

Christine and Ryan each finish with $2+rac{1}{3}$ votes, ahead of Kathy's $1+rac{1}{3}$. The ordered result is:

| candidate |
|---|
| Christine |
| Ryan |

#### Example 2

If one voter chooses Alice and Bob while another voter chooses only Bob, Alice receives $rac{1}{2}$ vote and Bob receives $1+rac{1}{2}$ votes. The result contains only `Bob`.

#### Example 3

If two voters each choose both Alice and Bob, both candidates receive one vote. Return `Alice` and `Bob` in ascending order.
