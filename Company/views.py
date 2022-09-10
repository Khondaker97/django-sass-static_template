from unicodedata import name
from django.shortcuts import render
import requests

# Create your views here.

def companies(request):
    response = requests.get("https://tva.staging.b2brain.com/search/autocomplete_org_all/").json()
    for r in response:
        name = r['company']
        sn = name[:2]
    return render(request, 'company.html', {"title": "Company List", "name": "Mahmud", 'companies' : response, "shortName": sn} )

def dashboard(request):
    return render(request, 'common.html', {"title": "Dashboard", "name": "Mahmud"} )
def intels(request):
    return render(request, 'common.html', {"title": "Intels", "name": "Mahmud"} )
def leads(request):
    return render(request, 'common.html', {"title": "Leads", "name": "Mahmud"} )
def integrations(request):
    return render(request, 'common.html', {"title": "Integrations", "name": "Mahmud"} )
def team(request):
    return render(request, 'common.html', {"title": "Team", "name": "Mahmud"} )
def support(request):
    return render(request, 'common.html', {"title": "Help/Support", "name": "Mahmud"} )