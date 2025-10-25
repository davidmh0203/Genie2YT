import requests
from bs4 import BeautifulSoup

def crawl_genie_playlist(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")

    songs = []
    for tr in soup.select("tr.list"):
        title_tag = tr.select_one("a.btn-info")
        artist_tag = tr.select_one("a.artist")
        img_tag = tr.select_one("td img")

        song = {
            "id": tr.get("songid"),
            "title": title_tag.text.strip() if title_tag else None,
            "artist": artist_tag.text.strip() if artist_tag else None,
            "album_img": "https:" + img_tag["src"] if img_tag else None
        }
        songs.append(song)

    return songs


# 테스트용
if __name__ == "__main__":
    url = "https://www.genie.co.kr/detail/albumInfo?axnm=86408704"
    for song in crawl_genie_playlist(url):
        print(f"{song['title']} - {song['artist']}")
