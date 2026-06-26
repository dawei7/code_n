# Allocate Minimum Number of Pages

| | |
|---|---|
| **ID** | `dc_13` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N log(Sum - Max)$) Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) |

## Problemstellung

Gegeben ist ein Array `arr` von Ganzzahlen der Größe `N`, wobei `arr[i]` die Anzahl der Seiten im i-ten Buch repräsentiert.
Es gibt `M` Studenten. Ihre Aufgabe ist es, alle Bücher so an die Studenten zu verteilen, dass:
1. Jeder Student mindestens ein Buch erhält.
2. Jedes Buch nur einem einzigen Studenten zugewiesen wird.
3. Die Zuweisung der Bücher streng zusammenhängend erfolgt (z. B. kann ein Student nicht Buch 1 und Buch 3 erhalten, ohne Buch 2 zu erhalten).
Das Ziel ist es, die **maximale Anzahl an Seiten**, die einem einzelnen Studenten zugewiesen werden, zu **minimieren**.

**Eingabe:** Ein Ganzzahl-Array `arr` und eine Ganzzahl `M`.
**Ausgabe:** Eine Ganzzahl, die die minimierte maximale Seitenzahl repräsentiert. Geben Sie -1 zurück, falls eine Zuweisung unmöglich ist (M > N).

## Wann ist dieses Verfahren anzuwenden?

- Das absolut bekannteste Problem für "Binäre Suche im Antwortraum" (oft umgangssprachlich als Min-Max oder Max-Min bezeichnet).
- Wenn ein Problem Sie auffordert, das "Maximum von X zu minimieren" oder das "Minimum von Y zu maximieren" über zusammenhängende Teilarrays hinweg, wird es fast sicher mit diesem Muster gelöst.

## Ansatz

**1. Definition des Antwortraums (Decrease and Conquer):**
Was ist die absolut *minimale* mögliche Antwort? Wenn wir M=N Studenten hätten, bekäme jeder Student genau ein Buch. Der Student, der das dickste Buch erhält, bestimmt die maximale Seitenzahl. Daher ist die minimal mögliche Antwort `max(arr)`.
Was ist die absolut *maximale* mögliche Antwort? Wenn wir nur M=1 Studenten hätten, müsste dieser arme Student JEDES Buch lesen. Daher ist die maximal mögliche Antwort `sum(arr)`.
Die perfekte optimale Antwort MUSS irgendwo im kontinuierlichen Ganzzahlbereich `[max(arr), sum(arr)]` liegen.

**2. Die Validierungsfunktion (Der "Ist es möglich?"-Test):**
Wenn ich eine zufällige Zahl `mid` aus diesem Bereich wähle (sagen wir 50 Seiten), woher weiß ich, ob es möglich ist, die Bücher so zuzuweisen, dass KEIN Student MEHR als 50 Seiten liest?
Wir verteilen die Bücher einfach gierig (greedy):
- `current_pages = 0`, `students_needed = 1`.
- Iterieren Sie durch die Bücher.
- Wenn `current_pages + book > mid`, können wir dieses Buch nicht dem aktuellen Studenten geben! Er würde das 50-Seiten-Limit überschreiten.
- Wir müssen dieses Buch einem NEUEN Studenten geben. `students_needed += 1`, `current_pages = book`.
- Wenn nach dem Überprüfen aller Bücher `students_needed > M` gilt, dann ist 50 Seiten definitiv zu wenig! Wir haben erzwungen, dass zu viele Studenten existieren.

**3. Die Binäre Suche:**
- Binäre Suche für `mid` zwischen `low = max(arr)` und `high = sum(arr)`.
- Wenn `is_possible(mid)` WAHR ist: Das bedeutet, `mid` Seiten ist eine gültige Obergrenze! Aber wir wollen das Maximum minimieren. Also speichern wir `mid` als Kandidaten `ans` und versuchen eine noch kleinere Obergrenze: `high = mid - 1`.
- Wenn `is_possible(mid)` FALSCH ist: `mid` Seiten ist zu restriktiv (erfordert zu viele Studenten). Wir müssen unsere Obergrenze erhöhen: `low = mid + 1`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_13: Allocate Minimum Number of Pages.

Given an array arr[] of n book page counts and m
"""


def solve(arr, n, m):
    """Binary search on the answer.

    Low = max(arr) (one student reads the longest book alone).
    High = sum(arr) (one student reads everything).
    The first `mx` for which we can split into <= m blocks
    is the answer.
    """
    lo = max(arr) if arr else 0
    hi = sum(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # Greedy: how many students do we need for max = mid?
        needed = 1
        pages = 0
        for pages_i in arr:
            if pages + pages_i <= mid:
                pages += pages_i
            else:
                needed += 1
                pages = pages_i
        if needed <= m:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

</details>

## Durchlauf

`arr = [12, 34, 67, 90]`, `m = 2`.
`low = max(arr) = 90`.
`high = sum(arr) = 203`.

1. **Schleife 1:**
   - `mid = (90 + 203) // 2 = 146`.
   - `is_possible(146)`:
     - S1 erhält 12, 34, 67 (Summe 113. Nächstes Buch 90 ergibt 203 > 146).
     - S2 erhält 90.
     - `students_needed = 2`. `2 <= 2`. Wahr!
   - `ans = 146`. Suche weiter unten: `high = 146 - 1 = 145`.
2. **Schleife 2:**
   - `mid = (90 + 145) // 2 = 117`.
   - `is_possible(117)`:
     - S1 erhält 12, 34, 67 (Summe 113. Nächstes 90 ergibt 203 > 117).
     - S2 erhält 90.
     - `students_needed = 2`. `2 <= 2`. Wahr!
   - `ans = 117`. Suche weiter unten: `high = 117 - 1 = 116`.
3. **Schleife 3:**
   - `mid = (90 + 116) // 2 = 103`.
   - `is_possible(103)`:
     - S1 erhält 12, 34 (Summe 46. Nächstes 67 ergibt 113 > 103).
     - S2 erhält 67. (Summe 67. Nächstes 90 ergibt 157 > 103).
     - S3 erhält 90.
     - `students_needed = 3`. `3 <= 2`. FALSCH!
   - Obergrenze ist zu eng. Suche weiter oben: `low = 103 + 1 = 104`.
*(... Die binäre Suche nähert sich 113 an ...)*

Das Ergebnis ist `113`. ✓ (S1 erhält `12+34+67=113`, S2 erhält `90`. Das Maximum ist `113`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * log(Sum - Max)$) | $O(1)$ |
| **Schlechtester Fall** | $O(N * log(Sum - Max)$) | $O(1)$ |

Die Größe des Bereichs für die binäre Suche ist `S - M` (wobei `S` die Summe und `M` das Maximum ist). Die while-Schleife läuft log(S-M) mal.
Innerhalb der while-Schleife führt `is_possible` einen linearen Scan der Ordnung $O(N)$ über das Array durch.
Die gesamte Zeitkomplexität beträgt strikt $O(N log(Sum - Max)$).
Die Platzkomplexität ist $O(1)$.

## Varianten & Optimierungen

- **Koko Eating Bananas (LeetCode 875):** "Minimiere die Essgeschwindigkeit K, sodass Koko alle Bananen innerhalb von H Stunden isst." Der exakt gleiche Algorithmus! Der Antwortraum ist `[1, max(piles)]`. `is_possible(K)` summiert einfach `ceil(pile / K)` und prüft, ob dies \le H ist.
- **Aggressive Cows (SPOJ):** "Maximiere den minimalen Abstand zwischen C Kühen, die in N Ställen platziert werden." Antwortraum `[1, max(stalls) - min(stalls)]`. Binäre Suche nach dem maximalen gültigen Abstand!

## Anwendungen in der Praxis

- **Lastverteilung (Load Balancing):** Verteilung zusammenhängender Abschnitte eines sequenziellen Batch-Verarbeitungsauftrags (wie eine massive Videorendering-Timeline) auf M Worker-Server, sodass der Server mit der höchsten Last so schnell wie möglich fertig wird.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Die Grundlage dieses algorithmischen Musters.
- **[dc_10 - Floor Square Root](dc_10_floor-square-root.md)** — Eine weitere Anwendung der binären Suche auf einem kontinuierlichen Antwortraum.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*