# Formale mathematische Spezifikation: N-Damen-Problem (Branch and Bound)

## 1. Definitionen und Notation

Sei $N \in \mathbb{Z}^+$ die Dimension eines quadratischen Schachbretts, das durch die Menge der Koordinaten $\mathcal{C} = \{ (r, c) \mid 0 \le r, c < N \}$ repräsentiert wird. Eine Konfiguration von $N$ Damen ist eine Menge von Positionen $\mathcal{Q} = \{ (r_0, c_0), (r_1, c_1), \dots, (r_{N-1}, c_{N-1}) \}$.

Das N-Damen-Problem erfordert das Finden der Menge aller gültigen Konfigurationen $\mathcal{S} \subseteq \mathcal{P}(\mathcal{C})$, sodass für zwei beliebige verschiedene Damen $(r_i, c_i), (r_j, c_j) \in \mathcal{Q}$ gilt:
1. **Zeilenbedingung:** $r_i \neq r_j$
2. **Spaltenbedingung:** $c_i \neq c_j$
3. **Hauptdiagonalbedingung:** $(r_i - c_i) \neq (r_j - c_j)$
4. **Nebendiagonalbedingung:** $(r_i + c_i) \neq (r_j + c_j)$

Zur Optimierung der Suche definieren wir den Zustandsraum $\mathcal{S}$ unter Verwendung der folgenden Indikatorvektoren (die "Bound"-Arrays):
- $\mathcal{R} \in \{0, 1\}^N$, wobei $\mathcal{R}_r = 1$, falls die Zeile $r$ belegt ist.
- $\mathcal{D}_1 \in \{0, 1\}^{2N-1}$, wobei $\mathcal{D}_{1, k} = 1$, falls die Hauptdiagonale $r - c + (N-1) = k$ belegt ist.
- $\mathcal{D}_2 \in \{0, 1\}^{2N-1}$, wobei $\mathcal{D}_{2, k} = 1$, falls die Nebendiagonale $r + c = k$ belegt ist.

## 2. Algebraische Charakterisierung

Der Algorithmus verwendet eine Tiefensuche (DFS) über den Spaltenindex $j \in \{0, \dots, N-1\}$. Sei $f(j)$ die Teilkonfiguration der Damen, die in den Spalten $0$ bis $j-1$ platziert wurden.

Für eine Kandidatenposition $(r, j)$ ist das Gültigkeitsprädikat $\Psi(r, j)$ definiert als:
$$\Psi(r, j) \iff (\mathcal{R}_r = 0) \land (\mathcal{D}_{1, r-j+N-1} = 0) \land (\mathcal{D}_{2, r+j} = 0)$$

Der Zustandsübergang in Spalte $j$ ist durch die Abbildung definiert:
$$\text{Update}(\mathcal{R}, \mathcal{D}_1, \mathcal{D}_2, r, j) \to (\mathcal{R}', \mathcal{D}_1', \mathcal{D}_2')$$
wobei:
$$\mathcal{R}'_i = \mathcal{R}_i \lor [i=r]$$
$$\mathcal{D}'_{1, k} = \mathcal{D}_{1, k} \lor [k = r-j+N-1]$$
$$\mathcal{D}'_{2, k} = \mathcal{D}_{2, k} \lor [k = r+j]$$

Der Algorithmus terminiert, wenn $j=N$, was eine erfolgreiche Platzierung von $N$ Damen repräsentiert. Der Backtracking-Mechanismus stellt sicher, dass wir für jeden Zustand $(j, \mathcal{R}, \mathcal{D}_1, \mathcal{D}_2)$ die Menge der gültigen Zeilen $r \in \{0, \dots, N-1\}$ untersuchen, für die $\Psi(r, j)$ wahr ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Suchraum wird durch einen Baum der Tiefe $N$ repräsentiert. Auf jeder Ebene $j$ iterieren wir über $N$ mögliche Zeilen. Der Verzweigungsfaktor nimmt aufgrund der Bedingungen ab, während wir den Baum durchlaufen.

Die Gesamtzahl der im schlechtesten Fall besuchten Knoten ist durch den Permutationsraum von $N$ Damen begrenzt, welcher $N!$ beträgt. Beim naiven Backtracking-Ansatz erfordert die `is_safe`-Prüfung $O(N)$ Zeit, um das Brett zu scannen. In dieser Branch-and-Bound-Formulierung wird das Gültigkeitsprädikat $\Psi(r, j)$ in $O(1)$ Zeit durch direkten Array-Zugriff ausgewertet.

Somit ergibt sich die gesamte Zeitkomplexität zu:
$$T(N) = \sum_{k=0}^{N-1} \frac{N!}{(N-k)!} \cdot O(1) = O(N!)$$
Während die asymptotische Komplexität bei $O(N!)$ bleibt, führt die Reduktion des konstanten Faktors von $O(N)$ auf $O(1)$ pro Knotenbesuch zu einer signifikanten praktischen Leistungssteigerung.

### Platzkomplexität
Die Platzkomplexität wird durch den zusätzlichen Speicherbedarf für die Bedingungs-Arrays und den Rekursions-Stack bestimmt:
1. **Bedingungs-Arrays:** $\mathcal{R}$ benötigt $O(N)$, während $\mathcal{D}_1$ und $\mathcal{D}_2$ jeweils $O(2N-1)$ benötigen. Gesamt: $O(N)$.
2. **Rekursions-Stack:** Die Tiefe des DFS-Baums beträgt $N$, was $O(N)$ Stack-Speicher erfordert.

Addiert man diese Komponenten, ergibt sich die gesamte zusätzliche Platzkomplexität zu:
$$S(N) = O(N) + O(N) = O(N)$$