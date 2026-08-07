## Function Contract

**Inputs**

- `operations`: A sequence beginning with construction of `Excel`, followed by `set`, `get`, or `sum` calls.
- `arguments`: The matching constructor dimensions, cell coordinates and values, or formula-reference lists.

**Source-native interface**

`Excel(height, width)` creates a `height x width` integer sheet. Valid row indices are in `[1, height]`, valid columns are in `['A', width]`, and every cell initially contains `0`.

`set(row, column, val)` replaces the target cell's current literal or formula with the integer `val`.

`get(row, column)` returns the target cell's current integer value.

`sum(row, column, numbers)` replaces the target cell with a sum formula, returns its current value, and keeps that formula active until the target is overwritten. Each entry in `numbers` is either a single-cell reference such as `F7` or a rectangular range such as `B3:F7`; range endpoints are the top-left and bottom-right cells, and both endpoints are included.

**Return value**

The app-local operation trace returns `null` for construction and `set`, and returns the requested integer for every `get` and `sum` call.
