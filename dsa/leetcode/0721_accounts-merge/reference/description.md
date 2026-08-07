## Description

Given a list of `accounts` where each element $\text{accounts}[i]$ is a list of strings, where the first element $\text{accounts}[i][0]$ is a name, and the rest of the elements are **emails** representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails **in sorted order**. The accounts themselves can be returned in **any order**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $accounts = [["John","johnsmith@\text{mail.com}","\text{john}_{newyork}@\text{mail.com}"],["John","johnsmith@\text{mail.com}","john00@\text{mail.com}"],["Mary","mary@\text{mail.com}"],["John","johnnybravo@\text{mail.com}"]]$
- **Output:** `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
- **Explanation:**
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
#### Example 2

- **Input:** $accounts = [["Gabe","Gabe0@\text{m.co}","Gabe3@\text{m.co}","Gabe1@\text{m.co}"],["Kevin","Kevin3@\text{m.co}","Kevin5@\text{m.co}","Kevin0@\text{m.co}"],["Ethan","Ethan5@\text{m.co}","Ethan4@\text{m.co}","Ethan0@\text{m.co}"],["Hanzo","Hanzo3@\text{m.co}","Hanzo1@\text{m.co}","Hanzo0@\text{m.co}"],["Fern","Fern5@\text{m.co}","Fern1@\text{m.co}","Fern0@\text{m.co}"]]$
- **Output:** `[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]`
### Constraints

- $1 \le \text{accounts.length} \le 1000$

- $2 \le \text{accounts}[i].length \le 10$

- $1 \le \text{accounts}[i][j].length \le 30$

- $\text{accounts}[i][0]$ consists of English letters.

- $\text{accounts}[i][j] (for j > 0)$ is a valid email.