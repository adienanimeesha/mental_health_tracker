from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306170912',
        'name': 'Adiena Nimeesha Adiwinastwan',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)