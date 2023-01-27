from rest_framework import serializers
from .models import FileUploadModels
from django.db.models import Sum

class FileUploadSerializer(serializers.ModelSerializer):
    total_loja = serializers.SerializerMethodField()
    total_transacoes = serializers.SerializerMethodField()

    class Meta:
        model = FileUploadModels
        fields = ('tipo', 'data', 'valor', 'cpf', 'cartao', 'hora', 'dono_da_loja', 'nome_loja', 'total_loja', 'total_transacoes')

    def get_total_loja(self, obj):
        return FileUploadModels.objects.filter(nome_loja=obj.nome_loja).aggregate(Sum('valor'))['valor__sum']

    def get_total_transacoes(self, obj):
        return FileUploadModels.objects.filter(nome_loja=obj.nome_loja).count()