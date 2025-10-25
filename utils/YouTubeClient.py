from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class YouTubeClient:
    def __init__(self, credentials: dict | None = None, dry_run: bool = False):
        self.dry_run = dry_run
        if credentials:
            creds = Credentials(**credentials)
            self.service = build("youtube", "v3", credentials=creds)
        else:
            self.service = None

    def search_video(self, query: str):
        if self.dry_run or not self.service:
            print(f"[DRY] Search: {query}")
            return "VIDEO_ID_FAKE"
        resp = self.service.search().list(
            q=query, part="id", maxResults=1, type="video"
        ).execute()
        items = resp.get("items", [])
        return items[0]["id"]["videoId"] if items else None
