# Guided Example: Check if Object Instance of Class

## 1. The instance and the exact question

The task is to decide whether a *value* is an instance of a *class*, where the statement deliberately defines instancehood by capability rather than by construction: a value counts as an instance of a class when it has access to that class's methods. Nothing is guaranteed about the inputs — either argument may be `undefined`, a primitive, a function, or an object.

The instance traced below is the inheritance case, whose required outcome is `true`:

| role | entity in this instance |
|---|---|
| value under test | an object created by the class named `Dog` |
| class asked about | the class named `Animal` |
| relationship | the class `Dog` is declared to extend the class `Animal` |
| required outcome | `true` |

Reaching that outcome requires an accurate model of *how* a value gets access to methods, because the obvious tool — the language's `instanceof` operator — gives the wrong answer for primitives and throws for non-callable targets. The lesson therefore derives the decision procedure from the runtime's own object model.

## 2. The object model that decides the question

Every ordinary object in the runtime carries one internal link to another object, its prototype, and that link is either another object or `null`. Property and method lookup follows the link repeatedly until the name is found or `null` is reached. A class declaration creates a prototype object, and every object constructed by that class receives it as the immediate prototype link. When one class extends another, the constructor's own prototype object is additionally linked to the superclass's prototype object, which is what makes inherited methods visible.

Those facts are the whole answer to "does this value have access to that class's methods":

$$
\text{value is an instance of } C \iff C\text{'s prototype object occurs somewhere in value's prototype chain.}
$$

| entity | its prototype link | why it matters here |
|---|---|---|
| object created by `Dog` | `Dog.prototype` | first link searched; it is not the target in this instance |
| `Dog.prototype` | `Animal.prototype` | the `extends` clause installs this link, so inherited methods are reachable |
| `Animal.prototype` | `Object.prototype` | the chain continues past the target, which is why stopping early matters |
| `Object.prototype` | `null` | the chain is finite and terminates; the search must also terminate |
| `null` | nothing | no lookup can succeed, so no value below this point has methods |

The comparison must be *identity* of prototype objects. Two different classes can share a name, a class can be anonymous, and a subclass's instances carry a different immediate prototype than the superclass's instances; only object identity distinguishes them reliably.

## 3. Two guards that must run before the walk

The search is over prototype links, so it needs a value that has a chain and a target that has a prototype object. Both conditions can fail.

| value | class asked about | pre-flight finding | outcome |
|---|---|---|---|
| `null` | `Object` | a null value has no prototype chain at all | `false` |
| `undefined` | any class | same reason | `false` |
| a plain object | `undefined` | the target is not a function, so it has no prototype object to look for | `false` |
| a plain object | an arrow function | it is a function but owns no prototype object, so no chain link can ever equal the target | `false` |
| the number `5` | `Number` | both checks pass; the walk proceeds after boxing | decide by the walk |

The `null` guard is not cosmetic. Boxing `null` produces a brand-new empty object whose chain reaches `Object.prototype`, so a search that skipped the guard would report `true` for a null value asked about `Object` — a value with no methods at all would be credited with all of them. The same trap exists for `undefined`. The function guard matters because a non-function target has no `prototype` object; comparing chain links against an absent target can never succeed, and doing so must be a definite `false` rather than an error.

## 4. Boxing normalizes primitives before the walk

Primitives are not objects and have no prototype link of their own, yet the statement insists that the primitive `5` is an instance of `Number` because it "accesses the Number methods" such as the formatting method used to print fixed decimals. The reconciliation is a temporary wrapper object: converting a primitive to an object yields a wrapper whose immediate prototype is the primitive's own prototype object.

| value under test | wrapper created for the walk | chain searched | link matching `Number.prototype` | outcome |
|---|---|---|---|---|
| `5` | number wrapper | `Number.prototype`, `Object.prototype`, `null` | first link | `true` |
| a symbol | symbol wrapper | `Symbol.prototype`, `Object.prototype`, `null` | first link | `true` |
| `null` | none — rejected by the guard | not searched | — | `false` |
| an already-boxed object | the object itself | its own chain | depends on its chain | decided normally |

Converting an object to an object is the identity operation, so one uniform walk handles both primitives and objects. This single step is precisely where the required semantics part company with `instanceof`, whose internal instance-of operation never boxes and therefore reports `false` for every primitive.

## 5. Executing the walk on the traced instance

The value's chain is `Dog.prototype` → `Animal.prototype` → `Object.prototype` → `null`, and the target is `Animal.prototype`. The walk starts at the first link and ascends one link per iteration, comparing identity each time.

| step | current chain link | identical to `Animal.prototype`? | action taken |
|---|---|---|---|
| 1 | `Dog.prototype` | no | ascend to its prototype |
| 2 | `Animal.prototype` | yes | stop and report `true` |
| — | `Object.prototype` | never reached | the early exit skips these links entirely |
| — | `null` | never reached | termination point not needed once a match is found |

The answer is `true` after two comparisons. Note what the trace proves about the search order: the match was found on the *second* link, so a procedure that only inspected the immediate prototype would have answered `false` incorrectly. The instance also demonstrates why the walk must not stop at the first link, and why it must not rely on the value's own constructor property, which for this instance names `Dog` rather than the requested `Animal`.

A companion trace shows the opposite extreme — the constructor asked about itself:

| step | value | current chain link | identical to `Date.prototype`? | action |
|---|---|---|---|---|
| 1 | the `Date` constructor | `Function.prototype` | no | ascend |
| 2 | the `Date` constructor | `Object.prototype` | no | ascend |
| 3 | the `Date` constructor | `null` | no | chain exhausted, report `false` |

The required outcome is `false`: a constructor is a function object, it is not constructed by itself, and none of its chain links is the prototype object it hands out to its own instances.

## 6. Invariant and correctness

Let $p_0, p_1, \dots, p_{k-1}, \dots$ be the chain of the boxed value, terminating at $p_{L} = \texttt{null}$, and let $T$ be the target's prototype object.

**Invariant.** At the start of iteration $k$, the cursor holds $p_k$, and the search has already compared $T$ against exactly $p_0, \dots, p_{k-1}$ without a match, so none of those links equals $T$.

*Base.* Before the first iteration the cursor holds $p_0$ and no comparison has been made, so the claim is vacuous.

*Step.* If the cursor equals $T$, the procedure returns `true`; by the definition in section 2 the target's prototype object occurs in the chain, so the value does have access to that class's methods. If it differs, the only remaining way to reach the target is further up, and the cursor advances to $p_{k+1}$, preserving the invariant with one more satisfied comparison.

*Termination and completeness.* Every iteration moves the cursor strictly upward, and the runtime refuses to install a prototype link that would close a cycle, so the chain is finite and the cursor reaches `null` after at most $L$ iterations. At that point the invariant says the target was compared against every link in the chain and matched none, so no method of the class is reachable — the answer `false` is sound, not merely a default. Conversely, if the target occurs anywhere in the chain, the invariant guarantees the walk reaches and recognises it before terminating. Together the two directions make the returned boolean exactly the statement's condition, for primitives, objects, functions and inherited classes alike.

The guards of section 3 preserve the same equivalence: a `null` or `undefined` value has an empty chain by definition, and a target without a prototype object has no methods to grant, so both cases correctly fall outside the definition rather than being special exceptions to it.

## 7. Traps this instance exposes

| trap | concrete symptom | correct handling |
|---|---|---|
| Delegating to the language's `instanceof` operator | the primitive `5` asked about `Number` must be `true`, while `instanceof` reports `false` for every primitive | Box the value first, then compare prototype objects |
| Letting the operator's own errors escape | asking with a non-callable target such as `undefined` throws an error under `instanceof`, but the contract requires `false` | Reject non-function targets before searching |
| Boxing before guarding for `null` | a null value asked about `Object` would become an empty object and be reported `true` | Test for `null` and `undefined` first |
| Comparing names or constructor properties | two unrelated classes may share a name, classes may be anonymous, and a subclass instance's constructor property names the subclass | Compare the prototype objects themselves by identity |
| Stopping at the immediate prototype | this instance's match is one link further up; an immediate-prototype check returns `false` | Walk the whole chain until the match or `null` |
| Assuming every object inherits from `Object` | an object created with a null prototype has an empty chain and must be `false` for `Object` | Treat the chain itself as the authority |
| Confusing an object with its class | the traced constructor asked about itself must be `false` | Only prototype links, never constructors, are compared |
| Assuming the target is one link deep | the requested class may be many links up a deep hierarchy | Cost is proportional to chain depth, so a loop is required; recursion adds stack depth for no benefit |
| Cross-realm classes | an object from another realm does not carry this realm's `Object.prototype` in its chain, so identity correctly fails | Accept the realm-local answer; there is no global name registry to consult |
| Circular chains | a manually installed prototype link that closes a loop would make the walk non-terminating | The runtime rejects the creation of such a cycle, so the chain is always acyclic and ends at `null` |

## 8. Complexity

**Time.** The walk performs at most one identity comparison and one prototype read per link, so the cost is

$$
O(d),
$$

where $d$ is the number of links from the boxed value up to `null`: the inheritance depth of the value's class plus the built-in links that end at `Object.prototype`. The two guards and the boxing step are constant-time, and the early exit on a match can only shorten the walk. In the traced instance $d = 3$ and the answer is produced after two comparisons; in a 64-level hierarchy the loop runs at most 64 times with no stack growth. The language's own `instanceof` operator has the same asymptotic cost but the wrong semantics for primitives and an exception path for invalid targets, so matching the contract costs nothing asymptotically.

**Auxiliary space.** One cursor holds the current link and one variable holds the target prototype: $O(1)$ extra space, independent of chain depth. The chain itself belongs to the input and is never copied or materialized as a list, which is why deep hierarchies are handled without allocating per level.
