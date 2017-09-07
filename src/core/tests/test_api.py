from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status

User = get_user_model()
from core.models import Distrito, Feira, SubPrefeitura


class APITestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.distrito_obj = Distrito()
        self.distrito_obj.des_distrito='Goiânia'
        self.distrito_obj.save()

        self.subprefeitura_obj = SubPrefeitura()
        self.subprefeitura_obj.des_subprefeitura='Anapolis'
        self.subprefeitura_obj.save()

        self.feira_obj = Feira()
        self.feira_obj.long = '-46488746'
        self.feira_obj.lat = '-23507319'
        self.feira_obj.setcens = '355030864000076'
        self.feira_obj.areap = '3550308005141'
        self.feira_obj.coddist = self.distrito_obj
        self.feira_obj.codsubpref = self.subprefeitura_obj
        self.feira_obj.regiao5 = 'Leste'
        self.feira_obj.regiao8 = 'Leste 2'
        self.feira_obj.nome_feira = 'VILA PONTE RASA'
        self.feira_obj.registro = '7173-0'
        self.feira_obj.logradouro = 'RUA AGENOR DE BARROS'
        self.feira_obj.numero = 'S/N'
        self.feira_obj.bairro = 'VL PONTE RASA'
        self.feira_obj.referencia = 'AV SAO MIGUEL E SIMPLICIO'
        self.feira_obj.save()

    def test_api_can_get_a_feira(self):
        """Test the api can get a given feira."""
        feira_obj = Feira.objects.get(id=1)
        response = self.client.get(
            '/api/feiras/',
            kwargs={'id': feira_obj.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, feira_obj)
