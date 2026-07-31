## Function Contract

LeetCode supplies the file and calls `read(buf, n)`. The canonical app uses an equivalent adapter so the behavior can run without an external file API.

**Inputs**

- `content`: The app-local string consumed as the file by successive simulated `read4` calls.
- `n`: The maximum number of characters requested by the single `read` call.

**Return value**

The app returns the substring copied into the simulated destination. Under the native interface, write those same characters into `buf` and return their count.
