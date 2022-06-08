from django.shortcuts import render
from markdown2 import Markdown

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

        })
