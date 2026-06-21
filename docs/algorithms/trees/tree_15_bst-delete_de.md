# Knoten in einem BST löschen

| | |
|---|---|
| **ID** | `tree_15` |
| **Kategorie** | Bäume |
| **Komplexität (erforderlich)** | $O(H)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/) |

## Problemstellung

Gegeben ist eine Referenz auf den `root`-Knoten eines BST und ein `key`. Löschen Sie den Knoten mit dem gegebenen Schlüssel im BST. Geben Sie die (möglicherweise aktualisierte) `root`-Knotenreferenz des BST zurück.
Die Löschung muss die Eigenschaften des Binary Search Tree perfekt beibehalten.

**Eingabe:** Ein BST `root`-Knoten und ein Integer `key`.
**Ausgabe:** Der Wurzelknoten des modifizierten BST.

## Wann man es verwendet

- Um die heilige Dreifaltigkeit der Datenstruktur-Operationen (Suchen, Einfügen, Löschen) zu vervollständigen.
- Als rigoroser Test Ihrer Fähigkeit, komplexe Pointer-Neuzuweisungen und Randfälle in einer Baumtopologie zu handhaben.

## Ansatz

**1. Den Knoten finden:**
Zuerst müssen wir den zu löschenden Knoten tatsächlich finden! Dies ist eine einfache binäre Suche (`tree_06`).
- Wenn `key < root.val`, befindet sich der zu löschende Knoten im linken Teilbaum: `root.left = delete(root.left, key)`.
- Wenn `key > root.val`, befindet er sich im rechten Teilbaum: `root.right = delete(root.right, key)`.

**2. Die drei Fälle der Löschung:**
Sobald wir den Knoten gefunden haben (`root.val == key`), stehen wir vor 3 völlig unterschiedlichen topologischen Szenarien!

- **Fall 1: Der Knoten ist ein Blatt (keine Kinder).**
  Dies ist trivial! Löschen Sie ihn einfach. Wir geben `null` an den Elternknoten zurück, wodurch die Verbindung effektiv getrennt wird.

- **Fall 2: Der Knoten hat genau EIN Kind.**
  Ebenfalls einfach! Wenn wir den Knoten löschen, würde sein einziges Kind "in der Luft hängen". Wir nehmen einfach dieses Kind und verbinden es direkt mit dem Elternknoten des gelöschten Knotens! Wir geben das nicht-null Kind zurück.

- **Fall 3: Der Knoten hat ZWEI Kinder.**
  Dies ist das Albtraumszenario! Wir können nicht beide Kinder an den Elternknoten zurückgeben (ein Elternknoten in einem Binärbaum kann nur einen linken Pointer haben!). Wir müssen den Baum komplett umstrukturieren!
  Anstatt den Knoten strukturell zu löschen, **überschreiben wir seinen Wert**!
  Welchen Wert können wir stehlen, der mathematisch die BST-Eigenschaft beibehält?
  Wir benötigen eine Zahl, die etwas größer als der aktuelle Knoten, aber kleiner als alles andere im rechten Teilbaum ist. Dies nennt man den **In-Order Successor** (In-Order-Nachfolger)!
  Der In-Order Successor wird gefunden, indem man in den rechten Teilbaum geht und so weit wie physikalisch möglich nach LINKS wandert.
  Wir kopieren den Wert des Successors in unseren aktuellen Knoten. Dann rufen wir rekursiv die Löschfunktion für den rechten Teilbaum auf, um den ursprünglichen Successor-Knoten physisch zu löschen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_15: BST Delete.

Delete a key from a BST. The setup picks a key that is in
the tree; the canonical solve removes it. Three cases:
leaf (just drop), one child (replace with child), two
children (replace with inorder successor).

Tree is given as a binary shape: children[i] = [left, right]
where -1 means absent.
"""


def solve(children, values, root, n, key):
    """Delete `key` from the BST. Return (new_children, new_values)."""
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        return new_children, new_values
    # Find the node to delete and its parent.
    u = root
    parent = -1
    while u != -1 and new_values[u] != key:
        parent = u
        u = new_children[u][0] if key < new_values[u] else new_children[u][1]
    if u == -1:
        return new_children, new_values  # not found
    left = new_children[u][0]
    right = new_children[u][1]
    if left == -1 and right == -1:
        # Leaf case.
        if parent == -1:
            return [], []
        if new_children[parent][0] == u:
            new_children[parent][0] = -1
        else:
            new_children[parent][1] = -1
    elif left == -1 or right == -1:
        # One child case.
        child = left if left != -1 else right
        if parent == -1:
            new_children[u] = [-1, -1]
        elif new_children[parent][0] == u:
            new_children[parent][0] = child
        else:
            new_children[parent][1] = child
    else:
        # Two children case: replace value with inorder successor
        # and unlink the successor.
        succ_parent = u
        succ = right
        while new_children[succ][0] != -1:
            succ_parent = succ
            succ = new_children[succ][0]
        new_values[u] = new_values[succ]
        if succ_parent == u:
            new_children[u][1] = new_children[succ][1]
        else:
            new_children[succ_parent][0] = new_children[succ][1]
    return new_children, new_values
```

</details>

## Durchlauf

Baum:
```text
      5
    /   \
   3     6
  / \     \
 2   4     7
```
`delete(5)`:
1. `root` ist `5`. `key == 5`. Knoten gefunden!
2. Hat er 2 Kinder? Ja (`3` und `6`). (Fall 3).
3. Successor finden: Gehe nach rechts zu `6`, dann so weit wie möglich nach links.
   `6` hat kein linkes Kind. Also IST `6` der Successor!
4. Wert der Wurzel überschreiben: `root.val` wird zu `6`.
5. Rekursiv den Wert des Successors (`6`) aus dem rechten Teilbaum löschen:
   - Aufruf `deleteNode(root.right, 6)`.
   - `root` ist `6`. `key == 6`. Knoten gefunden!
   - Hat `6` 1 Kind? Ja, das rechte Kind `7`. (Fall 2).
   - Gib `7` zurück.
6. `root.right` wird zu `7`.

Resultierender Baum:
```text
      6
    /   \
   3     7
  / \
 2   4
```
BST-Eigenschaften perfekt beibehalten! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Der Algorithmus erfordert das Durchlaufen des Baums, um den Knoten zu finden, und möglicherweise ein weiteres Durchlaufen, um den Successor zu finden.
Die maximale Anzahl der besuchten Knoten entspricht der Höhe des Baums $O(H)$.
In einem balancierten Baum ist die Zeitkomplexität $O(\log N)$.
In einem entarteten, Linked-List-ähnlichen Baum verschlechtert sich die Zeitkomplexität auf $O(N)$.
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack $O(H)$ begrenzt, was im Durchschnitt $O(\log N)$ und im schlechtesten Fall $O(N)$ entspricht. (Dies kann durch einen iterativen Ansatz mit Eltern-Pointern auf $O(1)$ Platz optimiert werden, aber der Code wird dadurch extrem komplex).

## Varianten & Optimierungen

- **In-Order Predecessor:** Anstatt den kleinsten Wert aus dem rechten Teilbaum (Successor) zu stehlen, können Sie mathematisch den GRÖSSTEN Wert aus dem LINKEN Teilbaum (Predecessor) stehlen! Gehen Sie einmal nach links, dann so weit wie möglich nach rechts. Es funktioniert identisch!

## Anwendungen in der Praxis

- **Löschen von Datenbankzeilen:** In SQL-Datenbanken, die B-Tree-Indizierung verwenden, nutzt das Löschen einer Zeile eine verallgemeinerte Version genau dieses Algorithmus, um die Baumseiten umzustrukturieren und Knoten physisch zusammenzuführen, falls eine Seite zu leer wird.

## Verwandte Algorithmen in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — Die wesentlich einfachere Operation des Hinzufügens eines Knotens.
- **[tree_22 - AVL Insert](tree_22_avl-insert-simplified.md)** — In einem selbstbalancierenden Baum müssen Sie nach dem Löschen des Knotens mit diesem Algorithmus den Baum rückwärts nach oben verfolgen und physische Rotationen durchführen, um ihn neu zu balancieren!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*