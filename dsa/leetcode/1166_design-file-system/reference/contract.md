## Function Contract

**Source-native class**

- `FileSystem()`: Initialize an empty file system.
- `createPath(path, value)`: Create `path`, associate it with `value`, and return `true` only when `path` is new and its immediate parent exists. Otherwise return `false` without changing the system. The implicit root permits a one-component path to be created directly.
- `get(path)`: Return the value associated with `path`, or `-1` if that path does not exist.

**App-local input**

- `operations`: A sequence of `createPath` and `get` calls, each represented by its method name and argument list. The adapter constructs one empty `FileSystem`, performs the calls in order, and returns their results in the same order. The source-native constructor entry and its `null` result are omitted from this adapted sequence.

Let

$$
S = \sum_{o \in \text{operations}} \lvert \operatorname{path}(o) \rvert
$$

be the total number of path characters processed across all calls.

**Return value**

- A list containing each operation's boolean or integer result in execution order.
