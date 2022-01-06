

from django.views.generic import ListView

from .models import Post

class HomePageView(ListView):
    template_name = "news/homepage.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nationarticles"] = Post.objects.filter(media_house='Nation Media Group')[:5]
        context["stararticles"] = Post.objects.filter(media_house='The Star')[:5]
        context["standardarticles"] = Post.objects.filter(media_house='Standard Media Group')[:5]
        return context