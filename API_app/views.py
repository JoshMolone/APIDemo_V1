import json
from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
import pprint
from API_app.config.settings import APP_ID
from rest_framework.response import Response
import requests


def index(request):
    return HttpResponse("Good server ")
    
def home(request):
    ID = APP_ID
    URL = "https://openexchangerates.org/api/latest.json?app_id=" + ID
    r = requests.get(URL)

    if r.status_code == 200:
        response = r.json().get('rates')
        keys = response.keys()
        key_arr = []
        rd = {
        }
        for keys in response:
            rd.update({keys: response[keys]})
            key_arr.append(keys)
            print(f"RATES KEYS {keys} :   RATES VALUE {response[keys]}")


        print(f"DEBUG CHECK --- Context :  {rd}")
        return render(request, 'home.html', {'rd': response})
    else:
        return HttpResponse('############### Error calling API or API responding, no data ')



def allCurrency(request):
    ID = APP_ID
    URL = "https://openexchangerates.org/api/currencies.json?app_id=" + ID
    r = requests.get(URL)

    if r.status_code == 200:
        response = r.json()
        keys = response.keys()
        key_arr = []
        rd = {
        }
        for keys in response:
            rd.update({keys: response[keys]})
            key_arr.append(keys)
            print(f"Dict Key {keys} :   Dict Value{response[keys]}")


        print(f"DEBUG CHECK --- Context :  {rd}")
        return render(request, 'currency.html', {'rd': response})
    else:
        return HttpResponse('############### Error calling API or API responding, no data ')





def fetchApi(request):
    ID = APP_ID
    URL = "https://openexchangerates.org/api/latest.json?app_id=" + ID
    # if request.method == 'POST':
    #     r = request.post(URL, params=request.POST)
    # else:
    r = requests.get(URL)
    if r.status_code == 200:
        response = r.json()
        print(response)
        return render(request, 'api.html')
    else:
        return HttpResponse('############### Error calling API or API responding, no data ')

    # return render(request, 'api.html', {})
    # Parameters for latest.json
    #     Parameters
    # Query Params
    # app_id:	stringRequired
    # Your unique App ID

    # base:	stringOptional
    # Change base currency (3-letter code, default: USD)

    # symbols:	stringOptional
    # Limit results to specific currencies (comma-separated list of 3-letter codes)

    # prettyprint:	booleanOptional
    # Set to false to reduce response size (removes whitespace)

    # show_alternative:	booleanOptional
    # Extend returned values with alternative, black market and digital currency rates

    # return HttpResponse("API FETCH")a


def dat(request):
    print("Requesting data from API via get request and expecting JSON data in return ")
    # response is a variable we are anitcipating to store the data we receive from our api acll.
    url = 'https://openexchangerates.org/api/latest.json?app_id=06ecdbab209b476991047973dcffa719'
    response = requests.get(
        'https://openexchangerates.org/api/latest.json?app_id=06ecdbab209b476991047973dcffa719')
    r = requests.get(url)
    data = json.loads(r.text)
    keyarr = []
    for keys in data['rates']:
        keyarr.append(keys)

    # for key in keyarr:
    #    print(key)

    # print(keyarr[0])
    first = keyarr[0]
    json_only = data['rates']
    first_val = json_only[first]
    # print(json_only)
    print(f"The curr {first} has a rate of {first_val}")
    # print("************** DATA NEW ")
    # for i in range(len(data['rates'].keys())):

    #     print(data['rates'].keys())
    # print((data['rates'].keys()))
    name_arr = []

    # for items in data:

    # Covering edge cases in such case the request/response cycle is not successful.
    if(response.status_code == 200):
        print("Successfully Retreived Data *****************")
        # print(response.json())
        jsonDict = response.json()
        cont_data = jsonDict.get('rates')
        # print(cont_data)
        # pprint.pprint(jsonDict.get('rates'))
        # print(jsonDict['rates'])
        currency = jsonDict['rates']
        name = currency.keys()
        rate = currency.values()
        # print(type(rate))
        # print(type(name))
        context = {


        }

        key_arr = []
        for keys in currency.keys():
            key_arr.append(keys)
            # print(f"key {keys}")
        # print(key_arr)
        count = 0
        for i in range(len(name)):

            context[key_arr[i]] = [currency[key_arr[i]]]

            count += 1

        # rate = currency[rate]
        # context = {
        #     'currency': currency,
        #     'rate': rate
        # }
        # # print(f" CONTEXT : {context}")

        d = {
        }

        for j in range(len(key_arr)):
            # d['Number'] = j
            # d['Currency'] = [key_arr[j]]
            # d['Rate'] = currency[key_arr[j]]
            d[key_arr[j]] = currency[key_arr[j]]
        # # count = 0
        # # while(count < len(key_arr)):
        # #     print(f" Name: {currency[currency[currency.count]]} & Rate: {d[key_arr[count]]}")
        # #     # print(f"FORST ################################################### {d[key_arr[j]]}")
        # #     # print(d)
        # #     count += 1
        # #     print(count)
        # # print(d)
        # a = currency
        # context = {

        #     "cur",
        #     "val"
        # }

        # idk = {['ID', 'Currency', 'Rate']}
        # for i in range(len(a)):
        #     idk['ID'] = i

        #     # context[] = [key_arr[i]]
        #     print(context)
        # print(idk)
        # items = {
        #     "Rate": a
        # }
        # for item in a:
        #     # print(item)
        #     print("----------------------------------------------------")
        # # print(r)
        # # for keys in r:
        # #     print(keys)
        # #     if keys == 'rates':
        # #         print(keys)

        # # currency_data = {
        # #     'rates':
        # # }

    else:
        print("!!! ERROR RETREIVING DATA $$$")

    # I believe our primary intention with this data will be to pass it through to our templates so we are able to render with HTTP through context (dictionary)
    print(f"Context being sent to templates is {d.keys()}")

    return render(request, 'index.html', {
        "id": d.keys(),
        "ra": d.values()
    })


# {'disclaimer': 'Usage subject to terms: https://openexchangerates.org/terms', 'license': 'https://openexchangerates.org/license', 'timestamp': 1638655212, 'base': 'USD', 'rates': {'AED': 3.6731, 'AFN': 96.022979, 'ALL': 106.911181, 'AMD': 490.225679, 'ANG': 1.801237, 'AOA': 565, 'ARS': 101.11498, 'AUD': 1.428163, 'AWG': 1.8005, 'AZN': 1.700805, 'BAM': 1.728528, 'BBD': 2, 'BDT': 85.671496, 'BGN': 1.734414, 'BHD': 0.376933, 'BIF': 1995, 'BMD': 1, 'BND': 1.368891, 'BOB': 6.891118, 'BRL': 5.653734, 'BSD': 1, 'BTC': 2.0485339e-05, 'BTN': 75.050207, 'BWP': 11.765267, 'BYN': 2.540787, 'BZD': 2.014582, 'CAD': 1.28486, 'CDF': 1998.386165, 'CHF': 0.917548, 'CLF': 0.030481, 'CLP': 841.06, 'CNH': 6.374225, 'CNY': 6.3764, 'COP': 3934.77685, 'CRC': 628.068962, 'CUC': 1, 'CUP': 25.75, 'CVE': 98.2, 'CZK': 22.50145, 'DJF': 177.92311, 'DKK': 6.5741, 'DOP': 56.728236, 'DZD': 138.835, 'EGP': 15.71012, 'ERN': 15.000155, 'ETB': 48.020768, 'EUR': 0.883861, 'FJD': 2.1273, 'FKP': 0.755715, 'GBP': 0.755715, 'GEL': 3.115, 'GGP': 0.755715, 'GHS': 6.161556, 'GIP': 0.755715, 'GMD': 52.4, 'GNF': 9502.008573, 'GTQ': 7.730623, 'GYD': 209.164811, 'HKD': 7.796105, 'HNL': 24.136986, 'HRK': 6.6757, 'HTG': 98.622935, 'HUF': 322.161, 'IDR': 14526, 'ILS': 3.16203, 'IMP': 0.755715, 'INR': 75.2275, 'IQD': 1458.17341, 'IRR': 42250, 'ISK': 129.58, 'JEP': 0.755715, 'JMD': 155.216987, 'JOD': 0.709, 'JPY': 112.805, 'KES': 112.636252, 'KGS': 84.784652, 'KHR': 4072, 'KMF': 434.224651, 'KPW': 900, 'KRW': 1184.375, 'KWD': 0.302704, 'KYD': 0.832877, 'KZT': 438.356013, 'LAK': 10886.672338, 'LBP': 1511.361649, 'LKR': 201.885733, 'LRD': 141.999978, 'LSL': 15.91224, 'LYD': 4.592223, 'MAD': 9.225011, 'MDL': 17.739991, 'MGA': 3975.475007, 'MKD': 54.454264,
# 'MMK': 1784.19004, 'MNT': 2854.559306, 'MOP': 8.022802, 'MRO': 356.999828, 'MRU': 36.239505, 'MUR': 42.983797, 'MVR': 15.45, 'MWK': 816.492482, 'MXN': 21.2698, 'MYR': 4.231, 'MZN': 63.875002, 'NAD': 16.11, 'NGN': 410.764648, 'NIO': 35.209901, 'NOK': 9.185, 'NPR': 120.080432, 'NZD': 1.481647, 'OMR': 0.384993, 'PAB': 1, 'PEN': 4.074326, 'PGK': 3.539726, 'PHP': 50.460225, 'PKR': 176.649996, 'PLN': 4.06388, 'PYG': 6818.562505, 'QAR': 3.64075, 'RON': 4.3738, 'RSD': 103.99022, 'RUB': 73.973, 'RWF': 1035.430822, 'SAR': 3.751354, 'SBD': 8.074316, 'SCR': 12.800643, 'SDG': 437.5, 'SEK': 9.15065, 'SGD': 1.372535, 'SHP': 0.755715, 'SLL': 11125.80017, 'SOS': 578.171412, 'SRD': 21.533, 'SSP': 130.26, 'STD': 21187.940504, 'STN': 21.9, 'SVC': 8.745029, 'SYP': 2512.5, 'SZL': 15.902784, 'THB': 33.863013, 'TJS': 11.283606, 'TMT': 3.5, 'TND': 2.8785, 'TOP': 2.286637, 'TRY': 13.7027, 'TTD': 6.782236, 'TWD': 27.6722, 'TZS': 2303, 'UAH': 27.279539, 'UGX': 3562.967389, 'USD': 1, 'UYU': 44.129911,
# 'UZS': 10754.05993, 'VES': 4.6322, 'VND': 22735, 'VUV': 111.99
