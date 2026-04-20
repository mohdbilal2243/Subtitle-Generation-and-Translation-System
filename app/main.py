from app.utils.path_manager import create_project_structure
from app.services.audio_extractor import extract_audio
from app.services.vocal_separator import separate_vocals
import os

video_path = "data/Srk_video_Eng.mp4"

# Step 1: Extract video name
video_name = os.path.splitext(os.path.basename(video_path))[0]

# Step 2: Create structured folders
paths = create_project_structure(video_name=video_name)

# Step 3: Extract audio
audio_path = extract_audio(video_path, paths["audio"], "input_1")

print("Audio:", audio_path)

# Step 4: Separate vocals
vocals_path = separate_vocals(audio_path, paths["vocals"])

print("Vocals:", vocals_path)