# utils/genie_scraper.py
from __future__ import annotations
import os, re, unicodedata, html as ihtml
import requests
from dataclasses import dataclass
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0"}

def _clean_spaces(s: str) -> str:
    if not s: return ""
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

def _prefer_text_then_attr(el, attr_name="title") -> str:
    if not el: return ""
    txt = " ".join(el.stripped_strings)
    txt = _clean_spaces(ihtml.unescape(txt))
    if not txt:
        raw = el.get(attr_name, "") or ""
        txt = _clean_spaces(ihtml.unescape(raw))
    return txt

@dataclass
class ScrapeStats:
    rows_found: int = 0
    table_hits: int = 0
    card_hits: int = 0
    success: int = 0
    skipped_no_title: int = 0
    skipped_no_artist: int = 0

def _save_debug_html(html: str, out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)

def _parse_soup(soup: BeautifulSoup, stats: ScrapeStats, debug: bool=False) -> list[str]:
    songs: list[str] = []

    # 1) 표 기반(현재 제공해주신 HTML 구조)
    rows = soup.select("tbody tr.list[songid]")
    stats.rows_found = len(rows)
    for tr in rows:
        td = tr.select_one("td.info")
        if not td:
            continue
        title_txt  = _prefer_text_then_attr(td.select_one("a.title"))
        artist_txt = _prefer_text_then_attr(td.select_one("a.artist"))
        if title_txt and artist_txt:
            songs.append(f"{title_txt} - {artist_txt}")
            stats.table_hits += 1
            stats.success += 1
        else:
            if not title_txt:  stats.skipped_no_title  += 1
            if not artist_txt: stats.skipped_no_artist += 1
            if debug:
                print("[SKIP] title:", title_txt, "| artist:", artist_txt)

    # 2) 카드 기반(백업 셀렉터)
    if not songs:
        items = soup.select("li.song-item, ul#songlist li, div.songlist li, li[data-song-id]")
        for li in items:
            t_el = li.select_one("a.title, .title.ellipsis, .song-title")
            a_el = li.select_one("a.artist, .artist.ellipsis, .song-artist, .meta .artist a")
            title_txt  = _prefer_text_then_attr(t_el)
            artist_txt = _prefer_text_then_attr(a_el)
            if title_txt and artist_txt:
                songs.append(f"{title_txt} - {artist_txt}")
                stats.card_hits += 1
                stats.success  += 1
            elif debug:
                print("[SKIP(card)] title:", title_txt, "| artist:", artist_txt)

    # 중복 제거(안정성)
    deduped = []
    seen = set()
    for s in songs:
        if s not in seen:
            seen.add(s)
            deduped.append(s)
    return deduped

def scrape_genie_playlist(url: str, debug: bool=False, debug_out: str="static/debug/genie_raw.html") -> tuple[list[str], ScrapeStats]:
    """지니 플레이리스트 URL을 받아 곡명-아티스트 리스트와 통계를 반환"""
    stats = ScrapeStats()
    url = url.replace("m.genie.co.kr", "www.genie.co.kr")
    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()
    html = r.text
    if debug:
        _save_debug_html(html, debug_out)
        print(f"[DEBUG] raw html saved -> {debug_out}")

    soup = BeautifulSoup(html, "html.parser")
    songs = _parse_soup(soup, stats, debug=debug)
    return songs, stats

def scrape_genie_html(html: str, debug: bool=False) -> tuple[list[str], ScrapeStats]:
    """원시 HTML 문자열을 바로 파싱 (테스트/디버그용)"""
    stats = ScrapeStats()
    soup = BeautifulSoup(html, "html.parser")
    songs = _parse_soup(soup, stats, debug=debug)
    return songs, stats
