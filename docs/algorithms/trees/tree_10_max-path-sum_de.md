# Binary Tree Maximum Path Sum

| | |
|---|---|
| **ID** | `tree_10` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) |

## Problemstellung

Gegeben ist der `root` eines Binary Tree. Geben Sie die **maximale Pfadsumme** eines beliebigen, nicht leeren Pfades zurück.
Ein Pfad ist definiert als eine beliebige Sequenz benachbarter Knoten (verbunden durch Kanten). Der Pfad kann an JEDEM Knoten im Baum beginnen und enden. Er muss nicht durch den `root` verlaufen.
Eine Pfadsumme ist die Summe der Werte der Knoten innerhalb des Pfades.

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Eine Ganzzahl, die die maximale Pfadsumme repräsentiert.

## Wann man es verwendet

- Das absolut schwierigste "Standard"-Problem für Binary Trees, dem Sie in einem FAANG-Vorstellungsgespräch begegnen werden.
- Ein exzellenter Test für Bottom-Up Post-Order DFS in Kombination mit dem Pruning (Beschneiden) negativer Zahlen.

## Ansatz

**1. Das "Bogen" vs. "Zweig"-Problem:**
Dieses Problem ist mathematisch identisch mit der Bestimmung des **Durchmessers eines Baumes (`tree_07`)**. Der maximale Pfad sieht aus wie ein riesiger "Bogen", der von einem Knoten auf der linken Seite ausgeht, NACH OBEN zu einem verbindenden `root` führt und NACH UNTEN zu einem Knoten auf der rechten Seite verläuft.
Für jeden beliebigen Knoten ist der maximale Bogen, der *durch* ihn hindurchgeht: `(Maximaler Pfad nach links unten) + (Knotenwert) + (Maximaler Pfad nach rechts unten)`.
Wenn ein Knoten jedoch einen Wert NACH OBEN an seinen Elternknoten zurückgibt, darf er KEINEN Bogen zurückgeben! Ein Pfad kann sich nicht in drei Richtungen verzweigen! Er kann nur eine gerade Linie (einen "Zweig") zurückgeben. Der Elternknoten muss wählen, ob er sich mit dem linken Zweig ODER dem rechten Zweig verbindet!

**2. Die Bottom-Up-Rekursion:**
Wir schreiben eine rekursive DFS-Funktion, die den maximalen "geraden Zweig" zurückgibt, der von einem Knoten nach unten führt.
- `left_branch = dfs(node.left)`
- `right_branch = dfs(node.right)`
Was gibt dieser Knoten an seinen Elternknoten zurück? Er gibt `node.val + max(left_branch, right_branch)` zurück.

**3. Die globale "Bogen"-Berechnung:**
Während wir diese Zweige berechnen, was ist der maximale "Bogen", der physisch vollständig DURCH diesen Knoten verlaufen kann?
Es ist `left_branch + node.val + right_branch`!
Wir berechnen diesen Bogenwert an jedem einzelnen Knoten und aktualisieren eine globale `max_sum`-Variable!

**4. Die Falle mit negativen Zahlen:**
Was ist, wenn `left_branch` gleich `-50` ist? Wenn wir `-50` zu unserem Bogen oder unserem zurückgegebenen Zweig addieren, verschlechtern wir unsere Summe definitiv!
Im Gegensatz zum Durchmesser-Problem (das Kanten zählt), verwendet dieses Problem Knotenwerte, die negativ sein können!
Wenn ein Kindknoten einen negativen Pfad zurückgibt, IGNORIEREN wir ihn einfach! Wir verhalten uns so, als ob der Zweig nicht existiert. Wir "beschneiden" ihn, indem wir `max(0, branch_sum)` verwenden.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_10: Max Path Sum.

Max root-to-leaf path sum (non-negative values).
"""


def solve(children, values, root, n):
    best = 0

    def walk(u):
        nonlocal best
        if not children[u]:
            if values[u] > best:
                best = values[u]
            return values[u]
        child_sums = [walk(v) for v in children[u]]
        s = values[u] + max(child_sums)
        if s > best:
            best = s
        return s

    walk(root)
    return best
```

</details>

## Durchlauf

Baum:
```text
     -10
     /  \
    9   20
       /  \
      15   7
```

1. **`dfs(15)`:**
   - Links null (0), Rechts null (0).
   - `local_arch_sum = 0 + 15 + 0 = 15`. `max_sum = 15`.
   - Gibt zurück: `15 + max(0, 0) = 15`.
2. **`dfs(7)`:**
   - Links null (0), Rechts null (0).
   - `local_arch_sum = 0 + 7 + 0 = 7`. `max_sum = max(15, 7) = 15`.
   - Gibt zurück: `7 + max(0, 0) = 7`.
3. **`dfs(20)`:**
   - Linker Zweig ist 15. Rechter Zweig ist 7.
   - `local_arch_sum = 15 + 20 + 7 = 42`. `max_sum = max(15, 42) = 42`.
   - Gibt zurück: `20 + max(15, 7) = 35`. *(Er sagt seinem Elternknoten: "Wenn du dich mit mir verbindest, ist der beste Pfad nach unten 35")*.
4. **`dfs(9)`:**
   - Links null (0), Rechts null (0).
   - `local_arch_sum = 9`. `max_sum = 42`.
   - Gibt zurück: `9`.
5. **`dfs(-10)` (Root):**
   - Linker Zweig ist 9. Rechter Zweig ist 35.
   - `local_arch_sum = 9 + (-10) + 35 = 34`. `max_sum = max(42, 34) = 42`.
   - Gibt zurück: `-10 + max(9, 35) = 25`.

Rekursion endet. Rückgabe `max_sum = 42`. ✓
*(Der Pfad ist `15 -> 20 -> 7`)*.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die DFS-Traversierung besucht jeden einzelnen Knoten genau einmal. An jedem Knoten werden $O(1)$ Additionen und `max()`-Operationen in konstanter Zeit durchgeführt.
Die Zeitkomplexität beträgt exakt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack begrenzt, welcher der Höhe des Baumes $O(H)$ entspricht. Im durchschnittlichen/besten Fall (ausgeglichener Baum) ist der Platzbedarf $O(\log N)$. Im schlechtesten Fall (einseitig ausgeprägter Baum) verschlechtert er sich auf $O(N)$.

## Varianten & Optimierungen

- **Kadane-Algorithmus für Arrays (`dynamic_04`):** Dieses Baum-Problem ist eigentlich eine direkte, topologische Weiterentwicklung der Suche nach der maximalen Teilsumme (Maximum Subarray Sum) in einem 1D-Array! Die Logik von `max(0, branch)` ist exakt dieselbe Logik wie "setze die laufende Summe auf 0 zurück, wenn sie negativ wird".

## Anwendungen in der Praxis

- **Logistik in Lieferketten:** Finden der profitabelsten kontinuierlichen Transportroute durch ein stark verzweigtes Verteilungsnetzwerk, bei dem einige Knoten (Maut/Steuern) negative Werte und andere (Städte) positive Gewinne aufweisen.

## Verwandte Algorithmen in cOde(n)

- **[tree_07 - Tree Diameter](tree_07_tree-diameter.md)** — Derselbe architektonische Ansatz, jedoch werden physische Kanten gezählt anstatt Werte zu summieren.
- **[dynamic_04 - Kadane's Algorithm](../dynamic/dp_04_maximum-subarray.md)** — Das 1D-Array-Äquivalent zu diesem Problem.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*