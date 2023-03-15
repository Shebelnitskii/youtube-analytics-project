import pytest
from src.channel import Channel
from googleapiclient.discovery import build
import os

@pytest.fixture()
def channel():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

def test_channel_init(channel):
    assert channel.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'

def test_channel_print(channel):
    assert channel.print_info() == None

def test_title(channel):
    assert channel.title == 'вДудь'

def test_video_count(channel):
    assert channel.video_count == '165'

def test_url(channel):
    assert channel.url == 'https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA'

def test_to_json(channel):
    assert channel.to_json('test') == None