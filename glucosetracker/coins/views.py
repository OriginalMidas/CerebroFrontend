import json
from django.shortcuts import render, HttpResponse
from .models import Cryptocurrency, Coin, Cryptocurrencytable
from django_tables2 import RequestConfig
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .reports import ChartData


# Create your views here.

def cryptocurrenciesView(request):
    """
    Provides data for the coins page by pulling Cryptocurrencies being watched, from the database and displaying them
    on the page.
    """
    template_name = 'coins/cryptocurrencies.html'
    user = User.objects.get(username=request.user.username)

    table = Cryptocurrencytable(Cryptocurrency.objects.all())
    RequestConfig(request).configure(table)

    return render(request=request, template_name=template_name, context={'cryptocurrency': table}, )


# def coinsChart(request):
#   return render()

@login_required
def coinsChartDataJson(request):
    data = {}
    params = request.GET
    # to pull from the js code from cryptocurrencies.html, use this method. If nothing is added, days = 0, name = ""
    # days = params.get('days', 0)
    # name = params.get('name', '')

    # TODO let currency choice get pulled from the webpage
    # data will contain crypto name, price, and the unix time
    data['chart_data'] = ChartData.getCurrencyData(currency='Bitcoin')

    return HttpResponse(json.dumps(data), content_type='application/json')
