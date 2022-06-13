from markdown2 import Markdown
from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")
    text = forms.CharField(widget=forms.Textarea(), label="Text")

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

def newpage(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            if title.lower() not in (i.lower() for i in util.list_entries()):
                util.save_entry(title, text)
                return redirect("wiki:title", title)
            else:
                return render(request, "encyclopedia/error2.html", {
                "title": title.capitalize()
                })
        else:
            return render(request, "encyclopedia/newpage.html", {
            "form": form
            })
    return render(request, "encyclopedia/newpage.html", {
        "form": NewPageForm()
    })
