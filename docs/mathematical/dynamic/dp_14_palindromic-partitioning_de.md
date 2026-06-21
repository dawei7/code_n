# Formale mathematische Spezifikation: Palindrom-Partitionierung (Boolesch)

## 1. Definitionen und Notation
String $S$. Bestimme, ob eine gültige Partitionierung existiert, bei der alle Teilstrings Palindrome sind (trivialerweise wahr für Schnitte der Länge 1). Hier definieren wir $C(i, j)$ als die minimale Anzahl an benötigten Schnitten.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $P(i, j)$ wahr, wenn $S[i \dots j]$ ein Palindrom ist. $C(j) = \min_{i \leq j, P(i, j)} (C(i-1) + 1)$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(n^2)$.
- **Platzkomplexität:** $O(n^2)$ für die $P$-Tabelle, $O(n)$ für $C$.