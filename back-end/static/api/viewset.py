from rest_framework import viewsets

from tarefas.api.serializers import TarefasSerializer
from tarefas.models import Tarefas


# Create your views here.
class TarefasViewSet(viewsets.ModelViewSet):

    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer
