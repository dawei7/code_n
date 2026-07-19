## General
**Find the rectangle point nearest the center.** Clamp `xCenter` to the closed interval from `x1` to `x2`, and clamp `yCenter` independently from `y1` to `y2`. The resulting `(closest_x, closest_y)` lies in the rectangle.

For an axis-aligned rectangle, independent clamping minimizes each squared coordinate difference, so this point minimizes Euclidean distance from the circle center to every rectangle point. If the center lies inside the rectangle, clamping leaves it unchanged and the minimum distance is zero.

The shapes overlap exactly when that minimum squared distance is at most `radius * radius`. Using squared values avoids square roots and preserves tangency through the non-strict comparison.

## Complexity detail
The input has fixed arity. A constant number of comparisons, arithmetic operations, and assignments gives $O(1)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Check only rectangle corners:** A circle can cross the middle of an edge while all four corners remain outside, so corner checks alone are insufficient.
- **Horizontal and vertical separation:** Compute the gap from the center to each rectangle interval and compare the squared gap vector. This is algebraically equivalent to clamping.
- **Center inside rectangle:** The minimum distance is zero, so overlap is guaranteed.
- **Edge tangency:** Equality between squared distance and squared radius counts as overlap.
- **Corner tangency:** Both coordinate gaps may be nonzero and must be combined with the Euclidean squared distance.
- **Negative coordinates:** Clamping and subtraction work without any coordinate translation.
