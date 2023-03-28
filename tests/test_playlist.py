import os
import pytest
import datetime
from src.playlist import PlayList

@pytest.fixture
def playlist():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')  # заменить на реальный ID плейлиста

def test_title(playlist):
    assert playlist.title == 'Редакция. АнтиТревел'

def test_url(playlist):
    assert playlist.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'

def test_video(playlist):
    assert len(playlist.video) == 5

def test_total_duration(playlist):
    assert isinstance(playlist.total_duration, datetime.timedelta)

def test_show_best_video(playlist):
    assert playlist.show_best_video() == 'https://youtu.be/9Bv2zltQKQA'


