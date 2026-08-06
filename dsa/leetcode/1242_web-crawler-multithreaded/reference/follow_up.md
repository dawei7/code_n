## Follow-up

Consider a crawl of one billion URLs distributed across 10,000 machines, with identical crawler software on every machine and knowledge of the full worker fleet.

- How would the design partition work evenly while minimizing communication between machines?
- How should the system tolerate a machine that fails or stops doing useful work?
- How can the distributed crawler determine that all work has finished?
