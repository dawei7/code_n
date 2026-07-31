## General

**Build one canonical address per email**

Split each address at its guaranteed single `@`. For the local name, keep only
the prefix before the first `+`, remove every dot from that prefix, and convert
the result to lowercase. Convert the domain to lowercase without removing its
dots. Joining these two normalized parts with `@` produces a canonical key.

Every normalization rule is reflected in that key. Two raw addresses in the
same group therefore produce equal keys: their normalized local and domain
names match. Conversely, equal keys have equal normalized parts on both sides
of the separator, so the source definition places them in the same group.

**Deduplicate canonical keys**

Insert each key into a set. Set membership collapses all raw spellings of one
group while retaining different normalized local-domain pairs. After all
addresses have been processed, the set size is exactly the number of unique
email groups.

## Complexity detail

Let

$$
S = \sum_{e \in \texttt{emails}} \lvert e \rvert.
$$

Splitting, local-name normalization, domain lowercasing, hashing, and insertion
process $O(\lvert e \rvert)$ characters for each email under expected hash-set
behavior. The total time is $O(S)$. The canonical strings stored in the set
contain at most $S$ characters altogether, so auxiliary space is $O(S)$.

The benchmark defines size as the email count $E$ and keeps every address
short. Each normalized key is unique. The accepted set scan is therefore
linear in $E$ (and equivalently in $S$ for these fixed-length workloads), while
the correct slower control linearly searches all earlier keys before appending
each new one.

## Alternatives and edge cases

- **List of normalized addresses:** Linear membership checks preserve the
  result but take $O(E^2L)$ time for $E$ distinct emails of length $L$.
- **Compare raw addresses:** This fails to merge case variants, dotted local
  names, and plus-tag variants that normalize to the same group.
- **Remove domain dots:** Dot removal belongs only to the local name; changing
  the domain would incorrectly merge addresses such as `a@x.y.com` and
  `a@xy.com`.
- **Ignore only the plus sign:** Everything after the first `+` must be
  discarded, including later dots and additional plus signs.
- **Case conversion on one side only:** Both the local and domain names are
  normalized to lowercase.
- **Repeated raw addresses:** A set naturally keeps exact duplicates in one
  group.
- **Maximum output:** At most 1,000 input addresses exist, so the group count
  fits within the source return type.
