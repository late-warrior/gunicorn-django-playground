from django.views.generic import View
from django.http import HttpResponse

from .connection import get_conn
import time

class NewView(View):

    def get(self, request):
        conn = get_conn()
        time.sleep(2)
        conn.close()
        return HttpResponse("Stuff")