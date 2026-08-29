import { useAppStore } from '../store/useAppStore';

export function TabBar() {
  const openIds = useAppStore((s) => s.openChallengeIds);
  const currentId = useAppStore((s) => s.currentDetail?.id);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const closeChallenge = useAppStore((s) => s.closeChallenge);
  const challenges = useAppStore((s) => s.challenges);

  if (openIds.length === 0) {
    return null;
  }

  return (
    <div className="flex items-end h-9 px-2 bg-coden-bg border-b border-coden-border overflow-x-auto select-none shrink-0 scrollbar-hide">
      {openIds.map((id) => {
        const isActive = id === currentId;
        const info = challenges.find((c) => c.id === id);
        const name = info ? info.name : id;
        return (
          <div
            key={id}
            onClick={() => selectChallenge(id)}
            className={[
              'group flex items-center h-8 px-3 min-w-[120px] max-w-[200px] border-r border-coden-border cursor-pointer rounded-t transition-colors',
              isActive
                ? 'bg-coden-surface text-coden-text border-t-2 border-t-coden-accent border-l border-coden-border relative top-[1px] z-10 font-medium shadow-sm'
                : 'bg-coden-surface-elevated/70 text-coden-muted border-t-2 border-t-transparent hover:bg-coden-surface hover:text-coden-text mb-[1px]',
            ].join(' ')}
            title={name}
          >
            <span className="truncate flex-1 text-[12.5px]">{name}</span>
            <button
              className="ml-2 w-4 h-4 flex items-center justify-center rounded text-coden-muted hover:text-coden-text hover:bg-coden-border/60 opacity-0 group-hover:opacity-100 shrink-0 text-[10px] transition-all"
              onClick={(e) => {
                e.stopPropagation();
                closeChallenge(id);
              }}
              title="Close tab"
              aria-label={`Close tab ${name}`}
            >
              ✕
            </button>
          </div>
        );
      })}
    </div>
  );
}
