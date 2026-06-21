# Binärzahlen von 1 bis N generieren

| | |
|---|---|
| **ID** | `queue_03` |
| **Kategorie** | queue |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **LeetCode-Äquivalent** | N/A (Grundlagenübung) |

## Problemstellung

Gegeben ist eine Ganzzahl `N`. Generieren und zurückgeben Sie ein Array von Strings, das die binären Äquivalente aller Zahlen von `1` bis `N` in sequenzieller Reihenfolge enthält.
Verwenden Sie keine eingebauten Funktionen zur Basiskonvertierung (wie Pythons `bin()` oder C++ `itoa()`). Generieren Sie diese stattdessen unter Verwendung der strukturellen Eigenschaften von Queues.

**Eingabe:** Eine Ganzzahl `N`.
**Ausgabe:** Eine Liste von Strings.

**Beispiel:**
`N = 5`
Ausgabe: `["1", "10", "11", "100", "101"]`.

## Wann man dies verwendet

- Um zu verstehen, wie Queues auf natürliche Weise eine **Level-Order Traversal** (BFS) modellieren. Das Generieren von Binärzahlen ist identisch mit dem Durchlaufen eines perfekt balancierten Binärbaums.

## Ansatz

Betrachten Sie Binärzahlen als einen Baum:
- Die Wurzel ist `"1"`.
- Jeder Knoten hat ein linkes Kind (Anhängen von `"0"`) und ein rechtes Kind (Anhängen von `"1"`).
- Wurzel `"1"` -> Linkes Kind `"10"`, rechtes Kind `"11"`.
- `"10"` -> Linkes Kind `"100"`, rechtes Kind `"101"`.
- `"11"` -> Linkes Kind `"110"`, rechtes Kind `"111"`.

Dies generiert Binärzahlen strikt in numerisch aufsteigender Reihenfolge!
Da wir sie in der richtigen Reihenfolge generieren möchten, können wir einfach eine **Breadth-First Search (BFS)** unter Verwendung einer Queue durchführen.

1. Erstellen Sie eine leere Queue von Strings.
2. Enqueue die Wurzel `"1"`.
3. Führen Sie eine Schleife `N` Mal aus:
   - Dequeue den vordersten String `curr`.
   - Hängen Sie `curr` an das Ergebnis-Array an.
   - Enqueue das linke Kind: `curr + "0"`.
   - Enqueue das rechte Kind: `curr + "1"`.
4. Geben Sie das Ergebnis-Array zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for queue_03: Generate Binary Numbers (1 to n).

Generate the binary representations of 1, 2, ..., n
"""


def solve(n):
    """Generate binary strings '1', '10', '11', '100', ... up to n."""
    from collections import deque
    if n <= 0:
        return []
    result = []
    q = deque(["1"])
    for _ in range(n):
        s = q.popleft()
        result.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return result
```

</details>

## Durchlauf

`N = 4`

1. Start: `q = ["1"]`, `result = []`.
2. **Schleife 1:**
   - Pop `"1"`.
   - `result = ["1"]`.
   - Push `"10"`, `"11"`.
   - `q = ["10", "11"]`.
3. **Schleife 2:**
   - Pop `"10"`.
   - `result = ["1", "10"]`.
   - Push `"100"`, `"101"`.
   - `q = ["11", "100", "101"]`.
4. **Schleife 3:**
   - Pop `"11"`.
   - `result = ["1", "10", "11"]`.
   - Push `"110"`, `"111"`.
   - `q = ["100", "101", "110", "111"]`.
5. **Schleife 4:**
   - Pop `"100"`.
   - `result = ["1", "10", "11", "100"]`.
   - Push `"1000"`, `"1001"`.
   - `q = ["101", "110", "111", "1000", "1001"]`.

Die Schleife endet.
Ausgabe: `["1", "10", "11", "100"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die Schleife läuft exakt N Mal. In jeder Iteration führen wir eine konstante String-Konkatenation und $O(1)$ Queue-Operationen durch. Die Zeitkomplexität ist strikt $O(N)$.
(Technisch gesehen wächst die Stringlänge bis $\log N$, was die bitweise Zeitkomplexität auf $O(N \log N)$ bringt, aber in der Praxis ist sie auf $O(N)$ begrenzt).
Die Platzkomplexität ist $O(N)$, da die Queue mit einer Rate von 1 Element pro Iteration wächst (2 x \text{Push} - 1 x \text{Pop} = +1), was bedeutet, dass die Queue am Ende N Strings enthält.

## Varianten & Optimierungen

- **Base-K Generierung:** Sie können dies trivial anpassen, um Zahlen zur Basis 3, Basis 4 usw. zu generieren, indem Sie eine `for i in range(K): q.append(curr + str(i))` Schleife anstelle der fest kodierten Werte "0" und "1" verwenden.

## Anwendungen in der Praxis

- **Lexikographische Zustandsautomaten:** Generative Algorithmen in der natürlichen Sprachverarbeitung (NLP) oder beim Brute-Force-Passwort-Knacken nutzen Queue-basierte BFS, um Testkombinationen zu generieren, die strikt nach Länge und Lexikographie geordnet sind.

## Verwandte Algorithmen in cOde(n)

- **[tree_05 - Level Order Traversal](../trees/tree_05_level-order-traversal.md)** — Die exakt gleiche Queue-Logik angewendet auf einen explizit definierten physischen Baum im Speicher.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*