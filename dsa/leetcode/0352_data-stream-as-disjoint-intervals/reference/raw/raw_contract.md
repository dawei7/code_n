## Function Contract

**Inputs**

- `values`: For the app adapter, the stream values passed to consecutive `addNum` operations. The native interface receives one `value` per `addNum` call.

**Return value**

The app adapter returns the current interval summary after each addition. In the native class, `getIntervals()` returns one such summary whenever queried.
