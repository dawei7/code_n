## General

The merge decision is local to each pair of values. First determine whether both are non-null objects and whether they are either both arrays or both non-array objects. If that compatibility test fails, the contract immediately selects the second value.

**Start from the first container**

For two compatible arrays, make a shallow copy of the first array. For two compatible objects, make a shallow copy of the first object. This preserves every key or index that appears only in `obj1` and chooses the correct result container type.

**Overlay the second container**

Visit every own enumerable key of `obj2`. If `obj1` also owns that key, recursively merge the two child values and assign the result. Otherwise, copy the second value directly. Arrays work without separate traversal logic because their enumerable keys are their populated indices and the shallow copy already retains any longer suffix from the first array.

At a primitive, null, or container-type mismatch, recursion stops with the second value. At a compatible container, every union key is either preserved from the first input, copied from the second, or recursively resolved exactly once. By induction over the JSON tree, every result position therefore follows the deep-merge rules.

## Complexity detail

Let $n$ and $m$ be the total numbers of JSON nodes and container entries in the two inputs. Each visited container is copied once and each relevant key or index is processed once, giving $O(n + m)$ time in the worst case. The result plus recursion stack uses $O(n + m)$ space; the stack alone is $O(h)$ for maximum shared nesting depth $h$.

## Alternatives and edge cases

- **Mutate `obj1` in place:** This can reduce new allocations, but it changes caller-owned data and makes reasoning about reused subtrees harder.
- **JSON serialization round trips:** Serializing at every recursive level can remain correct but repeats work and degrades to quadratic time on nested chains.
- **Treat every JavaScript object alike:** `null` must be handled as a leaf, and arrays may merge only with arrays.
- A primitive or incompatible container pair always resolves to the second value, even when the first contains deeper data.
- When the first array is longer, its untouched suffix remains; when the second is longer, its extra indices are added.
- Empty matching containers merge normally, and keys nested below them must still be copied.
- Inputs originate from `JSON.parse`, so functions, symbols, `undefined`, prototypes, and cyclic references are outside the contract.
