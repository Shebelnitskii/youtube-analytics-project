import pytest
from src.video import Video, PLVideo

@pytest.fixture()
def video():
    return Video('9lO06Zxhu88')

def test_video_id(video):
    assert video.video_id == '9lO06Zxhu88'

def test_video_title(video):
    assert str(video) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'

@pytest.fixture()
def plvideo():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

def test_plvideo_id(plvideo):
    assert plvideo.video_id == 'BBotskuyw_M'

def test_playlist_id(plvideo):
    assert plvideo.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'