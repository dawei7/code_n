# Modular Multiplicative Inverse

| | |
|---|---|
| **ID** | `math_08` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(log M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Modular Multiplicative Inverse](https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/) |

## Problemstellung

Gegeben sind eine Ganzzahl A und ein Modulo M. Finde das modulare multiplikative Inverse von A modulo M.
Das modulare Inverse ist eine Ganzzahl X, sodass gilt:
(A x X) \equiv 1 \pmod M
Der Wert von X muss im Bereich [1, M-1] liegen. Falls das Inverse nicht existiert, gib `-1` zurück.

**Eingabe:** Zwei Ganzzahlen `A` und `M`.
**Ausgabe:** Eine Ganzzahl `X`.

## Anwendung

- **Modulare Division:** In der Programmierung sind `(A + B) % M` und `(A * B) % M` völlig unbedenklich. Aber `(A / B) % M` ist MATHEMATISCH UNZULÄSSIG! Man kann den Modulo-Operator nicht auf Brüche anwenden. Um eine modulare Division \frac{A}{B} \pmod M durchzuführen, MUSS man sie als (A x B^{-1}) \pmod M umschreiben, wobei B^{-1} das modulare multiplikative Inverse von B ist!
- Wird ausgiebig in der Kombinatorik verwendet (z. B. erfordert die Berechnung von `nCr % M` die Division durch Fakultäten).

## Ansatz 1: Kleiner Fermatscher Satz (Einfacher, aber M MUSS eine Primzahl sein)

Der Kleine Fermatsche Satz besagt, dass für eine Primzahl M und jede Ganzzahl A, die nicht durch M teilbar ist, gilt:
A^{M-1} \equiv 1 \pmod M

Wenn wir beide Seiten durch A teilen, erhalten wir:
A^{M-2} \equiv A^{-1} \pmod M

Dies ist eine erstaunliche Abkürzung! Das Inverse A^{-1} ist buchstäblich A hoch M-2!
Wir können A^{M-2} \pmod M in $O(log M)$ Zeit mittels **Modularer Exponentiation (`math_03`)** berechnen.
*Einschränkung:* Dies funktioniert NUR, wenn M eine Primzahl ist. Wenn M zusammengesetzt ist (z. B. M=100), versagt der Kleine Fermatsche Satz vollständig.

## Ansatz 2: Erweiterter Euklidischer Algorithmus (Funktioniert für JEDES M)

Was ist, wenn M keine Primzahl ist? Wir kehren zur Definition zurück:
(A x X) \equiv 1 \pmod M

Nach der Definition des Modulo bedeutet ein Rest von 1 bei Division durch M, dass es sich um ein Vielfaches von M plus 1 handelt.
A \cdot X = M \cdot Y + 1
Umgestellt:
A \cdot X - M \cdot Y = 1

Kommt dir diese Gleichung bekannt vor? Es ist die Bézout-Identität: A \cdot x + B \cdot y = \text{GCD}(A, B)!
In unserer Gleichung ist der GCD `1`!
Dies beweist, dass ein modulares Inverses NUR EXISTIERT, wenn A und M teilerfremd sind (ihr GCD ist 1).
Wenn \text{GCD}(A, M) = 1 ist, führen wir einfach den **Erweiterten Euklidischen Algorithmus (`math_07`)** auf A und M aus. Der vom Algorithmus zurückgegebene Koeffizient `x` ist buchstäblich unsere Antwort!

*(Hinweis: Der Algorithmus könnte ein negatives `x` zurückgeben. Da wir uns in der Modulo-Arithmetik befinden, addieren wir einfach M dazu, um es positiv zu machen: `(x % M + M) % M`).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_08: Modular Multiplicative Inverse.

Given a and m (with gcd(a, m) = 1), find x such
"""


def solve(a, m):
    """Return a^-1 mod m using extended Euclidean."""
    if m == 1:
        return 0
    # Reduce a mod m first.
    a = a % m
    if a == 0:
        return 0  # no inverse
    # Extended gcd of (a, m).
    old_r, r = a, m
    old_s, s = 1, 0
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    # old_r = gcd(a, m); old_s is the coefficient of a.
    if old_r != 1:
        return 0  # no inverse
    # Normalize to [0, m).
    return old_s % m
```

</details>

## Durchlauf

Finde das Inverse von A=3 modulo M=11.

**Methode 1 (Fermat):**
Da 11 eine Primzahl ist: Berechne 3^{11-2} \pmod{11} -> 3^9 \pmod{11}.
3^2 = 9.
3^4 = 81 \equiv 4 \pmod{11}.
3^8 = 16 \equiv 5 \pmod{11}.
3^9 = 3^8 x 3^1 = 5 x 3 = 15 \equiv 4 \pmod{11}.
Ergebnis: `4`. ✓
Überprüfung: (3 x 4) \pmod{11} = 12 \pmod{11} = 1. Es funktioniert!

**Methode 2 (Erweiterter Euklidischer Algorithmus):**
A = 3, M = 11.
1. `ext_gcd(3, 11)` ruft `ext_gcd(11, 3)` auf.
2. `ext_gcd(11, 3)` ruft `ext_gcd(3, 2)` auf.
3. `ext_gcd(3, 2)` ruft `ext_gcd(2, 1)` auf.
4. `ext_gcd(2, 1)` ruft `ext_gcd(1, 0)` auf. (Basisfall gibt `1, 1, 0` zurück).
5. Abwicklung:
   - `ext_gcd(2, 1)`: x=0, y=1-(2//1)*0 = 1. Gibt `1, 0, 1` zurück.
   - `ext_gcd(3, 2)`: x=1, y=0-(3//2)*1 = -1. Gibt `1, 1, -1` zurück.
   - `ext_gcd(11, 3)`: x=-1, y=1-(11//3)*-1 = 4. Gibt `1, -1, 4` zurück.
   - `ext_gcd(3, 11)`: x=4, y=-1-(3//11)*4 = -1. Gibt `1, 4, -1` zurück.

Ergebnis `x = 4`. Es ist positiv, also `4 % 11 = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log M)$ | $O(1)$ oder $O(\log M)$ |
| **Schlechtester Fall** | $O(\log M)$ | $O(1)$ oder $O(\log M)$ |

Die Fermat-Methode basiert auf modularer Exponentiation, die $O(log(\text{Exponent}))$ -> $O(log M)$ Zeit und $O(1)$ Platz benötigt.
Der erweiterte Euklidische Algorithmus benötigt $O(log(\min(A, M)))$ -> $O(log A)$ Zeit und $O(log A)$ Platz für den Rekursions-Stack.

## Varianten & Optimierungen

- **Array-Inverse-Vorberechnung:** Wenn du das Inverse jeder Zahl von 1 bis N modulo M finden musst, dauert der Aufruf von `O(\log M)` für jede Zahl insgesamt $O(N log M)$. Es gibt einen mathematischen DP-Trick, der alle N Inversen in $O(N)$ linearer Zeit berechnet!
`inv[i] = M - (M // i) * inv[M % i] % M`

## Anwendungen in der Praxis

- **Kryptographie:** Wird überall in Public-Key-Kryptographie-Algorithmen (RSA, Diffie-Hellman, Elliptische Kurven) verwendet, bei denen Operationen in riesigen endlichen Körpern modulo P stattfinden.

## Verwandte Algorithmen in cOde(n)

- **[math_03 - Modular Exponentiation](math_03_modular-exponentiation.md)** — Die Abhängigkeit für den Kleinen Fermatschen Satz.
- **[math_07 - Extended Euclidean](math_07_extended-euclidean-algorithm.md)** — Die Abhängigkeit für den universellen Ansatz.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*