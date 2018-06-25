from django.shortcuts import render
from  django.http  import  HttpResponse


def  index ( request ): 
    retorna  HttpResponse ( "Olá, mundo. Você está no índice de enquetes." )
