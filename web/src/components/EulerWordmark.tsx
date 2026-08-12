type EulerWordmarkProps = {
  className?: string;
};

/** The Euler wordmark reveals the mathematical e in red and 'uler' in blue. */
export function EulerWordmark({ className = '' }: EulerWordmarkProps) {
  return (
    <span
      className={`inline-flex items-center select-none font-bold text-base tracking-tight ${className}`.trim()}
      aria-label="Euler"
      role="img"
    >
      <span
        aria-hidden="true"
        style={{
          fontFamily: "Georgia, 'Times New Roman', serif",
          fontStyle: 'italic',
          color: '#ef4444', // Red
          marginRight: '1px',
        }}
      >
        e
      </span>
      <span
        aria-hidden="true"
        style={{
          color: '#3b82f6', // Blue
        }}
      >
        uler
      </span>
    </span>
  );
}
