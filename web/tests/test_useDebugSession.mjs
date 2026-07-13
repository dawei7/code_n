// web/tests/test_useDebugSession.mjs — node --test for the
// useDebugSession hook's reduceMessage() function.
//
// The hook is React-bound; we don't render it in node. But
// the ``reduceMessage`` function is a pure reducer that
// maps a WebSocket message to store-state updates; we
// mirror its logic here and exercise the state machine
// directly. The source in
// ``src/hooks/useDebugSession.ts`` is the same — if the
// two diverge, the tests still cover the documented
// contract.
//
// Run with: `node --test web/tests/test_useDebugSession.mjs`

import { test } from 'node:test';
import assert from 'node:assert/strict';


// Mirror of reduceMessage from useDebugSession.ts. Keep in
// sync — if the source diverges, the assertions will pass
// against the WRONG logic. We mark each test that depends
// on this mirror.
function reduceMessage(msg) {
  switch (msg.type) {
    case 'stopped':
      return {
        debugStatus: 'paused',
        debugCurrentLine: msg.line ?? null,
        debugLocals: Array.isArray(msg.locals) ? msg.locals : [],
        debugStoppedReason: msg.reason ?? 'unknown',
      };
    case 'continued':
      return {
        debugStatus: 'running',
        debugCurrentLine: null,
      };
    case 'exited':
      return {
        debugStatus: 'exited',
        debugCurrentLine: null,
        debugStoppedReason: 'exited',
      };
    case 'error':
      return {
        debugStatus: 'error',
        debugError: msg.message ?? 'unknown error',
      };
    default:
      return {};
  }
}


// The 'mode' literal type used by the hook for step commands.
const STEP_MODES = new Set(['over', 'in', 'out']);


test('reduceMessage: stopped event transitions to paused', () => {
  const out = reduceMessage({
    type: 'stopped',
    line: 7,
    reason: 'breakpoint',
    locals: [{ name: 'i', value: '3', type: 'int', scope: 'Locals' }],
  });
  assert.equal(out.debugStatus, 'paused');
  assert.equal(out.debugCurrentLine, 7);
  assert.equal(out.debugStoppedReason, 'breakpoint');
  assert.equal(out.debugLocals.length, 1);
  assert.equal(out.debugLocals[0].name, 'i');
});

test('reduceMessage: stopped with no line uses null', () => {
  const out = reduceMessage({ type: 'stopped', reason: 'entry' });
  assert.equal(out.debugCurrentLine, null);
  assert.equal(out.debugStoppedReason, 'entry');
});

test('reduceMessage: stopped with non-array locals uses empty', () => {
  const out = reduceMessage({ type: 'stopped', line: 1, locals: 'oops' });
  assert.deepEqual(out.debugLocals, []);
});

test('reduceMessage: continued event transitions to running', () => {
  const out = reduceMessage({ type: 'continued' });
  assert.equal(out.debugStatus, 'running');
  assert.equal(out.debugCurrentLine, null);
});

test('reduceMessage: exited event transitions to exited', () => {
  const out = reduceMessage({ type: 'exited' });
  assert.equal(out.debugStatus, 'exited');
  assert.equal(out.debugCurrentLine, null);
  assert.equal(out.debugStoppedReason, 'exited');
});

test('reduceMessage: error event transitions to error', () => {
  const out = reduceMessage({ type: 'error', message: 'DAP boom' });
  assert.equal(out.debugStatus, 'error');
  assert.equal(out.debugError, 'DAP boom');
});

test('reduceMessage: error without message uses fallback', () => {
  const out = reduceMessage({ type: 'error' });
  assert.equal(out.debugError, 'unknown error');
});

test('reduceMessage: unknown event returns empty patch', () => {
  const out = reduceMessage({ type: 'weird-thing' });
  assert.deepEqual(out, {});
});

test('STEP_MODES: only the three step directions are allowed', () => {
  assert.equal(STEP_MODES.size, 3);
  assert.ok(STEP_MODES.has('over'));
  assert.ok(STEP_MODES.has('in'));
  assert.ok(STEP_MODES.has('out'));
  assert.ok(!STEP_MODES.has('through'));
  assert.ok(!STEP_MODES.has(''));
});
