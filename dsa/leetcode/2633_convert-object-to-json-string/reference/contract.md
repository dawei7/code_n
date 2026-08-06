## Function Contract

**Inputs**

- `object`: A valid JSON value (`null`, `boolean`, `number`, `string`, `Array`, or `Object`) with maximum nesting depth $\le 1000$ and serialized length $1 \le S \le 10^5$.

**Return value**

Return a compact JSON string representing `object` without invoking `JSON.stringify`.
