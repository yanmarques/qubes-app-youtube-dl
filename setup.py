#!/usr/bin/env python

from distutils.core import setup

import sys

setup(name='qubes-app-youtube-dl',
      version='0.2.1',
      license='BSD (3 clause)',
      description='A wrapper for youtube-dl-gui in a Qubes disposable vm',
      author='Yan Marques de Cerqueira',
      author_email='marques_yan@outlook.com',
      url='https://github.com/yanmarques/qubes-app-youtube-dl',
      download_url='https://github.com/yanmarques/qubes-app-youtube-dl/releases/download/v0.2.1/qubes-app-youtube-dl-0.2.1.tar.gz',
      scripts=['qvm-youtube-dl',],
      classifiers=[
          'Intended Audience :: End Users/Desktop',
          'Topic :: Multimedia :: Sound/Audio',
          'Topic :: Multimedia :: Video',
      ],
      data_files=[
          ('{}/share/applications/'.format(sys.prefix), 
            ['desktop-entries/download-yt-audio.desktop', 
             'desktop-entries/download-yt-video.desktop'],),
      ],
     )