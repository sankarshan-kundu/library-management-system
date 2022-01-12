import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views import View

from .models import Book

class BookView(View):
    def get(self, request):
        books = Book.objects.all()
        data=[]
        for b in books:
            data.append({'title':b.title,'authors':b.authors,'total_copies':b.total_copies})
        return HttpResponse(json.dumps(data), content_type="application/json")