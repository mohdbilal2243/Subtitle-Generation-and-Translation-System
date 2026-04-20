import os
import subprocess

def extract_audio(video_path, output_dir, filename):
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{filename}.wav")

    if not os.path.exists(output_path):
        print(f"Extracting audio...{output_path}")
        command = [
            "ffmpeg",
            "-i", video_path,
            "-vn",                # no video
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            output_path
        ]

        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        print(f"[SKIP] Audio already exists: {output_path}")

    return output_path