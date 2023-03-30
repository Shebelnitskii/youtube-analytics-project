from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os

class Video():
    def __init__(self, video_id) -> None:
        self.video_id = video_id
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.video_id).execute()
        if len(self.video_response['items']) == 0:
            print(f"Video with id '{self.video_id}' does not exist.")
            self.video_response = {'items': [{'snippet': {'title': None}, 'statistics': {'viewCount': None, 'likeCount': None}}]}
            self.title = self.video_response['items'][0]['snippet']['title']
            self.video_url: str = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
        else:
            self.title = self.video_response['items'][0]['snippet']['title']
            self.video_url: str = f'https://www.youtube.com/watch?v={self.video_id}'
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title

    def video_info(self):
        return f'id видео: {self.video_id}\n{str(self.title)}\n{self.video_url}\nПросмотры: {str(self.view_count)}\nКол-во лайков: {str(self.like_count)}'

class PLVideo(Video):
    def __init__(self, video_id, playlist_id) -> None:
        super().__init__(video_id)
        self.playlist_id = playlist_id


    def playlist_info(self):
        return f"id видео: {self.video_id}\n{self.title}\n{self.video_url}\nПросмотры: {self.view_count}\nКол-во лайков: {self.like_count}\nСсылка на плейлист: https://www.youtube.com/playlist?list={self.playlist_id}"
