from django.shortcuts import render
from projects.dao.ontology import Ontology

onto = Ontology('quanli_duan.owl')

# Create your views here.
def nhanvien_search(request):
    query = request.POST.get('q')
    nhanviens = onto.search_nhanviens(query)
    context = {
        'nhanviens': nhanviens,
        'keyword': query
    }
    return render(request, 'nhanvien_index.html', context)

def nhanvien_index(request):
    nhanviens = onto.get_nhanviens()

    context = {
        'nhanviens': nhanviens
    }

    return render(request, 'nhanvien_index.html', context)

def nhanvien_detail(request, id):
    nhanvien = onto.get_nhanvien(id)

    context = {
        'nhanvien': nhanvien
    }

    return render(request, 'nhanvien_detail.html', context)

def duan_search(request):
    query = request.POST.get('q')
    duans = onto.search_duans(query)
    context = {
        'duans': duans,
        'keyword': query
    }
    return render(request, 'duan_index.html', context)

def duan_index(request):
    duans = onto.get_duans()
    context = {
        'duans': duans
    }
    return render(request, 'duan_index.html', context)

def duan_detail(request, id):
    duan = onto.get_duan(id)
    context = {
        'duan': duan
    }
    return render(request, 'duan_detail.html', context)

def team_index(request):
    teams = onto.get_teams()
    context = {
        'teams': teams
    }
    return render(request, 'team_index.html', context)

def team_detail(request, id):
    team = onto.get_team(id)
    context = {
        'team': team
    }
    return render(request, 'team_detail.html', context)
