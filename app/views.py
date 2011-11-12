from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from api import pcr
from wrapper import *

def index(request):
  return render_to_response('index.html')

def department(request,dept):
  d=Department(pcr(''.join(('dept/',dept))))
  return render_to_response('department.html', {'c':d.coursehistories,})
