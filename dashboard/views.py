from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    raw_data = response.json()

    categories = {}

    posts = []
    for key, value in raw_data.items():
        item = value.copy()

        if item['category'] not in categories.keys():
            categories[item['category']] = 1
        else:
            n = categories[item['category']]
            categories[item['category']] = n + 1

        posts.append(item)

    total_responses = len(posts)

    # Puedes definir más indicadores aquí si quieres
    first_name = posts[0]['name'] if posts else "N/A"
    latest_name = posts[-1]['name'] if posts else "N/A"
    unique_emails = len(set([p['email'] for p in posts if 'email' in p]))

    chart_data = {'labels': list(categories.keys()), 'data': list(categories.values())}

    data = {
        'title': "Landing Page' Dashboard",
        'chart_title': "Contactos por Categoría",
        'posts': posts,

        'total_responses': total_responses,
        'first_name': first_name,
        'latest_name': latest_name,     
        'unique_emails': unique_emails,

        'chart_data': chart_data,
    }

    return render(request, 'dashboard/index.html', data)