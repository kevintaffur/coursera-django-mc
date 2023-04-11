from django.shortcuts import render
from django.http import HttpResponse
from .forms import BookingForm
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def about(request):
    about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}
    return render(request, 'about.html', about_content)

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}
    return render(request, 'menu.html', items_dict)

def book(request):
    return render(request, 'book.html', {})

def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffe',
        'te': 'type of beverage',
        'lemonade': 'type of refreshment',
        'water': 'it is what it is',
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(
        f"<h2>{drink_name}</h2> {choice_of_drink}"
    )

def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'booking.html', context={'form': form})
