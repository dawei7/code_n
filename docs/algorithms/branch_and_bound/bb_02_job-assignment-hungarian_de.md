# Aufgabenstellung (Branch-and-Bound)

| | |
|---|---|
| **ID** | `bb_02` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Worst Case |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Zuweisungsproblem](https://en.wikipedia.org/wiki/Assignment_problem) |

## Problemstellung

Gegeben sind N Arbeiter und N Aufgaben sowie eine zweidimensionale Kostenmatrix, wobei `cost[i][j]` die Kosten für die Zuordnung des Arbeiters `i` zur Aufgabe `j` angibt.
Jedem Arbeiter muss genau eine Aufgabe zugewiesen werden, und jede Aufgabe muss genau einem Arbeiter zugewiesen werden.
Finde die Zuordnung, die die Gesamtkosten minimiert.

Während der berühmte ungarische Algorithmus dieses Problem in $O(N^3)$-Zeit exakt löst, musst du zeigen, wie man es mithilfe einer generischen **Branch-and-Bound**-Zustandsraum-Suche löst.

**Eingabe:** Eine N × N-Matrix aus ganzen Zahlen `cost`.
**Ausgabe:** Die minimal möglichen Gesamtkosten.

## Wann man es verwendet

- Um zu lernen, wie man Untergrenzen für matrixbasierte kombinatorische Optimierungsprobleme konstruiert.
- „Branch and Bound“ ist äußerst anpassungsfähig: Wenn man komplexe nichtlineare Nebenbedingungen hinzufügt (z. B. „Arbeiter A darf am Dienstag nicht arbeiten, wenn Arbeiter B Aufgabe 3 ausführt“), versagt der ungarische Algorithmus vollständig, aber B&B kann das Problem dennoch lösen, indem es einfach ungültige Zustände verworfen!

## Vorgehensweise

Wir können dies als Entscheidungsbaum betrachten.
Auf Ebene 0 wird dem Arbeiter 0 eine Aufgabe zugewiesen. Auf Ebene 1 wird dem Arbeiter 1 eine Aufgabe zugewiesen usw.
Auf Ebene 0 hat Arbeiter 0 N Auswahlmöglichkeiten. Dadurch entstehen N Verzweigungen.
Wenn wir alle Verzweigungen untersuchen, prüfen wir N! Permutationen.

**Branch-and-Bound-Ausdünnung:**
Wir müssen für jede Teilzuweisung eine **untere Schranke** berechnen. Wenn wir die ersten beiden Arbeiter zugewiesen haben, wie hoch sind dann die absolut *minimalen* möglichen Kosten für die verbleibenden N-2 Arbeiter?
Da wir minimieren wollen: Wenn dieser `lower_bound` **größer oder gleich** unserem bisher ermittelten globalen `min_cost` ist, streichen wir den Zweig!

**Wie berechnet man die Untergrenze?**
Eine sehr einfache und schnelle Untergrenze: Für jeden noch nicht zugewiesenen Mitarbeiter betrachtet man die verfügbaren, noch nicht zugewiesenen Aufgaben und geht davon aus, dass er unabhängig die absolut günstigste davon übernehmen kann (wobei Konflikte ignoriert werden, bei denen zwei Mitarbeiter dieselbe günstige Aufgabe haben möchten).
`bound = current_accumulated_cost + sum(min(available jobs) for each unassigned worker)`.
Es ist mathematisch garantiert, dass diese Schranke \le den tatsächlichen Kosten für die Erledigung des Auftrags ist, sodass das Beschneiden sicher ist.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_02: Job Assignment.

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum-cost assignment. Brute-force
enumerate all n! permutations of jobs. Setup keeps n small
(n <= 6) so this is tractable.
"""


def solve(cost, n):
    if n == 0:
        return 0
    jobs = list(range(n))
    best = float("inf")

    def helper(worker, used, current):
        nonlocal best
        if worker == n:
            if current < best:
                best = current
            return
        for job in jobs:
            if not used[job]:
                used[job] = True
                helper(worker + 1, used, current + cost[worker][job])
                used[job] = False

    helper(0, [False] * n, 0)
    return best
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`Cost Matrix:`
```text
W0: [9, 2, 7]
W1: [6, 4, 3]
W2: [5, 8, 1]
```

1. **Wurzel (keine Zuweisungen):** Obergrenze = W0 min(2) + W1 min(3) + W2 min(1) = 6. Auf den Heap schieben.
2. **Wurzel entnehmen. Verzweigung W0:**
   - W0 nimmt J0 (Kosten 9). Gesamtwert = 9 + W1 min(3) + W2 min(1) = 13.
   - W0 nimmt J1 (Kosten 2). Gesamtwert = 2 + W1 min(3) + W2 min(1) = 6.
   - W0 nimmt J2 (Kosten 7). Obergrenze = 7 + W1 min(4) + W2 min(5) = 16. *(Beachte, dass sich min geändert hat, da J2 genommen wurde!)*
3. **Heap-Zustand:** `[6 (J1), 13 (J0), 16 (J2)]`.
4. **J1-Verzweigung entfernen (Best First). Verzweigung W1:**
   - W1 nimmt J0 (Kosten 6). Gesamt = 2+6=8. Obergrenze = 8 + W2 min(1) = 9.
   - W1 nimmt J2 (Kosten 3). Gesamt = 2+3=5. Obergrenze = 5 + W2 min(5) = 10.
5. **Tiefste Ebene:** Der Heap priorisiert die Erweiterung des Pfades `Bound 9`. W2 ist gezwungen, J2 zu wählen (Kosten 1). Gesamtkosten = 9.
   - `min_final_cost = 9`.
6. Nun betrachtet der Heap die Pfade `Bound 13` und `Bound 16` von W0 aus. Da 13 \ge 9 gilt, werden diese vollständig PRUNED und der Algorithmus bricht ab! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Deutlich schneller als N! | $O(2^N)$ |
| **Schlechtester Fall** | $O(N!)$ | $O(N!)$ |

Im absolut schlimmsten Fall, in dem die Grenze niemals etwas ausdünnt, erzeugt der Baum N! Blätter, was Fakultätszeit in Anspruch nimmt. Auch die Priority Queue explodiert und belegt Fakultätselemente im Speicher. Die „Best-First“-Suchheuristik sorgt jedoch dafür, dass bei Standarddatensätzen fast sofort die optimale Lösung gefunden wird, wobei der Großteil des Baums ausgedünnt wird.

## Varianten und Optimierungen

- **Ungarischer Algorithmus ($O(N^3)$):** Die exakte, deterministische DP-/kombinatorische Lösung. Er erstellt einen bipartiten Graphen und manipuliert die Zeilen und Spalten der Matrix, um perfekte Paarungen ohne Kosten zu finden. Für das reine Job-Assignment-Problem ist er rein mathematisch dem B&B-Algorithmus überlegen.

## Anwendungen in der Praxis

- **Mitfahrdienste:** Uber/Lyft ordnen gleichzeitig N Fahrer N Fahrgästen zu, um die globale Gesamtwartezeit zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[flow_03 – Zweiteilige Zuordnung](../flow/flow_03_bipartite-matching.md)** — Die ungewichtete, rein strukturelle Version des Zuordnungsproblems.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
