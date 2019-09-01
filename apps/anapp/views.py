from django.shortcuts import render
from .forms import MyForm
from django.views.generic.base import TemplateView
from django.contrib import messages


# Create your views here.
def index(request):
    form = MyForm()
    return render(request, 'anapp/index.html', {'form': form})


class HomePageView(TemplateView):
    template_name = "anapp/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        form = MyForm(self.request.POST or None)
        context['form'] = form
        messages.info(self.request, "hello http://django4u.com")
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['form'].is_valid():
            print('Form Valid!')
            # save your model
            # redirect

        return super(HomePageView, self).render_to_response(context)
