import pytest
from src.video import Video, PLVideo

@pytest.fixture()
def video():
    return Video('9lO06Zxhu88')

def test_video_id(video):
    assert video.video_id == '9lO06Zxhu88'

def test_video_title(video):
    assert str(video) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'

def test_video_info(video):
    # Тестирование для существующего видео на момент кол-ва просмотров 49454716 и кол-ва лайков 976842(может измениться)
    expected_output = f'id видео: 9lO06Zxhu88\nКак устроена IT-столица мира / Russian Silicon Valley (English subs)\nhttps://www.youtube.com/watch?v=9lO06Zxhu88\nПросмотры: 49454716\nКол-во лайков: 976842'
    assert video.video_info() == expected_output

@pytest.fixture()
def broken_video():
    return Video('broken_video_id')

def test_broken_video(broken_video):
    assert broken_video.title is None
    assert broken_video.like_count is None

def test_broken_video_info(broken_video):
    expected_output = "id видео: broken_video_id\nNone\nhttps://www.youtube.com/watch?v=broken_video_id\nПросмотры: None\nКол-во лайков: None"
    assert broken_video.video_info() == expected_output

@pytest.fixture()
def plvideo():
    return PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')

def test_plvideo_id(plvideo):
    assert plvideo.video_id == 'BBotskuyw_M'

def test_playlist_id(plvideo):
    assert plvideo.playlist_id == 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD'
