import csv
import os
import io

from django.core.exceptions import ValidationError


REQUIRED_HEADER = [
    'ID',
    'LONG',
    'LAT',
    'SETCENS',
    'AREAP',
    'CODDIST',
    'DISTRITO',
    'CODSUBPREF',
    'SUBPREFE',
    'REGIAO5',
    'REGIAO8',
    'NOME_FEIRA',
    'REGISTRO',
    'LOGRADOURO',
    'NUMERO',
    'BAIRRO',
    'REFERENCIA'
]


def csv_file_validator(value):
    filename, ext = os.path.splitext(value.name)
    if str(ext) != '.csv':
        raise ValidationError("Must be a csv file")
    decoded_file = value.read().decode('iso-8859-1')
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string, delimiter=',', quotechar='"')
    header_ = next(reader)[0].split(',')
    if header_[-1] == '':
        header_.pop()
    required_header = REQUIRED_HEADER
    if required_header != header_:
        raise ValidationError("Invalid File. Please use valid CSV Header and/or Staff Upload Template.")
    return True
