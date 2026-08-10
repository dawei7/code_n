## General

**Each truck slot should receive the most valuable available box**

Every box consumes exactly one unit of truck capacity, regardless of its type. The only quantity that differs is the number of units contributed by that box. Therefore, whenever capacity remains, taking a box with more units per box is never worse than taking one with fewer.

The source sorts `boxTypes` with `key=lambda x: -x[1]`. Negating the units-per-box value makes Python's ascending sort place larger original values first. The result is a new sorted list; the input `boxTypes` is not reordered by this call.

After sorting, a type represented by `[a, b]` has `a` available boxes and `b` units in each box. Types are visited from greatest `b` to least.

**Take as many as capacity permits**

For the current type, `min(truckSize, a)` is the number of boxes that can actually be loaded. If at least `a` slots remain, all boxes of the type are taken. If fewer slots remain, the truck takes only that remaining capacity and becomes full.

The contribution is

`b * min(truckSize, a)`,

which is added to `ans`. Multiplication is correct because every box within one type has the same unit count.

**Understand the source's capacity update**

After adding the correct number of units, the exact code executes `truckSize -= a`, subtracting the entire available batch count rather than the smaller number actually loaded.

When all `a` boxes fit, this is the ordinary remaining-capacity update. When only part of the batch fits, `truckSize` becomes zero or negative instead of exactly zero. The next condition `if truckSize <= 0: break` immediately stops, so that negative value is never used to load another type. The computed contribution already used the proper minimum, making this implementation detail harmless.

An alternative spelling could subtract `min(truckSize, a)` and stop at exactly zero, but that is not what this file does.

**Why filling greedily is optimal**

Suppose a proposed solution loads a box of type $L$ with $u_L$ units while leaving an available box of type $H$ with $u_H>u_L$ unloaded. Replacing the loaded low-value box with the high-value box uses the same one truck slot and increases the total by $u_H-u_L$.

Therefore no optimal loading can contain a lower-value box while excluding a higher-value available box. Repeating this exchange forces the structure used by the algorithm: take all possible boxes from the highest units-per-box type, then the next highest, and so on, with at most one partially taken type when capacity runs out.

The sorted scan constructs exactly that structure, so its total is optimal.

**Why unused capacity is sometimes correct**

Every unit-per-box value is positive under the constraints. Thus it is beneficial to fill every slot whenever enough boxes exist. If the sum of all box counts is smaller than `truckSize`, the loop simply finishes after taking every box, leaving capacity unused because no more boxes are available. The answer is then the total units of all boxes.

There is no requirement to load exactly `truckSize` boxes, only at most that many.

**Trace the first example**

For `boxTypes = [[1,3],[2,2],[3,1]]`, the list is already in descending unit order. With capacity four:

- Take the one three-unit box. `ans = 3` and effective remaining capacity is three.
- Take both two-unit boxes. `ans = 7` and remaining capacity is one.
- The last type has three boxes, but `min(1,3) = 1`, so one unit is added and `ans = 8`.

The source then subtracts three, making `truckSize = -2`, and breaks. The negative bookkeeping does not mean extra boxes were loaded; the contribution used only one.

**Ties do not need special handling**

If two types have the same units per box, their relative sorted order cannot affect the total. Taking a slot from either contributes the same value. Python's stable sort preserves their original order, but correctness does not depend on that stability.

## Complexity detail

Let $t$ be the number of box types. Sorting takes $O(t\log t)$ time. The loop visits at most all $t$ types and performs constant work per type, adding $O(t)$. Total time is $O(t\log t)$, matching the manifest.

`sorted(...)` creates a new list of $t$ references, and Python's sorting implementation may use additional linear temporary storage. Auxiliary space is therefore $O(t)$. The returned result and loop variables use constant space.

The algorithm does not expand types into individual boxes, so its resource use depends on the number of types rather than the potentially much larger total box count or truck capacity.

## Alternatives and edge cases

- **Repeatedly search for the best type:** Finding the maximum remaining units in a full scan can cost $O(t^2)$ across all types.
- **Max-heap of types:** Heapify by negative units and pop in priority order. It also works in $O(t\log t)$ time and $O(t)$ space.
- **Counting by unit value:** Because units per box are bounded by 1000, a frequency/count array can achieve $O(t+U)$ time, where $U$ is the value range.
- **Expand every box:** Sorting individual boxes can require space and time proportional to the total number of boxes and is unnecessary.
- **Truck fits all boxes:** Every type is processed and all units are included, even though `truckSize` remains positive.
- **Partial final type:** The contribution uses `min`, and the subsequent negative capacity triggers immediate termination.
- **Capacity filled exactly:** Subtracting the batch makes `truckSize == 0` and the loop breaks.
- **One type:** Load the smaller of its count and capacity.
- **Equal unit values:** Any order among tied types produces the same answer.
- **Large truck capacity:** Runtime does not depend on iterating individual slots.
- **Positive unit guarantee:** Taking another available box never reduces the objective.
- **Input preservation:** `sorted` returns a new outer list; it does not reorder `boxTypes`.
- **Capacity variable after partial load:** Its negative value is internal control state only and does not represent an actual negative number of slots.
