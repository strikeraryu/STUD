from django.http import HttpResponse
from django.shortcuts import render

from .models import Batch, Mentor

def batch_view(request, *args, **kargs):

    batches = []
    for b in Batch.objects.all():
        mentor_name = Mentor.objects.get(batch_no = b.batch_no).mentor_name
        batches.append({'batch_no' : b.batch_no, 'mentor_name' : mentor_name})

    return render(request, 'batch.html', {'batches' : batches})