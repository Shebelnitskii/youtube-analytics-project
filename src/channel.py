from googleapiclient.discovery import build
import os
import json

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return print(channel)

    @property
    def title(self):
        """Возвращает название канала."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        """Возвращает количество видео в канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel['items'][0]['statistics']['videoCount']

    @property
    def url(self):
        """Возвращает url канала."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return f'https://www.youtube.com/channel/{channel["items"][0]["id"]}'

    def get_service():
        """Возвращает сервис для работы с каналами."""
        youtube = build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))
        return youtube

    def to_json(self,file):
        """ Сохраняет данные канала в файл json """
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        with open(file, 'w') as f:
            json.dump(channel, f)
