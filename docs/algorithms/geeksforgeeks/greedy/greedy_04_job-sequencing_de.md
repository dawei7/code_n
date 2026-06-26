# Job Sequencing Problem

| | |
|---|---|
| **ID** | `greedy_04` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Job Sequencing Problem](https://www.geeksforgeeks.org/job-sequencing-problem/) |

## Problemstellung

Gegeben sind `N` Jobs, wobei jeder Job durch eine `Job ID`, eine `Deadline` und einen `Profit` repräsentiert wird.
Jeder Job benötigt genau 1 Zeiteinheit zur Fertigstellung. Es kann immer nur ein Job gleichzeitig ausgeführt werden.
Ein Job bringt seinen `Profit` NUR dann ein, wenn er strikt zum oder vor dem Ablauf seiner `Deadline` abgeschlossen wird.
Finden Sie den maximalen Gesamtprofit, den Sie erzielen können, sowie die Anzahl der abgeschlossenen Jobs.

**Eingabe:** Ein Array von `Job`-Objekten `[id, deadline, profit]`.
**Ausgabe:** Ein Tupel `(number_of_jobs_done, max_profit)`.

## Wann ist es anzuwenden?

- Um Aufgaben mit einer Dauer von einer Einheit optimal vor ihrem Ablauf zu planen und den Ertrag zu maximieren.
- *Einschränkung:* Wenn Jobs VARIABLE Zeitspannen zur Fertigstellung benötigen (z. B. Job 1 benötigt 3 Stunden, Job 2 benötigt 5 Stunden), schlägt der Greedy-Ansatz fehl und Sie müssen DP (Weighted Job Scheduling) verwenden.

## Ansatz

**1. Die Greedy-Entscheidung (Maximierung des Profits):**
Wenn wir den maximalen Profit erzielen wollen, sollten wir offensichtlich die Jobs priorisieren, die am meisten einbringen!
Wir beginnen damit, die Jobs basierend auf ihrem `Profit` in absteigender Reihenfolge zu sortieren.

**2. Die Planungslogik (Maximierung der freien Zeit):**
Nehmen wir an, der bestbezahlte Job hat eine `Deadline` an Tag 5. Wann sollten wir ihn einplanen?
- Wenn wir ihn an Tag 1 einplanen, verschwenden wir einen wertvollen frühen Slot! Was, wenn ein anderer hochbezahlter Job eine `Deadline` an Tag 1 hat? Wir könnten dann nicht beide erledigen.
- Wir sollten ihn **SO SPÄT WIE MÖGLICH** einplanen, direkt bevor er abläuft! Wenn seine `Deadline` Tag 5 ist, planen wir ihn an Tag 5 ein! Dies lässt die Tage 1-4 komplett offen für andere Jobs mit engeren Deadlines.

**3. Das Time-Slots-Array:**
Wir finden die absolute maximale `Deadline` unter allen Jobs (nennen wir sie D_{max}).
Wir erstellen ein `slots`-Array der Größe D_{max} + 1, initialisiert mit `False`.
Wir iterieren durch unsere sortierten Jobs. Für jeden Job betrachten wir seine `Deadline` d.
Wir prüfen `slots[d]`. Wenn er frei ist, planen wir den Job dort ein und markieren ihn als `True`.
Wenn Tag d bereits durch einen zuvor geplanten, höher bezahlten Job belegt ist, suchen wir rückwärts in der Zeit: `d-1`, `d-2`, usw. Wir nehmen den ersten verfügbaren freien Slot!
Wenn wir Tag 1 erreichen und alle Slots voll sind, kann dieser Job nicht abgeschlossen werden. Wir überspringen ihn.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_04: Job Sequencing.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n²) time.
"""


def solve(deadline, profit, n):
    # Build job tuples and sort by profit descending.
    jobs = sorted(
        ((profit[i], deadline[i]) for i in range(n)),
        key=lambda j: j[0],
        reverse=True,
    )
    # latest_free[t] is the latest time slot that is still available
    # up to t. We collapse the search with a simple boolean array.
    slots = [False] * (n + 1)
    total = 0
    for p, d in jobs:
        # Find the latest free slot <= min(d, n).
        for t in range(min(d, n), 0, -1):
            if not slots[t]:
                slots[t] = True
                total += p
                break
    return total
```

</details>

## Durchlauf

Jobs: `J1(d=2, p=100)`, `J2(d=1, p=19)`, `J3(d=2, p=27)`, `J4(1, 25)`, `J5(3, 15)`.

1. Sortierung absteigend nach `Profit`:
   `J1(2, 100)`, `J3(2, 27)`, `J4(1, 25)`, `J2(1, 19)`, `J5(3, 15)`.
2. `max_deadline = 3`. `slots = [F, F, F, F]`.
3. Auswertung `J1` (Deadline 2, Profit 100):
   - Slot 2 ist frei. `slots[2] = True`. `profit = 100`.
4. Auswertung `J3` (Deadline 2, Profit 27):
   - Slot 2 ist belegt.
   - Slot 1 ist frei. `slots[1] = True`. `profit = 127`.
5. Auswertung `J4` (Deadline 1, Profit 25):
   - Slot 1 ist belegt.
   - Schleife erreicht 0. Kann nicht geplant werden! Überspringen.
6. Auswertung `J2` (Deadline 1, Profit 19):
   - Slot 1 belegt. Überspringen.
7. Auswertung `J5` (Deadline 3, Profit 15):
   - Slot 3 ist frei. `slots[3] = True`. `profit = 142`.

Ergebnis `jobs_done = 3`, `total_profit = 142`. ✓ (Sequenz: J3, J1, J5).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(Max\_Deadline)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(Max\_Deadline)$ |
| **Schlechtester Fall** | $O(N * Max\_Deadline)$ | $O(Max\_Deadline)$ |

Das Sortieren benötigt $O(N \log N)$.
Die verschachtelte Schleife iteriert N-mal, und die innere Schleife läuft rückwärts von `deadline` bis 1. Im schlechtesten Fall (z. B. alle Jobs haben eine riesige `Deadline` von 10.000, aber die Slots füllen sich von rechts nach links) leistet die innere Schleife $O(Max\_Deadline)$ Arbeit für jeden Job. Die Gesamtzeit beträgt $O(N \log N + N \cdot Max\_Deadline)$.
Wenn `Max_Deadline` durch N begrenzt ist, vereinfacht sich dies zu $O(N^2)$.
Die Platzkomplexität beträgt $O(Max\_Deadline)$ für das Boolean-Array.

## Varianten & Optimierungen

- **Disjoint Set (Union-Find) Optimierung:** Wir können die $O(N^2)$ rückwärts gerichtete lineare Suche komplett eliminieren! Unter Verwendung eines Disjoint Set (`graph_09`) können wir jeden Zeitslot direkt auf den *nächstgelegenen verfügbaren leeren Slot links davon* zeigen lassen. Wenn Slot 5 belegt ist, liefert `find(5)` sofort 4 zurück. Wenn 4 belegt ist, liefert es sofort 3 zurück! Dies reduziert die Packungsphase auf $O(N \cdot \alpha(N))$, wodurch der gesamte Algorithmus strikt $O(N \log N)$ ist, begrenzt durch das Sortieren!
- **Weighted Job Scheduling (DP):** Wenn Jobs >1 Zeiteinheit benötigen, sortieren wir nach `Finish Time` und verwenden binäre Suche mit DP, um die optimale Sequenz ohne Überschneidungen zu finden (`dp_08`).

## Praxisanwendungen

- **Freiberufliche Auftragsvergabe:** Ein Berater mit mehreren Auftragsangeboten (jeweils 1 Tag Dauer, unterschiedliche Bezahlung, unterschiedliche Ablaufdaten), der seinen wöchentlichen Verdienst maximieren möchte.
- **Wartungsfenster für Server:** Ausführung von Hintergrund-Wartungsaufgaben mit hoher Priorität auf einer Datenbank, bevor tägliche Nutzungsspitzen die Tabellen sperren.

## Verwandte Algorithmen in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — Das ungewichtete Äquivalent, das die reine Anzahl der Aktivitäten anstelle des Profits maximiert.
- **[graph_09 - Union-Find](../graphs/graph_09_union-find.md)** — Die Datenstruktur, die erforderlich ist, um die lineare Slot-Suche auf $O(1)$ zu optimieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*