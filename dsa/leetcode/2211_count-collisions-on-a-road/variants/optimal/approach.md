## General

The exact solution avoids simulating collision times. It identifies cars that can escape forever and observes that every other moving car eventually participates in a collision.

Cars escaping left are precisely the consecutive `L` cars at the beginning. Cars escaping right are precisely the consecutive `R` cars at the end. After trimming those two groups, the answer is the number of moving cars remaining.

**Remove leading left-moving cars**

`directions.lstrip("L")` removes only `L` characters from the beginning.

These cars have no car to their left. They all move left at the same speed, so cars behind them cannot catch them, and they never collide.

The stripping stops at the first `R` or `S`. A later `L` is not guaranteed to escape because a right-moving or stationary car lies somewhere to its left.

**Remove trailing right-moving cars**

`rstrip("R")` then removes only `R` characters from the end of the already left-trimmed string.

These cars have no car to their right and move away forever at equal speed. A right-moving car earlier in the string is not stripped if some non-`R` car remains to its right and can eventually block it.

The resulting core `s` contains exactly the cars not eliminated by obvious outward escape.

**Why every moving car in the core collides**

Consider an `R` inside `s`. Because all trailing `R` cars were removed, there is some `L` or `S` to its right. Moving toward a stationary car, an oncoming left car, or a stopped collision group eventually prevents this `R` from escaping; it collides.

Symmetrically, every `L` in the core has some `R` or `S` to its left because all leading `L` cars were removed. It eventually collides with a moving or stationary obstruction.

Stationary cars do not move, but they can become collision points for several incoming cars.

**Translate collision scoring into moving-car counting**

When an `R` and `L` collide head-on, the score increases by two. Exactly two previously moving cars stop.

When one moving car hits a stationary car or an already stopped collision group, the score increases by one. Exactly one newly moving car stops.

After its first collision, a car becomes stationary and never contributes again as a moving participant. It may be struck later, but that later collision's one point belongs to the newly arriving moving car.

Therefore the total collision score equals the number of moving cars that eventually stop.

**Exclude stationary characters from the count**

`len(s)` counts every car in the core. `s.count("S")` counts those that were stationary from the start.

Subtracting leaves the number of `L` and `R` characters in the core, which is exactly the number of colliding moving cars:

`len(s) - s.count("S")`.

**Why no chronological simulation is needed**

Equal speeds and one-dimensional ordering prevent moving cars traveling in the same direction from overtaking. The only cars that avoid all obstructions are outward-moving boundary groups.

Once those are removed, whether a particular car first hits an original stationary car or a collision-created stationary group does not affect its contribution: it adds one when it stops. Head-on pairs add two, equivalent to counting both participants.

This conservation-style count determines the final score without calculating positions or event times.

**Why trimming both ends is exact**

Every stripped car provably escapes and contributes zero. Every unstripped moving car provably encounters an obstruction and contributes exactly one to the collision score.

The groups are disjoint and cover all moving cars, so counting only core movers yields the exact total.

For `"RLRSLL"`, neither end has an escaping group, so the core is unchanged. It contains five moving characters and one stationary character, yielding five.

For `"LLRR"`, leading Ls and trailing Rs are all stripped. The core is empty and the answer is zero.

## Complexity detail

Let $n$ be the string length. `lstrip` scans a leading prefix, `rstrip` scans a trailing suffix of the intermediate string, and `count` scans the remaining core. Total time is $O(n)$.

Python strings are immutable. The strip operations create intermediate/result strings whose total peak storage is $O(n)$. Thus exact auxiliary space is $O(n)$, matching the manifest. A manual two-pointer scan could achieve $O(1)$ auxiliary space.

## Alternatives and edge cases

- **State simulation:** Track pending right-moving cars and stopped regions in one pass. It also runs in $O(n)$ time but uses more branching.
- **Two pointers without slicing:** Find the first non-`L` and last non-`R` indices, then count movers between them for constant extra space.
- **All `L`:** Every car escapes left; trimming leaves empty and returns zero.
- **All `R`:** Every car escapes right; trimming also leaves empty.
- **All `S`:** No moving car exists, so length minus stationary count is zero.
- **Head-on `RL`:** Both remain in the core, contributing two.
- **Moving into stationary `RS` or `SL`:** The one moving character contributes one.
- **Collision chain:** Each later incoming moving car contributes one when it hits the stopped group.
- **Leading stationary car:** It prevents following left-moving cars from escaping through it.
- **Trailing stationary car:** It prevents preceding right-moving cars from escaping.
- **Same-direction cars:** Equal speeds prevent catching, but an obstruction ahead can stop the whole sequence through successive collisions.
- **Empty core:** String methods and count handle it naturally.
- **Input preservation:** Stripping returns new strings; `directions` remains unchanged.
