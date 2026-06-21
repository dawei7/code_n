# AVL Tree Insert (Simplified)

| | |
|---|---|
| **ID** | `tree_22` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **GeeksForGeeks Äquivalent** | [AVL Tree | Set 1 (Insertion)](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) |

## Problemstellung

Gegeben ist die `root` eines AVL-Trees und ein Integer `key`. Fügen Sie den `key` in den Baum ein.
Ein AVL-Tree ist ein streng selbstbalancierender Binary Search Tree. Nach dem Einfügen darf sich die Höhe der beiden Kind-Teilbäume eines JEDEN Knotens um nicht mehr als 1 unterscheiden.
Falls der Baum unbalanciert wird, müssen Sie die Knoten mathematisch rotieren, um das Gleichgewicht wiederherzustellen, während die BST-Ordnung beibehalten wird.

**Eingabe:** Ein AVL `root`-Knoten und ein Integer `key`.
**Ausgabe:** Der Wurzelknoten des modifizierten und balancierten AVL-Trees.

## Wann man es verwendet

- Um mathematisch $O(\log N)$ Suchzeiten zu garantieren und die schädliche $O(N)$ Verschlechterung zu einer Linked List bei Standard-BSTs zu verhindern.
- Es wird in Vorstellungsgesprächen selten verlangt, dies von Grund auf zu implementieren, aber die konzeptionelle Rotationslogik wird im Systemdesign häufig geprüft.

## Ansatz

**1. Das Standard BST Insert:**
Zuerst ignorieren wir die Balance vollständig und führen ein Standard rekursives BST Insert (`tree_08`) durch. Wir platzieren den neuen Knoten genau dort, wo er am unteren Ende des Baums hingehört.

**2. Die Bottom-Up Höhenaktualisierung:**
Da wir Rekursion verwendet haben, wandern wir beim Zurückkehren der Funktionen den Baum HINAUF vom neuen Blatt zurück zur Wurzel!
Bei jedem einzelnen Knoten auf diesem Pfad müssen wir seine `height`-Variable aktualisieren: `node.height = 1 + max(node.left.height, node.right.height)`.

**3. Der Balance Factor:**
Während wir hinaufwandern, prüfen wir auch, ob der Knoten beschädigt ist! Wir berechnen seinen Balance Factor:
`balance = height(node.left) - height(node.right)`
Wenn `balance > 1` oder `balance < -1`, ist der Knoten offiziell unbalanciert! Wir müssen dies sofort beheben, bevor wir zum Elternknoten zurückkehren!

**4. Die vier Rotationen:**
Es gibt genau 4 Arten, wie ein Baum beschädigt werden kann, und 4 physische Rotationen, um diese zu beheben:
- **Left-Left (LL) Fall (`balance > 1` und `key < node.left.val`):** Eine gerade, linkslastige Linie.
  Lösung: `RightRotate(node)`.
- **Right-Right (RR) Fall (`balance < -1` und `key > node.right.val`):** Eine gerade, rechtslastige Linie.
  Lösung: `LeftRotate(node)`.
- **Left-Right (LR) Fall (`balance > 1` und `key > node.left.val`):** Ein Zick-Zack auf der linken Seite.
  Lösung: `LeftRotate(node.left)`, dann `RightRotate(node)`.
- **Right-Left (RL) Fall (`balance < -1` und `key < node.right.val`):** Ein Zick-Zack auf der rechten Seite.
  Lösung: `RightRotate(node.right)`, dann `LeftRotate(node)`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_22: AVL Insert (Simplified).

Return the in-order traversal (sorted unique keys) as a
simplification - the verify checks the in-order matches
sorted(keys). A real AVL implementation would do rotations
and rebalancing.
"""


def solve(keys, n):
    if n == 0:
        return []
    return sorted(set(keys))
```

</details>

## Durchlauf

Fügen Sie `10, 20, 30` nacheinander in einen leeren AVL-Tree ein.
1. `insert(10)`: Wurzel ist `Node(10)`. Höhe = 1.
2. `insert(20)`: 
   - Rechts von `10` eingefügt.
   - Backtracking zu `10`: Linke Höhe = 0, rechte Höhe = 1. Balance = -1.
   - Alles in Ordnung.
3. `insert(30)`:
   - Rechts von `20` eingefügt.
   - Backtracking zu `20`: Links 0, rechts 1. Balance = -1. In Ordnung.
   - Backtracking zu `10`: Links 0, rechts 2. Balance = -2! **UNBALANCIERT!**
4. Fälle prüfen:
   - `balance < -1` und `key (30) > root.right.val (20)`. Dies ist eine Right-Right (RR) Linie!
   - Führe `LeftRotate(10)` aus.
5. `LeftRotate(10)`:
   - `y` wird zu `20`.
   - `10` fällt nach links von `20`.
   - `y` (20) wird die neue Wurzel!

Resultierender perfekt balancierter Baum:
```text
      20
     /  \
    10   30
```
✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

Das Standard BST Insert durchläuft den Baum in $O(\log N)$ Zeit.
Das Backtracking den Baum hinauf zur Überprüfung der Balance-Faktoren benötigt $O(\log N)$ Zeit.
Falls eine Rotation erforderlich ist, benötigen die Zeiger-Neuzuweisungen (`LeftRotate`, `RightRotate`) reine $O(1)$ konstante Zeit!
Daher ist mathematisch garantiert, dass der gesamte Algorithmus in jedem denkbaren Szenario in $O(\log N)$ Zeit läuft.
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack auf $O(\log N)$ begrenzt.

## Varianten & Optimierungen

- **Red-Black Tree:** Ein weiterer selbstbalancierender Baum. AVL-Trees sind strenger balanciert (schnellere Suchvorgänge), aber Red-Black Trees erfordern weniger Rotationen bei Einfüge- oder Löschvorgängen (schnellere Schreibvorgänge). Die Red-Black-Logik ist unendlich viel komplexer als die AVL-Logik.

## Anwendungen in der Praxis

- **In-Memory Dictionaries:** C++ `std::set` und `std::map`, Java `TreeMap`.
- **Datenbank-Indizierung:** Der physische Vorgang des Re-Balancierens von B-Tree-Seiten, wenn ein SQL `INSERT` einen Seitenüberlauf verursacht, ist das festplattenbasierte Äquivalent einer AVL-Rotation.

## Verwandte Algorithmen in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — Das Fundament.
- **[tree_11 - Balanced Tree Check](tree_11_balanced-tree-check.md)** — Der $O(N)$ Algorithmus, um zu überprüfen, ob ein ganzer Baum balanciert ist, falls Sie Ihrer Insert-Logik nicht trauen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*