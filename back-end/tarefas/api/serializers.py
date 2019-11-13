from rest_framework import serializers
from tarefas.models import Tarefas 

class TarefasSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tarefas
        fields = '__all__'