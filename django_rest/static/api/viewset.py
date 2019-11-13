from rest_framework import viewsets
from tarefas.models import Tarefas 
from tarefas.api.serializers import TarefasSerializer


# Create your views here.
class TarefasViewSet(viewsets.ModelViewSet):

    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer