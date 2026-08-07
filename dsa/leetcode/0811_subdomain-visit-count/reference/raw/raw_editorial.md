[TOC]

---
### Approach 1: Hash Map

The algorithm is straightforward: we just do what the problem statement tells us to do.

For an address like `a.b.c`, we will count `a.b.c`, `b.c`, and `c`.  For an address like `x.y`, we will count `x.y` and `y`.

To count these strings, we will use a hash map.  To split the strings into the required pieces, we will use library `split` functions.


```python
class Solution(object):
    def subdomainVisits(self, cpdomains):
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in xrange(len(frags)):
                ans[".".join(frags[i:])] += count

        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]
```


#### Complexity Analysis

Let $n$ be the number of domain strings in the input array `cpdomains`, and $m$ be the maximum number of fragments in any domain.

- Time complexity: $O(n \cdot m)$

    The outer loop iterates over each string in `cpdomains`, which takes $O(n)$ time. For each string, `split("\\s+")` is used to separate the count from the domain name, which takes $O(1)$ time. Then, `split("\\.")` is used to split the domain into fragments. The number of fragments is proportional to $m$ (e.g., "mail.google.com" splits into 3 parts). This splitting takes $O(m)$ time.
    
    The inner loop constructs subdomains by iterating over the fragments in reverse order. For each subdomain, it updates the count in the map, which also takes $O(m)$ time since updating and retrieving from the `HashMap` is $O(1)$.
    
    Therefore, the total time for each domain string is $O(m)$, and for all $n$ domain strings, the overall time complexity is $O(n \cdot m)$.

- Space complexity: $O(n \cdot m)$

    The `counts` map stores up to $O(n \cdot m)$ subdomains because, for each domain in `cpdomains`, there can be up to $m$ subdomains.

    The `ans` stores at most $O(n \cdot m)$ results, as each subdomain and its associated count is stored as a string.

    The temporary arrays `cpinfo` and `frags` each take $O(m)$ space for each iteration, but they are not cumulative since they are overwritten in each iteration.

    Therefore, the total space complexity is $O(n \cdot m)$.