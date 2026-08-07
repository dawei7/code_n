## Function Contract

**Inputs**

- `houses`: the array of house positions on the line
- `heaters`: the array of heater positions on the line

**Return value**

- Return the minimum nonnegative integer radius that, when assigned to every heater, warms every house.

A heater covers positions whose distance from it is at most the shared radius. Different houses may be covered by
different heaters.
