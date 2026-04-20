# app/utils/path_manager.py

import os

def create_project_structure(base_dir="results", video_name="Input_Video_1"):
    root = os.path.join(base_dir, video_name)

    paths = {
        "root": root,
        "audio": os.path.join(root, "extract_audio"),
        "vocals": os.path.join(root, "vocals"),
        "transcript": os.path.join(root, "transcripts"),
        "output_srt": os.path.join(root, "output_srt"),
    }

    for path in paths.values():
        os.makedirs(path, exist_ok=True)

    return paths