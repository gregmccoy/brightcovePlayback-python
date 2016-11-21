from distutils.core import setup

setup(
    name="playbackapi",
    version="0.1",
    license="GPL",
    description="a python wrapper from the Brightcove Playback API",
    author="Greg McCoy",
    author_email="gmccoy4242@gmail.com",
    url="https://github.com/gregmccoy/playbackapi",
    requires=[
        'requests',
    ],
    packages = ['brightcovePlayback'],
)
