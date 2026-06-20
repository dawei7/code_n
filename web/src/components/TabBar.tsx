import { useAppStore } from '../store/useAppStore';

export function TabBar() {
  const openIds = useAppStore((s) => s.openChallengeIds);
  const currentId = useAppStore((s) => s.currentDetail?.id);
  const selectChallenge = useAppStore((s) => s.selectChallenge);
  const closeChallenge = useAppStore((s) => s.closeChallenge);
  const challenges = useAppStore((s) => s.challenges);

  if (openIds.length === 0) {
    return null; // or a placeholder if preferred
  }

  return (
    <div className="flex items-end h-9 px-2 bg-[#1e1e1e] border-b border-coden-border overflow-x-auto select-none shrink-0 scrollbar-hide">
      {openIds.map((id) => {
        const isActive = id === currentId;
        const info = challenges.find((c) => c.id === id);
        const name = info ? info.name : id;
        return (
          <div
            key={id}
            onClick={() => selectChallenge(id)}
            className={[
              'group flex items-center h-8 px-3 min-w-[120px] max-w-[200px] border-r border-[#2d2d2d] cursor-pointer rounded-t',
              isActive
                ? 'bg-[#1e1e1e] text-coden-text border-t border-t-coden-accent relative top-[1px] z-10'
                : 'bg-[#2d2d2d] text-coden-muted border-t border-t-transparent hover:bg-[#2a2d2e] hover:text-coden-text mb-[1px]',
            ].join(' ')}
            title={name}
          >
            <span className="truncate flex-1 text-[13px]">{name}</span>
            <button
              className="ml-2 w-5 h-5 flex items-center justify-center rounded hover:bg-white/10 opacity-0 group-hover:opacity-100 shrink-0 text-xs"
              onClick={(e) => {
                e.stopPropagation();
                closeChallenge(id);
              }}
              title="Close"
            >
              ✕
            </button>
          </div>
        );
      })}
    </div>
  );
}
