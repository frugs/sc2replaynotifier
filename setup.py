from distutils.core import setup

VERSION = '0.0.2'

setup(
  name='sc2replaynotifier',
  packages=['sc2replaynotifier'],
  version=VERSION,
  description='Utility for watching for and handling new SC2 replays as they are generated by the game',
  author='Hugo Wainwright',
  author_email='wainwrighthugo@gmail.com',
  url='https://github.com/frugs/sc2replaynotifier',
  download_url='https://github.com/frugs/sc2replaynotifier/tarball/' + VERSION,
  keywords=['sc2', 'replay'],
  classifiers=[],
)
