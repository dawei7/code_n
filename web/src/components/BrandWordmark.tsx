type BrandWordmarkProps = {
  className?: string;
};


/** The product wordmark reveals the mathematical O(n) inside “code”. */
export function BrandWordmark({ className = '' }: BrandWordmarkProps) {
  return (
    <span
      className={`coden-wordmark ${className}`.trim()}
      aria-label="cOde(n)"
      role="img"
    >
      <span className="coden-wordmark-code" aria-hidden="true">c</span>
      <span className="coden-wordmark-complexity" aria-hidden="true">O</span>
      <span className="coden-wordmark-code" aria-hidden="true">de</span>
      <span className="coden-wordmark-complexity" aria-hidden="true">(n)</span>
    </span>
  );
}
