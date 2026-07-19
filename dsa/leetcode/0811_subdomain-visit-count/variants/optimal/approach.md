## General
**Extract the count and full domain**

Split each input once at the space, parse the visit count, and add it to a hash counter under the full domain.

**Walk through suffix boundaries**

After counting the current domain, find its first dot and discard the leading label. Count that suffix, then repeat until no dot remains. For `discuss.leetcode.com`, this visits exactly `discuss.leetcode.com`, `leetcode.com`, and `com`.

Every reported visit to a full domain is also a visit to each suffix beginning at a label boundary, and the loop adds its count to all and only those names. Summing contributions in the counter therefore yields the exact aggregate for every distinct subdomain. Formatting each counter entry produces the required result, with order intentionally irrelevant.

## Complexity detail
Let `c` be the total number of characters across the input. Each domain has only the bounded label structure from the problem contract, so parsing its suffixes and hashing them takes $O(c)$ expected time overall. Stored distinct suffix strings and counts use $O(c)$ space.

## Alternatives and edge cases
- **Split labels then join suffixes:** Build `labels[i:]` for every position; this is straightforward and has the same bound under the limited domain depth.
- **Sort all contributions:** Emit every `(subdomain, count)` pair, sort by subdomain, and combine adjacent matches; hashing avoids the $O(k \log k)$ ordering step.
- **Linear list aggregation:** Searching a growing result list for every suffix is correct but can take $O(k^2)$ comparisons for `k` distinct subdomains.
- **Repeated input domain:** Counts must add rather than overwrite.
- **Top-level domain:** With no dot, it contributes only to itself.
- **Shared parent:** Unrelated full domains may still aggregate under the same suffix.
- **Output order:** Do not rely on a particular hash-table traversal order.
