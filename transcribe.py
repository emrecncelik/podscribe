import os
import json
import whisper
import warnings
from tqdm import tqdm
from loguru import logger
from dataclasses import dataclass
from simple_parsing import ArgumentParser

warnings.filterwarnings("ignore")


@dataclass
class TranscriptionOptions:
    indir: str = "./episodes"  # Input directory, defaults to ./episodes
    outdir: str = "./transcriptions"  # Output directory, defaults to ./transcriptions
    model: str = "tiny"  # Name of the whisper model on HuggingFace Hub
    language: str = "en"  # Language of audio files
    extension: str = "mp3"  # Extension of audio files


parser = ArgumentParser()
parser.add_arguments(TranscriptionOptions, dest="opt")
args = parser.parse_args()

logger.info("Initializing speech to text model.")
episodes = [i for i in os.listdir(args.opt.indir) if "." + args.opt.extension in i]
model = whisper.load_model(args.opt.model)

if not os.path.exists(args.opt.outdir):
    os.mkdir(args.opt.outdir)

for episode in tqdm(episodes):
    out = os.path.join(args.opt.outdir, episode.replace(args.opt.extension, "json"))
    if os.path.exists(out):
        logger.info(f"Skipping {out}, already exists.")
        continue

    result = model.transcribe(
        os.path.join(args.opt.indir, episode),
        language=args.opt.language,
    )

    with open(out, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
