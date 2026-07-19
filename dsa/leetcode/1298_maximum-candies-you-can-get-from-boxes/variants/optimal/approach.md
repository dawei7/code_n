## General
**Two independent prerequisites**

Track possession and openability separately. A key makes its target openable even if that box has not been found yet; finding a box records possession even if its key is still missing. Whenever an update makes both facts true, enqueue the box.

Initialize possession from `initialBoxes`, initialize openability from `status`, and enqueue every initially possessed box that is already openable. When a queued box is opened, mark it processed before collecting its candies so that duplicate discoveries cannot count it twice.

For every key inside the box, mark the target openable and enqueue it if already possessed. For every contained box, mark it possessed and enqueue it if already openable. This symmetric treatment handles both event orders. Every box that can legally become usable is queued when its second prerequisite arrives, so the traversal cannot miss collectible candies. Conversely, the queue admits only boxes satisfying both prerequisites, so every collected candy is reachable under the rules.

## Complexity detail
Each box is opened at most once. Its key list and contained-box list are scanned only when it opens, so the total work is $O(n+K+B)=O(S)$. The possession, openability, and processed arrays plus the queue use $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Repeated full rescanning:** Rechecking every box after each newly acquired key or box is correct, but a dependency chain can make it take $O(nS)$ time.
- **One combined state flag:** Collapsing possession and openability loses the distinction between owning a locked box and holding a key for a box not yet found.
- **Key before box:** The openable flag must persist until the corresponding box is acquired.
- **Box before key:** A possessed locked box must become eligible as soon as its key appears later.
- **Unreachable open box:** An initially open box contributes nothing unless it is also possessed eventually.
- **Duplicate discovery paths:** A processed flag prevents collecting one box's candies more than once.
