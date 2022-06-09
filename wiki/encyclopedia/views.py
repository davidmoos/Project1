from django.shortcuts import render
from markdown2 import Markdown
from django.shortcuts import render, redirect
from django.db.models import Q

from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    content_md = util.get_entry(title)


    if content_md is not None:
        content_html = Markdown().convert(content_md)
        return render(request, "encyclopedia/title.html", {
         "content": content_html,
         "title": title.capitalize()
        })
    else:
        return render(request, "encyclopedia/error.html", {
        "title": title.capitalize()
        })


def search(request):
    if request.method == "GET":
        q = request.GET["q"]
        q_low = q.lower()

        if q_low in (q.lower() for q in util.list_entries()):
            return redirect("wiki:title", q)
        else:
            search = [i for i in util.list_entries() if q_low in i.lower()]
            return render(request, "encyclopedia/search.html", {
            "entries": search

        })
