# Usage
## Installation
```bash
git clone git+url
pip install -r podscribe/requirements.txt
```
## Download episodes
### Help
```bash
(base) emrecan@runny:~/workspace/podscribe$ python download.py -h
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