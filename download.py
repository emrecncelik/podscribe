import os
import re
import warnings
import requests
import pandas as pd
from tqdm import tqdm
from dataclasses import dataclass
from simple_parsing import ArgumentParser

warnings.filterwarnings("ignore")


@dataclass
class DownloadOptions:
    """Set options for the download."""

    url: str  # Apple podcasts url
    outdir: str = "./episodes"  # Output directory
    max_episodes: int = None  # Maximum num. of episodes to download
    only_metadata: bool = False  # Only download metadata (name, descr, url)


parser = ArgumentParser()
parser.add_arguments(DownloadOptions, dest="opt")
args = parser.parse_args()


def find_feed(url: str):
    request = requests.get(url)
    feed = re.findall(
        r"https://www.buzzsprout\.com/[0-9]+",
        str(request.content),
    )[0]

    return feed + ".rss"


def download_episode(url: str, dir: str):
    response = requests.get(url)
    filename = name_from_url(url)
    with open(os.path.join(dir, filename), "wb") as f:
        f.write(response.content)


def name_from_url(url: str):
    return "".join(url.split("/")[-1].split("-")[1:])


feed = find_feed(args.opt.url)
page = requests.get(feed).content
soup = BeautifulSoup(page, parser="lxml")

items = (
    soup.find_all("item")
    if args.opt.max_episodes is None
    else soup.find_all("item")[: args.opt.max_episodes]
)

titles = [i.find("title").text for i in items]
descriptions = [i.find("description").text for i in items]
urls = [i.find("enclosure")["url"] for i in items]

if not os.path.exists(args.opt.outdir):
    os.mkdir(args.opt.outdir)

metadata = pd.DataFrame(
    {
        "title": titles,
        "description": descriptions,
        "url": urls,
    }
)

metadata.to_csv(os.path.join(args.opt.outdir, "metadata.csv"), index=False)

if not args.opt.only_metadata:
    for url in tqdm(urls):
        download_episode(url, args.opt.outdir)
