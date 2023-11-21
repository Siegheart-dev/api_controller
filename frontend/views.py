import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

def get_vehicle_info(vin_code):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinExtended/{vin_code}?format=json'
    response = requests.get(url)
    data = response.json()

    variable_map = {
        'Manufacturer Name': 'make',
        'Model Year': 'model_year',
        'Body Class': 'body_class',
        'Gross Vehicle Weight Rating From': 'gross_weight',
    }

    vehicle_info = {variable_map.get(item.get('Variable'), ''): item.get('Value') for item in data.get('Results', [])}

    return vehicle_info.get('make', ''), vehicle_info.get('model_year', ''), vehicle_info.get('body_class', ''), vehicle_info.get('gross_weight', '')

def carfax(request):
    vin_code = request.GET.get('vin-code', "")
    make, model_year, body_class, gross_weight = get_vehicle_info(vin_code)

    if make:
        # Redirect to the results page with the data
        return redirect(f'/carfax/results/?make={make}&model_year={model_year}&body_class={body_class}&gross_weight={gross_weight}')
    else:
        return render(request, 'frontend/carfax.html', {'error': 'Make not found for the given VIN code'})    

def carfax_results(request):
    vehicle_info = {key: request.GET.get(key, '') for key in ['make', 'model_year', 'body_class', 'gross_weight']}

    # Check if some of data are 'None', replace with "No access to this information"
    for key in ['body_class', 'gross_weight']:
        vehicle_info[key] = 'No access to this information' if vehicle_info[key] == 'None' else vehicle_info[key]

    return render(request, 'frontend/carfax_results.html', vehicle_info)
