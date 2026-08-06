## Function Contract

**Inputs**

- `startGene`: The valid gene string from which mutation begins.
- `endGene`: The gene string to reach.
- `bank`: The gene strings allowed after mutation steps.

**Return value**

Return the minimum number of one-character mutations from `startGene` to `endGene`, or `-1` when the target is
unreachable through valid bank genes.
