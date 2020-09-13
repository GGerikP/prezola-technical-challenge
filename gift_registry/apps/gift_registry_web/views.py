from django.shortcuts import render

def show_web_index(request):

    response = {}
    response["SITE_TITLE"] = "Fancy Gift Registry"

    return render(request, "gift_registry_web/index.html", response)

