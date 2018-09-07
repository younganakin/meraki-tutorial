from urllib.parse import unquote, urlencode
from furl import furl
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Contacts
from django.utils import timezone

# Create your views here.


def index(request):
    base_grant_url = request.GET['base_grant_url']
    user_continue_url = request.GET['user_continue_url']
    node_id = request.GET['node_id']
    node_mac = request.GET['node_mac']
    gateway_id = request.GET['gateway_id']
    client_ip = request.GET['client_ip']
    client_mac = request.GET['client_mac']

    request.session['base_grant_url'] = base_grant_url
    request.session['user_continue_url'] = user_continue_url
    request.session['node_id'] = node_id
    request.session['node_mac'] = node_mac
    request.session['gateway_id'] = gateway_id
    request.session['client_ip'] = client_ip
    request.session['client_mac'] = client_mac

    return render(request, 'kfc/index.html')


@login_required
def home(request):
    base_grant_url = request.session['base_grant_url']
    user_continue_url = request.session['user_continue_url']
    node_id = request.session['node_id']
    node_mac = request.session['node_mac']
    gateway_id = request.session['gateway_id']
    client_ip = request.session['client_ip']
    client_mac = request.session['client_mac']
    user_email = request.user.email

    contact = Contacts(email=user_email,
                       node_id=node_id,
                       node_mac=node_mac,
                       gateway_id=gateway_id,
                       client_ip=client_ip,
                       client_mac=client_mac,
                       logged_in=timezone.now())

    contact.save()

    continue_url = 'https://www.google.com/'

    redirect_url = base_grant_url + '/?continue_url=' + continue_url
    return redirect(redirect_url)
