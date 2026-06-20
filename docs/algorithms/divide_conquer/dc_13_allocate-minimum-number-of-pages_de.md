# Mindestanzahl an Seiten zuweisen

| | |
|---|---|
| **ID** | `dc_13` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N log(Sum - Max)$) Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) |

## Aufgabenstellung

Gegeben ist ein Array von Ganzzahlen `arr` der Größe `N`, wobei `arr[i]` die Anzahl der Seiten im i-ten Buch angibt.
Es gibt `M` Schüler. Ihre Aufgabe ist es, alle Bücher den Schülern so zuzuweisen, dass:
1. Jeder Schüler mindestens ein Buch erhält.
2. Jedes Buch nur einem Schüler zugewiesen wird.
3. Die Zuweisung der Bücher streng zusammenhängend erfolgt (d. h., ein Schüler kann nicht Buch 1 und Buch 3 erhalten, ohne auch Buch 2 zu erhalten).
Das Ziel ist es, **die maximale Seitenzahl**, die einem einzelnen Schüler zugewiesen wird, zu minimieren.

**Eingabe:** Ein Ganzzahl-Array `arr` und eine Ganzzahl `M`.
**Ausgabe:** Eine ganze Zahl, die die minimierte maximale Seitenanzahl angibt. Gib -1 zurück, wenn eine Zuweisung unmöglich ist (M > N).

## Wann man es verwendet

- Das mit Abstand bekannteste Problem der „binären Suche im Lösungsraum“ (umgangssprachlich oft als Min-Max oder Max-Min bezeichnet).
- Wenn in einer Aufgabe verlangt wird, „das Maximum X zu minimieren“ oder „das Minimum Y zu maximieren“ über zusammenhängende Teilarrays, lässt sich diese fast immer mit diesem Muster lösen.

## Vorgehensweise

**1. Definieren des Lösungsraums (Teile und herrsche):**
Was ist die absolut *kleinstmögliche* Antwort? Bei M = N Schülern erhält jeder Schüler genau ein Buch. Der Schüler, der das dickste Buch erhält, bestimmt die maximale Seitenzahl. Somit lautet die kleinstmögliche Antwort `max(arr)`.
Was ist die absolut *maximal* mögliche Lösung? Hätten wir nur M = 1 Schüler, müsste dieser arme Schüler JEDES Buch lesen. Somit ist die maximal mögliche Lösung `sum(arr)`.
Die perfekte optimale Lösung MUSS irgendwo im kontinuierlichen ganzzahligen Bereich `[max(arr), sum(arr)]` liegen.

**2. Die Validierungsfunktion (der „Ist es möglich?“-Test):**
Wenn ich eine Zufallszahl `mid` aus diesem Bereich wähle (sagen wir 50 Seiten), woher weiß ich dann, ob es möglich ist, die Bücher so zu verteilen, dass KEIN Schüler MEHR als 50 Seiten liest?
Wir verteilen die Bücher einfach nach dem Greedy-Prinzip!
- `current_pages = 0`, `students_needed = 1`.
- Durchlaufen wir die Bücher.
- Wenn `current_pages + book > mid`, können wir dieses Buch dem aktuellen Schüler nicht geben! Er würde die 50-Seiten-Grenze überschreiten.
- Wir müssen dieses Buch einem NEUEN Schüler geben. `students_needed += 1`, `current_pages = book`.
- Nachdem alle Bücher überprüft wurden: Wenn `students_needed > M`, dann sind 50 Seiten eindeutig zu wenig! Wir haben zu viele Schüler „erzwungen“.

**3. Die binäre Suche:**
- Binäre Suche `mid` zwischen `low = max(arr)` und `high = sum(arr)`.
- Wenn `is_possible(mid)` WAHR ist: Das bedeutet, dass `mid` Seiten eine gültige Obergrenze sind! Aber wir wollen das Maximum MINIMIEREN. Also speichern wir `mid` als Kandidaten `ans` und probieren eine noch kleinere Obergrenze aus: `high = mid - 1`.
- Wenn `is_possible(mid)` FALSE ist: `mid` Seiten sind zu restriktiv (erfordern zu viele Studierende). Wir müssen unsere Obergrenze erhöhen: `low = mid + 1`.

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

## Schritt-für-Schritt-Anleitung

`arr = [12, 34, 67, 90]`, `m = 2`.
`low = max(arr) = 90`.
`high = sum(arr) = 203`.

1. **Schleife 1:**
   - `mid = (90 + 203) // 2 = 146`.
   - `is_possible(146)`:
 - S1 erhält 12, 34, 67 (insgesamt 113. Das nächste Buch mit 90 ergibt 203 > 146).
 - S2 erhält 90.
     - `students_needed = 2`. `2 <= 2`. Richtig!
   - `ans = 146`. Nach unten verschieben: `high = 146 - 1 = 145`.
2. **Schleife 2:**
   - `mid = (90 + 145) // 2 = 117`.
   - `is_possible(117)`:
 - S1 erhält 12, 34, 67 (Gesamt 113. Die nächsten 90 ergeben 203 > 117).
     - S2 erhält 90.
 - `students_needed = 2`. `2 <= 2`. Richtig!
   - `ans = 117`. Weiter nach unten: `high = 117 - 1 = 116`.
3. **Schleife 3:**
   - `mid = (90 + 116) // 2 = 103`.
   - `is_possible(103)`:
 - S1 erhält 12, 34 (Gesamt: 46. Die nächsten 67 ergeben 113 > 103).
 - S2 erhält 67. (Insgesamt 67. Die nächsten 90 ergeben 157 > 103).
 - S3 erhält 90.
 - `students_needed = 3`. `3 <= 2`. FALSCH!
   - Die Obergrenze ist zu eng. Nach oben verschieben: `low = 103 + 1 = 104`.
*(... Die binäre Suche grenzt den Wert auf 113 ein ...)*

Das Ergebnis ist `113`. ✓ (S1 erhält `12+34+67=113`, S2 erhält `90`. Das Maximum ist `113`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N * log(Sum - Max)$) | $O(1)$ |
| **Schlimmster Fall** | $O(N * log(Sum - Max)$) | $O(1)$ |

Die Größe des Suchbereichs bei der binären Suche beträgt `S - M` (wobei `S` die Summe und `M` das Maximum ist). Die while-Schleife wird log(S-M) Mal durchlaufen.
Innerhalb der while-Schleife führt `is_possible` einen linearen Durchlauf $O(N)$ durch das Array durch.
Die gesamte Zeitkomplexität beträgt streng $O(N log(Sum - Max)$).
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Koko isst Bananen (LeetCode 875):** „Minimiere die Essgeschwindigkeit K so, dass Koko alle Bananen innerhalb von H Stunden isst.“ Genau derselbe Algorithmus! Der Lösungsraum ist `[1, max(piles)]`. `is_possible(K)` summiert einfach `ceil(pile / K)` und prüft, ob das Ergebnis \le H ist.
- **Aggressive Cows (SPOJ):** „Maximiere den minimalen Abstand zwischen C Kühen, die in N Ställen untergebracht sind.“ Der Lösungsraum beträgt `[1, max(stalls) - min(stalls)]`. Binäre Suche nach dem maximalen gültigen Abstand!

## Anwendungen in der Praxis

- **Lastenausgleich:** Verteilung zusammenhängender Blöcke eines sequenziellen Batch-Verarbeitungsauftrags (wie einer umfangreichen Video-Rendering-Zeitleiste) auf M Worker-Server, sodass der Server mit der höchsten Auslastung so schnell wie möglich fertig wird.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** — Die Grundlage dieses algorithmischen Musters.
- **[dc_10 – Floor-Quadratwurzel](dc_10_floor-square-root.md)** – Eine weitere Anwendung der binären Suche auf einem kontinuierlichen Lösungsraum.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde
und sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
