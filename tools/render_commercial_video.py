import os
import subprocess
from pathlib import Path

BASE_DIR = Path("C:/Users/david/.gemini/antigravity-ide/brain/e907292b-45e1-4fd9-9687-6bb35593451d")
PROD_DIR = BASE_DIR / "video_production"
FFMPEG = r"C:\Users\david\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"

CHAPTERS = [
    {
        "id": "ch1_hook",
        "audio": PROD_DIR / "ch1_hook.mp3",
        "image": BASE_DIR / "coden_youtube_thumbnail_1787990841700.jpg",
        "title": "cOde(n) // The Offline Algorithm Studio",
    },
    {
        "id": "ch2_reference",
        "audio": PROD_DIR / "ch2_reference.mp3",
        "image": BASE_DIR / "twosum_reference_tab_1787989671584.png",
        "title": "Reference Tab // Problem Specification & Type Contracts",
    },
    {
        "id": "ch3_guided",
        "audio": PROD_DIR / "ch3_guided.mp3",
        "image": BASE_DIR / "twosum_guided_example_tab_1787989688207.png",
        "title": "Guided Example // Zero-Spoiler Pedagogical Walkthrough",
    },
    {
        "id": "ch4_editorial",
        "audio": PROD_DIR / "ch4_editorial.mp3",
        "image": BASE_DIR / "twosum_editorial_tab_1787989699823.png",
        "title": "Editorial // Mathematical Rigor & LaTeX Proofs",
    },
    {
        "id": "ch5_editor",
        "audio": PROD_DIR / "ch5_editor.mp3",
        "image": BASE_DIR / "twosum_restored_passed_1787990050099.png",
        "title": "In-App Coden Editor // Local Real-Test Execution",
    },
    {
        "id": "ch6_complexity",
        "audio": PROD_DIR / "ch6_complexity.mp3",
        "image": BASE_DIR / "twosum_run_result_1787989812309.png",
        "title": "Complexity Benchmarking & AI Socratic Guidance",
    },
    {
        "id": "ch7_outro",
        "audio": PROD_DIR / "ch7_outro.mp3",
        "image": BASE_DIR / "coden_youtube_thumbnail_1787990841700.jpg",
        "title": "cOde(n) // Master Algorithms Today",
    },
]

def get_audio_duration(audio_file: Path) -> float:
    cmd = [
        FFMPEG,
        "-i", str(audio_file),
        "-f", "null", "-"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    # Parse Duration: 00:00:25.43
    for line in res.stderr.splitlines():
        if "Duration:" in line:
            parts = line.split("Duration:")[1].split(",")[0].strip().split(":")
            h, m, s = float(parts[0]), float(parts[1]), float(parts[2])
            return h * 3600 + m * 60 + s
    return 30.0

def build_segment(chapter, index):
    audio_file = chapter["audio"]
    img_file = chapter["image"]
    dur = get_audio_duration(audio_file) + 0.8  # Add slight padding
    out_segment = PROD_DIR / f"segment_{index}_{chapter['id']}.mp4"
    
    print(f"Rendering segment {index}: {chapter['id']} (duration: {dur:.2f}s)...")
    
    # Create smooth 1080p 60fps video with subtle slow zoom
    # scale to 1920x1080
    cmd = [
        FFMPEG, "-y",
        "-loop", "1",
        "-i", str(img_file),
        "-i", str(audio_file),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-vf", f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:color=black",
        "-t", f"{dur:.2f}",
        "-r", "60",
        str(out_segment)
    ]
    subprocess.run(cmd, check=True)
    return out_segment

def main():
    segments = []
    for idx, ch in enumerate(CHAPTERS):
        seg = build_segment(ch, idx + 1)
        segments.append(seg)
    
    concat_list = PROD_DIR / "concat_list.txt"
    with open(concat_list, "w") as f:
        for seg in segments:
            # Escape path for ffmpeg concat
            f.write(f"file '{seg.as_posix()}'\n")
    
    final_output = BASE_DIR / "cOden_5min_Commercial_Showcase_1080p.mp4"
    print(f"Stitching all segments into final video: {final_output.name}...")
    concat_cmd = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(final_output)
    ]
    subprocess.run(concat_cmd, check=True)
    print(f"\n==========================================")
    print(f"SUCCESS! Master Video Rendered:")
    print(f"Path: {final_output}")
    print(f"Size: {final_output.stat().st_size / (1024*1024):.2f} MB")
    print(f"==========================================")

if __name__ == "__main__":
    main()
