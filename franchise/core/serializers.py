from rest_framework import serializers

from .models import Collectable, Franchise


class FranchiseSerializer(serializers.ModelSerializer):
    '''
    Franchise
    '''

    class Meta:
        model = Franchise
        fields = '__all__'
        read_only_fields = ('id',)


class CollectableSerializer(serializers.ModelSerializer):
    '''
    Coleção Completa

    O read_only=True resolve o bug

    AssertionError: The `.update()` method does not support writable
    nested fields by default.
    Write an explicit `.update()` method for
    serializer `core.serializers.CollectableSerializer`,
    or set `read_only=True` on nested serializer fields.
    '''
    franchise = FranchiseSerializer(many=True, read_only=True)

    class Meta:
        model = Collectable
        fields = ('id', 'name', 'type', 'franchise')
