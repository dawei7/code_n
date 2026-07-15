# Visual Walkthrough Framework

Visual walkthroughs are an offline-first teaching surface built from validated,
package-authored state snapshots. They are neither recordings nor executions of
the learner's code.

## Reuse boundary

The framework deliberately separates four responsibilities:

1. `visualization.json` owns the problem-specific example, teaching phases,
   narration, semantic code anchors, timing, and exact state at every step.
2. `server/app/visualizations.py` validates the manifest, resolves anchors
   against the canonical package solution, and rejects inconsistent traces.
3. `web/src/components/visualization/VisualizationPlayer.tsx` owns reusable
   playback, phase navigation, keyboard controls, speed, narration, learning
   goals, invariants, complexity labels, and the Monaco code stage.
4. `web/src/components/visualization/renderers/` owns only data-structure
   presentation. The renderer registry is the single dispatch point for new
   visual families.

When another problem uses an existing visual family, author only its manifest.
Add React code only when the problem needs a genuinely different scene, such as
a tree, graph, matrix, sliding window, stack, heap, linked list, or dynamic
programming table.

## Canonical source and semantic anchors

Never duplicate solution source as a JSON array of lines. Point to a real
package solution and identify the concepts that the lesson needs to highlight:

```json
{
  "code": {
    "language": "python",
    "source_path": "solutions/python.py",
    "anchors": {
      "scan": { "start": "for i, value in enumerate(nums):" },
      "lookup": { "start": "if need in seen:" },
      "return": { "start": "return [seen[need], i]" }
    }
  }
}
```

Every anchor must match exactly one source line. An optional `end` string can
define a multi-line range. A source refactor that makes an anchor ambiguous or
missing fails validation instead of silently highlighting the wrong code.

The API returns the actual source text plus resolved line ranges. The frontend
renders it in a read-only Monaco editor and synchronizes decorations from step
anchor names.

## Teaching manifest

Version 2 manifests define reusable teaching metadata at the top level:

- `pattern`: the algorithm or data-structure pattern;
- `learning_objective`: the mental move the learner should acquire;
- `invariant`: the condition to watch remain true across transitions;
- `complexity`: the final time and space result;
- `phases`: a short conceptual progression; and
- `steps`: the tightly authored trace for one representative example.

Each step contains reusable presentation fields and renderer-specific state:

```json
{
  "id": "hit-two",
  "phase": "connect",
  "title": "Retrieve the earlier index",
  "description": "Key 2 maps to index 1.",
  "insight": "The earlier index is distinct by construction.",
  "badge": { "label": "Match found", "tone": "success" },
  "active_code": ["lookup"],
  "duration_ms": 2700,
  "state": {
    "event": "found"
  }
}
```

Renderer state has its own strict schema. For example, `array-hash-map` requires
the current index, matched index, visited prefix, variables, hash entries,
result, and changed fields. `binary-partition` requires the active cut-search
range, complementary cuts, four boundary values, both cross-array comparison
results, the directional violation, and the final median.

The reviewed package examples exercise different reuse levels:

- `0001_two-sum` uses the `array-hash-map` scene to teach complement lookup and
  the check-before-store invariant.
- `0004_median-of-two-sorted-arrays` uses the `binary-partition` scene and a
  trace that demonstrates both binary-search failure directions before proving
  the final balanced partition.

## Educational quality

- Choose a compact example that exposes the algorithm's important semantic
  trap, not merely its happy path.
- Derive the method from the contract before showing mechanics.
- Make every transition explain what changed and why it was legal.
- Use `insight` for correctness, prediction, or tradeoff reasoning that is not
  already visible in the scene.
- Keep phases conceptual and few; keep steps atomic enough that one visible
  change has one explanation.
- Give pivotal reasoning steps more viewing time with `duration_ms`.
- Preserve the algorithm's invariant throughout the authored state.
- End by connecting the returned answer to the promised complexity.
- Use theme tokens, text labels, and shapes so color is never the only signal.

## Adding a walkthrough

1. Select the smallest existing renderer that represents the algorithm.
2. Add `visualization.json` to the canonical problem package.
3. Point `code.source_path` at a real `solutions/*` artifact.
4. Author unique semantic anchors and a representative trace.
5. Add route-level regression assertions for the renderer's important
   correctness and teaching properties.
6. Verify the full player in light and dark themes, at desktop and narrow
   widths, including autoplay, manual stepping, scrubbing, keyboard controls,
   speed changes, and reduced motion.

If no renderer fits, add a strict backend state model, a matching discriminated
TypeScript definition, one renderer component, and one registry case. Do not
fork the player, controls, narration, phase timeline, or Monaco code stage.

## Validation

```powershell
.\.venv\Scripts\python.exe -m pytest server\tests\test_visualizations.py -q
npm.cmd run build --prefix web
npm.cmd run build --prefix electron
.\.venv\Scripts\python.exe -m ruff check engine server challenges tools tests
git diff --check
```
