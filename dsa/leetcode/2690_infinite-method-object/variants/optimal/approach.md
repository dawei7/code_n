## General

JavaScript's `Proxy` can intercept a property read even when the target object has no declared property with that name. Create a proxy around an empty object and provide a `get` trap. The trap receives the requested property key and returns a new zero-argument closure that captures that key.

When the caller immediately invokes the returned closure, it returns the captured key. No registry or predeclared method set is needed, so ordinary names, punctuation-heavy bracket-notation names, the empty string, and names such as `toString` or `__proto__` all follow the same path. The trap handles the read before prototype lookup can supply unrelated behavior.

## Complexity detail

Each property read creates one closure, and each call directly returns its captured key. Both operations take $O(1)$ time and $O(1)$ additional space per outstanding closure. The certificate records this per-operation bound because there is no finite input corpus over which predeclaring all possible string property names forms a genuine slower algorithmic class.

## Alternatives and edge cases

- **Pre-populated object:** Declaring a finite collection of methods cannot satisfy arbitrary property names and therefore is not a correct general alternative.
- **Class method lookup:** Ordinary prototypes still require methods to exist in advance and do not synthesize unknown names.
- The empty string is a valid property name and must return an empty string when invoked.
- Punctuation and spaces require bracket notation but are still ordinary string property keys.
- Prototype-associated names such as `toString` and `__proto__` must be intercepted rather than inheriting their usual behavior.
- The closure must capture the requested property, not return a fixed value or the target object.
