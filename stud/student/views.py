from django.http import HttpResponse
from django.shortcuts import render

from .models import Batch, Mentor


def batch_view(request, *args, **kargs):

    batches = []
    totol_batch = 0
    for b in Batch.objects.all():
        totol_batch += 1
        mentor_name = Mentor.objects.get(batch_no=b.batch_no).mentor_name
        batches.append({'batch_no': b.batch_no, 'mentor_name': mentor_name})

    return render(request, 'batch.html', {'batches': batches, 'total_batch': totol_batch})

