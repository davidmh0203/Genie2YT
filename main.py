# main.py
from __future__ import annotations
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from utils.genie_scraper import scrape_genie_playlist
from utils.youtube_api import YouTubeClient

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET", "dev-secret")
DEBUG_DEFAULT = True  # 기본 디버그 on (원하면 False로)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/preview", methods=["POST"])
def preview():
    url = request.form.get("genie_url", "").strip()
    debug = request.args.get("debug", "1" if DEBUG_DEFAULT else "0") == "1"
    if not url:
        flash("지니 플레이리스트 URL을 입력해주세요.")
        return redirect(url_for("index"))

    try:
        songs, stats = scrape_genie_playlist(
            url,
            debug=debug,
            debug_out="static/debug/genie_raw.html"
        )
    except Exception as e:
        flash(f"스크랩 실패: {e}")
        songs, stats = [], None

    return render_template(
        "preview.html",
        url=url,
        songs=songs,
        stats=stats,
        debug=debug,
        raw_html_path="/static/debug/genie_raw.html" if debug else None
    )

@app.route("/to-youtube", methods=["POST"])
def to_youtube():
    # 선택된 곡들을 받아 유튜브에 넣는 엔드포인트 (옵션)
    playlist_id = request.form.get("playlist_id", "").strip() or "PLAYLIST_ID_FAKE"
    selected = request.form.getlist("songs[]")  # preview.html에서 name="songs[]" 로 전달
    debug = request.args.get("debug", "1" if DEBUG_DEFAULT else "0") == "1"

    yt = YouTubeClient(dry_run=debug)
    added = 0
    for q in selected:
        vid = yt.search_video(q)
        if vid and yt.add_to_playlist(vid, playlist_id):
            added += 1

    return render_template("success.html", added=added, total=len(selected), debug=debug)

if __name__ == "__main__":
    # 개발 편의를 위해 auto-reload
    app.run(host="0.0.0.0", port=5001, debug=True)
