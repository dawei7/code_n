### 1. Description

Suppose we have a class:

```
public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
```

The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.

### 2. Function Contract

**Methods**

- `Foo()`: Initializes the data structure.
- `first(printFirst: 'Callable[[], None]')`: Executes operation.
- `second(printSecond: 'Callable[[], None]')`: Executes operation.
- `third(printThird: 'Callable[[], None]')`: Executes operation.

### 3. Note

We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seem to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

### 4. Examples

#### Example 1

- **Input:** `nums = [1,2,3]`
- **Output:** `"firstsecondthird"`
- **Explanation:** There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

#### Example 2

- **Input:** `nums = [1,3,2]`
- **Output:** `"firstsecondthird"`
- **Explanation:** The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

### 5. Constraints

- `nums` is a permutation of `[1, 2, 3]`.
