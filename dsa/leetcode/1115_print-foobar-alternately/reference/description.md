## Description

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

<ul>
	<li>thread `A` will call `foo()`, while</li>
	<li>thread `B` will call `bar()`.</li>
</ul>

Modify the given program to output `"foobar"` `n` times.
