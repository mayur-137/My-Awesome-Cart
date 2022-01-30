from django.http import HttpResponse

def index(request):
    return HttpResponse(''' 
        <h1> <pre> <center> Hello, Welcome To My Awesome Cart,
        <a href="shop"> My Awesome Cart </a> Here</pre>
            </h1></center>
    ''')