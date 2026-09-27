# Guided Example: JSON Deep Equal

## 1. The instance and the verdict to derive

A comparison is **deeply equal** when two values agree all the way down their JSON structure: primitives must pass the strict equality check, arrays must hold the same elements in the same order, and objects must expose the same keys with deeply equal values. Both inputs are guaranteed to be the output of parsing JSON text, so they are acyclic trees built from `null`, booleans, numbers, strings, arrays, and objects.

The instance traced here is a pair whose outer shapes agree everywhere and whose only disagreement sits at the deepest leaf:

- $o1 = \{\texttt{"x"}: \texttt{null}, \texttt{"L"}: [1, 2, 3]\}$
- $o2 = \{\texttt{"x"}: \texttt{null}, \texttt{"L"}: [\texttt{"1"}, \texttt{"2"}, \texttt{"3"}]\}$
- required answer: `false`

This pair is worth tracing because nothing at the top level is wrong. The key sets are identical, both values under the key `x` are `null`, and the arrays under the key `L` have the same length. Only the *type* of the array elements differs, and the lesson must show how a verdict formed at one leaf travels back to the root. The statement bounds the work: each serialized input satisfies $1 \le \lvert \text{JSON.stringify}(o1) \rvert \le 10^{5}$ and the same for $o2$, with $maxNestingDepth \le 1000$.

## 2. The decision taken at one pair of nodes

Let $E(u, v)$ denote the verdict for a pair of JSON values. The whole method is the observation that $E$ decomposes into five disjoint cases, and every case shrinks the problem to strictly smaller sub-pairs or terminates:

| Shape of the pair $(u, v)$ | Verdict | Why this case is decided on the spot |
|---|---|---|
| $u$ and $v$ are the identical primitive or the same `null` | true | strict equality already certifies agreement; this also covers equal strings, equal numbers, and `null` against `null` |
| exactly one side is `null`, or exactly one side is not an object | false | a primitive can never be deeply equal to a structure, and different primitive values fail strict equality |
| both are objects but exactly one of them is an array | false | an array and an object are different shapes even when their index-like keys coincide |
| both are arrays | same length, then element-wise $E$ at every index | arrays inherit equality from position-aligned elements, so the order of positions must be preserved |
| both are non-array objects | the same number of own keys, then every key of $u$ must exist in $v$ with $E$ holding on its values | object equality is keyed, not positional, so key *order* carries no meaning while key *membership* does |

Two properties of this table decide the instance. First, the array and object branches are reached only after the shape test, so the numeric keys of an object never masquerade as array indices. Second, the object branch compares key *sets*, never key sequences, which is why `{"y": 2, "x": 1}` and `{"x": 1, "y": 2}` are the same value.

## 3. Step-by-step trace of the instance

The comparison descends depth-first. Each row is one visited pair, and the verdict of a parent waits on its children.

| Step | Pair under comparison | Shape test outcome | Decision | Result |
|---|---|---|---|---|
| 1 | the two roots | both are non-array objects with the two own keys `x` and `L` | recurse into each key of $o1$, checking membership in $o2$ first | pending |
| 2 | the values under `x`: `null` against `null` | identical primitives | accepted by strict equality | true |
| 3 | the values under `L`: `[1, 2, 3]` against `["1", "2", "3"]` | both arrays of length 3 | lengths agree, so compare index by index | pending |
| 4 | index 0: `1` against `"1"` | not identical; neither side is an object | a number and a string fail strict equality, and no coercion is applied | false |
| 5 | indices 1 and 2 | never reached | the failing child already forces the array, and therefore the root, to be unequal | not visited |

The failure at step 4 is the only disagreement in the entire structure, and it is enough. The array comparison at step 3 returns false, and the root's keyed comparison at step 1 returns false because the value associated with `L` is not deeply equal.

```text
root (objects: keys x, L)
  |-- key x : null  vs  null                      -> true
  |-- key L : arrays of length 3                  -> needs all indices
        |-- index 0 : 1  vs  "1"                  -> false
        |-- index 1 : not visited (short circuit)
        |-- index 2 : not visited (short circuit)
  root verdict: false
```

The same descent also explains the positive case. When two structures are deeply equal, every visited pair returns true, every array length matches, and every key of the first object is found in the second; the root then reports true without any special handling.

## 4. Correctness of the recursion: soundness, completeness, termination

**Soundness.** Whenever a pair is accepted, the acceptance is backed by a finite derivation: an identity witness, or equal array lengths together with a witness for each index, or matching key sets together with a witness for each key. Structural induction on the height of the pair builds a full derivation of deep equality from these local witnesses, so an accepted pair really is deeply equal.

**Completeness.** Suppose two values are deeply equal. If they are primitives they are identical, which the first case accepts. If they are arrays, deep equality forces the same length and deeply equal elements at every index, which is exactly the array branch. If they are objects, deep equality forces the same key set and deeply equal values per key, which is exactly the object branch. Every necessary condition therefore passes, so the method cannot reject a pair that is genuinely equal. Conversely, a rejection always names a violated necessary condition — unequal length, a missing key, or a non-equal primitive — so no equal pair is rejected and no unequal pair is accepted.

**Termination and well-foundedness.** Each recursive call replaces a pair with a pair of direct children of the corresponding JSON nodes. The inputs are acyclic, because parsing JSON text cannot produce a cycle, and their depth is bounded by 1000, so the descent strictly decreases a well-founded measure. No visited set is needed for that reason, which is why the same subtrees may legitimately be compared twice if they appear twice.

**The traversal order does not change the verdict.** Every case is a conjunction of independent requirements, so the order in which keys and indices are visited affects only how early a false verdict is discovered. Discovering the failure at index 0 rather than at index 2 changes the number of visited pairs, not the answer.

## 5. Boundary and trap analysis

| Instance pair | Verdict | The trap it exposes |
|---|---|---|
| `{"y": 2, "x": 1}` against `{"x": 1, "y": 2}` | true | key order is not part of a JSON object's identity; a positional comparison of key sequences would wrongly reject it |
| `{"0": 1}` against `[1]` | false | an object whose keys look like indices is still an object; only the shape test keeps the two branches apart |
| `null` against `{}` | false | `null` is a primitive here, not an empty object, and it is not interchangeable with one |
| `{"a": 1, "b": 2}` against `{"a": 1, "c": 2}` | false | equal key *counts* prove nothing; each key of the first side must be present on the second |
| `{"items": [1, {"v": 2}, 3]}` against `{"items": [1, 3, {"v": 2}]}` | false | arrays are compared position by position, so a permutation of the same elements is a different array |
| `{"array": [], "object": {}}` against `{"object": {}, "array": []}` | true | empty structures are equal regardless of key order, and the recursion must handle a zero-length element list without a special branch |
| `true` against `false` | false | distinct booleans are distinct primitives; there is no notion of a structurally equal pair of different primitives |
| `1` against `"1"` | false | equality is strict, so a numeric value and its textual form are different values even though they print alike |

## 6. Alternatives this instance eliminates

| Alternative | Behaviour on this instance | Why it is eliminated |
|---|---|---|
| Comparing serialized text | produces different text for `{"y": 2, "x": 1}` and `{"x": 1, "y": 2}`, so it reports false for a pair that is deeply equal | serialization preserves key order, which JSON identity does not |
| Matching on the number of keys only | accepts `{"a": 1, "b": 2}` against `{"a": 1, "c": 2}` | key membership, not key count, is the requirement |
| Loose equality for primitives | accepts `1` against `"1"` and would accept the traced instance | value coercion is not part of the specification, which asks for the strict check |
| Treating arrays as ordinary objects | makes `[1]` equal to `{"0": 1}` and weakens the array-order requirement | an array's identity includes its length and its positional order |
| Canonical serialization with sorted keys | returns the right verdicts but must build and compare two full canonical strings | correct yet strictly more memory and no early exit; the recursive form can reject this instance after four comparisons instead of scanning both inputs |
| An explicit stack instead of recursion | same verdicts, same asymptotics | a legitimate trade-off: it removes the dependence on the runtime call stack for the depth bound of 1000, at the cost of holding the pending pairs explicitly |

## 7. Time and auxiliary space complexity

Let $S$ be the combined serialized size, that is $\lvert \text{JSON.stringify}(o1) \rvert + \lvert \text{JSON.stringify}(o2) \rvert$, and let $d = maxNestingDepth$ be the depth of the deeper value. Enumerating the own keys of an object node costs time proportional to that node's key count, and every node pair is entered at most once per visit, so the traversal performs $O(S)$ work in the worst case — reached by a deeply equal pair, where every node must be inspected. The best case is $O(1)$: the traced instance stops after the root shape test, one key match, one length test, and a single primitive comparison, because the first failing index ends the descent. There is no hashing, sorting, or canonicalization anywhere in the method.

The auxiliary space is the state of the descent. The comparison is depth-first, so only one root-to-leaf path can be pending at any moment, giving $O(d)$ stack frames, and the per-node key list held while iterating adds at most the own-key count of the nodes on that path. With $maxNestingDepth \le 1000$ and $\lvert \text{JSON.stringify}(o1) \rvert \le 10^{5}$, the retained key lists remain bounded by the input size, so the auxiliary space is $O(d)$ frames and $O(S)$ in the pathological case of a single object with a very large key list. Nothing proportional to the number of *already compared* subtrees is retained, because no memo or visited set is used.
