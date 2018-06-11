#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import os
from os.path import join, dirname
from dotenv import load_dotenv
import boto3

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class S3Interface:
    """ S3 interface """

    def __init__(self):
      session = boto3.session.Session();
      self.client = session.client(
          service_name='s3',
          aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
          aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
          endpoint_url='http://hb.bizmrg.com',
      )

    def save_media(self, file, name, type):
        self.client.put_object(
            ACL='public-read',
            Bucket='urbantrip',
            Body=file,
            Key=name,
            ContentType=type
        )
