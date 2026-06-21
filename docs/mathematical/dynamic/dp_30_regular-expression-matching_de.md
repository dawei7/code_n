# Formale mathematische Spezifikation: Regular Expression Matching

## 1. Definitionen und Notation
String $S$, Pattern $P$ mit `.` und `*`.

## 2. Algebraische Charakterisierung (Rekursionsgleichung)
Sei $M(i, j)$ wahr, wenn $S[1 \dots i]$ auf $P[1 \dots j]$ passt. Für `*` an der Stelle $P[j]$ gilt $M(i, j) = M(i, j-2) \lor (M(i-1, j) \land (S[i] == P[j-1] \lor P[j-1] == '.'))$.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** $O(nm)$.
- **Platzkomplexität:** $O(nm)$.