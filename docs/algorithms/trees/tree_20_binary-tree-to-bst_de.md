# Konvertierung eines Binary Tree in einen BST

| | |
|---|---|
| **ID** | `tree_20` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Binary Tree to Binary Search Tree Conversion](https://www.geeksforgeeks.org/binary-tree-to-binary-search-tree-conversion/) |

## Problemstellung

Gegeben ist ein Standard-Binary Tree. Dieser soll in einen Binary Search Tree (BST) umgewandelt werden, wobei die ursprüngliche topologische Struktur des Baums vollständig erhalten bleiben muss.
(Sie dürfen die Pointer oder Knoten nicht umstrukturieren; Sie können lediglich die Werte innerhalb der Knoten überschreiben.)

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Derselbe `root`-Knoten, jedoch mit Werten, die so angeordnet sind, dass sie einen BST bilden.

## Anwendungsbereiche

- Zur Überprüfung des fundamentalen Verständnisses eines In-Order-Durchlaufs: **Ein In-Order-Durchlauf eines Binary Search Tree liefert immer ein perfekt sortiertes Array.**
- Um schnell unorganisierte Baumdaten zu bereinigen, ohne neue Speicherbereiche für Knoten zu allokieren oder komplexe Pointer-Strukturen umbauen zu müssen.

## Ansatz

**1. Die In-Order-Eigenschaft:**
Wenn wir einen gültigen BST haben und einen In-Order-Durchlauf (`Left -> Root -> Right`) durchführen, sind die gelesenen Werte perfekt von klein nach groß sortiert!
Diese mathematische Eigenschaft funktioniert in beide Richtungen! Wenn wir die exakte topologische Form eines Baums haben, einen In-Order-Durchlauf durchführen und während des Besuchs der Knoten physisch eine sortierte Liste von Werten in die Knoten SCHREIBEN, ist der resultierende Baum mathematisch garantiert ein gültiger BST!

**2. Der Drei-Schritte-Prozess:**
1. **Extrahieren:** Durchlaufen Sie den ursprünglichen Binary Tree (unter Verwendung eines beliebigen Durchlaufs, z. B. Pre-Order oder BFS) und extrahieren Sie alle Knotenwerte in ein Array.
2. **Sortieren:** Sortieren Sie das extrahierte Array von Werten in aufsteigender Reihenfolge.
3. **Injizieren:** Führen Sie einen strikten In-Order-Durchlauf (`tree_02`) auf dem ursprünglichen Baum durch. Während Sie jeden Knoten besuchen, überschreiben Sie dessen Wert mit dem nächsten Wert aus Ihrem perfekt sortierten Array!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_20: Binary Tree to BST.

Convert a binary tree to a binary SEARCH tree holding the
same values. In-order walk to collect nodes; sort values;
walk in-order again, replacing each node's value with
the next sorted value.
"""


def solve(children, values, root, n):
    if n == 0 or root == -1:
        return [], []
    out = []

    def collect(i):
        if i == -1:
            return
        collect(children[i][0])
        out.append(i)
        collect(children[i][1])
    collect(root)
    sorted_vals = sorted(values)
    new_values = list(values)
    for idx, node in enumerate(out):
        new_values[node] = sorted_vals[idx]
    return list(children), new_values
```

</details>

## Durchlauf

Ursprünglicher Baum (kein BST):
```text
      10
     /  \
    30   15
   /      \
  20       5
```

1. **Extrahieren:** Alle Werte lesen. `values = [10, 30, 20, 15, 5]`.
2. **Sortieren:** `values = [5, 10, 15, 20, 30]`.
3. **Injizieren (In-Order-Durchlauf):**
   - Gehe zum tiefsten linken Knoten: `20`. Überschreibe mit `values[0]` (`5`).
   - Gehe zum Elternknoten: `30`. Überschreibe mit `values[1]` (`10`).
   - Das rechte Kind von `30` ist null.
   - Gehe zur Wurzel: `10`. Überschreibe mit `values[2]` (`15`).
   - Gehe zum rechten Teilbaum, `15`. Gehe tief nach links (null).
   - Verarbeite `15`: Überschreibe mit `values[3]` (`20`).
   - Gehe zum rechten Kind: `5`. Überschreibe mit `values[4]` (`30`).

Resultierender Baum:
```text
      15
     /  \
    10   20
   /      \
  5       30
```
Es ist ein perfekter BST! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Schritt 1 (Extraktion) benötigt $O(N)$ Zeit.
Schritt 2 (Sortierung) benötigt $O(N \log N)$ Zeit.
Schritt 3 (Injektion) benötigt $O(N)$ Zeit.
Die gesamte Zeitkomplexität wird durch den Sortierschritt dominiert: $O(N \log N)$.
Die Platzkomplexität beträgt strikt $O(N)$, da wir ein zusätzliches Array erstellen müssen, um alle $N$ Werte für die Sortierung zu speichern.

## Varianten & Optimierungen

- **Konvertierung eines sortierten Arrays in einen BST:** Wenn Sie ein sortiertes Array erhalten und einen komplett neuen, balancierten BST von Grund auf neu konstruieren sollen (Sie sind nicht durch eine bestehende Topologie eingeschränkt), verwenden Sie diesen Algorithmus nicht! Sie wählen einfach das mittlere Element als Wurzel und bauen rekursiv die linke und rechte Hälfte auf. Dies benötigt exakt $O(N)$ Zeit!
- **In-Place Umstrukturierung (Day-Stout-Warren-Algorithmus):** Sie können einen Binary Tree tatsächlich in $O(N)$ Zeit und $O(1)$ Platz in einen perfekt balancierten BST umwandeln, indem Sie Baumrotationen verwenden, um den Baum in eine Linked List (eine "Rebe" bzw. "Vine") zu verwandeln und ihn dann zurück in einen balancierten Baum zu rotieren. Dies ist jedoch extrem komplex.

## Praxisanwendungen

- **Datenbereinigung:** In der Spieleentwicklung können Sie, falls ein räumlicher Partitionierungsbaum aufgrund von Fehlern in der Physik-Engine beschädigt wurde, die Bounding Boxes der Knoten schnell retten und neu sortieren, ohne neuen Speicher zu allokieren.

## Verwandte Algorithmen in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Die Engine, die die BST-Ordnungseigenschaft erzwingt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*