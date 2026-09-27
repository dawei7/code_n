# Guided Example: Group By

## 1. The instance and the required grouping

Grouping adds a method to arrays that walks the receiver once and returns a plain object whose keys are the string keys produced by a selector callback and whose values are the items that produced each key. Two requirements constrain the result beyond the key-to-bucket mapping itself: every bucket must list its items in the order they appear in the source array, while the order of the keys themselves is explicitly free.

The instance traced here is the six-element array $[5, 2, 3, 8, 1, 4]$ with a selector that reports the parity of its argument:

| Index | Item | Selector verdict | Bucket the item belongs to |
|---|---|---|---|
| 0 | 5 | odd | odd |
| 1 | 2 | even | even |
| 2 | 3 | odd | odd |
| 3 | 8 | even | even |
| 4 | 1 | odd | odd |
| 5 | 4 | even | even |

The required result is therefore the object `{"odd": [5, 3, 1], "even": [2, 8, 4]}`. This instance is chosen because the two groups alternate: the first four items alone would already exercise a bucket switch, and the final two confirm that a bucket appended to early keeps its relative order even after other buckets have received items in between. A contiguous split, such as ten numbers separated at a threshold, would never test that interleaving.

The statement bounds the instance by $0 \le \text{array.length} \le 10^{5}$ and states that the callback returns a string key. The selector is applied once per item, so the number of selector evaluations is fixed at six here regardless of how the buckets are managed.

## 2. The accumulator: one pass, one bucket per key

The method needs exactly one piece of state: a lookup from key to bucket, plus the guarantee that a bucket is created the first time its key appears. The table below lists what has to be remembered and why each fact matters.

| State | Meaning | Why it is required |
|---|---|---|
| key-to-bucket lookup | one bucket per distinct key produced so far | an item must join the bucket of items that share its key |
| bucket contents | items appended in the order they were visited | the required result preserves source order inside each bucket, so a bucket behaves as a queue and never as a set |
| own-key membership | whether the lookup already owns a bucket under this key | a bucket may be empty only at the instant it is created, so membership must be determined from the lookup's own data rather than from the truthiness of what a key resolves to |

Because each item is appended to exactly one bucket as it is visited, one left-to-right pass is enough. No sorting, no second scan of the array, and no reordering of a bucket is ever needed.

## 3. Step-by-step trace of the instance

| Step | Item | Key computed | Action | `odd` bucket | `even` bucket |
|---|---|---|---|---|---|
| 1 | 5 | `"odd"` | the key is new, so its bucket is created and the item is appended | `[5]` | not created yet |
| 2 | 2 | `"even"` | the key is new, so its bucket is created and the item is appended | `[5]` | `[2]` |
| 3 | 3 | `"odd"` | the key already owns a bucket, so the item is appended without creating anything | `[5, 3]` | `[2]` |
| 4 | 8 | `"even"` | the key already owns a bucket, so the item is appended | `[5, 3]` | `[2, 8]` |
| 5 | 1 | `"odd"` | the key already owns a bucket, so the item is appended | `[5, 3, 1]` | `[2, 8]` |
| 6 | 4 | `"even"` | the key already owns a bucket, so the item is appended | `[5, 3, 1]` | `[2, 8, 4]` |

The two buckets end with exactly the required contents. Notice that step 3 appends to `odd` after step 2 touched `even`, and step 5 appends to `odd` again after two further `even` insertions: neither appending disturbs the other bucket, which is what stability means here.

```text
source order     5   2   3   8   1   4
odd bucket       5       3       1
even bucket          2       8       4
result           {"odd": [5, 3, 1], "even": [2, 8, 4]}
```

## 4. The partition and stability invariant, and why the result is correct

After the step that processes index $k$, the accumulator satisfies two claims at once:

1. **Partition.** Every item of the prefix $\text{arr}[0..k]$ lies in exactly one bucket, and it lies in the bucket whose key is the selector's verdict for that item.
2. **Stability.** Inside every bucket, the items appear in increasing order of their original index.

**Maintenance.** Step $k+1$ computes the key $v = fn(\text{arr}[k+1])$ once. If no bucket owns $v$, an empty bucket is created; either way the item is appended to the bucket for $v$. Before the step, the item was in no bucket; after it, the item is in the bucket for $v$ and in no other, so the partition claim holds for the longer prefix. The item is appended after every item already in that bucket, and all of those have smaller indices, so the bucket stays ordered by index. Buckets for other keys are untouched, and their internal order was already correct, so stability holds everywhere.

**Conclusion.** By induction over the indices, after the final step the accumulator is a partition of the whole array into buckets keyed by the selector, with each bucket in source order. That is precisely the definition of the grouped array, so the method's output is correct for every input, including inputs whose keys appear many times and inputs whose keys appear once.

**Why the key order is free but the item order is not.** The accumulator's buckets are independent queues; the order in which keys were first created has no effect on any bucket's contents, so permuting the keys of the result leaves it equally valid, which is why the statement accepts any key order. The item order inside a bucket is observable, however, and the single append-only discipline is exactly what preserves it.

## 5. Boundary and trap analysis

| Situation | Concrete input | Required result | The trap it exposes |
|---|---|---|---|
| Empty receiver | no items at all | an empty object | the pass performs no steps, so the result has no keys; no bucket may be created eagerly |
| Constant selector | `["a", "b", "c"]` with a selector that always returns the same key | one bucket holding all three items in order | a single group is not a special case; the bucket is created once and then appended to |
| A key naming a prototype accessor | `[1, 2]` with the selector returning the key `"__proto__"` | `{"__proto__": [1, 2]}` as an ordinary own key | assigning that key directly would reach the prototype's accessor instead of creating a bucket, so the bucket must be installed as an own data property |
| A key naming an inherited member | any selector returning a key such as `"toString"` or `"constructor"` | a fresh bucket for that key, holding the matching items | a truthiness test on the looked-up key would find the inherited function instead of nothing, conclude that a bucket exists, and then fail to append to it |
| Selector-controlled key typing | `[1, "1", 2, "2"]` with a selector that tags the runtime type | four buckets: `"number:1"`, `"string:1"`, `"number:2"`, `"string:2"` | the key is whatever the selector returns; equal-looking values are separated only if the selector separates them |
| Boolean verdicts | the numbers one through ten with a selector comparing against five | the keys `"true"` and `"false"` | the selector's output is stringified, so a boolean predicate yields two string keys rather than a numeric split |
| Integer-like keys | keys such as `"2"` and `"1"` alongside `"odd"` | any key order is accepted | integer-like keys are enumerated before other keys by the host's ordinary key ordering, which is one reason the statement declines to fix an order |
| All keys distinct | six items with six different keys | six buckets of one item each | bucket creation must not be confused with the number of distinct keys already seen |

## 6. Alternatives this instance eliminates

| Alternative | Behaviour on this instance | Why it is eliminated |
|---|---|---|
| Sorting the array before grouping | buckets would read `[1, 3, 5]` and `[2, 4, 8]` | sorting destroys the source order that each bucket must preserve |
| Prepending instead of appending | buckets would read `[1, 3, 5]` and `[4, 8, 2]` | the required order is the order the items appear in the array |
| Deciding membership by the truthiness of the looked-up key | would mis-handle keys that collide with inherited members, and would also treat an empty bucket as absent | a bucket's presence is a fact about the accumulator's own data, not about the value that a key happens to resolve to |
| Assigning a bucket by ordinary property assignment for every key | fails outright for a key like `"__proto__"` | such a key resolves to prototypal access instead of creating an own property, so the bucket must be defined as own data |
| Grouping by the item itself instead of by the selector's verdict | would produce one bucket per distinct item | the buckets are keyed by $fn(\text{arr}[i])$, and equal items may legitimately land in different buckets when the selector is not injective |
| Building a key-value map first and converting it at the end | same result, extra pass | correct but it allocates a second container and copies every bucket, with no gain over writing directly into the result object |

## 7. Time and auxiliary space complexity

Let $n = \text{array.length}$ and let $k$ be the number of distinct keys the selector produces. The pass touches each item exactly once: one selector evaluation, one lookup for the item's key, and one append. With an ordinary expected-$O(1)$ hash lookup, the running time is $O(n)$ expected, and it is $\Theta(n)$ selector evaluations regardless of how the buckets are stored. This is optimal in the comparison-free sense, because every item must be examined at least once to learn its key, and $n \le 10^{5}$ bounds the pass.

The auxiliary space is the accumulated result plus one running bucket reference: the buckets together hold all $n$ items, and the lookup holds $k$ bucket references, so the state is $O(n)$ overall and $O(k)$ for the key table alone. The result object is the required output rather than scratch space, and no copy of the input is made, so the method never duplicates the array itself. Per item, the additional working memory beyond the result is $O(1)$.
