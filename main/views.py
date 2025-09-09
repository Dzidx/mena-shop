from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406406351',
        'name': 'Dzaky Ahmad Trinindito',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)