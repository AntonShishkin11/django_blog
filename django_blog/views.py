from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"
    # def get(self, request, *args, **kwargs):
    #     # перенаправление
    #     return redirect(reverse_lazy('article', kwargs={'tags': 'python', 'article_id': 42}))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'юзер'
        return context


def about(request):
    return render(request, 'about.html')