from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from covidstatus.api.serializers import NepalStatusSerializer, HealthFacilitySerializer, HealthFacilitiesListSerializer
import requests
import json
import feedparser

@api_view(['GET',])
def get_latest_status(request):
    if request.method == 'GET':
        r = requests.get('https://covid19.mohp.gov.np/covid/api/confirmedcases')
        data = NepalStatusSerializer().to_representation(r.json()['nepal'])
        return Response(data)
    return Response('Error')

@api_view(['GET',])
def get_testing_health_facilities(request):
    if request.method == 'GET':
        r = requests.get('https://covidapi.mohp.gov.np/api/v1/health-facility/?type=15')
        data = HealthFacilitiesListSerializer().to_representation(r.json())
        return Response(data)
    return Response('Error')

@api_view(['GET',])
def get_health_facilities(request):
    if request.method == 'GET':
        r = requests.get('https://covidapi.mohp.gov.np/api/v1/health-facility/?type=6')
        data = HealthFacilitiesListSerializer().to_representation(r.json())
        return Response(data)
    return Response('Error')

@api_view(['GET',])
def get_latest_news(request):
    if request.method == 'GET':
        r = requests.get('https://www.nepalisansar.com/coronavirus/feed/')
        feed = feedparser.parse(r.content)
        return Response(feed)
    return Response('Error')