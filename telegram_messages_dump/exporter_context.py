#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
from pathlib import Path

class ExporterContext:
    """ Exporter context """

    def get_media_folder_name(self, datetime, name):
        return self.media_root / f'{datetime.date().isoformat()}' / name

    @staticmethod
    def is_photo(media):
        return hasattr(media, 'photo')

    @staticmethod
    def is_video(media):
        return media.document.mime_type == 'video/mp4'

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods
    def __init__(self):
        # Is processing the first record
        self.is_first_record = False
        # Is processing the last record
        self.is_last_record = True
        # Is working in continue/incremental mode
        self.is_continue_mode = False
        # Media root dir
        self.media_root = Path('./media')
