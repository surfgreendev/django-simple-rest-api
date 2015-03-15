from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View
import datetime
from django.http import JsonResponse

# Create your views here.
class TimeNowView(View):
    def get(self, request):
        #Get current timestamp
        now = datetime.datetime.now()
        today = now.strftime('%d-%m-%Y')
        time = now.strftime('%H:%M:%S')
        #Serialize it to a JSON object
        obj = {"time": time, "today": today}
        #Return the JSON object
        return JsonResponse(obj)
        
        