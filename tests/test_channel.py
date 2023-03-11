import pytest
from src.channel import Channel

@pytest.fixture()
def channel():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

def test_channel_init(channel):
    assert channel.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'

def test_channel_print(channel):
    assert channel.print_info() == None