import csv
import logging
import os
from os.path import join

from django.utils.six.moves import input
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from core.models import (
    Feira,
    Distrito,
    SubPrefeitura,
)

logger = logging.getLogger("project")


class Command(BaseCommand):
    args = 'Arguments is not needed'
    help = 'Import csv file for Feiras Layout'

    def get_csv_file_header(self, csvHeader):
        header_ = csvHeader
        # cols = [x.replace(' ', '_').lower() for x in str(header_).split(",")]
        cols = [x.replace(' ', '_').lower() for x in header_]
        return cols

    def boolean_input(self, question, default=None):
        result = input("%s " % question)
        if not result and default is not None:
            return default
        while len(result) < 1 or result[0].lower() not in "yn":
            result = input("Please answer yes or no: ")
        return result[0].lower() == "y"

    def csv_upload_post_save(self, *args, **kwargs):
        csv_file = join(settings.BASE_DIR, 'csv', 'DEINFO_AB_FEIRASLIVRES_2014.csv')
        CODDIST = 5
        CODSUBPREF = 7
        logger.debug('csv_upload_post_save: start import_csv: Check if csv file exists')
        if not os.path.exists(csv_file):
            raise CommandError('Feiras file "%s" does not exist' % csv_file)

        with open(csv_file, newline='', encoding='iso-8859-1') as f:
            reader = csv.reader(f)
            header_ = next(reader)
            header_cols = self.get_csv_file_header(header_)
            for line in reader:
                logger.debug('csv_upload_post_save: line: ', line)
                feira_obj = Feira()
                i = 0
                # TODO: verificar o split de linha esta errado
                # row_item = str(line).split(',')
                for item in line:
                    key = header_cols[i]
                    if i == CODDIST:
                        distrito_obj = self.check_distrito(
                            pk=item,
                            descricao=line[6],
                        )
                        item = distrito_obj

                    if i == CODSUBPREF:
                        subprefeitura_obj = self.check_subprefeitura(
                            pk=item,
                            descricao=line[8],
                        )
                        item = subprefeitura_obj

                    setattr(feira_obj, key, item)
                    i += 1
                logger.debug('csv_upload_post_save:line: ', line)
                feira_obj.save()

    def check_distrito(self, pk, descricao):
        logger.debug('check_distrito: ', pk, descricao)
        pk = int(pk)
        descricao = descricao.replace("'", "").lstrip()
        obj, created = Distrito.objects.get_or_create(
            cod_distrito=pk,
            defaults={'des_distrito': descricao},
        )
        return obj

    def check_subprefeitura(self, pk, descricao):
        logger.debug('check_subprefeitura: ', pk, descricao)
        pk = int(pk)
        descricao = descricao.replace("'", "").lstrip()
        obj, created = SubPrefeitura.objects.get_or_create(
            cod_subprefeitura=pk,
            defaults={'des_subprefeitura': descricao},
        )
        return obj

    '''
    Import file from csv directory
    file name: DEINFO_AB_FEIRASLIVRES_2014.csv
    the layout must be respect.
    '''
    def handle(self, *args, **options):
        question_result = self.boolean_input('Execute this command (yes/[no])')
        if not question_result:
            return

        logger.debug('handle: start import_csv')
        self.csv_upload_post_save(self, *args, **options)

        # for line in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        return
