# Sublist Search

| | |
|---|---|
| **ID** | `search_10` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(N \times M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Sublist Search (Search a linked list in another list)](https://www.geeksforgeeks.org/sublist-search-search-a-linked-list-in-another-list/) |

## Problemstellung

Gegeben sind zwei Singly Linked Lists: eine Ziel-`sublist` und eine Haupt-`list`.
Ermitteln Sie, ob die `sublist` vollständig und zusammenhängend innerhalb der Haupt-`list` vorhanden ist.
Falls sie existiert, geben Sie `True` zurück (oder den Startknoten der Übereinstimmung). Andernfalls geben Sie `False` zurück.

**Eingabe:** Zwei Head-Knoten `sublist` und `list`.
**Ausgabe:** Ein Boolean.

## Wann ist dies zu verwenden?

- Bei der Durchführung von String-Matching (wie dem Finden eines Teilstrings in einem Text), wenn die Datenstruktur jedoch eine Linked List anstelle eines String-Arrays ist.
- Ein klassischer Test für die Manipulation mehrerer Pointer, ohne den Überblick über die ursprünglichen Startpositionen zu verlieren.

## Ansatz

**1. Die Analogie des Sliding Window:**
Stellen Sie sich vor, Sie nehmen ein transparentes Lineal (die `sublist`) und schieben es langsam über ein langes Blatt Papier (die `list`).
Sie platzieren das Lineal ganz am Anfang. Sie prüfen, ob JEDER Zentimeter des Lineals perfekt mit dem Papier darunter übereinstimmt.
Wenn auch nur ein Zentimeter nicht übereinstimmt, heben Sie das Lineal an, verschieben es um genau 1 Position auf dem Papier nach vorne und versuchen erneut, das gesamte Lineal von Grund auf abzugleichen!

**2. Die Pointer-Strategie:**
Wir benötigen drei aktive Pointer:
- `first`: Zeigt auf den Knoten in der Hauptliste, an dem wir derzeit versuchen, eine Übereinstimmung zu beginnen.
- `main_ptr`: Zeigt auf den spezifischen Knoten in der Hauptliste, den wir *während* eines Übereinstimmungsversuchs gerade prüfen.
- `sub_ptr`: Zeigt auf den spezifischen Knoten in der Sublist, den wir gerade prüfen.

**3. Die Matching-Schleife:**
1. Initialisieren Sie `first = list.head`.
2. Starten Sie eine äußere Schleife, solange `first` nicht null ist.
3. Setzen Sie `main_ptr = first` und `sub_ptr = sublist.head`.
4. Starten Sie eine innere Schleife, solange sowohl `main_ptr` als auch `sub_ptr` nicht null sind.
   - Wenn `main_ptr.val == sub_ptr.val`, stimmen sie überein! Bewegen Sie BEIDE Pointer vorwärts.
   - Wenn sie nicht übereinstimmen, brechen Sie die innere Schleife sofort ab!
5. Prüfen Sie nach dem Abbruch der inneren Schleife, warum sie abgebrochen wurde. Wenn `sub_ptr == null`, bedeutet dies, dass wir erfolgreich jeden einzelnen Knoten in der Sublist abgeglichen haben! Geben Sie `True` zurück.
6. Falls nicht, ist die Übereinstimmung fehlgeschlagen. Bewegen Sie `first` um 1 Knoten vorwärts und versuchen Sie es erneut!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_10: Sublist Search.

Find the first index where ``sub`` appears as a contiguous run
in ``data``, or -1 if it never does. Sliding window of length
m scanned across an n-length list. O(n * m) worst case.
"""


def solve(data, sub, n, m):
    if m == 0:
        return 0
    if m > n:
        return -1
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if data[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1
```

</details>

## Durchlauf

`sublist = 1 -> 2 -> 3`.
`main_list = 5 -> 1 -> 2 -> 4 -> 1 -> 2 -> 3 -> 9`.

1. `first = 5`.
   - `main_ptr = 5`, `sub_ptr = 1`.
   - `5 != 1`. Innere Schleife bricht ab.
2. `first = 1` (zweiter Knoten).
   - `main_ptr = 1`, `sub_ptr = 1`. Match!
   - `main_ptr = 2`, `sub_ptr = 2`. Match!
   - `main_ptr = 4`, `sub_ptr = 3`. `4 != 3`. Mismatch! Innere Schleife bricht ab.
3. `first = 2`. Mismatch am ersten Knoten (`2 != 1`).
4. `first = 4`. Mismatch (`4 != 1`).
5. `first = 1` (fünfter Knoten).
   - `main_ptr = 1`, `sub_ptr = 1`. Match!
   - `main_ptr = 2`, `sub_ptr = 2`. Match!
   - `main_ptr = 3`, `sub_ptr = 3`. Match!
   - Beide rücken vor. `sub_ptr` wird `None`!
   - Bedingung der inneren Schleife schlägt fehl (`sub_ptr is not None` ist False). Innere Schleife bricht ab.
6. Prüfe `sub_ptr is None`? TRUE!
Gibt `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N \times M)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N \times M)$ | $O(1)$ |

Sei N die Länge der Hauptliste und M die Länge der Sublist.
Im schlechtesten Fall (z. B. `main = a-a-a-a-a-a-b`, `sub = a-a-b`) wird die innere Schleife fast alle M Zeichen erfolgreich abgleichen, bevor sie am allerletzten Knoten fehlschlägt, und dies wird N-mal wiederholt. Die gesamte Zeitkomplexität beträgt $O(N \times M)$.
Die Platzkomplexität ist strikt $O(1)$, da wir unabhängig von der Listengröße nur drei Knoten-Pointer instanziieren.

## Varianten & Optimierungen

- **KMP Algorithmus (`string_06`):** Die $O(N \times M)$ Zeitkomplexität im schlechtesten Fall ist identisch mit dem Brute-Force-Substring-Matching. Wenn Sie die Linked Lists in Arrays umwandeln, können Sie den Knuth-Morris-Pratt-Algorithmus verwenden, um ein "Longest Prefix Suffix" (LPS) Array vorzuberechnen. Dies reduziert die Zeitkomplexität auf ein strikt lineares $O(N + M)$, indem redundante Pointer-Resets vermieden werden!

## Anwendungen in der Praxis

- **DNA-Sequenzanalyse:** Durchsuchen einer massiven Genomsequenz (gespeichert als Linked List, um schnelle $O(1)$ Mutationen/Einfügungen ohne Speicherneuzuweisung zu ermöglichen), um das Vorhandensein einer spezifischen kurzen viralen RNA-Subkette zu finden.

## Verwandte Algorithmen in cOde(n)

- **[string_06 - KMP Pattern Matching](../strings/string_06_kmp-pattern-matching.md)** — Die mathematisch optimierte $O(N+M)$ Version genau dieses Problems, angewendet auf Strings/Arrays.
- **[linked_list_07 - Intersection of Two Lists](../linked_list/ll_07_intersection-two-lists.md)** — Ein weiterer Algorithmus zur Traversierung von Linked Lists mit mehreren Pointern, der jedoch auf physische Speicherüberschneidungen anstatt auf Wert-Teilmengen prüft.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*