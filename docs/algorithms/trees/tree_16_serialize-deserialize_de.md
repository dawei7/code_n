# Serialize and Deserialize Binary Tree

| | |
|---|---|
| **ID** | `tree_16` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |

## Problemstellung

Entwerfen Sie einen Algorithmus zur Serialisierung und Deserialisierung eines Binary Tree.
Serialisierung ist der Prozess, bei dem eine Datenstruktur in eine Sequenz von Bits (oder einen String) umgewandelt wird, sodass sie in einer Datei gespeichert oder über ein Netzwerk übertragen werden kann.
Deserialisierung ist der Prozess, bei dem dieser String genommen und die exakte ursprüngliche Baumstruktur im Speicher rekonstruiert wird.

**Eingabe:** Ein Binary Tree `root` node (zur Serialisierung) oder ein `string` (zur Deserialisierung).
**Ausgabe:** Ein `string` (aus der Serialisierung) oder ein Binary Tree `root` node (aus der Deserialisierung).

## Wann man es verwendet

- Um den exakten topologischen Zustand einer Tree Data Structure auf einer Festplatte oder in einer Datenbank zu speichern.
- Als definitiver Test dafür, ob man wirklich verstanden hat, wie Tree Traversals auf 1D-Arrays abgebildet werden.

## Ansatz

**1. Das "Null"-Pointer-Problem:**
Wenn man einfach eine standardmäßige Pre-Order-Traversierung (`[1, 2, 3]`) durchführt, ist es mathematisch unmöglich, den Baum zu rekonstruieren! Warum? Weil `[1, 2, 3]` ein Baum sein könnte, bei dem 1 die Wurzel, 2 das linke Kind und 3 das linke Kind von 2 ist. ODER 1 ist die Wurzel, 2 das rechte Kind und 3 das rechte Kind von 2. Sie sehen identisch aus!
Der EINZIGE Weg, die Topologie eines Baums perfekt zu erfassen, besteht darin, EXAKT aufzuzeichnen, wo die Blätter enden, indem man `null`-Pointer explizit speichert!
Wir repräsentieren `null` als den String `"N"`.
Unsere Pre-Order-Serialisierung für `1 -> 2 -> null` lautet: `"1,2,N,N,N"`.

**2. Serialisierung (Baum zu String):**
Wir verwenden eine standardmäßige DFS Pre-Order-Traversierung.
1. Wenn der Node `null` ist, hängen wir `"N"` an unser Array an.
2. Andernfalls hängen wir `str(node.val)` an.
3. Rekursive Serialisierung des linken Kindes.
4. Rekursive Serialisierung des rechten Kindes.
Schließlich verbinden wir das Array mit Kommas: `"1,2,N,N,3,N,N"`.

**3. Deserialisierung (String zu Baum):**
Wir teilen den String anhand der Kommas in eine Queue von Werten (oder eine List mit einem Iterator) auf.
Da der String mittels Pre-Order (Wurzel, Links, Rechts) generiert wurde, ist das allererste Element in der Queue GARANTIERT die Wurzel!
Wir schreiben eine rekursive Funktion:
1. Entfernen des ersten Elements aus der Queue.
2. Wenn es `"N"` ist, geben wir `None` zurück (wir haben eine Blattgrenze erreicht).
3. Andernfalls erstellen wir einen neuen `TreeNode(val)`.
4. Rekursiver Aufruf der Funktion, um das `left` Kind zu bauen!
5. Rekursiver Aufruf der Funktion, um das `right` Kind zu bauen!
6. Rückgabe des konstruierten Node.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_16: Serialize / Deserialize.

Standard format: preorder traversal with 'N' for null,
comma-separated. The serialize-then-deserialize round-trip
preserves the structure on a valid binary tree. Deserialization
uses the original node indices from the tokens so the round-trip
is a structural identity.
"""


def solve(children, root, n):
    """Serialize the tree, then deserialize it. Return the new children list."""
    # Serialize: preorder with 'N' for null.
    parts = []

    def ser(u):
        if u == -1:
            parts.append("N")
            return
        parts.append(str(u))
        ser(children[u][0])
        ser(children[u][1])

    ser(root)
    tokens = ",".join(parts).split(",")

    # Deserialize: pre-register each new node at the index named
    # by the token, then recurse on left/right.
    idx = [0]
    new_children = []

    def build():
        tok = tokens[idx[0]]
        idx[0] += 1
        if tok == "N":
            return -1
        node_idx = int(tok)
        while len(new_children) <= node_idx:
            new_children.append([-1, -1])
        new_children[node_idx][0] = build()
        new_children[node_idx][1] = build()
        return node_idx

    build()
    return new_children
```

</details>

## Durchlauf

Baum:
```text
    1
   / \
  2   3
```

**Serialisierung:**
1. `dfs(1)`: Hänge `"1"` an.
   2. `dfs(2)`: Hänge `"2"` an.
      3. `dfs(null)`: Hänge `"N"` an.
      4. `dfs(null)`: Hänge `"N"` an.
   5. `dfs(3)`: Hänge `"3"` an.
      6. `dfs(null)`: Hänge `"N"` an.
      7. `dfs(null)`: Hänge `"N"` an.
String: `"1,2,N,N,3,N,N"`.

**Deserialisierung:**
`vals = ["1", "2", "N", "N", "3", "N", "N"]`. `i = 0`.
1. `dfs()` liest `"1"`. Erstellt `Node(1)`. Ruft `dfs()` für links auf.
   2. `dfs()` liest `"2"`. Erstellt `Node(2)`. Ruft `dfs()` für links auf.
      3. `dfs()` liest `"N"`. Gibt `None` zurück. (Node 2's linkes Kind ist null).
      4. `dfs()` liest `"N"`. Gibt `None` zurück. (Node 2's rechtes Kind ist null).
   5. Node 1's linkes Kind ist nun vollständig aufgebaut! Ruft `dfs()` für rechts auf.
   6. `dfs()` liest `"3"`. Erstellt `Node(3)`. Ruft `dfs()` für links auf.
      7. `dfs()` liest `"N"`. Gibt `None` zurück.
      8. `dfs()` liest `"N"`. Gibt `None` zurück.
   9. Node 1's rechtes Kind ist vollständig aufgebaut!
10. Gibt `Node(1)` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Sowohl bei der Serialisierung als auch bei der Deserialisierung verarbeiten wir jeden einzelnen Node genau einmal. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität erfordert $O(N)$ Speicher, um den massiven serialisierten String und das gesplittete Array physisch zu speichern. Der rekursive Aufruf-Stack benötigt ebenfalls $O(H)$ Platz, aber $O(N)$ dominiert.

## Varianten & Optimierungen

- **Level-Order-Serialisierung (BFS):** Die tatsächliche visuelle Darstellung von Bäumen in LeetCode (z. B. `[1, 2, 3, null, null, 4, 5]`) verwendet BFS! Sie können die Serialisierung mittels einer Queue durchführen. Anstatt nur gültige Nodes hinzuzufügen, fügen Sie auch `null`-Pointer hinzu. Während der Deserialisierung verwenden Sie eine Queue, um den Baum Ebene für Ebene zu rekonstruieren!
- **BST-Serialisierung ($O(N)$ Zeit, $O(1)$ String-Platz!):** Wenn garantiert ist, dass der Baum ein Binary Search Tree ist, müssen Sie KEINE `"N"`-Null-Marker speichern! Sie geben einfach einen standardmäßigen Pre-Order-String aus (`"5,3,2,4,7,6"`). Aufgrund der BST-Eigenschaft (`tree_06`) weiß der Deserialisierer mathematisch EXAKT, wann er aufhören muss, den linken Zweig zu bauen und zum rechten Zweig zu wechseln, indem er eine `max_bound` durch den rekursiven Stack weitergibt! Dies spart massiv Speicherplatz auf der Festplatte.

## Anwendungen in der Praxis

- **Network Payloads (JSON):** Jedes Mal, wenn eine Web-API ein komplexes, verschachteltes, hierarchisches JSON-Objekt an einen Frontend-Client sendet, durchläuft es genau diesen architektonischen Prozess der Umwandlung eines Speicher-Graphen in einen 1D-String und dessen Parsen zurück in den Speicher!

## Verwandte Algorithmen in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Die grundlegende Traversierungsstrategie, die in dieser spezifischen Implementierung verwendet wird.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — Die grundlegende Traversierungsstrategie, falls Sie sich entscheiden, die BFS-Variante stattdessen zu implementieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*