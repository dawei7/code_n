## General

**Maintain frequency and ordered uniqueness as separate facts**

The data structure must answer two questions:

1. Is a value currently unique?
2. Among unique values, which one entered the queue earliest?

A frequency map answers the first. An insertion-ordered mapping containing only currently unique values answers the second.

The implementation stores:

- `self.cnt`, a Counter of every value's total occurrences.
- `self.unique`, an OrderedDict whose keys are exactly values with frequency one, in their original insertion order.

The OrderedDict values are all the dummy value 1. Only key presence and key order matter, so it is being used as an ordered set.

**Build constructor state in two passes**

```python
self.cnt = Counter(nums)
```

first counts the complete initial queue. This makes it possible to know immediately which values occur exactly once.

Then:

```python
self.unique = OrderedDict(
    {v: 1 for v in nums if self.cnt[v] == 1}
)
```

iterates the original sequence from left to right and includes only frequency-one values. Python dictionaries preserve insertion order, and OrderedDict explicitly maintains it. Thus the first key is the earliest unique number in the initial queue.

A value with frequency greater than one is never inserted, even at its first occurrence, because the Counter already knows the completed initial frequency. A truly unique value appears only once in `nums`, so it creates exactly one key.

**Return the first key without removing it**

`showFirstUnique` is:

```python
return -1 if not self.unique else next(
    v for v in self.unique.keys()
)
```

An empty OrderedDict means no currently unique value exists, so -1 is returned.

Otherwise, iteration over `self.unique.keys()` follows insertion order, and `next` returns its first key. The method does not pop that key. Showing a value does not remove it from the conceptual queue and does not change its frequency, so later calls may return the same number.

**Adding a value has only three cases**

Every `add(value)` begins with:

```python
self.cnt[value] += 1
```

Counter returns zero for an unseen key, so its first occurrence becomes one.

If the new count is one:

```python
self.unique[value] = 1
```

the value has just appeared for the first time. It is unique and is appended at the end of OrderedDict order, matching its arrival at the back of the queue.

If the count is at least two and the value is still in `self.unique`, it has just lost uniqueness:

```python
self.unique.pop(value)
```

OrderedDict can remove a key directly without scanning from the front. Removing it immediately ensures `showFirstUnique` never has to skip stale nonunique entries.

If the count exceeds two, the value was already removed on its second occurrence. The membership test fails and no ordered-state change is needed. Since the structure supports additions only, a duplicate value can never become unique again.

**Trace the first example**

Initialization with `[2,3,5]` gives counts of one for all three and ordered unique keys `[2,3,5]`. Showing returns 2.

- Adding 5 changes its count to two and removes key 5. Order is `[2,3]`; showing still returns 2.
- Adding 2 changes its count to two and removes key 2. Order is `[3]`; showing returns 3.
- Adding 3 changes its count to two and removes key 3. The ordered set is empty; showing returns -1.

The original queue still conceptually contains all added values. The implementation does not need to store every occurrence in queue form because frequency and unique arrival order are sufficient for all supported operations.

**Why values, rather than occurrences, can be keys**

A value is eligible only when its global current frequency is exactly one. In that situation, it has exactly one occurrence, so using the value as the ordered key unambiguously represents that occurrence's position. Once a second copy arrives, neither occurrence is unique and the key is removed.

**Why the invariants prove correctness**

After construction, Counter has exact frequencies and OrderedDict contains exactly frequency-one values in queue order. An addition updates the exact frequency, inserts a newly unique first occurrence at the back, or removes a value precisely when its second occurrence arrives. Later duplicates require no change.

Therefore, after every operation, `self.unique` contains all and only unique values in their queue order. Its first key is exactly the first unique number, and emptiness exactly means none exists.

## Complexity detail

Let $n$ be the initial list length and $q$ the number of later operations. Construction counts and scans the initial values in $O(n)$ expected time. Each `add` performs a constant number of expected $O(1)$ hash and OrderedDict operations. `showFirstUnique` checks emptiness and obtains the first iterator item in $O(1)$ time.

Across construction and $q$ operations, total expected time is $O(n+q)$. The Counter stores each distinct value ever seen, and OrderedDict stores a subset of those values, so space is $O(n+q)$ in the worst case.

## Alternatives and edge cases

- **Queue plus status map:** Enqueue first occurrences and lazily remove stale duplicates from the front during show. Operations are $O(1)$ amortized but one show call may perform several removals.
- **Scan the complete queue on every show:** Count or check each value repeatedly. This can be linear or quadratic per query and wastes prior frequency work.
- **Plain unordered set:** It tracks uniqueness but cannot identify which unique value appeared first.
- **Linked hash set:** In languages that provide one, it directly supports ordered keys with constant-time insertion and removal, analogous to OrderedDict.
- **All initial values duplicated:** `self.unique` starts empty and show returns -1.
- **One initial value:** It is returned until the same value is added again.
- **Third and later occurrence:** The key is already absent, so only Counter changes.
- **A new value after no uniques remain:** Its count becomes one, it enters the ordered mapping, and it becomes the first unique.
- **Show does not consume:** Repeated show calls without additions return the same first value.
- **Arrival order:** Removing an earlier key does not disturb the relative order of remaining keys.
