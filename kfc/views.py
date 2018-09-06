from urllib.parse import unquote, urlencode
from furl import furl
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'kfc/index.html')


@login_required
def home(request):
    print(request.META.HTTP_REFERER)
    meraki_url = 'https://jnjuguna.com/kfc/?base_grant_url=https%3A%2F%2Fn171.network-auth.com%2Fsplash%2Fgrant&user_continue_url=http%3A%2F%2Fclickserve.dartsearch.net%2Flink%2Fclick%3Flid%3D43700022066692152%26ds_s_kwgid%3D58700002559034278%26%26ds_e_adid%3D257449475172%26ds_e_matchtype%3Dsearch%26ds_e_device%3Dc%26ds_e_network%3Dg%26%26ds_url_v%3D2%26ds_dest_url%3Dhttps%3A%2F%2Fslack.com%2Flp%2F0818%3Fcvosrc%3Dppc.google.d_ppc_google_africa_en_brand-hv%26cvo_creative%3D257449475172%26utm_medium%3Dppc%26utm_source%3Dgoogle%26utm_campaign%3Dd_ppc_google_africa_en_brand-hv%26utm_term%3Dslack%26cvosrc%3Dppc.google.slack%26cvo_campaign%3D%26cvo_crid%3D257449475172%26Matchtype%3De%26utm_source%3Dgoogle%26utm_medium%3Dppc%26c3api%3D5523%2C257449475172%2Cslack%26gclid%3DCjwKCAjw_b3cBRByEiwAdG8WqoUCynWqtpkn0mW2jtEBcZoi7_JD0x787I81AHr6wk0MmDfHpRKDSxoC048QAvD_BwE&node_id=247165641720654&node_mac=e0:cb:bc:46:83:4e&gateway_id=247165641720654&client_ip=10.244.217.102&client_mac=f4:06:69:3b:b2:49'
    f = furl(unquote(meraki_url))
    print(f.args['base_grant_url'])
    print(f.args['user_continue_url'])
    print(f.args['node_id'])
    print(f.args['node_mac'])
    print(f.args['gateway_id'])
    print(f.args['client_ip'])
    print(f.args['client_mac'])

    redirect_url = f.args['base_grant_url'] + '?' + 'duration=' + '3600'
    print(redirect_url)
    return render(request, 'kfc/home.html')


def logout(request):
    return render(request, 'kfc/logout.html')
