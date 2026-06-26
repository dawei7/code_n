# Formale mathematische Spezifikation: Run-Length-Encoding

## 1. Definitionen und Notation
Sei $S \in \Sigma^*$ ein String der Länge $n$.
Ein String kann eindeutig in eine Sequenz von Runs $(c_k, L_k)$ für $1 \leq k \leq r$ zerlegt werden, wobei $c_k \in \Sigma$, $L_k \in \mathbb{N}^+$, $c_k \neq c_{k+1}$ und $S = \prod_{k=1}^r c_k^{L_k}$ gilt.

## 2. Formalisierung des Algorithmus
Die RLE-Funktion $f : \Sigma^* \to (\Sigma \times \mathbb{N}^*)^*$ wird über einen deterministischen endlichen Automaten (DFA) in einem einzigen Durchlauf (Single-Pass) oder eine prozedurale Schleife berechnet:
1. Initialisiere einen Zähler $C = 1$.
2. Für $i = 2 \dots n$:
   - Wenn $S[i] = S[i-1]$, $C \leftarrow C + 1$.
   - Wenn $S[i] \neq S[i-1]$, gib $(S[i-1], C)$ aus und setze $C \leftarrow 1$ zurück.
3. Gib $(S[n], C)$ aus.

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Die Sequenz wird genau einmal durchlaufen. Die Zeitkomplexität beträgt $O(n)$.
- **Platzkomplexität:** Die Ausgabe benötigt $O(r)$ Platz, wobei $r$ die Anzahl der Runs ist. Die In-Place-Verfolgung erfordert einen Platz-Overhead von $O(1)$.