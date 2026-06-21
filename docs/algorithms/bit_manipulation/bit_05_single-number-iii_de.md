# Single Number III

| | |
|---|---|
| **ID** | `bit_05` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Single Number III](https://leetcode.com/problems/single-number-iii/) |

## Problemstellung

Gegeben ist ein Array `nums` von Ganzzahlen, in dem genau **zwei** Elemente nur einmal vorkommen und alle anderen Elemente genau zweimal vorkommen. Finden Sie die zwei Elemente, die nur einmal vorkommen. Sie können das Ergebnis in beliebiger Reihenfolge zurückgeben.
Sie müssen einen Algorithmus schreiben, der eine lineare Zeitkomplexität aufweist und nur konstanten zusätzlichen Speicherplatz benötigt.

**Eingabe:** Ein Array `nums` von Ganzzahlen.
**Ausgabe:** Ein Array mit zwei Ganzzahlen, die die eindeutigen Zahlen repräsentieren.

## Wann man es verwendet

- Um absolute Beherrschung der XOR-Eigenschaften und der Bit-Isolierung zu demonstrieren.
- Dies ist eine Kombination aus zwei bekannten Bit-Tricks: Der XOR-Array-Kollaps (`bit_03`) UND Brian Kernighans Isolierung des niedrigsten gesetzten Bits (`bit_01`).

## Ansatz

**1. Der anfängliche XOR-Kollaps:**
Wenn wir jede Zahl im Array mittels XOR verknüpfen (genau wie bei Single Number I), heben sich alle gepaarten Zahlen zu `0` auf.
Was bleibt übrig? Seien A und B die beiden eindeutigen Zahlen.
Das Endergebnis ist `xor_sum = A ^ B`.
Da A und B eindeutige Zahlen sind, gilt A \neq B. Das bedeutet, `xor_sum` KANN NICHT 0 sein. Es MUSS mindestens ein Bit in `xor_sum` auf `1` gesetzt sein!

**2. Die Bedeutung eines '1'-Bits im XOR:**
Was bedeutet ein `1`-Bit in einem XOR-Ergebnis? Es bedeutet, dass A und B an dieser spezifischen Bit-Position UNTERSCHIEDLICHE Werte hatten! (Einer von ihnen hatte eine `1`, der andere eine `0`).
Wenn wir *irgendein* `1`-Bit aus `xor_sum` isolieren können, haben wir ein Unterscheidungsmerkmal zwischen A und B gefunden.

**3. Isolierung des Bits (Brian Kernighans Variante):**
Um das absolut niedrigste (am weitesten rechts stehende) `1`-Bit einer beliebigen Zahl zu isolieren, verwenden wir den folgenden Trick:
`diff_bit = xor_sum & -xor_sum`
(Hinweis: In der Zweierkomplement-Arithmetik ist `-n` äquivalent zu `~n + 1`. Die UND-Verknüpfung beider Werte setzt alles außer dem niedrigsten gesetzten Bit auf Null).

**4. Aufteilen des Arrays:**
Nun haben wir ein `diff_bit` (z. B. `00100`). Wir wissen sicher, dass A an dieser Position eine `1` hat und B eine `0` (oder umgekehrt).
Wir können das ursprüngliche Array erneut durchlaufen und die Zahlen in zwei völlig getrennte Buckets aufteilen:
- Bucket 1: Zahlen, die an der `diff_bit`-Position eine `1` haben (`(num & diff_bit) != 0`).
- Bucket 2: Zahlen, die an der `diff_bit`-Position eine `0` haben (`(num & diff_bit) == 0`).

**5. Die finale Aufhebung:**
A landet vollständig in Bucket 1. B landet vollständig in Bucket 2.
Was ist mit den gepaarten Zahlen? Da gepaarte Zahlen identisch sind, haben sie IMMER identische Bits! Daher landen die Paare ENTWEDER beide in Bucket 1 ODER beide in Bucket 2!
Nun enthält Bucket 1 A umgeben von Paaren. Bucket 2 enthält B umgeben von Paaren.
Wir wenden nun einfach den Standard-XOR-Trick von Single Number I auf beide Buckets unabhängig voneinander an, um A und B zu enthüllen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_05: Single Number III.

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the two elements that appear exactly once (sorted)."""
    xor_all = 0
    for v in arr:
        xor_all ^= v
    diff_bit = xor_all & -xor_all
    a, b = 0, 0
    for v in arr:
        if v & diff_bit:
            a ^= v
        else:
            b ^= v
    return sorted([a, b])
```

</details>

## Durchlauf

`nums = [1, 2, 1, 3, 2, 5]`. (Die eindeutigen Zahlen sind 3 und 5).

1. **Schritt 1 (XOR-Kollaps):**
   - `xor_sum = 1^2^1^3^2^5`
   - `1`er heben sich auf. `2`er heben sich auf.
   - `xor_sum = 3 ^ 5`. (`011 ^ 101 = 110`). `xor_sum = 6`.
2. **Schritt 2 (Bit isolieren):**
   - `diff_bit = 6 & -6`.
   - `6` ist `0110`. `-6` ist `...11111010`.
   - `0110 & 1010 = 0010`. `diff_bit = 2`.
   - (Dies beweist, dass das 2. Bit von rechts zwischen 3 und 5 UNTERSCHIEDLICH ist).
3. **Schritt 3 (Aufteilen & XOR):**
   - Initialisiere `a = 0`, `b = 0`.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 0 ^ 1 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 0 ^ 2 = 2`.
   - `num = 1 (001)`: `1 & 2 == 0`. Bucket B. `b = 1 ^ 1 = 0`. (Paar aufgehoben!).
   - `num = 3 (011)`: `3 & 2 != 0`. Bucket A. `a = 2 ^ 3 = 1`.
   - `num = 2 (010)`: `2 & 2 != 0`. Bucket A. `a = 1 ^ 2 = 3`. (Paar aufgehoben!).
   - `num = 5 (101)`: `5 & 2 == 0`. Bucket B. `b = 0 ^ 5 = 5`.

Ergebnis `a = 3`, `b = 5`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau zweimal durchlaufen. Bitweise Operationen sind $O(1)$. Die Gesamtzeit ist strikt $O(N)$.
Die Platzkomplexität ist $O(1)$, da wir nur die Ganzzahlvariablen `xor_sum`, `diff_bit`, `a` und `b` verwenden.

## Varianten & Optimierungen

- **Vermeidung von Integer-Überlauf:** In Sprachen mit strikten 32-Bit-Ganzzahlen (wie Java/C++), führt die Negation `-xor_sum`, wenn `xor_sum == Integer.MIN_VALUE` ist, zu einem Überlauffehler! Sie müssen explizit auf `MIN_VALUE` prüfen oder vor der Isolierung in eine 64-Bit-Ganzzahl umwandeln. (Python skaliert die Ganzzahlpräzision dynamisch und vermeidet dies).

## Anwendungen in der Praxis

- **Verteiltes Netzwerk (Gossip-Protokolle):** Abgleich von Synchronisationszuständen zwischen zwei massiven Datenbanken. Durch den Austausch von XOR-Signaturen der Datensätze kann ein Server exakt isolieren, welche zwei Datensätze nicht synchron sind, ohne den gesamten Multi-Gigabyte-Datensatz über das Netzwerk übertragen zu müssen!

## Verwandte Algorithmen in cOde(n)

- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — Der grundlegende Voraussetzungs-Algorithmus.
- **[bit_01 - Count Set Bits](bit_01_count-set-bits.md)** — Erklärt die Magie hinter der `n & -n` Bit-Isolierungstechnik.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*