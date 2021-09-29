from django.shortcuts import render, get_object_or_404
from .models import Cuisine
# Cuisine_list view as a function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""
    cuisines = Cuisine.objects.all()
    object_list = Cuisine.objects.all()
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        cuisines = paginator.page(page)
    except PageNotAnInteger: # If page is not an integer deliver the first page
        cuisines = paginator.page(1)
    except EmptyPage: # If page is out of range deliver last page of results
        cuisines = paginator.page(paginator.num_pages)
    return render(
        request,
        'cuisine/cuisine/list.html',
        {'page': page,'cuisines': cuisines}
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
