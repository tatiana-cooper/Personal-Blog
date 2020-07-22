from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.models import Publication
from my_project import settings


def index(request):
    """ Return main.html page """
    return render(request, 'main.html')


def contacts(request):
    """ Return contacts.html page """
    return render(request, 'contacts.html')


def post(request):
    """
    :param request: needed to define method of request. If method POST - update database and redirect
    to '/publications' page, if method GET - returns the 'post.html' page.
    """

    if request.method == 'POST':

        # get title, text, password from request
        title = request.POST.get('title')[:30]  # cut the long title to fit in page
        text = request.POST.get('text')
        password = request.POST.get('password')

        # if secret key is incorrect - sends error to post.html page
        if password != settings.SECRET_KEY:
            return render(request, 'post.html', {
                'error': 'The password is incorrect!'
            })

        # if text, title aren't empty
        if text and title:
            # create a new publication in database and redirect to the '/publications' page
            Publication.objects.create(title=title, text=text)
            return redirect('/publications')
        else:

            # sends error to post.html page
            return render(request, 'post.html', {
                'error': 'Text and Title should be entered!'
            })

    return render(request, 'post.html')


def publications(request):
    """ The function sorts database and sends it to 'publications.html' page.
        Returns 'publications.html' page. """

    publications_sorted = Publication.objects.order_by('-date')  # sorted by date, -date — reversed sorting

    return render(request, 'publications.html', {
        'publications': publications_sorted
    })


def publication_(request, pub_id):

    """
    :param request: request
    :param pub_id: id of publication
    :return: specified publication page by given id (pub_id)
    """

    # if database doesn't have such publication — redirect user to 'main.html' page
    try:
        publication = Publication.objects.get(id=pub_id)

    except Publication.DoesNotExist:
        return redirect('/')

    return render(request, 'publication.html', {
        'publication': publication
    })


def status(request):
    """ Return HttpResponse """
    return HttpResponse('Status OK')
