## Function Contract

**Inputs**

- `n`: The app-local board dimension supplied to the native constructor.
- `moves`: For the app adapter, chronological triples `[row,col,player]` passed to native `move` calls.

**Return value**

The app adapter returns the status from every move. Each native call returns `0` without a winner or the ID of the player who has just won.
