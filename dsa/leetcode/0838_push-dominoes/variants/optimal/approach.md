## General
**Only neighboring explicit forces govern a gap**

Add a virtual `L` just before the string and a virtual `R` just after it. These sentinels express that dots before the first `L` fall left, dots after the last `R` fall right, and otherwise no outside force enters the line. Scan consecutive non-dot symbols and resolve the dots between them as one independent segment.

For boundary forces `L...L` or `R...R`, every intervening domino falls in that shared direction. Between `L...R`, the forces point away from the gap, so every dot stays upright. Between `R...L`, forces move inward at equal speed: fill the left half with `R`, the right half with `L`, and retain one central `.` exactly when the gap length is odd.

The initially pushed symbols themselves never change. Every dot lies in exactly one segment between consecutive forces, and the four boundary-direction combinations exhaust all possibilities. The segment rule matches the arrival time and direction of the nearest possible forces, including equal-time cancellation, so concatenating the resolved segments yields the unique final state.

## Complexity detail
The scan visits every input symbol once, and the total number of generated output characters is $n$. This gives $O(n)$ time. The sentinel string and output pieces together use $O(n)$ space.

## Alternatives and edge cases
- **Simulate one second at a time:** Applying simultaneous updates across the whole line until stable is correct, but a single force crossing a long dot run can require $O(n)$ rounds of $O(n)$ scanning, for $O(n^2)$ time.
- **Two directional force arrays:** Left-to-right and right-to-left passes can record arrival distances and compare them at each domino, also achieving $O(n)$ time with $O(n)$ space.
- **All upright:** With no real force, the virtual `L...R` pair leaves every domino as `.`.
- **Outward forces:** A segment `L...R` remains upright because neither force enters the gap.
- **Odd inward gap:** In `R...L`, the middle domino receives both forces simultaneously and stays upright.
- **Already falling neighbor:** A force does not pass through as an extra instantaneous push; propagation still advances only one adjacent upright domino per second.
