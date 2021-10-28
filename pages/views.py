from django.views.generic import TemplateView
from django.shortcuts import render

from .models import *

class HomePageView(TemplateView):
    template_name = 'pages/rawlocation.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


def index(request):
    all = Tbllocationdata.objects.order_by('stampedtime')
    user = Tblassets.objects.get(firstname='Brooklyn')
    badge = Tblbadges.objects.get(asset=user)
    #all = all.filter(badgeid=badge.badgeid)
    raw_data_list = list()
    for row in all:
        r = Tblnodes.objects.filter(nodeid=row.nodeid)
        a = Tblbadges.objects.filter(badgeid=row.badgeid)
        if len(r) > 0:
            r = str(r[0].room)
        else:
            r = str(row.nodeid)
        if len(a) > 0:
            a = str(a[0].asset)
        else:
            a = str(row.badgeid)
        raw_data_list.append({'id': row.id, 'stampedtime': row.stampedtime, 'asset': a, 'room': r})
    # print(raw_data_list)
    # print(raw_data_list[0])
    context = {'raw_data_list': raw_data_list}
    return render(request, 'pages/rawlocation.html', context)

def detail(request, locdata_id):
    try:
        dp = Tbllocationdata.objects.get(id=locdata_id)
        r = Tblnodes.objects.filter(nodeid=dp.nodeid)
        a = Tblbadges.objects.filter(badgeid=dp.badgeid)
        if len(r) > 0:
            r = str(r[0].room)
        else:
            r = 'None Associated'
        if len(a) > 0:
            a = str(a[0].asset)
        else:
            a = 'None Associated'
        dpf = {'id': dp.id, 'stampedtime': dp.stampedtime, 'asset': a, 'room': r, 'badgeid': dp.badgeid, 'nodeid': dp.nodeid}
    except:
        return
    return render(request, 'pages/detail.html', {'dp': dpf})
