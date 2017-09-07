from django.core.exceptions import ValidationError
from django.test import TestCase
from core.models import Distrito, Feira, SubPrefeitura


class DistritoModelTest(TestCase):
    def test_create(self):
        """
        start by creating a new Distrito object with Description Goiânia
        """
        distrito_obj = Distrito()
        distrito_obj.des_distrito='Goiânia'
        distrito_obj.save()

        distrito_all = Distrito.objects.all()
        self.assertEqual(len(distrito_all), 1)
        distrito_only = distrito_all[0]
        self.assertEqual(distrito_only, distrito_obj)


class SubPrefeituraModelTest(TestCase):
    def test_create(self):
        """
        start by creating a new SubPrefeitura object with Description Anapolis
        """
        subprefeitura_obj = SubPrefeitura()
        subprefeitura_obj.des_subprefeitura='Anapolis'
        subprefeitura_obj.save()

        subprefeitura_all = SubPrefeitura.objects.all()
        self.assertEqual(len(subprefeitura_all), 1)
        subprefeitura_only = subprefeitura_all[0]
        self.assertEqual(subprefeitura_only, subprefeitura_obj)


class FeiraModelTest(TestCase):
    def test_create(self):
        """
        start by creating a new Feira object with Description Aparecida de Goiânia
        """

        distrito_obj = Distrito()
        distrito_obj.des_distrito='Goiânia'
        distrito_obj.save()

        subprefeitura_obj = SubPrefeitura()
        subprefeitura_obj.des_subprefeitura='Anapolis'
        subprefeitura_obj.save()

        feira_obj = Feira()
        feira_obj.long = '-46488746'
        feira_obj.lat = '-23507319'
        feira_obj.setcens = '355030864000076'
        feira_obj.areap = '3550308005141'
        feira_obj.coddist = distrito_obj
        feira_obj.codsubpref = subprefeitura_obj
        feira_obj.regiao5 = 'Leste'
        feira_obj.regiao8 = 'Leste 2'
        feira_obj.nome_feira = 'VILA PONTE RASA'
        feira_obj.registro = '7173-0'
        feira_obj.logradouro = 'RUA AGENOR DE BARROS'
        feira_obj.numero = 'S/N'
        feira_obj.bairro = 'VL PONTE RASA'
        feira_obj.referencia = 'AV SAO MIGUEL E SIMPLICIO'
        feira_obj.save()

        feira_all = Feira.objects.all()
        self.assertEqual(len(feira_all), 1)
        feira_only = feira_all[0]
        self.assertEqual(feira_only, feira_obj)
