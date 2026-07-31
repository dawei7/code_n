## Function Contract

**Inputs**

- `size`: The fixed maximum number of recent values in the window.
- `stream`: For the app adapter, the values supplied to consecutive native `next(val)` calls.

**Return value**

The app adapter returns the sequence of moving averages. Each native `next` call returns only the new average after its value is added.
