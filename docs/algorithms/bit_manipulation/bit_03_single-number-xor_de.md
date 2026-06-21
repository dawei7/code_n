# Single Number (XOR)

| | |
|---|---|
| **ID** | `bit_03` |
| **Kategorie** | bit_manipulation |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Single Number](https://leetcode.com/problems/single-number/) |

## Problemstellung

Gegeben ist ein nicht leeres Array von Integern `nums`, in dem jedes Element *zweimal* vorkommt, außer einem. Finden Sie dieses einzelne Element.
Sie müssen eine Lösung mit linearer Zeitkomplexität implementieren, die nur konstanten zusätzlichen Speicherplatz verwendet.

**Eingabe:** Ein Integer-Array `nums`.
**Ausgabe:** Ein Integer, der die einzelne Zahl repräsentiert.

## Wann man es verwendet

- Um die magischen, kommutativen Eigenschaften des bitweisen XOR-Operators (`^`) zu demonstrieren.
- Als grundlegender "Auslöschungs"-Trick, der zur Lösung einer ganzen Familie von Problemen mit gepaarten Array-Elementen verwendet wird.

## Ansatz

**1. Die Schwächen der Standardansätze:**
- **Hash Map:** Zählen Sie die Häufigkeiten jeder Zahl und iterieren Sie dann durch die Map, um den Eintrag mit der Häufigkeit 1 zu finden. Dies benötigt $O(N)$ Zeit, aber $O(N)$ Platz, was die Platzbeschränkung des Problems verletzt!
- **Sortierung:** Sortieren Sie das Array und iterieren Sie dann in 2er-Schritten hindurch. Wenn `nums[i] != nums[i+1]`, haben Sie das Ziel gefunden. Dies benötigt $O(1)$ Platz, aber das Sortieren erfordert $O(N \log N)$ Zeit, was die lineare Zeitbeschränkung verletzt!

**2. Die Magie von XOR:**
Der bitweise XOR-Operator (`^`) vergleicht zwei Binärzahlen Bit für Bit. Wenn die Bits gleich sind, ist das Ergebnis `0`. Wenn sie unterschiedlich sind, ist das Ergebnis `1`.
Dies führt zu zwei unglaublichen mathematischen Axiomen:
1. **Selbstauslöschung:** Jede Zahl, die mit sich selbst XOR-verknüpft wird, ergibt 0! `A ^ A = 0`.
2. **Identität:** Jede Zahl, die mit 0 XOR-verknüpft wird, bleibt sie selbst! `A ^ 0 = A`.

**3. Die kommutative Eigenschaft:**
XOR ist kommutativ und assoziativ. Das bedeutet, dass `A ^ B ^ A` mathematisch identisch mit `(A ^ A) ^ B` ist.
Da `A ^ A = 0` gilt, vereinfacht sich die Gleichung zu `0 ^ B`, was gleich `B` ist!
Beachten Sie, dass die Reihenfolge der Zahlen im Array KEINE Rolle spielt.
Wenn wir eine Variable `result = 0` initialisieren und sie mit jeder einzelnen Zahl im Array XOR-verknüpfen, werden sich alle Zahlen, die zweimal vorkommen, gegenseitig vollständig auslöschen (zu `0` werden), egal wie weit sie voneinander entfernt sind!
Die einzige Zahl, die in `result` übrig bleibt, ist die einzelne Zahl!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bit_03: Single Number (XOR).

Every element in the input array appears exactly
"""


def solve(arr):
    """Return the element that appears exactly once (others appear twice)."""
    result = 0
    for v in arr:
        result ^= v
    return result
```

</details>

## Durchlauf

`nums = [4, 1, 2, 1, 2]`. `result = 0`.

1. **num = 4:**
   - `result = 0 ^ 4 = 4` (`000 ^ 100 = 100`)
2. **num = 1:**
   - `result = 4 ^ 1 = 5` (`100 ^ 001 = 101`)
3. **num = 2:**
   - `result = 5 ^ 2 = 7` (`101 ^ 010 = 111`)
4. **num = 1:**
   - `result = 7 ^ 1 = 6` (`111 ^ 001 = 110`)
   - *(Beachten Sie, dass das '1'-Bit der ersten `1` ausgelöscht wurde!)*
5. **num = 2:**
   - `result = 6 ^ 2 = 4` (`110 ^ 010 = 100`)
   - *(Beachten Sie, dass das '1'-Bit der ersten `2` ausgelöscht wurde!)*

Das endgültige `result` ist 4. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Das Array wird genau einmal durchlaufen, wobei bei jedem Schritt eine einzelne $O(1)$ XOR-Operation durchgeführt wird. Die Zeitkomplexität ist strikt $O(N)$.
Wir verwenden nur eine einzige Integer-Variable `result`, wodurch die Platzkomplexität strikt $O(1)$ ist.

## Varianten & Optimierungen

- **Missing Number (1 bis N):** Gegeben ist ein Array von N verschiedenen Zahlen aus dem Bereich 0 bis N. Eine Zahl fehlt. Finden Sie diese.
  Sie können dies mit XOR lösen! Im Array fehlt genau EINE gepaarte Zahl. Wenn Sie alle Indizes `0...N` XOR-verknüpfen und dann alle Werte im Array `nums` XOR-verknüpfen, wird sich jede Zahl paaren und auslöschen, *außer* dem fehlenden Index!
- **Single Number II (Jedes Element erscheint 3-mal):** Der XOR-Trick schlägt fehl, da `A ^ A ^ A = A` gilt und nicht `0`. Sie müssen einen Zustandsautomaten mit zwei Variablen (`ones`, `twos`) verwenden, um die Bits modulo 3 zu verfolgen.
- **Single Number III (Zwei Elemente erscheinen einmal):** Wenn zwei Zahlen einzigartig sind, ist das endgültige XOR-Ergebnis `A ^ B`. Sie müssen Brian Kernighans Trick (`result & -result`) verwenden, um ein unterscheidendes Bit zu isolieren, dann das Array in zwei Buckets aufteilen und den XOR-Trick erneut auf beide Buckets anwenden! (`bit_05`)

## Anwendungen in der Praxis

- **RAID-Speichersysteme:** RAID 4- und RAID 5-Arrays verteilen Daten auf mehrere Festplatten und verwenden ein zusätzliches "Paritäts"-Laufwerk. Das Paritätslaufwerk ist buchstäblich nur das bitweise XOR aller anderen Laufwerke! Wenn ein einzelnes Laufwerk ausfällt, können die exakten Daten des fehlenden Laufwerks wiederhergestellt werden, indem die verbleibenden Laufwerke mit dem Paritätslaufwerk XOR-verknüpft werden.

## Verwandte Algorithmen in cOde(n)

- **[bit_05 - Single Number III](bit_05_single-number-iii.md)** — Die deutlich schwierigere Variante, bei der genau ZWEI Zahlen einmal vorkommen.
- **[bit_10 - Missing Number](bit_10_missing-number.md)** — Die Variante, bei der Sie gegen eine bekannte erwartete Sequenz XOR-verknüpfen müssen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*