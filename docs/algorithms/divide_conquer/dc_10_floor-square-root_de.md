# Sqrt(x) (Floor-Quadratwurzel)

| | |
|---|---|
| **ID** | `dc_10` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) |

## Aufgabenstellung

Gegeben sei eine nicht-negative ganze Zahl `x`, berechne und gib die Quadratwurzel von `x` zurück.
Da der Rückgabetyp eine ganze Zahl ist, werden die Dezimalstellen abgeschnitten und nur der ganzzahlige Teil des Ergebnisses zurückgegeben.
Es ist nicht erlaubt, integrierte Exponentialfunktionen oder -operatoren wie `pow(x, 0.5)` oder `x ** 0.5` zu verwenden.

**Eingabe:** Eine nicht-negative ganze Zahl `x`.
**Ausgabe:** Eine ganze Zahl, die den ganzzahligen Teil der Quadratwurzel darstellt.

## Anwendungsfälle

- Um zu beweisen, dass man die binäre Suche auf einen kontinuierlichen mathematischen Bereich anwenden kann, anstatt auf ein Array diskreter Objekte.
- Es führt das Konzept der Suche in einem „Antwortraum“ ein (Teile und herrsche).

## Vorgehensweise

**1. Der „Antwortraum“:**
Wir haben kein Array, das wir durchsuchen können. Aber wir wissen, dass die Quadratwurzel von X irgendwo zwischen 0 und X liegen MUSS.
Daher ist unser „Array“ buchstäblich nur die stetige Folge von ganzen Zahlen [0, 1, 2 \dots X].
Da diese Folge von Natur aus sortiert ist, können wir die binäre Suche anwenden!

**2. Die Logik der binären Suche:**
- `low = 0`, `high = x`.
- `mid` finden.
- `square = mid * mid` berechnen.
- Wenn `square == x`: Wir haben die exakte Quadratwurzel gefunden! Gib `mid` zurück.
- Wenn `square < x`: `mid` ist zu klein. Aber Moment mal: Da wir den *ganzzahligen Teil* der Quadratwurzel wollen, könnte `mid` tatsächlich die richtige Antwort sein, wenn das Quadrat der nächsten ganzen Zahl zu groß ist! Wir speichern `mid` in einer Variablen `ans` und suchen dann weiter oben (`low = mid + 1`).
- Wenn `square > x`: `mid` zu groß ist. Die Antwort MUSS kleiner sein. Suche weiter unten (`high = mid - 1`).

**3. Randfälle:**
Wenn X = 0 oder X = 1 ist, ist die Quadratwurzel einfach X. Dies kannst du direkt am Anfang der Funktion behandeln, um mathematische Anomalien zu vermeiden.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_10: Floor Square Root.

Given a non-negative integer n, return floor(sqrt(n)).
"""


def solve(n):
    """Return floor(sqrt(n)) via binary search (D&C style)."""
    if n < 2:
        return n
    lo, hi, res = 1, n, 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        sq = mid * mid
        if sq <= n:
            res = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return res
```

</details>

## Schritt-für-Schritt-Anleitung

`x = 8`. `low = 1`, `high = 4` (da 8/2 = 4).

1. **Schleife 1:**
   - `mid = (1 + 4) // 2 = 2`.
   - `square = 2 * 2 = 4`.
   - `4 < 8`. Das ist ein Kandidat! `ans = 2`.
   - Nach oben verschieben: `low = 2 + 1 = 3`.
2. **Schleife 2:**
   - `mid = (3 + 4) // 2 = 3`.
   - `square = 3 * 3 = 9`.
   - `9 > 8`. Eindeutig zu groß.
   - Nach unten verschieben: `high = 3 - 1 = 2`.
3. **Schleife 3:**
   - `low (3) <= high (2)` ist FALSE. Die Schleife endet.

Das Ergebnis `ans` ist `2`. ✓ (Da 2^2 = 4 und 3^2 = 9 ist, ist der ganzzahlige Teil von \sqrt{8} gleich 2).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log x)$ | $O(1)$ |
| **Schlechteste** | $O(log x)$ | $O(1)$ |

Der Suchraum beginnt bei x/2 und wird wiederholt halbiert. Die Zeitkomplexität beträgt genau $O(log X)$.
Es werden keine zusätzlichen Arrays zugewiesen. Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Newton-Raphson-Verfahren:** Eine auf der Analysis basierende Optimierung, die quadratisch statt logarithmisch konvergiert. Ausgehend von einer Anfangsschätzung r = x aktualisiert man die Schätzung wiederholt mit r = \frac{1}{2} (r + \frac{x}{r}), bis r x r \le x gilt. Dies erfordert Gleitkommadivision, ist jedoch blitzschnell und mathematisch elegant.
- **Ermittlung der exakten Gleitkomma-Quadratwurzel:** Wenn in der Aufgabe die Quadratwurzel mit 5 Dezimalstellen statt des ganzzahligen Teils verlangt wird, kannst du keine ganzzahlige Division verwenden. Du initialisierst `low = 0.0`, `high = max(1.0, x)`. Sie durchlaufen `while (high - low) > 0.00001` (Ihren Genauigkeitsschwellenwert) in einer Schleife und berechnen `mid = (low + high) / 2.0`.

## Praktische Anwendungen

- **Computergrafik (Beleuchtungsmodelle):** Die Berechnung des euklidischen Abstandsvektors zwischen einer Lichtquelle und einer Pixelnormalen erfordert eine enorme Anzahl von Quadratwurzel-Aufrufen. Grafik-Hardware-Pipelines nutzen oft äußerst clevere Bit-Hacks (wie die berühmte schnelle inverse Quadratwurzel `0x5f3759df` aus Quake III), um die Newton-Methode sofort zu approximieren.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** – Die exakt gleiche Kernlogik, nur dass sie auf einen virtuellen Ganzzahlraum statt auf ein Array angewendet wird.
- **[math_01 – Schnelle Potenzierung](../math/math_01_fast-exponentiation.md)** – Ein weiterer mathematischer „Teile-und-herrsche“-Algorithmus.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
