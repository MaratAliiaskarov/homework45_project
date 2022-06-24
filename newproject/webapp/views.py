from django.shortcuts import render

# Create your views here.

def index_view(request):
    query = request.GET.get("name", "rrr")
    context = {"name": query}
    return render(request, "index.html", context)


def create_article(request):
    if request.method == "GET":
        return render(request, "create.html")
    else:
        context = {
            "project": request.POST.get("project"),
            "content": request.POST.get("content"),
            "author": request.POST.get("author"),
        }

        return render(request, "article_view.html", context)