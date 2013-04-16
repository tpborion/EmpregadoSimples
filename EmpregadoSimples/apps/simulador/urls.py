# -*- coding: utf-8 -*-

'''
Created on 15/04/2013

@author: ThiagoP
'''

from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('EmpregadoSimples.apps.simulador.views',
                       url(r'^simular_contratacao/?$', 'simulate_contract'),
                       url(r'^contratacao_simulada/?$', 'simulated_contract'),
                       )