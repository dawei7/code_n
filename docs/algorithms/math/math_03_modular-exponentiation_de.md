# Modulare Exponentiation (Binäre Exponentiation)

| | |
|---|---|
| **ID** | `math_03` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(log E)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Pow(x, n)](https://leetcode.com/problems/powx-n/) |

## Problemstellung

Gegeben sind eine Basis `B`, ein Exponent `E` und ein Modulo `M`.
Berechne (B^E) \pmod M effizient.
(Falls das Problem kein Modulo spezifiziert, nimm M = \infty an, um einfach B^E zu berechnen).

**Eingabe:** Drei Ganzzahlen `B`, `E` und `M`.
**Ausgabe:** Eine Ganzzahl, die das Ergebnis darstellt.

## Wann man es verwendet

- Zur Berechnung riesiger Exponenten, bei denen eine Standard-Multiplikation in $O(E)$ mittels `for i in range(E)` zu einem Time Limit Exceed führen würde.
- Wenn B^E so astronomisch groß ist (z. B. 10^{1000}), dass der Speicher der Programmiersprache überlaufen würde, wenn man das Modulo M nicht dynamisch während der Berechnung anwendet.

## Ansatz

**1. Der Fehler der linearen Multiplikation:**
Um 3^{10} zu berechnen, multipliziert man 3 x 3 x 3... zehnmal. Wenn E = 10^9 ist, erfordert dies eine Milliarde Operationen!

**2. Die Kraft des Halbierens (Divide and Conquer):**
Beachte, dass 3^{10} exakt in zwei Hälften geteilt werden kann!
3^{10} = 3^5 x 3^5.
Wenn wir 3^5 nur EINMAL berechnen und in einer Variable X speichern, erhalten wir 3^{10} einfach durch X x X. Wir haben sofort 4 Multiplikationen übersprungen!
Was ist mit einem ungeraden Exponenten wie 3^5? Er lässt sich nicht gleichmäßig teilen.
Aber wir können eine Basis herausziehen: 3^5 = 3 x 3^4.
Und 3^4 ist gerade! Es lässt sich perfekt in 3^2 x 3^2 teilen.

**3. Der Algorithmus der binären Exponentiation:**
Wir können dies von unten nach oben auswerten, indem wir die Binärdarstellung des Exponenten E betrachten.
Wir führen ein laufendes `result` (initialisiert auf 1).
Solange E > 0:
- Wenn E ungerade ist (d. h. `E % 2 == 1`), multiplizieren wir unser laufendes `result` mit der aktuellen `base`.
- Dann MÜSSEN wir unsere `base` quadrieren (B = B x B), da wir zur nächsten Zweierpotenz übergehen!
- Schließlich halbieren wir unseren Exponenten mittels Ganzzahldivision (E = E // 2).

**4. Die Modulo-Injektion:**
Mathematische Eigenschaft des Modulo: (X x Y) \pmod M = ((X \pmod M) x (Y \pmod M)) \pmod M.
Aufgrund dieser Eigenschaft können wir bei jedem einzelnen Multiplikationsschritt frei `% M` auf unser `result` und unsere `base` anwenden! Dies verhindert perfekt, dass die Variablen jemals die Größe von M^2 überschreiten, was es speichersicher für jede Sprache macht.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_03: Modular Exponentiation.

Repeated squaring. Maintain a result and a base. At each bit
of exp, square the base; if the bit is set, multiply the
result by the base. Take mod after every multiplication to
keep numbers small. O(log exp) time.
"""


def solve(base, exp, mod):
    if mod == 1:
        return 0
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result
```

</details>

## Durchlauf

Berechne 3^{13} \pmod{100}.
B = 3, E = 13, M = 100. `result = 1`.
Die Binärdarstellung von 13 ist `1101` (8 + 4 + 1).

1. `E = 13`. Ungerade!
   - `result = (1 * 3) % 100 = 3`.
   - `B = (3 * 3) % 100 = 9`.
   - `E = 13 // 2 = 6`.
2. `E = 6`. Gerade.
   - `B = (9 * 9) % 100 = 81`.
   - `E = 6 // 2 = 3`.
3. `E = 3`. Ungerade!
   - `result = (3 * 81) % 100 = 243 % 100 = 43`.
   - `B = (81 * 81) % 100 = 6561 % 100 = 61`.
   - `E = 3 // 2 = 1`.
4. `E = 1`. Ungerade!
   - `result = (43 * 61) % 100 = 2623 % 100 = 23`.
   - `B = (61 * 61) % 100 = 3721 % 100 = 21`.
   - `E = 1 // 2 = 0`.
5. `E = 0`. Schleife terminiert!

Ergebnis: `23`. ✓
*(Überprüfung der Berechnung: 3^{13} = 1594323. Modulo 100 ist tatsächlich `23`! Wir haben es in genau 4 Schleifendurchläufen statt 13 berechnet).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log E)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log E)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log E)$ | $O(1)$ |

Da wir den Exponenten E bei jedem Schritt durch 2 teilen, führt die `while`-Schleife exakt \lfloorlog_2(E)\rfloor + 1 Durchläufe aus. Die Zeitkomplexität ist strikt $O(log E)$. Dies verwandelt eine Milliarde Operationen ($O(10^9)$) in nur 30 Operationen ($O(log_2(10^9)$))!
Die Platzkomplexität beträgt $O(1)$ für den iterativen Ansatz.

## Varianten & Optimierungen

- **Matrix-Exponentiation:** Du kannst exakt dieselbe Halbierungslogik auf quadratische Matrizen anwenden! Wenn du die N-te Fibonacci-Zahl in $O(\log N)$ Zeit berechnen möchtest, kannst du eine Zustandsübergangsmatrix definieren und sie mit dieser `while`-Schleife auf die Potenz N erheben! Du ersetzt lediglich die skalare Multiplikation `*` durch eine Matrix-Multiplikationsfunktion!

## Anwendungen in der Praxis

- **Diffie-Hellman-Schlüsselaustausch:** Der mathematische Kern des sicheren Internetverkehrs (HTTPS/TLS) beruht darauf, dass zwei Computer über ein öffentliches Netzwerk sicher einen geheimen Schlüssel vereinbaren. Dies geschieht durch die Übertragung riesiger Zahlen mittels modularer Exponentiation g^a \pmod p, wobei p eine 2048-Bit-Primzahl ist.

## Verwandte Algorithmen in cOde(n)

- **[math_08 - Modulares Multiplikatives Inverses](math_08_modular-multiplicative-inverse.md)** — Wenn du eine modulare *Division* durchführen musst (z. B. (A / B) \pmod M), musst du (A x B^{-1}) \pmod M berechnen. Der kleine Fermatsche Satz besagt B^{-1} \equiv B^{M-2} \pmod M. Um B^{M-2} zu berechnen, verwendest du exakt diesen Algorithmus der modularen Exponentiation!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*