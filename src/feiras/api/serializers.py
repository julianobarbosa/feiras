from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
)

from core.models import Feira


class FeiraCreateSerializer(ModelSerializer):
    class Meta:
        model = Feira
        fields = [
            #'id',
            'long',
            'lat',
            'setcens',
            'areap',
            'coddist',
            'codsubpref',
            'regiao5',
            'regiao8',
            'nome_feira',
            'registro',
            'logradouro',
            'numero',
            'bairro',
            'referencia',
        ]


class FeiraDetailSerializer(ModelSerializer):
    class Meta:
        model = Feira
        fields = [
            'id',
            'long',
            'lat',
            'setcens',
            'areap',
            'coddist',
            'codsubpref',
            'regiao5',
            'regiao8',
            'nome_feira',
            'registro',
            'logradouro',
            'numero',
            'bairro',
            'referencia',
        ]


class FeiraListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='feiras-api:detail',
        lookup_field='id',
    )
    delete_url = HyperlinkedIdentityField(
        view_name='feiras-api:delete',
        lookup_field='id',
    )

    class Meta:
        model = Feira
        fields = [
            'id',
            'url',
            'long',
            'lat',
            'setcens',
            'areap',
            'coddist',
            'codsubpref',
            'regiao5',
            'regiao8',
            'nome_feira',
            'registro',
            'logradouro',
            'numero',
            'bairro',
            'referencia',
            'delete_url',
        ]
