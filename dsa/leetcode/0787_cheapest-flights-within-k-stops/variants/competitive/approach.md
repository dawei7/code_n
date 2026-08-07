## General
The competitive solution optimizes for raw execution speed, low memory overhead, and minimal runtime cost (sourced from `kamyu104/LeetCode-Solutions`).

- **Core Strategy**: Employs bitwise operations and bitmasking for low-level memory and speed optimization.
- **High-Performance Techniques**: Uses bit manipulation tricks to evaluate conditions in single CPU clock cycles.
- **Benchmark Design**: Tailored for high-throughput automated judging environments where constant-factor speed is critical.

## Complexity detail
- **Time Complexity**: $O((k + 1) \cdot E)$ — High-efficiency runtime performance.
- **Space Complexity**: $O(V)$ — Minimal auxiliary memory overhead.

## Alternatives and edge cases
- **Low constant factor optimization:** Minimizes object allocations, inlines loop logic, and leverages bitwise or mathematical shortcuts.
- **Competitive judging performance:** Optimized for raw execution speed on large automated test suites.
