from django.shortcuts import render, get_object_or_404
from .models import Cuisine
# Cuisine_list view as a function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView,DetailView

from .forms import ShareCuisineViaEmailForm, CommentForm
from django.core.mail import send_mail

# *************************************************************
# cuisine_share view as a function
def ShareCuisineViaEmail(request, cuisine_id):
 # Retrieve cuisine by id
     cuisine = get_object_or_404(Cuisine, id=cuisine_id, status='published')
     sent = False # email has not yet been sent
     if request.method == 'POST':
 # Form was submitted
         submittedFrm = ShareCuisineViaEmailForm(request.POST)
         if submittedFrm.is_valid():
 # Form fields passed form validation
             cd = submittedFrm.cleaned_data # dictionary of the validated data, if any
             cuisine_url = request.build_absolute_uri(cuisine.get_absolute_url())
             subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],
             cd['emailFrm'],
             cuisine.name)
             message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(cuisine.name,
             cuisine_url,
             cd['name'],
            cd['emailContent'])
             send_mail(subject, message, 'admin@my.com', [cd['emailTo']])
             sent = True
     else:
         submittedFrm = ShareCuisineViaEmailForm()
     return render(request,
         'cuisine/cuisine/share.html',
        {'cuisine': cuisine,
         'form': submittedFrm,
         'sent': sent}
         )

class CuisineListView(ListView):
    queryset = Cuisine.objects.all()
    context_object_name = 'cuisines'
    paginate_by = 5
    template_name = 'cuisine/cuisine/list.html'

def Cuisine_list(request):
    """function to implement the logic of the list view for Cuisine"""
    cuisines = Cuisine.objects.all()
    object_list = Cuisine.objects.all()
    paginator = Paginator(object_list, 5) # 3 posts in each page
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

    comments = cuisineClicked.comments.filter(active=True)
    commented = False
    if request.method == 'POST':
    # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
    # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.cuisine = cuisineClicked
            # Save the comment to the database
            new_comment.save()
            commented = True
    else:
        comment_form = CommentForm()
    return render(
    request,
    'cuisine/cuisine/detail.html',
    {'cuisine': cuisineClicked,
    'commented': commented,
    'comments': comments,
    'comment_form': comment_form
    }
    )
