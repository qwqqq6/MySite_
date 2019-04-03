from django.shortcuts import render_to_response


def home(request):
    content = {}
    return render_to_response('home.html', content)
