from django.shortcuts import render
from django.views import View
from browser.scrape import browser
import requests
# Create your views here.
class MainPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'browser/main_page.html')

class Search(View):
    def get(self, request, *args, **kwargs):
        if request:
            r = request.GET.get('q')
        try:
            br = browser(r)
            context = {'result': br}
        except Exception:
            a = 'Incorrect URL'
            context = {'error': a}
        return render(request, 'browser/search.html', context=context)

