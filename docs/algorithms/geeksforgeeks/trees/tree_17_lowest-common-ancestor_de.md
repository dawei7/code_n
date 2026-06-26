# Lowest Common Ancestor eines Binary Tree

| | |
|---|---|
| **ID** | `tree_17` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |

## Problemstellung

Gegeben ist ein Binary Tree. Finde den Lowest Common Ancestor (LCA) zweier gegebener Knoten `p` und `q` im Baum.
Der Lowest Common Ancestor ist für zwei Knoten `p` und `q` als der tiefste Knoten in `T` definiert, der sowohl `p` als auch `q` als Nachfahren hat (wobei ein Knoten auch als Nachfahre seiner selbst gilt).
Es ist mathematisch garantiert, dass `p` und `q` im Baum existieren und `p != q` gilt.

**Eingabe:** Ein `root`-Knoten eines Binary Tree sowie zwei Zielknoten `p` und `q`.
**Ausgabe:** Der `TreeNode`, der den LCA repräsentiert.

## Wann wird es verwendet?

- Um den kürzesten Pfad oder die Distanz zwischen zwei beliebigen Knoten in einem Baum zu finden.
- Eines der am häufigsten gestellten, eleganten rekursiven DFS-Probleme in der gesamten Informatik.

## Ansatz

**1. Die "Reporting"-Rekursion:**
Stellen Sie sich einen Vorgesetzten (die Root) vor, der seine beiden Manager (linkes Kind, rechtes Kind) fragt: "Durchsucht eure Abteilungen und sagt mir, ob ihr Mitarbeiter P oder Mitarbeiter Q findet!"
Wir schreiben eine rekursive DFS-Funktion. Wenn sie einen Knoten besucht:
- Wenn der Knoten `null` ist, gib `null` zurück. (Sackgasse, niemanden gefunden).
- Wenn der Knoten `p` ODER `q` IST, gib den Knoten selbst zurück! (Ich habe einen von beiden gefunden! Melde es nach oben!).

**2. Die drei Szenarien für einen Elternknoten:**
Wenn ein Elternknoten die Berichte seiner linken und rechten Teilbäume erhält, steht er vor genau drei Szenarien:

- **Szenario 1: Sowohl links als auch rechts wurde ein nicht-null Knoten zurückgegeben.**
  Der linke Teilbaum hat `p` gefunden. Der rechte Teilbaum hat `q` gefunden.
  Was bedeutet das? Es bedeutet, dass DIESER KNOTEN der Punkt ist, an dem sich die Pfade trennen! DIESER Knoten ist mathematisch gesehen der Lowest Common Ancestor! Der Elternknoten gibt SICH SELBST an die Kette weiter nach oben zurück!
  
- **Szenario 2: Eine Seite gab einen Knoten zurück, die andere `null`.**
  Der linke Teilbaum hat jemanden gefunden (vielleicht `p`, vielleicht `q`, oder der LCA wurde bereits tief unten gefunden und wird nach oben durchgereicht). Der rechte Teilbaum hat nichts gefunden.
  Was macht der Elternknoten? Er reicht den erfolgreichen Bericht einfach nach oben weiter! Gib die Seite zurück, die nicht `null` ist!
  
- **Szenario 3: Beide Seiten gaben `null` zurück.**
  In keinem der Teilbäume wurde jemand gefunden. Gib `null` an die Kette nach oben zurück.

**3. Der Spezialfall "Nachfahre seiner selbst":**
Was ist, wenn `p = 5` und `q = 4`, aber `4` tatsächlich ein direktes Kind von `5` ist?
Wenn die DFS `5` erreicht, gibt sie sofort `5` zurück! Sie bricht die Suche komplett ab und findet `4` gar nicht erst!
Ist das ein Fehler? NEIN! Es ist ein geniales Feature! Wenn `q` ein Kind von `p` ist, dann IST `p` mathematisch gesehen der Lowest Common Ancestor! Indem `p` sofort zurückgegeben wird, wird es korrekt als Antwort bis zur Root nach oben durchgereicht!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_17: Lowest Common Ancestor.

Return the index of the LCA of two nodes in a binary tree.
Walk the tree; find the path from the root to each node, and
take the last common node on both paths.
"""


def solve(children, root, n, p, q):
    """Return the LCA of p and q in a binary tree."""
    if root == -1:
        return -1

    def path_to(u, target):
        if u == -1:
            return None
        if u == target:
            return [u]
        left = path_to(children[u][0], target)
        if left is not None:
            return [u] + left
        right = path_to(children[u][1], target)
        if right is not None:
            return [u] + right
        return None

    pp = path_to(root, p)
    pq = path_to(root, q)
    if pp is None or pq is None:
        return -1
    last = -1
    for a, b in zip(pp, pq):
        if a == b:
            last = a
        else:
            break
    return last
```

</details>

## Walk-through

Baum:
```text
      3
    /   \
   5     1
  / \   / \
 6   2 0   8
    / \
   7   4
```
`p = 6`, `q = 4`.

1. **`dfs(3)`:** Ruft links (5) und rechts (1) auf.
   2. **`dfs(1)`:** Weder P noch Q. Ruft links (0) und rechts (8) auf. Beide geben null zurück.
      - Gibt `null` zurück.
   3. **`dfs(5)`:** Weder P noch Q. Ruft links (6) und rechts (2) auf.
      4. **`dfs(6)`:** Moment! Knoten ist P (6)! Gibt sofort Knoten `6` zurück.
      5. **`dfs(2)`:** Ruft links (7) und rechts (4) auf.
         6. **`dfs(7)`:** Gibt null zurück.
         7. **`dfs(4)`:** Knoten ist Q (4)! Gibt Knoten `4` zurück.
      - `dfs(2)` erhält `null` von links, `4` von rechts.
      - Gibt `4` nach oben zurück.
   - `dfs(5)` erhält `6` von links, `4` von rechts!
   - Beide sind NICHT-NULL! Knoten 5 erkennt, dass ER DER LCA IST!
   - Gibt `node 5` nach oben zurück!
- `dfs(3)` erhält `node 5` von links, `null` von rechts.
- Gibt `node 5` nach oben zurück.

Der Root-Aufruf gibt `node 5` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Im schlechtesten Fall (wenn `p` und `q` tiefe Blätter sind), besucht die DFS jeden einzelnen Knoten im Baum genau einmal. Die Zeitkomplexität beträgt exakt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack $O(H)$ begrenzt. Der durchschnittliche Fall ist $O(\log N)$ bei balancierten Bäumen. Der schlechteste Fall ist $O(N)$ bei entarteten (skewed) Bäumen.

## Varianten & Optimierungen

- **LCA eines Binary Search Tree (BST) ($O(\log N)$):** Wenn der Baum ein BST ist, benötigen Sie KEINE DFS! Sie starten einfach bei der Root. Wenn sowohl P als auch Q kleiner als die Root sind, gehen Sie nach links. Wenn beide größer sind, gehen Sie nach rechts. Der ERSTE Knoten, auf den Sie treffen, an dem sich die Pfade von P und Q trennen, ist mathematisch garantiert der LCA! Dies benötigt $O(\log N)$ Zeit und $O(1)$ Platz!
- **LCA mit Parent-Pointern:** Wenn jeder `TreeNode` einen `parent`-Pointer besitzt, verwandelt sich dieses Problem sofort in **Intersection of Two Linked Lists (`linkedlist_06`)**! Sie verfolgen P bis zur Root, verfolgen Q bis zur Root und finden den ersten gemeinsamen Knoten!

## Anwendungen in der Praxis

- **CSS / DOM Event Bubbling:** Finden des exakten HTML-DOM-Containers, der zwei angeklickte Elemente umschließt, um einen gemeinsamen UI-Effekt anzuwenden.
- **Git Merge / Versionskontrolle:** Wenn sich Branch A und Branch B auseinanderentwickelt haben, muss Git deren Lowest Common Ancestor Commit finden, um einen intelligenten 3-Wege-Merge durchzuführen!

## Verwandte Algorithmen in cOde(n)

- **[tree_03 - Post-order Traversal](tree_03_postorder-traversal.md)** — Der Kernmechanismus (zuerst Kinder verarbeiten, dann den Elternknoten auswerten), der verwendet wird, um die Berichte "nach oben durchzureichen".

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*