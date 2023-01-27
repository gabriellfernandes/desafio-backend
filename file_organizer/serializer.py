from rest_framework import serializers
from .models import FileUploadModels
from django.db.models import Sum

class FileUploadSerializer(serializers.ModelSerializer):
    total_da_loja = serializers.SerializerMethodField()
    total_transacoes = serializers.SerializerMethodField()
    tipo_da_transacao = serializers.SerializerMethodField()
    valor_da_transacao = serializers.SerializerMethodField()
    class Meta:
        model = FileUploadModels
        fields = ('data','cpf', 'cartao', 'hora', 'dono_da_loja', 'nome_loja', 'total_da_loja', 'total_transacoes', 'tipo_da_transacao', "valor_da_transacao")
 
        
    def get_total_da_loja(self, obj):
        totalEntradas = FileUploadModels.objects.filter(nome_loja=obj.nome_loja, tipo__in=[1,4,5,6,7,8]).aggregate(Sum('valor'))['valor__sum'] or 0
        totalSaidas = FileUploadModels.objects.filter(nome_loja=obj.nome_loja, tipo__in=[2,3,9]).aggregate(Sum('valor'))['valor__sum'] or 0
        valorTotal = totalEntradas - totalSaidas
        
        return valorTotal
        
    def get_total_transacoes(self, obj):
        return FileUploadModels.objects.filter(nome_loja=obj.nome_loja).count()

    def get_valor_da_transacao(self, obj):
        valores = {
            "1": obj.valor, 
            "2": obj.valor *-1, 
            "3": obj.valor *-1,
            "4": obj.valor, 
            "5": obj.valor, 
            "6": obj.valor,  
            "7": obj.valor,
            "8": obj.valor,  
            "9": obj.valor *-1,
        }
        return valores.get(obj.tipo)

    def get_tipo_da_transacao(self, obj):
        tipos = {
            "1": "Debito", 
            "2": "Boleto", 
            "3": "Financiamento", 
            "4": "Crédito", 
            "5": "Recibimento Empréstimo", 
            "6": "Vendas", 
            "7": "Recebimento TED", 
            "8": "Recebimento Doc", 
            "9": "Aluguel"
        }
        return tipos.get(obj.tipo)