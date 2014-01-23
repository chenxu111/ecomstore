from django.http.response import HttpResponse
from django.template import Context
from django.template.loader import render_to_string

def catalog(request):
    print 'catalog'
    site_name = "Modern Musician"
    response_html = u'<html><body>welcome %s</body></htm>' %site_name
    return HttpResponse(response_html)

def catalog2(request):
    my_context = Context({'site_name':"Modern Music"})
    response_html = render_to_string('sample.html',my_context)
    return HttpResponse(response_html)
