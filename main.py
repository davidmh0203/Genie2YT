# main.py
import os
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv

# 로컬 환경 변수 불러오기
load_dotenv()

from utils import get_genie_playlist
from utils import YouTubeClient

# Flask 초기화
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "dev_secret")

# ✅ OAuth 설정
oauth = OAuth(app)
google = oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    access_token_url="https://oauth2.googleapis.com/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
    api_base_url="https://www.googleapis.com/oauth2/v1/",
    client_kwargs={"scope": "openid email profile https://www.googleapis.com/auth/youtube"},
)

# 홈
@app.route("/")
def index():
    user = session.get("user")
    return render_template("index.html", user=user)

# ✅ 구글 로그인
@app.route("/login")
def login():
    redirect_uri = url_for("authorize", _external=True)
    return google.authorize_redirect(redirect_uri)

# ✅ 구글 인증 후 콜백
@app.route("/authorize")
def authorize():
    token = google.authorize_access_token()
    user_info = google.get("userinfo").json()
    session["user"] = user_info
    session["token"] = token
    return redirect(url_for("index"))

# ✅ 로그아웃
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

# ✅ Genie 플레이리스트 → YouTube 업로드
@app.route("/convert", methods=["POST"])
def convert_playlist():
    if "user" not in session:
        return jsonify({"error": "로그인이 필요합니다."}), 401

    genie_url = request.json.get("genie_url")
    playlist = get_genie_playlist(genie_url)

    # 세션 토큰 기반 YouTube API 연결
    yt_client = YouTubeClient(credentials=session.get("token"))

    uploaded = []
    for title in playlist:
        video_id = yt_client.search_video(title)
        uploaded.append({"title": title, "video_id": video_id})

    return jsonify({"uploaded": uploaded})


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=True)
