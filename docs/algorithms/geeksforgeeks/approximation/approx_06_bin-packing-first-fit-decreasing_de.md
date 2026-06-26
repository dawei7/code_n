# Bin Packing (First Fit Decreasing)

| | |
|---|---|
| **ID** | `approx_06` |
| **Kategorie** | approximation |
| **Komplexität (erforderlich)** | $O(N \log N)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem) |

## Problemstellung

Gegeben sind $N$ Elemente mit unterschiedlichen Gewichten und eine unendliche Anzahl an Bins mit einer maximalen Kapazität $C$. Es ist die **minimale Anzahl an Bins** zu finden, die benötigt wird, um alle Elemente zu verpacken.
Dies ist ein klassisches NP-schweres Problem. Sie müssen den **First Fit Decreasing (FFD)** Algorithmus implementieren, der garantiert nicht mehr als $\frac{11}{9} OPT + 1$ Bins benötigt (ein erstaunlich enges Approximationsverhältnis von ~1,22!).

**Eingabe:** Eine Liste von `weights` der Elemente und eine `capacity` $C$ der Bins.
**Ausgabe:** Eine Ganzzahl, die die minimale Anzahl der verwendeten Bins repräsentiert.

## Wann ist dieser Algorithmus zu verwenden?

- Zum Packen von Datenpaketen in Netzwerk-MTU-Frames fester Größe.
- Zur Planung von Aufgaben unterschiedlicher Dauer auf identischen Maschinen, wobei jede Maschine nur für eine 8-Stunden-Schicht verfügbar ist.

## Ansatz

Ein naiver Greedy-Ansatz (First Fit) betrachtet die Elemente einfach in der gegebenen Reihenfolge und schiebt sie in das erste Bin, das genügend Platz bietet. Wenn kein Bin Platz hat, wird ein neues Bin geöffnet. Dies liefert eine 1,7-Approximation.
Wir können dies drastisch verbessern, indem wir einen einfachen Schritt hinzufügen: **Sortieren Sie die Elemente zuerst von groß nach klein!**

**First Fit Decreasing (FFD):**
Wenn wir die massiven, schwer unterzubringenden Elemente zuerst platzieren, belegen diese auf natürliche Weise ihre eigenen Bins. Danach können die kleinen Elemente perfekt in die "verbleibenden" Lücken der bereits geöffneten Bins einsortiert werden!

1. Sortieren Sie die Elemente in **absteigender** Reihenfolge.
2. Verwalten Sie eine Liste der aktuell offenen Bins, initialisiert als leer. Jedes Bin verfolgt seine *verbleibende Kapazität*.
3. Iterieren Sie durch die sortierten Elemente:
   - Für jedes Element wird die Liste der offenen Bins linear von links nach rechts durchsucht (First Fit).
   - Wenn ein Bin eine `remaining_capacity >= item_weight` aufweist, platzieren Sie das Element in diesem Bin, aktualisieren Sie dessen Kapazität und brechen Sie die Suchschleife ab.
   - Wenn KEIN offenes Bin genügend Platz bietet, öffnen Sie ein neues Bin, platzieren Sie das Element darin und fügen Sie es der Liste der offenen Bins hinzu.
4. Geben Sie die Gesamtzahl der offenen Bins zurück.

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

## Durchlauf

`weights = [2, 5, 4, 7, 1, 3, 8]`, `capacity = 10`.

1. **Absteigend sortieren:** `[8, 7, 5, 4, 3, 2, 1]`.
2. **Iterieren:**
   - `8`: Keine Bins vorhanden. Öffne Bin 1. `bins = [2]`.
   - `7`: Bin 1 hat noch 2 Platz. Zu klein. Öffne Bin 2. `bins = [2, 3]`.
   - `5`: Bin 1(2), Bin 2(3) zu klein. Öffne Bin 3. `bins = [2, 3, 5]`.
   - `4`: Bin 1(2), Bin 2(3) zu klein. Passt in Bin 3! `bins = [2, 3, 1]`.
   - `3`: Bin 1(2) zu klein. Passt in Bin 2! `bins = [2, 0, 1]`.
   - `2`: Passt in Bin 1! `bins = [0, 0, 1]`.
   - `1`: Bin 1(0), Bin 2(0). Passt in Bin 3! `bins = [0, 0, 0]`.

Ausgabe: `3` Bins. ✓
*(Beachten Sie, wie die kleineren Elemente 4, 3, 2, 1 die Lücken, die von den großen Elementen hinterlassen wurden, perfekt aufgefüllt haben! Hätten wir sie in aufsteigender Reihenfolge verarbeitet, hätten wir massiv Platz verschwendet).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N)$ |

Das Sortieren benötigt $O(N \log N)$. Im schlechtesten Fall (wenn jedes Element das Öffnen eines neuen Bins erzwingt) durchsucht die innere Schleife 1, dann 2, dann 3... Bins, was zu einer Zeitkomplexität von $O(N^2)$ führt.
Die Platzkomplexität beträgt $O(N)$, da wir im schlechtesten Fall genau $N$ Bins öffnen könnten.

## Varianten & Optimierungen

- **$O(N \log N)$ FFD mittels Segment Trees:** Der $O(N^2)$-Suchlauf kann mittels eines Segment Tree auf $O(\log N)$ pro Element optimiert werden! Der Segment Tree speichert den *maximal verfügbaren Platz* in jedem Bin innerhalb eines gegebenen Bereichs. Beim Platzieren eines Elements verwenden wir den Segment Tree für eine binäre Suche nach dem ersten Bin (dem am weitesten links liegenden Blatt), das einen maximalen Platz $\ge$ `item_weight` hat! Dies reduziert die Gesamtlaufzeit von FFD strikt auf $O(N \log N)$.
- **Best Fit Decreasing (BFD):** Anstatt das *erste* Bin zu wählen, das passt, wählen Sie das Bin, das nach dem Platzieren des Elements den *geringsten verbleibenden Platz* hat (die kleinste Lücke hinterlässt). Es hat dieselbe $\frac{11}{9}$-Approximationsschranke wie FFD, schneidet aber in empirischen Tests etwas besser ab.

## Anwendungen in der Praxis

- **Cloud Computing:** Packen von virtuellen Maschinen (Elemente mit RAM-Anforderungen) auf physische Hypervisor-Server (Bins mit RAM-Kapazität).
- **Logistik:** Beladen von Kartons unterschiedlicher Größe auf Standard-Versandpaletten.

## Verwandte Algorithmen in cOde(n)

- **[segment_tree_01 - Point Update](../segment_tree/segtree_01_point-update-range-query.md)** — Die Datenstruktur, die erforderlich ist, um die innere Suchschleife dieses Algorithmus auf $O(\log N)$ zu optimieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*