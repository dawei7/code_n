"""Per-category algorithm spec lists.

Each sub-module exports a :data:`SPECS` list of
:class:`~challenges.spec.AlgorithmSpec` entries. The order of the
list is the order challenges appear in the navigator (within
their category).

Adding a new algorithm to cOde(n) is a single :class:`AlgorithmSpec`
entry here, plus optionally a hand-curated
``optimal_solutions/<dataset>/<category>/<doc-stem>.py`` (the Solve button will use
``spec.source`` if the file is missing).
"""
