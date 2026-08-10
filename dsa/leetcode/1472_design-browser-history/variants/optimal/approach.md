## General

**Represent the current page at the top of the history stack.** `stk1` stores every page from the earliest reachable page through the current page. Its final element is always the current URL. `stk2` stores pages that can be reached by moving forward.

The constructor creates both empty lists and calls `visit(homepage)`. Reusing the normal visit operation appends the homepage to `stk1` and clears the already-empty forward stack. This establishes one current page and guarantees `stk1[-1]` is safe afterward.

**Visiting creates a new branch.** `visit(url)` appends the new URL to `stk1`, making it current. It then clears `stk2`. If the user had moved backward, those forward pages belong to the abandoned history branch and must no longer be reachable.

Clearing forward history is not optional. After going from page C back to page A and visiting X, pressing forward must not return to B or C.

**Move backward by transferring pages.** While steps remain and `stk1` contains more than one page, `back` pops the current URL from `stk1` and appends it to `stk2`. The newly exposed top of `stk1` becomes current.

The condition `len(stk1) > 1` protects the homepage or earliest retained page. The method stops there even when the requested step count is larger, implementing “at most steps.”

Pages moved backward are appended to `stk2` in the exact order needed for forward navigation. The most recently left page sits at its top and should be the first restored.

**Move forward by reversing that transfer.** While steps remain and `stk2` is nonempty, `forward` pops its top URL and appends it to `stk1`. That page becomes current. When no forward page remains, the method stops even if steps are left.

Both navigation methods return `stk1[-1]`, so the representation has no separate current-page variable that could become inconsistent.

**Trace a branch change.** Suppose `stk1` represents homepage, Google, Facebook, YouTube and `stk2` is empty. Back twice moves YouTube and then Facebook to `stk2`, leaving Google current. Forward once pops Facebook back, making it current and leaving YouTube available.

Visiting LinkedIn now appends it after Facebook and clears YouTube from `stk2`. A subsequent forward call cannot move because the old future was invalidated.

**The central invariant.** `stk1` is the chronological path ending at the current page. Reading `stk2` from top to bottom gives the chronological pages available ahead. Their concatenation in that orientation describes the active history line.

Back and forward transfer one boundary page while preserving this invariant. Visit adds a new endpoint and discards everything beyond the old endpoint. Induction over calls proves every returned URL matches browser semantics.

**Understand actual operation cost.** A back or forward call loops once per page actually moved, so it costs `O(r)` where `r` is bounded by the requested steps and available history. `list.clear()` must release every stored forward reference, so visit costs `O(f)` when `f` forward pages are discarded, although append itself is amortized constant time.

Across a sequence, each URL is appended, moved, or cleared according to actual navigation. The manifest's `O(q)` time treats bounded steps and amortized stack operations as constant per call. The exact general description is proportional to total page transfers plus visits and cleared entries.

## Complexity detail

For one `back` or `forward` call moving `r` pages, time is `O(r)` and auxiliary work is constant. A visit that clears `f` forward pages takes `O(f)` to release them and amortized `O(1)` to append.

Let `M` be the total number of successful one-page moves across all navigation calls and `V` the number of visits. Total sequence time is `O(V + M)` plus entries cleared from abandoned futures; each such entry was previously stored, so this is naturally amortized over history operations.

At any moment, each active history URL appears in exactly one stack. If `v` pages have been visited and not discarded from representation, storage is `O(v)`. The lists' dynamic-array capacity is also linear.

With the problem's step limit of one hundred, each navigation call has a fixed bounded loop, which motivates the manifest's compact `O(q)` total-call notation.

## Alternatives and edge cases

- **Dynamic array with current and last indices:** Back and forward become constant-time index clamps, and visit overwrites the next slot while moving the valid boundary.
- **Doubly linked list:** Previous and next pointers model navigation directly, but each multi-step call still walks nodes and allocation overhead is higher.
- **Single stack only:** It supports back but cannot recover pages for forward navigation.
- **Back beyond the homepage:** The `len(stk1) > 1` guard stops at the earliest page.
- **Forward beyond available history:** An empty `stk2` stops movement.
- **Visit after going back:** Forward history is cleared, producing a new branch.
- **Visit while already latest:** Clearing an empty forward stack changes nothing.
- **Repeated URL strings:** Entries represent visits, not unique URLs, so repetitions remain separate history positions.
- **Constructor:** Calling `visit` establishes the same invariants used by later visits.
- **Current-page safety:** `stk1` never becomes empty because back preserves at least one entry.
- **Clear complexity:** Python list clearing is linear in removed references, not literally constant.
- **Amortized append:** Occasional list resizing is spread across many pushes.
