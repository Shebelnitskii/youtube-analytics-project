from googleapiclient.discovery import build
import os

class Video():
    def __init__(self, video_id) -> None:
        self.video_id = video_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)
        self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',id=self.video_id).execute()

    def __str__(self):
        self.video_title: str = self.video_response['items'][0]['snippet']['title']
        self.video_url: str = f'https://www.youtube.com/watch?v={self.video_id}'
        self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        return self.video_title

    def video_info(self):
        return f'id видео: {self.video_id}\n{self.video_title}\n{self.video_url}\nПросмотры: {self.view_count}\nКол-во лайков: {self.like_count}'

class PLVideo(Video):
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id


    def playlist_info(self):
        # playlist_videos = self.youtube.playlistItems().list(playlistId=self.playlist_id,part='contentDetails',maxResults=50,).execute()
        # video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return f"id видео: {self.video_id}\n{self.video_title}\n{self.video_url}\nПросмотры: {self.view_count}\nКол-во лайков: {self.like_count}\nСсылка на плейлист: https://www.youtube.com/playlist?list={self.playlist_id}"
