# -*- coding: utf-8 -*-
# import urllib2
# from bs4 import BeautifulSoup
# from django.http import HttpResponse
from django.shortcuts import render
# from django.conf import settings
from django.views.generic import TemplateView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

class IndexView(TemplateView):
    template_name = 'index.html'

# @api_view(['GET'])
# def search(request):
#     query = request.query_params['query'].encode('utf-8')
#     url = "http://music.naver.com/search/search.nhn?target=track&query=" + query
#     html = urllib2.urlopen(url).read()
#     soup = BeautifulSoup( html )
#     list = soup.find_all('tr', '_tracklist_move')

#     ret = []
#     for data in list:
#         try:
#             name = data.find('td', 'name').find('span', 'ellipsis').getText().strip()
#             artist = data.find('td', 'artist').find('a').getText().strip()
#             ret.append({'name' : name, 'artist' : artist})
#         except:
#             pass
#     return Response(ret)

