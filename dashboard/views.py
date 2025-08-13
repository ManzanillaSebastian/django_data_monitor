from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    raw_data = response.json()

    posts = []
    for key, value in raw_data.items():
        item = value.copy()
        item["id"] = key  # opcional si quieres mostrar el ID
        posts.append(item)

    total_responses = len(posts)

    # Puedes definir más indicadores aquí si quieres
    first_name = posts[0]['name'] if posts else "N/A"
    latest_name = posts[-1]['name'] if posts else "N/A"
    unique_emails = len(set([p['email'] for p in posts if 'email' in p]))

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'first_name': first_name,
        'posts': posts,
    }

    return render(request, 'dashboard/index.html', data)