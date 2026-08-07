## General
**Optimal Approach — Event Emitter**

The JavaScript solution solves **Event Emitter** using ES6 `Map`/`Set` collections for fast $O(1)$ key lookups, Functional JavaScript array methods (`map`, `filter`, `reduce`).

**Why This Approach Was Chosen:**
Written using modern ES6+ features with strict type safety and high-efficiency execution in V8 environment.

## Complexity detail
- **Time Complexity**: $O(1 + k(a + 1))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(s + k)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **ES6+ Best Practices:** Clean array manipulations and efficient memory usage.
- **Type Safety:** Well-defined parameters and predictable return contracts.
