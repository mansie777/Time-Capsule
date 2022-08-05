from django.shortcuts import render
from .models import Article


# Create your views here
def pictures(request):

      list = Article.objects.all()
      content = {'lists':list}
      return render(request,"index.html",content)


def details(request,id_article):
      return render(request,"details.html")
