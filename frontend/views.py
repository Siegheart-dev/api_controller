import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import json
from django.shortcuts import render, redirect


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return super().default(obj)


def carfax(request):
    
    vin_code = request.GET.get('vin-code', "")
    make=""
    #articles1 = []
    if vin_code:
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinExtended/{vin_code}?format=json'
        response = requests.get(url)
        data = response.json()
        

        if 'Results' in data:
            results = data['Results']
            for item in results:
                if item.get('Variable') == 'Manufacturer Name':
                    make = item.get('Value')
                    #articles.append({make})

    if make:
        #Redirect to the results page with the 'make' data
        return redirect(f'/carfax/results/?make={make}')
    else:
        return render(request, 'frontend/carfax.html', {'error': 'Make not found for the given VIN code'})    

def carfax_results(request):
    make = request.GET.get('make', '')
    context = {'make': make}
    return render(request, 'frontend/carfax_results.html', context)


