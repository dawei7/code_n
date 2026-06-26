# Missing Number

| | |
|---|---|
| **ID** | `bit_10` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Missing Number](https://leetcode.com/problems/missing-number/) |

## Problemstellung

Gegeben ist ein Array `nums` mit `n` verschiedenen Zahlen im Bereich `[0, n]`. Geben Sie die einzige Zahl im Bereich zurück, die im Array fehlt.

**Eingabe:** Ein Integer-Array `nums` der Länge `n`.
**Ausgabe:** Ein Integer, der die fehlende Zahl repräsentiert.

## Wann man es verwendet

- Um die kommutativen und selbstaufhebenden Eigenschaften von XOR in einem etwas anderen Kontext als bei `Single Number` zu demonstrieren.
- Wenn Sie eine einzelne Diskrepanz zwischen einer bekannten "erwarteten" Sequenz und einer "tatsächlichen" Sequenz finden müssen.

## Ansatz

**1. Der mathematische Ansatz (Gaußsche Summenformel):**
Die Summe der ersten `N` Zahlen ist mathematisch definiert als: \text{Expected Sum} = \frac{n(n + 1)}{2}.
Wenn wir über das Array iterieren und die \text{Actual Sum} berechnen, ist die fehlende Zahl einfach \text{Expected Sum} - \text{Actual Sum}.
*Warum könnte dies in einem Vorstellungsgespräch scheitern?* Wenn N extrem groß ist (z. B. 10^5), könnte die mathematische Summe in Sprachen wie Java oder C++ zu einem Integer-Überlauf führen!

**2. Der XOR-Ansatz:**
Wir wissen aus `bit_03`, dass jede Zahl, die mit sich selbst XOR-verknüpft wird, zu `0` wird (`A ^ A = 0`).
Wenn wir die erwartete Sequenz `[0, 1, 2, 3]` und die tatsächliche Sequenz `[0, 1, 3]` haben, was passiert, wenn wir ALLE diese Zahlen gleichzeitig XOR-verknüpfen?
`Expected = 0 ^ 1 ^ 2 ^ 3`
`Actual   = 0 ^ 1 ^     3`
`Result   = (0^0) ^ (1^1) ^ 2 ^ (3^3)`
`Result   =   0   ^   0   ^ 2 ^   0`
`Result   = 2`!

Jede Zahl, die im Array vorhanden ist, bildet ein perfektes Paar mit ihrer entsprechenden Indexzahl in der erwarteten Sequenz und hebt sich auf! Die EINZIGE Zahl, die übrig bleibt, ist die fehlende Zahl, da sie im tatsächlichen Array keinen Partner hatte, um sich aufzuheben.

**3. Ausführung:**
Initialisieren Sie eine Variable `missing = len(nums)`. (Da die Schleifenindizes nur von `0` bis `n-1` laufen, müssen wir die letzte erwartete Zahl `n` manuell in den XOR-Akkumulator einfügen).
Schleife `i` von `0` bis `n-1`.
`missing ^= i ^ nums[i]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_10: Missing Number.

Given an array arr of n distinct integers in
"""


def solve(arr, n):
    """Find the missing integer in arr (length n, values in [0, n])."""
    # XOR all values and all indices 0..n; the missing value
    # is the survivor.
    result = n  # include the index n in the XOR
    for i, v in enumerate(arr):
        result ^= i ^ v
    return result
```

</details>

## Durchlauf

`nums = [3, 0, 1]`. N = 3.
Initial `missing = 3`.

1. **i = 0:**
   - `missing ^= 0` (Erwarteter Index) -> `3 ^ 0 = 3`
   - `missing ^= nums[0]` (`3`) -> `3 ^ 3 = 0` (Die '3'en haben sich aufgehoben!)
2. **i = 1:**
   - `missing ^= 1` (Erwarteter Index) -> `0 ^ 1 = 1`
   - `missing ^= nums[1]` (`0`) -> `1 ^ 0 = 1` (Die '0'en haben sich implizit aufgehoben)
3. **i = 2:**
   - `missing ^= 2` (Erwarteter Index) -> `1 ^ 2 = 3`
   - `missing ^= nums[2]` (`1`) -> `3 ^ 1 = 2` (Die '1'en haben sich aufgehoben!)

Ergebnis `missing = 2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau einmal durchlaufen. Bitweise XOR-Operationen benötigen $O(1)$ Zeit. Die gesamte Zeitkomplexität beträgt strikt $O(N)$.
Es wird nur eine Integer-Variable `missing` verwendet. Die Platzkomplexität beträgt $O(1)$.
Im Gegensatz zur mathematischen Summenformel führen XOR-Operationen NIEMALS zu einem Integer-Überlauf.

## Varianten & Optimierungen

- **Find the Duplicate Number:** Sie erhalten ein Array der Größe N+1 mit Zahlen im Bereich [1, N]. Es gibt genau EINE doppelte Zahl. Können Sie XOR verwenden? *NEIN!* Da die doppelte Zahl 3- oder 4-mal vorkommen könnte, was die XOR-Aufhebungsregeln bricht. Sie müssen Floyds Zykluserkennung (Tortoise and Hare) oder binäre Suche verwenden.

## Anwendungen in der Praxis

- **Erkennung von Netzwerk-Paketverlusten:** Beim Übertragen eines sequenziellen Stroms von UDP-Paketen (nummeriert von 1 bis N) kann der Empfänger eine laufende XOR-Prüfsumme führen. Wenn genau ein Paket verloren geht, enthüllt die XOR-Prüfsumme sofort dessen ID, ohne die gesamte empfangene Liste scannen zu müssen!

## Verwandte Algorithmen in cOde(n)

- **[bit_03 - Single Number (XOR)](bit_03_single-number-xor.md)** — Der grundlegende Voraussetzungs-Algorithmus.
- **[two_pointers_03 - Find the Duplicate Number](../two_pointers/two_pointers_03_find-the-duplicate-number.md)** — Das Problem, das identisch aussieht, aber strikt nicht mit Bitmanipulation gelöst werden kann.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientiertes Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*