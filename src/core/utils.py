import csv
import io
from os.path import join

import os
from django.conf import settings

from core.models import Feira

def upload_csv_file(instance, filename):
    qs = instance.__class__.objects.filter(user=instance.user)
    if qs.exists():
        num_ = qs.last().id + 1
    else:
        num_ = 1
    return f'csv/{num_}/{instance.user.username}/{filename}'


def convert_header(csvHeader):
    header_ = csvHeader[0]
    cols = [x.replace(' ', '_').lower() for x in header_.split(",")]
    return cols




# post_save.connect(csv_upload_post_save, sender=StaffCSVUpload)


