import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

def carfax(request):
    
    vin_code = request.GET.get('vin-code', "")
    make = ""
    model_year = ""
    body_class = ""
    gross_weight = ""

    if vin_code:
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinExtended/{vin_code}?format=json'
        response = requests.get(url)
        data = response.json()

        if 'Results' in data:
            results = data['Results']
            for item in results:
                if item.get('Variable') == 'Manufacturer Name':
                    make = item.get('Value')
                elif item.get('Variable') == 'Model Year':
                    model_year = item.get('Value')
                elif item.get('Variable') == 'Body Class':
                    body_class = item.get('Value')
                elif item.get('Variable') == 'Gross Vehicle Weight Rating From':
                    gross_weight = item.get('Value')

    if make:
        # Redirect to the results page with the 'make' data
        return redirect(f'/carfax/results/?make={make}&model_year={model_year}&body_class={body_class}&gross_weight={gross_weight}')
    else:
        return render(request, 'frontend/carfax.html', {'error': 'Make not found for the given VIN code'})    

def carfax_results(request):
    make = request.GET.get('make', '')
    model_year = request.GET.get('model_year', '')
    body_class = request.GET.get('body_class', '')
    gross_weight = request.GET.get('gross_weight', '')

    # Check if body_class and gross_weight are 'None', replace with "No access to this information"
    body_class = 'No access to this information' if body_class == 'None' else body_class
    gross_weight = 'No access to this information' if gross_weight == 'None' else gross_weight

    context = {'make': make, 'model_year': model_year, 'body_class': body_class, 'gross_weight': gross_weight}
    return render(request, 'frontend/carfax_results.html', context)
