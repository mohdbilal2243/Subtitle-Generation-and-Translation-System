import os
import subprocess
import shutil

def separate_vocals(audio_path, vocals_dir):
    os.makedirs(vocals_dir, exist_ok=True)

    file_name = os.path.splitext(os.path.basename(audio_path))[0]
    final_vocals_path = os.path.join(vocals_dir, f"{file_name}_vocals.wav")

    print("[INFO] Checking vocals output...")

    # ✅ ONLY RUN IF NOT EXISTS
    if not os.path.exists(final_vocals_path):

        print("[RUN] Running Demucs for vocal separation...")

        subprocess.run(
            [
                "demucs",
                "--two-stems=vocals",
                "-o", "results/_temp_demucs",
                audio_path
            ],
            check=True
        )

        # Find Demucs output dynamically
        demucs_vocals = None

        for root, dirs, files in os.walk("results/_temp_demucs"):
            if "vocals.wav" in files:
                demucs_vocals = os.path.join(root, "vocals.wav")
                break

        if demucs_vocals is None:
            raise FileNotFoundError("Demucs vocals not found")

        # Move to final destination
        shutil.move(demucs_vocals, final_vocals_path)

        # Cleanup temp folder
        shutil.rmtree("results/_temp_demucs", ignore_errors=True)

    else:
        print(f"[SKIP] Vocals already exist: {final_vocals_path}")

    return final_vocals_path