## Function Contract

LeetCode repeatedly calls `read(buf, n)` while preserving the reader's state. The canonical app represents those calls as one equivalent batch.

**Inputs**

- `content`: The app-local string consumed as the persistent file.
- `requests`: The successive `n` values passed to the same reader instance.

**Return value**

The app returns the substring copied by each request. Under the native interface, each call instead writes that substring into the shared destination `buf` and returns its character count.
