## Function Contract

**Inputs**

- `width`: The number of screen columns.
- `height`: The number of screen rows.
- `food`: Food coordinates in appearance order.
- `directions`: For the app adapter, the sequence supplied to native `move` calls.

**Return value**

The app adapter returns every move's score or `-1` result. The native method returns the result of one move.
