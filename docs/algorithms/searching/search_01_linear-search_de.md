# Linear Search

| | |
|---|---|
| **ID** | `search_01` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 1/10 |
| **Wikipedia** | [Linear search](https://en.wikipedia.org/wiki/Linear_search) |

## Problemstellung

Gegeben ist ein Array `arr` mit `N` Elementen und ein `target`-Wert.
Finde den Index des `target` im Array. Falls das `target` nicht vorhanden ist, gib `-1` zurück.

**Eingabe:** Ein Array `arr` und ein `target`-Wert.
**Ausgabe:** Ein Integer, der den Index des `target` repräsentiert.

## Wann man es verwendet

- Wenn das Array komplett unsortiert ist und keine anderen Datenstrukturen (wie Hash Maps) verfügbar oder erlaubt sind.
- Als Brute-Force-Basislösung, um zu beweisen, warum ein komplexerer Algorithmus (wie Binary Search) notwendig ist.

## Ansatz

**1. Die "Alles-prüfen"-Philosophie:**
Wenn man seine Schlüssel in einem unordentlichen Raum verliert, muss man physisch jeden einzelnen Ort überprüfen, bis man sie findet.
Da das Array komplett unsortiert ist, gibt es keine mathematische Abkürzung, um zu erraten, wo sich das `target` befinden könnte.
Das Element könnte am allerersten oder am allerletzten Index stehen.
Daher müssen wir das gesamte Array vom Index `0` bis zum Index `N-1` durchlaufen.

**2. Die Abbruchbedingung:**
Bei jedem Schritt vergleichen wir `arr[i]` mit dem `target`.
Wenn sie übereinstimmen, geben wir sofort den Index `i` zurück.
Wenn die Schleife jedes einzelne Element überprüft hat und wir nichts zurückgegeben haben, wissen wir mit Sicherheit, dass das Element nicht existiert. Wir geben `-1` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_01: Linear Search.

Walk the array until the target is found or the end is reached.
O(n) time.
"""


def solve(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1
```

</details>

## Durchlauf

`arr = [10, 50, 30, 70, 80, 60, 20, 90, 40]`, `target = 20`.

1. `i = 0`: `arr[0] = 10`. `10 == 20`? Falsch.
2. `i = 1`: `arr[1] = 50`. `50 == 20`? Falsch.
3. `i = 2`: `arr[2] = 30`. `30 == 20`? Falsch.
4. `i = 3`: `arr[3] = 70`. `70 == 20`? Falsch.
5. `i = 4`: `arr[4] = 80`. `80 == 20`? Falsch.
6. `i = 5`: `arr[5] = 60`. `60 == 20`? Falsch.
7. `i = 6`: `arr[6] = 20`. `20 == 20`? WAHR!
   - Gib `6` zurück.

Ergebnis: `6`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Szenario im Bestfall ist, dass das `target` das allererste Element im Array ist, was sofort in $O(1)$ Zeit zurückgegeben wird.
Das Szenario im schlechtesten Fall ist, dass das `target` das allerletzte Element ist oder gar nicht existiert, was uns dazu zwingt, alle N Elemente in $O(N)$ Zeit zu überprüfen.
Die Platzkomplexität ist $O(1)$, da wir nur eine einzige Integer-Variable `i` für den Schleifenzähler verwenden.

## Varianten & Optimierungen

- **Transpositions-Optimierung:** Wenn Sie erwarten, dass bestimmte Elemente mehrfach gesucht werden (wie bei einem Caching-System), tauschen Sie das gefundene `target` am Index `i` mit dem Element am Index `i-1`, bevor Sie es zurückgeben! Über viele Suchvorgänge hinweg werden häufig aufgerufene Elemente natürlich an den Anfang des Arrays "aufsteigen", wodurch ihre zukünftigen Suchzeiten näher an $O(1)$ rücken.
- **Move-to-Front-Optimierung:** Ähnlich wie bei der Transposition, aber anstatt mit `i-1` zu tauschen, tauschen Sie das gefundene `target` sofort ganz an den Index `0`!

## Anwendungen in der Praxis

- **Suche in Linked Lists:** Die lineare Suche ist der EINZIGE Weg, eine Linked List zu durchsuchen, da Linked Lists keinen wahlfreien Zugriff (Random Access) unterstützen, was Algorithmen wie Binary Search unmöglich macht.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Die $O(\log N)$-Alternative, die die lineare Suche komplett ersetzt, aber zwingend voraussetzt, dass das Array zuvor sortiert wurde.
- **[hash_01 - Two Sum](../hashing/hash_01_two-sum.md)** — Verwendet eine Hash Map, um eine verschachtelte $O(N^2)$ doppelte lineare Suche auf $O(N)$ zu reduzieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*