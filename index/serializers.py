from rest_framework import serializers
from .models import PersonInfo, Vocation

nameList = PersonInfo.objects.values('name').all()
NAME_CHOICES = [item['name'] for item in nameList]


class PersonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonInfo
        fields = '__all__'


class VocationSerializer(serializers.ModelSerializer):
    info = PersonInfoSerializer()

    class Meta:
        model = Vocation
        # fields = '__all__'
        fields = ('id', 'job', 'title', 'payment', 'info')

    def create(self, validated_data):
        # validated_data中获取模型PersonInfo的数据
        info = validated_data.get('info', '')
        id = validated_data.get('id', 0)
        p = PersonInfo.objects.filter(id=id).first()
        # 根据id判断模型PersonInfo是否存在模型对象
        # 若存在，则只对Vocation新增数据
        # 若不存在，则先对PersonInfo新增数据
        if not p:
            p = PersonInfo.objects.create(**info)
        data = validated_data
        data['info'] = p
        v = Vocation.objects.create(**data)
        return v

    def updata(self, validated_data):
        info = validated_data.get('info', '')
        id = validated_data.get('id', 0)
        p = PersonInfo.objects.filter(id=info['id']).first()
        if p:
            p = PersonInfo.objects.filter(id=info['id']).update(**info)
            data = validated_data
            data['info'] = p
            v = Vocation.objects.filter(id=id).update(**data)
            return v
