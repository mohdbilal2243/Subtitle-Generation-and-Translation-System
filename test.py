import whisper
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

model = whisper.load_model("base", device=device)

result = model.transcribe("data/Aud_6_english.WAV")
print(result["text"])

