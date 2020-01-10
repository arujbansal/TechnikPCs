from django.shortcuts import render
from PCBuilder import models as m


def builder(request):
    categories = m.Category.objects.all()
    prices = m.Price.objects.all()
    if request.method == "GET":
        return render(request, "PCBuilder/builder.html", {"categories": categories, "prices": prices})
    else:
        requirement = request.POST.get("requirement")
        budget = int(request.POST.get("budget"))
        config_parts = m.FinalProduct.objects.filter(cat_price=budget, category=requirement)[0].parts.all()
        return render(request, "PCBuilder/builder.html",
                      {"categories": categories, "prices": prices, "parts": config_parts})
