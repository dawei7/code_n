# Bin-Packing (First-Fit-Verfahren mit absteigender Reihenfolge)

| | |
|---|---|
| **ID** | `approx_06` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Bin-Packing-Problem](https://en.wikipedia.org/wiki/Bin_packing_problem) |

## Problemstellung

Gegeben sind N Gegenstände mit unterschiedlichen Gewichten und eine unbegrenzte Anzahl von Behältern mit einer maximalen Kapazität von jeweils C. Bestimmen Sie die **minimale Anzahl an Behältern**, die erforderlich ist, um alle Gegenstände zu verpacken.
Dies ist ein klassisches NP-schweres Problem. Sie müssen den **First-Fit-Decreasing-Algorithmus (FFD)** implementieren, der garantiert nicht mehr als genau \frac{11}{9} OPT + 1 Behälter verwendet (ein unglaublich enges Approximationsverhältnis von ~1,22!).

**Eingabe:** Eine Liste von Gegenständen `weights` und Behältern `capacity` mit Kapazität C.
**Ausgabe:** Eine ganze Zahl, die die minimale Anzahl der verwendeten Behälter angibt.

## Anwendungsfälle

- Zum Verpacken von Datenpaketen in Netzwerk-MTU-Frames fester Größe.
- Zur Einplanung von Aufgaben unterschiedlicher Dauer auf identische Maschinen, wobei jede Maschine nur für eine 8-Stunden-Schicht zur Verfügung steht.

## Vorgehensweise

Ein naiver, gieriger Ansatz (First Fit) betrachtet die Elemente einfach in der Reihenfolge, in der sie angegeben werden, und schiebt sie in den ersten Behälter, der genügend Platz bietet. Wenn kein Behälter Platz hat, wird ein neuer Behälter angelegt. Dies ergibt eine Approximation von 1,7.
Wir können dies durch eine einfache Maßnahme drastisch verbessern: **Sortiere die Elemente zunächst vom größten zum kleinsten!**

**First Fit Decreasing (FFD):**
Wenn wir die großen, schwer unterzubringenen Elemente zuerst platzieren, beanspruchen sie ganz natürlich ihre eigenen Fächer. Dann fügen sich die winzigen Elemente perfekt in die „übrig gebliebenen“ Lücken dieser bereits geöffneten Behälter ein!

1. Sortiere die Elemente in **absteigender** Reihenfolge.
2. Führe eine Liste der derzeit offenen Behälter, die zunächst leer ist. Jeder Behälter erfasst seine *verbleibende Kapazität*.
3. Durchlaufe die sortierten Gegenstände:
   - Durchsuche für jeden Gegenstand die Liste der offenen Behälter linear von links nach rechts (First Fit).
   - Wenn ein Behälter `remaining_capacity >= item_weight` hat, lege den Gegenstand in diesen Behälter, aktualisiere seine Kapazität und beende die Durchlaufschleife.
   - Wenn KEIN offener Behälter genügend Platz hat, eröffne einen brandneuen Behälter, lege das Element hinein und füge ihn der Liste der offenen Behälter hinzu.
4. Gib die Gesamtzahl der offenen Behälter zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_06: Bin Packing (First-Fit Decreasing).

Given a list of item sizes in (0, 1] and unit-
"""


def solve(sizes, n):
    """First-Fit Decreasing bin packing."""
    if n == 0:
        return 0
    # Sort items by size descending.
    items = sorted(sizes, reverse=True)
    bins = []  # each entry is the remaining capacity of a bin
    for s in items:
        placed = False
        for i in range(len(bins)):
            if bins[i] >= s:
                bins[i] -= s
                placed = True
                break
        if not placed:
            bins.append(1.0 - s)
    return len(bins)
```

</details>

## Schritt-für-Schritt-Anleitung

`weights = [2, 5, 4, 7, 1, 3, 8]`, `capacity = 10`.

1. **Absteigend sortieren:** `[8, 7, 5, 4, 3, 2, 1]`.
2. **Iterieren:**
   - `8`: Keine Behälter. Behälter 1 öffnen. `bins = [2]`.
   - `7`: In Behälter 1 sind noch 2 übrig. Zu klein. Behälter 2 öffnen. `bins = [2, 3]`.
   - `5`: Behälter 1 (2), Behälter 2 (3) zu klein. Behälter 3 öffnen. `bins = [2, 3, 5]`.
   - `4`: Behälter 1 (2), Behälter 2 (3) zu klein. Passt in Behälter 3! `bins = [2, 3, 1]`.
   - `3`: Fach 1(2) zu klein. Passt in Fach 2! `bins = [2, 0, 1]`.
   - `2`: Passt in Fach 1! `bins = [0, 0, 1]`.
   - `1`: Fach 1(0), Fach 2(0). Passt in Fach 3! `bins = [0, 0, 0]`.

Ausgabe: `3` Behälter. ✓
*(Beachten Sie, wie die kleineren Elemente 4, 3, 2, 1 die Lücken, die die großen Elemente hinterlassen haben, perfekt ausgefüllt haben! Hätten wir sie in aufsteigender Reihenfolge verarbeitet, hätten wir enorme Mengen an Platz verschwendet).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N)$ |

Das Sortieren dauert $O(N \log N)$. Im schlimmsten Fall (wenn jedes Element das Öffnen eines neuen Behälters erzwingt) durchsucht die innere Schleife 1, dann 2, dann 3 … Behälter, was zu einer Zeitkomplexität von $O(N^2)$ führt.
Die Platzkomplexität beträgt $O(N)$, da im schlimmsten Fall genau N Behälter geöffnet werden müssen.

## Varianten & Optimierungen

- **$O(N \log N)$ FFD mittels Segmentbäumen:** Der $O(N^2)$-Durchlauf lässt sich mithilfe eines Segmentbaums auf $O(\log N)$ pro Element optimieren! Der Segment Tree speichert den *maximal verfügbaren Platz* in jedem Behälter innerhalb eines bestimmten Bereichs. Beim Einlegen eines Gegenstands nutzen wir den Segment Tree, um per binärer Suche das erste Fach (das am weitesten links liegende Blatt) zu finden, dessen maximaler Platz \ge dem Gewicht des Gegenstands ist! Dadurch sinkt die Gesamtlaufzeit von FFD auf streng $O(N \log N)$.
- **Best Fit Decreasing (BFD):** Anstatt den *ersten* Behälter auszuwählen, der passt, wählt man den Behälter aus, der nach dem Einlegen des Objekts den *engsten verbleibenden Platz* aufweist (und die kleinste Lücke hinterlässt). Es hat genau dieselbe Näherungsgrenze von \frac{11}{9} wie FFD, schneidet in empirischen Tests jedoch etwas besser ab.

## Praktische Anwendungen

- **Cloud Computing:** Packen von virtuellen Maschinen (Elemente mit RAM-Anforderungen) auf physische Hypervisor-Server (Behälter mit RAM-Kapazität).
- **Logistik:** Beladen von Standard-Versandpaletten mit Kartons unterschiedlicher Größe.

## Verwandte Algorithmen in cOde(n)

- **[segment_tree_01 - Point Update](../segment_tree/segtree_01_point-update-range-query.md)** — Die Datenstruktur, die erforderlich ist, um die innere Scan-Schleife dieses Algorithmus gemäß $O(\log N)$ zu optimieren.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
