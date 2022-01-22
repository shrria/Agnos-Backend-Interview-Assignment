from asyncio.windows_events import NULL
import json
from urllib import response
from rest_framework import status
from rest_framework.test import APITestCase

from api.views import is_match

class GetAPISuccessTestCase(APITestCase):
    
    def test_get_api1(self):
        body = {
            'message': 'aa',
            'pattern': 'a'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['is_match'], False)
    
    def test_get_api2(self):
        body = {
            'message': 'aa',
            'pattern': '*'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['is_match'], True)
    
    def test_get_api3(self):
        body = {
            'message': 'cb',
            'pattern': '?a'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['is_match'], False)

class GetAPIBadRequestTestCase(APITestCase):
    
    def test_get_api4(self):
        body = {
            'empty': 'aa'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content)['is_match'], None)

    
    def test_get_api5(self):
        body = {
            'message': 'aa'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content)['is_match'], None)

    def test_get_api6(self):
        body = {
            'pattern': 'aa'
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content)['is_match'], None)

    def test_get_api7(self):
        body = {
            'message': ''
        }
        response = self.client.get("/api/is_match/", body)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(json.loads(response.content)['is_match'], None)
