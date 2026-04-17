from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <h1>ClinicFlow</h1>
    <p>Welcome to the clinic managment system.</p>
    <p>This is my Django project for Object-Oriented Programming.</p>
    """)

