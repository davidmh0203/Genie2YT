# utils/youtube_api.py
from __future__ import annotations

class YouTubeClient:
    def __init__(self, dry_run: bool=True):
        """
        dry_run=True: 실제 API 호출 없이 콘솔 출력만
        """
        self.dry_run = dry_run
        # 실제 구현 시: build('youtube', 'v3', credentials=...)
        self.service = None

    def search_video(self, query: str) -> str | None:
        if self.dry_run:
            print(f"[DRY-RUN] search: {query}")
            return "VIDEO_ID_FAKE"
        # TODO: 실제 구현
        # resp = self.service.search().list( ... ).execute()
        # return resp['items'][0]['id']['videoId'] if items else None
        return None

    def add_to_playlist(self, video_id: str, playlist_id: str) -> bool:
        if self.dry_run:
            print(f"[DRY-RUN] add to playlist: video={video_id} -> playlist={playlist_id}")
            return True
        # TODO: 실제 구현
        # self.service.playlistItems().insert( ... ).execute()
        return True
