## General

**Simulate one complete day at a time**

The choice of which region to quarantine depends on the current grid, and every unquarantined region spreads before the next choice. The exact solution therefore repeats four phases:

1. Discover every active infected region.
2. Measure how many distinct uninfected cells each region threatens and how many walls would surround it.
3. Quarantine the uniquely most threatening region.
4. Let every other active region spread one layer.

The grid uses three states during the simulation:

- `0` is currently uninfected.
- `1` is actively infected and can spread.
- `-1` is infected but quarantined and can no longer spread.

The input begins with only zeroes and ones; `-1` is an internal marker introduced by the algorithm.

**Discover one four-directional region**

At the start of each day, `vis` is reset because the active components may have changed after the previous spread. DFS begins at every unvisited cell whose value is one.

For the current component, the solution creates:

- `areas[-1]`: a list of all active infected coordinates in the component.
- `boundaries[-1]`: a set of distinct zero-valued cells threatened by the component.
- `c[-1]`: the number of infected-to-uninfected edges, which equals the required wall count.

DFS marks the infected cell visited, adds it to the area, and inspects its four side neighbors. An unvisited active infected neighbor continues the same DFS. A zero neighbor contributes one wall edge and is inserted into the boundary set.

**Why wall count and threatened-cell count differ**

One uninfected cell can touch the same infected region on two or more sides. It is still only one cell that would become infected tonight, so the boundary uses a set and counts it once when deciding which region threatens the most cells.

However, every shared side needs its own wall. The counter `c` increments for every infected-to-zero adjacency, including several sides around the same zero cell. This distinction explains why saving one central cell in a surrounding ring can require four walls.

**Choose the mandated region**

`max(boundaries, key=len)` finds a boundary set with the greatest number of distinct threatened cells. The problem guarantees that the relevant maximum is unique, so the corresponding index is unambiguous.

The solution adds `c[idx]` to the answer, because that is the number of shared boundaries around the selected region, then changes every cell in that area from one to `-1`. Those cells remain present in the grid but will not be discovered as active regions and will not spread on later days.

**Spread every region that was not quarantined**

For each other area, the algorithm revisits its original active infected cells and changes every adjacent zero to one.

The area lists were captured before spreading begins. Newly infected cells are not added to those lists during the same night, so they cannot spread a second step immediately. This correctly models one simultaneous layer of infection.

Different active regions may threaten the same zero cell. Whichever region processes it first changes it to one; the later region then sees a nonzero value. The final grid is still correct because that cell should become infected once.

**Why sequential mutation still models simultaneous spread**

Only cells that were zero and adjacent to an original cell of some unquarantined area are changed. No newly changed cell is iterated as an area member during this phase. Therefore the set of newly infected cells is exactly the union of all precomputed one-step frontiers, independent of processing order.

**When the simulation ends**

At the beginning of a day, if no active `1` component is found, `areas` is empty and the loop stops. The grid may contain quarantined `-1` cells and uninfected cells, but no virus can spread.

If infection fills all remaining cells, the active component has an empty boundary and needs zero new walls. The simulation can mark it quarantined with no added cost and then terminate. The accumulated answer is still the number of walls actually constructed.

**Why the complete simulation is correct**

DFS partitions all active infected cells into exactly their four-connected components. For each component, the boundary set equals the distinct cells it would infect next, while `c` equals the exact number of walls needed to isolate every such adjacency. The unique maximum therefore identifies the region required by the rule.

Marking that region `-1` prevents all later spread across its frontier. Every other component infects exactly its current zero neighbors and no cells farther away. Thus one loop iteration reproduces one legal day and night. Repeating until no active region remains produces the mandated process, and summing the daily wall counts gives the requested total.

## Complexity detail

Let `N = mn` be the number of grid cells. One day’s discovery visits every active cell and examines four edges, and the quarantine/spread phase also performs `O(N)` work.

Every nonterminal day quarantines at least one active cell or infection advances toward termination. A conservative bound allows `O(N)` rounds, producing `O(N^2) = O((mn)^2)` time.

The visited matrix, component coordinate lists, and boundary sets together hold `O(N)` entries during one day. Recursive DFS can also reach `O(N)` depth. Auxiliary space is `O(mn)`. The grid is mutated in place.

## Alternatives and edge cases

- **Recompute walls from only distinct boundary cells:** This undercounts when one zero cell touches several infected sides. Threat size uses unique cells; wall cost uses edges.

- **Spread newly infected cells immediately:** That would allow multiple layers in one night. Spread only from the areas recorded before mutation.

- **Build a separate next-grid copy:** It makes simultaneous spread visually explicit but uses another `O(mn)` matrix. Fixed pre-spread area lists make in-place mutation safe.

- **Quarantined marker:** Using `-1` distinguishes contained cells from both active infection and healthy cells without a separate status structure.

- **Regions sharing a threatened cell:** The cell becomes infected once; sequential writes do not change the correct union of frontiers.

- **No active region:** The loop exits and returns the walls already built.

- **Fully infected world:** No uninfected boundary remains, so no additional wall edge is necessary.

- **Recursive depth:** A large winding component may approach Python’s recursion limit; iterative DFS would preserve the algorithm with an explicit stack.
