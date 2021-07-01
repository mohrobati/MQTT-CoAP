from django.shortcuts import render, HttpResponse
from .subscriber import Subscriber
import threading

subscriber = Subscriber(['farm', 'home', 'hospital'], "IoT_9631028_MQTT/")
threading.Thread(target=subscriber.runSubscriber).start()


def index(request):
    return render(request, 'index.html')


def application_index(request, application):
    return render(request, 'instances.html', {'application': application, 'range': range(10)})


def details(request, application, id):
    params = getParameters(application, id)
    return render(request, 'details.html', {
        'application': application,
        'id': id,
        'params': params,
    })


def parameter(request, application, id, parameter):
    value = subscriber.getStore().getValues(application + "/" + str(id) + "/" + parameter)
    return HttpResponse(value)


def getParameters(application, id):
    icons = []
    params = []
    values = []
    key_value = subscriber.getStore().getValues(application + "/" + str(id))
    if application == 'hospital':
        params = ['bloodPressure', 'fever', 'heartbeat', 'oxygen', 'energy']
        values = [key_value['bloodPressure'], key_value['fever'], key_value['heartbeat'],
                    key_value['oxygen'], key_value['energy']]
        icons.append('vial')
        icons.append('temperature-high')
        icons.append('heartbeat')
        icons.append('diagnoses')
        icons.append('battery-half')
    elif application == 'home':
        params = ['parking', 'lights', 'doorlock', 'temperature', 'energy']
        values = [key_value['parking'], key_value['lights'], key_value['doorlock'],
                    key_value['temperature'], key_value['energy']]
        icons.append('car')
        icons.append('lightbulb')
        icons.append('door-open')
        icons.append('temperature-low')
        icons.append('battery-half')
    elif application == 'farm':
        params = ['humidity', 'light', 'moisture', 'temperature', 'energy']
        values = [key_value['humidity'], key_value['light'], key_value['moisture'],
                    key_value['temperature'], key_value['energy']]
        icons.append('cloud-rain')
        icons.append('sun')
        icons.append('water')
        icons.append('temperature-low')
        icons.append('battery-half')
    return list(zip(params, icons, values))
