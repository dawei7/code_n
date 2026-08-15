### 1. Description

Suppose you are given the following code:

```
class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
```

The same instance of `FooBar` will be passed to two different threads:

- thread `A` will call `foo()`, while

- thread `B` will call `bar()`.

Modify the given program to output `"foobar"` `n` times.

### 2. Function Contract

**Methods**

- `FooBar(n)`: Initializes the data structure.
- `foo(printFoo: 'Callable[[], None]')`: Executes operation.
- `bar(printBar: 'Callable[[], None]')`: Executes operation.

### 3. Examples

#### Example 1

- **Input:** $n = 1$
- **Output:** `"foobar"`
- **Explanation:** There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

#### Example 2

- **Input:** $n = 2$
- **Output:** `"foobarfoobar"`
- **Explanation:** "foobar" is being output 2 times.

### 4. Constraints

- $1 \le n \le 1000$
