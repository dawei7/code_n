# Minimum Coins (Greedy-Variante)

| | |
|---|---|
| **ID** | `greedy_10` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(V)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **GeeksForGeeks Äquivalent** | [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/) |

## Problemstellung

Gegeben ist ein Integer `V`, der einen Zielwert repräsentiert, sowie ein Array von Münzwerten (`coins`), die das Standardwährungssystem eines Landes darstellen (z. B. Indische Rupie `[1, 2, 5, 10, 20, 50, 100, 500, 1000]`).
Finden Sie die absolute Mindestanzahl an Münzen, die erforderlich ist, um exakt den Wert `V` zu erreichen. Sie verfügen über einen unendlichen Vorrat jeder Münzstückelung.

**Eingabe:** Zielwert `V`, Array von Integer-Münzwerten `coins`.
**Ausgabe:** Ein Integer, der die Mindestanzahl an Münzen repräsentiert, oder eine Liste der verwendeten Münzen.

## Wann man diesen Ansatz verwendet

- Wenn die gegebenen Stückelungen "kanonisch" sind (wie US-Dollar, Indische Rupien, Euro).
- *Kritische Einschränkung:* Wenn die Stückelungen NICHT-kanonisch sind (z. B. `[1, 3, 4]`), SCHEITERT dieser Greedy-Ansatz mathematisch, und Sie müssen Dynamische Programmierung (`dp_05`) verwenden.

## Ansatz

**1. Die Greedy-Philosophie:**
Wenn Sie die *Anzahl* der physischen Münzen in Ihrer Hand minimieren möchten, sollten Sie offensichtlich die Münzen mit dem höchstmöglichen Wert verwenden!
Warum zehn `10`-Scheine verwenden, wenn man einfach einen `100`-Schein nehmen kann?

**2. Die kanonische Garantie:**
In einem Standardwährungssystem funktioniert die Greedy-Wahl perfekt, da jede größere Münze einer Kombination aus kleineren Münzen, die sie ersetzt, strikt überlegen ist. Sie werden niemals auf einen bizarren Grenzfall stoßen, bei dem die Verwendung einer kleineren Münze eine effizientere globale Kombination ermöglicht.

**3. Der Algorithmus:**
1. Sortieren Sie das `coins`-Array in absteigender Reihenfolge (falls nicht bereits geschehen).
2. Iterieren Sie durch die `coins`.
3. Solange die aktuelle `coin` \le dem verbleibenden Zielwert `V` ist, subtrahieren Sie diese gierig von `V`!
   - (Optimierte Mathematik: Anstatt einer `while`-Schleife zur Subtraktion verwenden Sie Ganzzahldivision: `count = V // coin` und aktualisieren `V = V % coin`).
4. Fahren Sie fort, bis `V` den Wert 0 erreicht.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_10: Minimum Coins.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        if c <= 0:
            continue
        while amount >= c:
            amount -= c
            count += 1
        if amount == 0:
            break
    if amount == 0:
        return count
    return -1
```

</details>

## Durchlauf

`V = 43`. `coins = [1, 2, 5, 10, 20, 50, 100]` (Bereits absteigend sortiert: `[100, 50, 20, 10, 5, 2, 1]`).

1. `coin = 100`: 100 \le 43 ist falsch.
2. `coin = 50`: 50 \le 43 ist falsch.
3. `coin = 20`: 20 \le 43 ist wahr!
   - `count = 43 // 20 = 2`.
   - `ans` erhält zwei `20`er. `ans = [20, 20]`.
   - `V = 43 % 20 = 3`.
4. `coin = 10`: 10 \le 3 ist falsch.
5. `coin = 5`: 5 \le 3 ist falsch.
6. `coin = 2`: 2 \le 3 ist wahr!
   - `count = 3 // 2 = 1`.
   - `ans` erhält eine `2`. `ans = [20, 20, 2]`.
   - `V = 3 % 2 = 1`.
7. `coin = 1`: 1 \le 1 ist wahr!
   - `count = 1 // 1 = 1`.
   - `ans` erhält eine `1`. `ans = [20, 20, 2, 1]`.
   - `V = 1 % 1 = 0`.
8. Die Schleife endet, da V=0.

Ergebnis `[20, 20, 2, 1]`. (Anzahl = 4). ✓

*Warum es bei nicht-kanonischen Werten wie `[1, 3, 4]` und `V=6` scheitert:*
Greedy nimmt `4`. Rest `2`. Nimmt `1`, `1`. Gesamtzahl der Münzen = 3 (`[4, 1, 1]`).
Die optimale DP-Lösung nimmt `3`, `3`. Gesamtzahl der Münzen = 2 (`[3, 3]`).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(C)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(C)$ | $O(1)$ |
| **Schlechtester Fall** | $O(C)$ | $O(1)$ |

Wobei C die Anzahl der verfügbaren Münzstückelungen ist (z. B. 9 im Indischen Rupien-System).
Da wir Mathematik (`//` und `%`) anstelle einer `while`-Schleife verwenden, benötigt die Verarbeitung jeder Münzstückelung $O(1)$ Zeit, unabhängig davon, wie groß V ist! Daher ist die Zeitkomplexität strikt durch die Größe des Stückelungs-Arrays $O(C)$ begrenzt.
Da C normalerweise eine kleine Konstante wie 10 ist, läuft der Algorithmus in konstanter Zeit $O(1)$.
Die Platzkomplexität beträgt $O(1)$, wenn nur die Anzahl zurückgegeben wird, oder $O(\text{Anzahl der Ergebnisse})$, wenn die spezifische Liste der Münzen zurückgegeben wird.

## Varianten & Optimierungen

- **Coin Change II (Kombinationen):** Das Finden der Mindestanzahl an Münzen ist eine Sache, aber was ist, wenn Sie die GESAMTE Anzahl der eindeutigen Möglichkeiten finden möchten, den Wert V zu bilden? Das ist strikt ein DP-Problem (`dp_04`) und kann nicht gierig gelöst werden.

## Praxisanwendungen

- **Registrierkassen / Geldautomaten:** Der exakte Algorithmus, der auf dem Mikroprozessor eines Geldautomaten läuft, um zu berechnen, welche physischen Scheine ausgegeben werden sollen, wenn ein Benutzer einen ungeraden Auszahlungsbetrag wie `$380` anfordert.

## Verwandte Algorithmen in cOde(n)

- **[greedy_09 - Lemonade Change](greedy_09_lemonade-change.md)** — Eine fest codierte Anwendung genau dieser Logik, die speziell auf 5-, 10- und 20-Dollar-Scheine beschränkt ist.
- **[dp_05 - Coin Change Problem](../dynamic/dp_05_coin-change.md)** — Die mathematisch verallgemeinerte DP-Lösung, die nicht-kanonische (bizarre) Währungssysteme korrekt handhabt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*