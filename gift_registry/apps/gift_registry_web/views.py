from django.shortcuts import render

def show_web_index(request):

    response = {}
    response["SITE_TITLE"] = "Simle Gift Registry"

    return render(request, "gift_registry_web/index.html", response)

def show_registry_gift_report(request):
    response = {}
    response["SITE_TITLE"] = "Simple Gift Registry Report"

    return render(request, "gift_registry_web/report.html", response)

