from django.shortcuts import render
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    content_md = util.get_entry(title)
    content_html = Markdown().convert(content_md)
    return render(request, "encyclopedia/title.html", {
         "content": content_html
        })
