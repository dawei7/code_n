## General

**Reverse each dependency so availability can propagate**

A recipe becomes possible when all its ingredient names are available. The source builds a reverse graph:

`g[ingredient]` contains every recipe that depends on that ingredient.

`indeg[recipe]` stores how many required ingredients have not yet been processed as available. It starts as the full length of that recipe's ingredient list.

This resembles topological sorting. Ingredient and supply names are vertices, while each requirement is a directed edge from ingredient to recipe.

**Begin with initially available supplies**

The processing list `q` begins with all names in `supplies`. Every one is infinitely available, so it can satisfy one requirement of every dependent recipe.

For an available name `i`, the code visits every recipe `j` in `g[i]` and decrements `indeg[j]`.

When the counter reaches zero, all of that recipe's required ingredients have become available. The recipe is appended to `ans` and also appended to `q`, because a producible recipe may serve as an ingredient for other recipes.

Python's list iterator continues over items appended during iteration. Thus

`for i in q`

acts as a growing queue and propagates newly made recipes without an explicit deque.

**Why each requirement is decremented exactly once**

Every ingredient list contains no duplicates. Each available name is processed once under the valid uniqueness structure: initial supply names are unique, recipe names are unique, and the two sets are disjoint.

Therefore, each dependency edge is traversed once when its ingredient becomes available. A recipe reaches zero exactly after all distinct requirements have been satisfied.

A missing ingredient that is neither an initial supply nor a producible recipe is never placed in `q`. Its dependency edge is never processed, so the recipe's counter stays positive.

**How cycles are handled**

Two recipes may depend on each other. A cycle alone cannot create its first available item, so none of its counters reaches zero and it remains unproduced.

If every recipe in a dependency cycle also somehow becomes enabled through the required external structure, propagation can proceed only when individual counters genuinely reach zero. The algorithm never assumes that being a recipe name makes it automatically available.

For a simple cycle `A` needs `B` and `B` needs `A` with neither supplied, the initial queue contains neither name. Both remain unavailable, correctly.

**Trace a dependency chain**

Suppose bread needs yeast and flour, while sandwich needs bread and meat. Initial supplies are yeast, flour, and meat.

- processing yeast and flour decrements bread's two requirements; after the second, bread reaches zero and is appended;
- meat reduces sandwich's counter but does not finish it;
- when the growing loop later processes bread, sandwich's final requirement reaches zero and sandwich is appended.

The returned order reflects discovery, but any order is allowed.

**Why the algorithm is correct**

Every recipe appended to `ans` has counter zero. Each decrement corresponds to an ingredient proven available either initially or as an already producible recipe. Thus all of its ingredients are available, so every returned recipe can be created.

Conversely, consider any recipe that can be created through the closure of initial supplies and recipes. Following a valid production order, all its ingredients eventually enter `q` and traverse their edges. Its counter reaches zero, so the algorithm appends it. By induction through the production order, no possible recipe is missed.

The result is exactly the availability closure.

**Exact input mutation**

The assignment `q = supplies` does not copy the list. Appending recipes to `q` also appends them to the caller-provided `supplies` list.

This mutation does not change the returned answer, but it is an observable side effect of the exact source. Using `q = list(supplies)` or a deque would preserve the input.

## Complexity detail

Let $V$ be the number of distinct names represented in the dependency structure and initial supplies, and let

$$
E=\sum_i\lvert\texttt{ingredients[i]}\rvert.
$$

Graph construction takes $O(V+E)$ time when including map initialization. Each available name and dependency edge is processed at most once, so propagation is $O(V+E)$.

The reverse adjacency lists store $E$ edges. Counters, the growing queue, and the answer store $O(V)$ names. Total auxiliary structure is $O(V+E)$.

Because `q` aliases `supplies`, some queue storage is added directly to the input list rather than a separate object, but the total stored names remain linear.

## Alternatives and edge cases

- **Repeatedly scan all recipes:** Marking newly possible recipes until no change works but can revisit every ingredient many times. Reverse edges process each requirement once.
- **DFS with states:** Recursive availability checks can detect cycles and memoize results, but topological propagation is iterative and direct.
- **Treat recipe names as initially available:** Incorrect; a recipe becomes available only after all its ingredients are satisfied.
- **Missing ingredient:** Its dependent counter never reaches zero.
- **Pure dependency cycle:** No initial available name enters the cycle, so no recipe is returned.
- **Recipe with all direct supplies:** Its counter reaches zero as those supplies are processed.
- **Recipe used by several others:** Its name is processed once and satisfies one edge for every dependent recipe.
- **No duplicate ingredients:** Ensures one available name should decrement a recipe only once.
- **Any answer order:** Discovery order is valid.
- **Growing-list iteration:** Python processes appended recipes later in the same `for` loop.
- **Supplies mutation:** `q = supplies` means produced recipe names are appended to the input list.
- **Input-preserving variant:** Copy supplies before using it as a queue.
