from .models import Person, Stats
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonCreateSerializer, PersonRetrieveSerializer, StatsSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonRetrieveSerializer
    
    def get_serializer_class(self):
        if self.action == 'create':
           return PersonCreateSerializer
        return super().get_serializer_class()

    def create(self, request):
        response = None
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.validate_dna(request.data.get('dna', []))
            instance = serializer.create(serializer.validated_data)
            if instance.is_mutant:
                response = Response(serializer.data, status=status.HTTP_200_OK)
            else:
                response = Response(instance.data, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            message = {'message': str(e)}
            response = Response(message, status=status.HTTP_400_BAD_REQUEST)
        return response
    
class StatsViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = StatsSerializer

    def list(self, request):
        estadisticas = Stats.get_instance()
        data = {
            'count_mutant_dna': estadisticas.count_mutant_dna,
            'count_human_dna': estadisticas.count_human_dna,
            'ratio': estadisticas.ratio,
        }
        return Response(data)