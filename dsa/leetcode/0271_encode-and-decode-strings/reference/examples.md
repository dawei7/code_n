## Examples

**Example 1**

- Input: `dummy_input = ["Hello","World"]`
- Output: `["Hello","World"]`
- Explanation: Machine 1 creates a `Codec`, passes `strs` to `encode`, and sends the resulting message. Machine 2 creates its own `Codec` and calls `decode` on that message to recover the displayed list.

```mermaid
flowchart LR
    accTitle: Encoded message transmission
    accDescr: Machine 1 encodes the list and sends one encoded message to Machine 2, which decodes it back into the list.
    sender["Machine 1: encode(strs)"] -->|encoded message| receiver["Machine 2: decode(message)"]
```

**Example 2**

- Input: `dummy_input = [""]`
- Output: `[""]`
