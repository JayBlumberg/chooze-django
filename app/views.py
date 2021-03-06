"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import HttpResponse


from django.http import HttpResponse

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def current_datetime(request):
    now = datetime.now()
    import marc1
    import marc2
    now = marc1.fib2(1000) 
    now = marc2.function1(1)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def marc(request):
    import marc2
    now = marc2.function1(1)
    html = "<html><body>%s</body></html>" % now
    return HttpResponse(html)

def jay(request):
    import jay1
    now = jay1.function1(1)
    html = "<html><body>%s</body></html>" % now
    return HttpResponse(html)
