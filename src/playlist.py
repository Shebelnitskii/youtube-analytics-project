import datetime
from googleapiclient.discovery import build
import os
import isodate

class PlayList:
    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        api_key = os.getenv('YT_API_KEY')
        self.__youtube = build('youtube', 'v3', developerKey=api_key)
        self.__request = self.__youtube.playlists().list(part="snippet", id=self.__playlist_id).execute()
        self.__title = self.__request["items"][0]["snippet"]["title"]
        self.__url = f'https://www.youtube.com/playlist?list={self.__playlist_id}'
        self.__video = self.get_video_statistics()

    @property
    def title(self):
        return self.__title
    @property
    def url(self):
        return self.__url

    @property
    def video(self):
        return self.__video

    def get_video_pl(self):
        playlist_videos = self.__youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    def get_video_statistics(self):
        videos = []
        for video in self.get_video_pl():
            video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video
                                                   ).execute()
            video_title: str = video_response['items'][0]['snippet']['title']
            view_count: int = video_response['items'][0]['statistics']['viewCount']
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            comment_count: int = video_response['items'][0]['statistics']['commentCount']
            iso_8601_duration = video_response['items'][0]['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            video_info = [video_title,f'https://youtu.be/{video}',duration,like_count]
            videos.append(video_info)
        return videos
    @property
    def total_duration(self):
        total = datetime.timedelta()
        for video in self.__video:
            total += video[2]
        return total

    def show_best_video(self):
        best_video = None
        best_likes = 0
        for video in self.video:
            if int(video[3]) > best_likes:
                best_video = str(video[1])
                best_likes = int(video[3])
        return best_video