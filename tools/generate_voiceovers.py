import asyncio
import os
from pathlib import Path
import edge_tts

OUTPUT_DIR = Path("C:/Users/david/.gemini/antigravity-ide/brain/e907292b-45e1-4fd9-9687-6bb35593451d/video_production")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

VOICE = "en-US-ChristopherNeural"  # Professional, confident, clear tech narrator

SCRIPTS = {
    "ch1_hook": (
        "Mastering algorithms shouldn't mean juggling five browser tabs, squinting at spoilers on forums, "
        "or waiting on remote web servers just to test your code. "
        "Welcome to cOde(n) — the ultimate offline-first engineering and algorithm mastery studio, "
        "built from the ground up for developers who take their craft seriously. "
        "With over four thousand canonical LeetCode packages and more than one thousand Project Euler challenges stored locally on your machine, "
        "cOde(n) transforms technical preparation into a seamless, distraction-free IDE experience."
    ),
    "ch2_reference": (
        "Let's take a look at problem number one: Two Sum. "
        "In the Reference tab, every detail is engineered for clarity. "
        "The hero banner immediately gives you the problem taxonomy, Elo difficulty rating, and target asymptotic complexity bounds. "
        "Every section — from the type-hinted function contract to comprehensive constraints and examples — is presented with textbook-level precision. "
        "And unlike standard web platforms, the verified canonical solution remains securely locked until you've solved the problem yourself, "
        "completely eliminating accidental spoilers."
    ),
    "ch3_guided": (
        "When you're stuck on a tricky challenge, traditional platforms force you to choose between being completely lost or looking up the code and ruining the learning process. "
        "cOde(n) solves this with Guided Examples — interactive, code-free pedagogical walkthroughs. "
        "Here, you step through a representative input step by step. "
        "You trace the complement math, observe the hash map state mutations in real time, and build genuine intuition from first principles without seeing a single line of solution syntax."
    ),
    "ch4_editorial": (
        "When you're ready for deep mathematical rigor, the Editorial tab delivers comprehensive, textbook-grade breakdowns. "
        "Every problem includes multiple algorithmic approaches — from naive brute-force baselines to mathematically optimal one-pass solutions. "
        "Every complexity proof is rendered in crisp LaTeX KaTeX, paired with syntax-highlighted Monaco code blocks and full space-time trade-off matrices."
    ),
    "ch5_editor": (
        "Now let's write code. The built-in Monaco editor gives you full type intelligence, auto-completion, and starter harnesses. "
        "With one click on the Run button, your solution executes instantly against local hidden test cases with zero server lag. "
        "You get detailed runtime execution diagnostics and memory traces. "
        "And when you need pure immersion, tap Focus Mode to expand your editor into a distraction-free, full-screen canvas designed for deep flow state."
    ),
    "ch6_complexity": (
        "cOde(n) goes far beyond basic problem solving. "
        "The built-in Complexity Engine runs empirical benchmarks across scaling input sizes to scientifically verify your Big-O runtime claims. "
        "Need a hint? The AI Tutor offers Socratic guidance without giving away answers. "
        "And the interactive Career Path skill tree maps your journey across data structure hierarchies, unlocking new algorithmic domains as you progress toward interview mastery."
    ),
    "ch7_outro": (
        "Over four thousand LeetCode challenges. Over one thousand Project Euler packages. "
        "Full mathematical proofs, zero-spoiler pedagogical walkthroughs, and complete local privacy. "
        "cOde(n) is the definitive desktop studio for algorithmic excellence. "
        "Download cOde(n) today, clone the repository on GitHub, and take complete control of your engineering mastery. "
        "Check the links in the description below, subscribe for more algorithmic deep dives, and happy coding!"
    )
}

async def generate_all():
    print(f"Generating audio voiceovers with voice: {VOICE}...")
    for key, text in SCRIPTS.items():
        out_path = OUTPUT_DIR / f"{key}.mp3"
        print(f"Generating {out_path.name}...")
        communicate = edge_tts.Communicate(text, VOICE, rate="+3%", pitch="+0Hz")
        await communicate.save(str(out_path))
        print(f"Saved {out_path.name} ({out_path.stat().st_size} bytes)")

if __name__ == "__main__":
    asyncio.run(generate_all())
