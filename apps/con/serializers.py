from django.forms import widgets
from rest_framework import serializers
from models import Item,Dinar


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item


"""
class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
"""
class DinarSerializer(serializers.Serializer):
    pk=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    inicial= serializers.DateTimeField()
    fim= serializers.DateTimeField()
    #itens = ItemSerializer(many=True)
