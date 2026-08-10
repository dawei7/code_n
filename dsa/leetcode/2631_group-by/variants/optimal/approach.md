## General

**One callback result chooses one output bucket**

For every source item $x$, callback `fn(x)` returns the string key of the group that should contain $x$.

The result is an object whose relationship is:

$$
\texttt{groups[key]}
=
\text{all source items whose callback result is }\texttt{key}.
$$

The solution constructs this relationship in one left-to-right pass. It does not need to know all possible keys in advance.

**Attach one shared method to arrays**

The implementation defines `Array.prototype.groupBy` as a normal function. Any ordinary array can find this method through its prototype chain.

When called as `array.groupBy(fn)`, the normal function receives the array as `this`. An arrow function would not work reliably because it would capture lexical `this` rather than the receiver.

The method reads source items and returns a separate grouping object. It never reorders or mutates the source array.

**Create a bucket on first use**

`groups` begins as an empty object. For each `item`:

1. evaluate `const key = fn(item)`;
2. determine whether `groups` already has its own property for that key;
3. create an empty array if this is the first occurrence;
4. append `item` to the bucket.

The callback is invoked exactly once per source item. Its result is reused for the membership check and lookup rather than recomputed.

**Why “own property” matters**

Ordinary objects inherit properties such as `toString` and a special historical accessor named `__proto__` from `Object.prototype`.

A test such as `if (!groups[key])` can be wrong:

- an inherited property may appear even though no group was created;
- truthiness is not the same as ownership;
- assigning `groups["__proto__"] = []` can trigger prototype mutation semantics rather than create a normal data bucket.

The exact solution checks:

`Object.prototype.hasOwnProperty.call(groups, key)`.

This asks whether the result object itself already owns the group key, independent of inherited names.

**Why `Object.defineProperty` is deliberately used**

For a first occurrence, the code defines the bucket with:

`Object.defineProperty(groups, key, { value: [], enumerable: true, writable: true, configurable: true })`.

This safely creates an ordinary own data property even for key `"__proto__"`. Direct assignment to that name on a normal object could invoke the inherited prototype setter.

The descriptors also make the property behave like a usual object property:

- enumerable, so it appears in `Object.keys` and JSON-style output;
- writable, so its value could be replaced;
- configurable, so it could be redefined or deleted.

For the algorithm, only the array's mutability is needed after creation, but these flags produce the expected plain grouped object behavior.

**Appending preserves item order**

The loop is `for (const item of this)`, which visits the array from beginning to end. Whenever an item maps to key $k$, it is pushed to the end of `groups[k]`.

Suppose items for one key occur at indices:

$$
i_0<i_1<\cdots<i_r.
$$

They are appended in exactly that order, so the bucket becomes:

$$
[\texttt{this}[i_0],\texttt{this}[i_1],\ldots,\texttt{this}[i_r]].
$$

This proves the required within-group stability without sorting.

The order in which object keys appear is not required. The solution generally creates keys at their first occurrence, but correctness depends only on their buckets.

**Trace the identifier example**

For items with identifiers one, one, and two:

- the first item yields key `"1"`, so an empty bucket is defined and the item is pushed;
- the second yields `"1"` again, finds the own bucket, and appends after the first;
- the third yields `"2"`, creating a second bucket.

The result has two properties, with the two identifier-one objects retaining source order.

The objects themselves are not copied. Each bucket stores the original item reference.

**Trace a Boolean-like key**

If `fn` returns `String(n > 5)`, keys are strings `"false"` and `"true"`.

Values one through five append to the false bucket, while six through ten append to the true bucket. The key strings are ordinary property names; the algorithm does not interpret them as Boolean values.


After processing the first $i$ source elements, maintain:

> For every callback key observed in that prefix, `groups[key]` contains exactly the prefix items producing that key, in their original order; no other own group properties have been created.

The empty prefix satisfies the statement. Processing the next item computes its unique key. Creating a missing bucket establishes the correct empty history, and pushing the item extends exactly that bucket at the end. Other buckets remain unchanged.

After all elements, the invariant is precisely the requested grouped output.

**Why a one-pass construction is optimal**

Every element must be passed to `fn` because an arbitrary callback may assign it to any group. The solution makes that one necessary call and one append per item.

No preliminary key collection, sorting, or second pass is needed.

## Complexity detail

Let $n$ be the array length. The loop visits every item once. Assuming `fn` and property lookup are $O(1)$, total time is expected $O(n)$.

The bucket arrays collectively store exactly $n$ item references, and the object has at most $n$ group properties. Output space is $O(n)$. Apart from the output, only current `item` and `key` use $O(1)$ auxiliary space.

The source array remains unchanged.

## Alternatives and edge cases

- **`reduce` construction:** Can build the same object but is no more efficient and adds accumulator callback syntax.
- **Use a `Map`:** Avoids prototype-name concerns naturally, but the contract requires an object result.
- **Plain assignment for new keys:** Usually works but mishandles special names such as `__proto__` on ordinary objects.
- **Empty array:** The loop performs no callback calls and returns an empty object.
- **All items share one key:** One bucket receives every item in source order.
- **Every item has a unique key:** The result has $n$ one-element buckets.
- **Key `"toString"`:** Own-property checking distinguishes the new group from the inherited method.
- **Key `"__proto__"`:** `Object.defineProperty` safely creates a data property instead of changing the result's prototype.
- **Object or array items:** Buckets store the original references without cloning.
- **Callback order:** `fn` is called once per item from left to right.
