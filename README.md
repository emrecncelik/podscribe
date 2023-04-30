# Usage
Only supports podcasts hosted by buzzsprout for now.
## Installation
```bash
git clone git+url
pip install -r podscribe/requirements.txt
```
## Download episodes
### Help
```bash
(base) emrecan@runny:~/workspace/podscribe$ python download.py -h
```
```
usage: download.py [-h] --url str [--outdir str] [--max_episodes int] [--only_metadata bool]

options:
  -h, --help            show this help message and exit

DownloadOptions ['opt']:
  Set options for the download.

  --url str             Apple podcasts url (default: None)
  --outdir str          Output directory (default: ./episodes)
  --max_episodes int    Maximum num. of episodes to download (default: None)
  --only_metadata bool, --noonly_metadata bool
                        Download metadata only if True (default: False)
```

### Example
```bash
python download.py \
    --url "https://podcasts.apple.com/us/podcast/o-tarz-m%C4%B1/id1332079636" \
    --max_episodes 10
```

## Transcribe
### Help
```bash
(base) emrecan@runny:~/workspace/otm$ python transcribe.py -h
```
```
usage: transcribe.py [-h] [--indir str] [--outdir str] [--model str] [--language str] [--extension str]

options:
  -h, --help       show this help message and exit

TranscriptionOptions ['opt']:
  TranscriptionOptions(indir: str = './episodes', outdir: str = './transcriptions', model: str = 'tiny', language: str = 'en', extension: str = 'mp3')

  --indir str      Input directory, defaults to ./episodes (default: ./episodes)
  --outdir str     Output directory, defaults to ./transcriptions (default: ./transcriptions)
  --model str      Name of the whisper model on HuggingFace Hub (default: tiny)
  --language str   Language of audio files (default: en)
  --extension str  Extension of audio files (default: mp3)
```
### Example
```bash
python transcribe.py \
    --model "tiny"
    --language "tr"
```