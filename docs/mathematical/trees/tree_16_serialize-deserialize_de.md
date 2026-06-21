# Formale mathematische Spezifikation: Baum-Serialisierung

## 1. Definitionen und Notation
Sei $V \cup \{\#\}$ die Menge der Knoten einschließlich eines Null-Terminators. Wir definieren eine bijektive Kodierungsabbildung $E: \mathcal{T} \to (V \cup \{\#\})^*$.

## 2. Algebraische Charakterisierung
Unter Verwendung einer topologischen Pre-order-Abbildung:
$$ E(T) = \begin{cases} 
\# & \text{if } T = \emptyset \\
r \cdot E(T_L) \cdot E(T_R) & \text{if } T = (r, T_L, T_R)
\end{cases} $$
Da jeder Knoten genau zwei nachfolgende rekursive Aufrufe vorschreibt, besitzt der Parsing-Algorithmus eine deterministische, eindeutige Inverse $E^{-1}$. 

## 3. Komplexitätsanalyse
- **Zeitkomplexität:** Sowohl $E$ als auch $E^{-1}$ besuchen jeden strukturellen Knoten genau einmal. $O(|V|)$.
- **Platzkomplexität:** Der serialisierte String hat die Größe $2|V|+1$. Der Platzbedarf ist strikt $O(|V|)$.