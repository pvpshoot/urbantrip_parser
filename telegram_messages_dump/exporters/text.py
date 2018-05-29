#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import re
from .common import common

class text(object):
    """ text exporter plugin.
        By convention it has to be called exactly the same as its file name.
        (Apart from .py extention)
    """

    def __init__(self):
        """ constructor """
        self.ESCAPE = re.compile(r'[\x00-\x1f\b\f\n\r\t]')
        self.ESCAPE_DICT = {
            '\\': '\\\\',
            # '"': '\\"',
            '\b': '\\b',
            '\f': '\\f',
            '\n': '\\n',
            '\r': '\\r',
            '\t': '\\t',
        }
        for i in range(0x20):
            self.ESCAPE_DICT.setdefault(chr(i), '\\u{0:04x}'.format(i))

    def format(self, msg, exporter_context):
        """ Formatter method. Takes raw msg and converts it to a *one-line* string.
            :param msg: Raw message object :class:`telethon.tl.types.Message` and derivatives.
                        https://core.telegram.org/type/Message

            :returns: *one-line* string containing one message data.
        """
        # pylint: disable=unused-argument
        name, _, content, re_id, _, _, _ = common.extract_message_data(msg)
        # Format a message log record

        msg_date = '{}-{:02d}-{:02d}'.format(msg.date.year, msg.date.month, msg.date.day)

        msg_dump_str = '{} \n'.format(
            self._py_encode_basestring(content))

        folder_name = 'media'
        file_name = str(msg.id)
        img_ext = ".jpg"
        video_ext = ".mp4"
        file_path = f"{folder_name}/{file_name}"

        if msg.media:
          if exporter_context.is_photo(msg.media):
            return (f'![{msg_date}]({file_path}{img_ext} "{name}")')
          elif exporter_context.is_video(msg.media):
            return '[![{}](https://raw.github.com/GabLeRoux/WebMole/master/ressources/WebMole_Youtube_Video.png)](http://youtu.be/vt5fpE0bzSY)'

        return msg_dump_str

    def begin_final_file(self, resulting_file, exporter_context):
        """ Hook executes at the beginning of writing a resulting file.
            (After BOM is written in case of --addbom)
        """
        pass

    # This code is inspired by Python's json encoder's code
    def _py_encode_basestring(self, s):
        """Return a JSON representation of a Python string"""
        if not s:
            return s
        def replace(match):
            return self.ESCAPE_DICT[match.group(0)]
        return self.ESCAPE.sub(replace, s)
