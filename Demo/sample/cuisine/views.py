from django.shortcuts import render, get_object_or_404
from .models import Cuisine
# Cuisine_list view as a function
def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""
    cuisines = Cuisine.objects.all()
    return render(
    request,
    'cuisine/cuisine/list.html',
    {'cuisines': cuisines}
    )

def Cuisine_detail(request, cuisine):
    """function to implement the logic of the detail view for Cuisine"""
    cuisineClicked = get_object_or_404(
    Cuisine,
    slug=cuisine,
    status='published'
    )
    return render(
    request,
    'cuisine/cuisine/detail.html',
    {'cuisine': cuisineClicked}
    )
