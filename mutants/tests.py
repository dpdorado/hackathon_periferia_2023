from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from mutants.api import StatsViewSet, PersonViewSet
import csv
import ast


class StatsViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_stats_list(self):
        request = self.factory.get('/api/stats/')
        view = StatsViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        self.assertAlmostEqual(response.status_code, status.HTTP_200_OK)

class MutantViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_mutant_create(self):
        with open('datos_test.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dna = ast.literal_eval(row[0])
                status_code = int(row[2])
                data = {
                    'dna': dna
                }
                try:
                    request = self.factory.post('/api/mutant/', data, format='json')
                    view = PersonViewSet.as_view(actions={'post': 'create'})
                    response = view(request)
                    code = status.HTTP_200_OK
                    if (status_code == status.HTTP_403_FORBIDDEN):
                        code = status.HTTP_403_FORBIDDEN
                    else:
                        code = status.HTTP_400_BAD_REQUEST
                    self.assertAlmostEqual(response.status_code, code)
                except Exception as e:
                    print(str(e))
    print('Finished test_mutant_create')

