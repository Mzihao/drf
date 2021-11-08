from rest_framework import serializers
from .models import PersonInfo, Vocation

nameList = PersonInfo.objects.values('name').all()
NAME_CHOICES = [item['name'] for item in nameList]


# class MySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     job = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=100)
#     payment = serializers.CharField(max_length=100)
#     name = serializers.PrimaryKeyRelatedField(queryset=nameList)
#
#     def create(self, validated_data):
#         return Vocation.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         return instance.updata(**validated_data)
class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = '__all__'


class VocationSerializer(serializers.ModelSerializer):
    name = PersonInfoSerializer()

    class Meta:
        model = Vocation
        # fields = '__all__'
        fields = ('id', 'job', 'title', 'payment', 'name')

    def create(self, validated_data):
        #
        name = validated_data.get('name', '')
        id = validated_data('id', 0)
        p = PersonInfo.objects.filter(id=id).first()
        if not p:
            p = PersonInfo.objects.create(**name)
        data = validated_data
        data['name'] = p
        v = Vocation.objects.create(**data)
        return v

    def updata(self, operation, validated_data):
        name = validated_data.get('name', '')
        id = validated_data('id', 0)
        p = PersonInfo.objects.filter(id=id).first()
        if p:
            PersonInfo.objects.filter(id=id).update(**name)
            data = validated_data
            data['name'] = p
            id = validated_data.get('id', '')
            v = Vocation.objects.filter(id=id).update(**data)
            return v
