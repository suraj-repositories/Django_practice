from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Person
from .serializer import PersonSerializer


@api_view(['GET'])
def getData(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def saveData(request):
    serializer = PersonSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)