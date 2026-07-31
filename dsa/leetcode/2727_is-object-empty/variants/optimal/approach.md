## General

Attempt to enumerate the container with `for...in`. For JSON-parsed objects, the enumerable names are exactly their key-value properties; for arrays, populated indices are enumerable names. If the loop produces any name, return `false` immediately because one property or element proves the container is nonempty.

If enumeration produces no name, execution reaches the final `true`. This covers both `{}` and `[]`. The algorithm never examines stored values, so `null`, `false`, zero, empty strings, nested containers, and other falsy data correctly count whenever their key or index exists.

## Complexity detail

The decision uses $O(1)$ auxiliary space. It performs no loop body for an empty container and returns on the first enumerable entry for a nonempty container, giving the requested $O(1)$ decision work under the JSON-container model. The matching $\Omega(1)$ output-decision lower bound is recorded in the asymptotic-optimality certificate.

## Alternatives and edge cases

- **`Object.keys(obj).length`:** Concise and correct, but it materializes every key and therefore takes $O(n)$ time and space for $n$ entries.
- **`JSON.stringify(obj)`:** Comparing with `"{}"` or `"[]"` traverses and serializes the entire container.
- **Array length special case:** `obj.length === 0` is constant time for arrays but does not handle ordinary objects by itself.
- Falsy values still make their containing object or array nonempty.
- A property whose value is an empty object or array still counts as a property.
- The empty-string property name is a valid key and proves nonemptiness.
- The `JSON.parse` guarantee avoids custom enumerable prototype properties.
