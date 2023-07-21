from django.shortcuts import render,redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Link

from django.views import View
from django.conf import settings
from .serializer import LinkSerializer
# Create your views here.

# DRF view for listing all the shortend links

class ShortenerListAPIView(ListAPIView):
    queryset=Link.objects.all()
    serializer_class=LinkSerializer

# DRF view for creating shortend links
    
class ShortenerCreateApiView(CreateAPIView):
    serializer_class=LinkSerializer
    
# DRF view for redirecting shortend links to original links

class Redirector(View):
    def get(self,request,shortener_link,*args, **kwargs):
        shortener_link=settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link=Link.objects.filter(shortend_link=shortener_link).first().original_link
        return redirect(redirect_link)