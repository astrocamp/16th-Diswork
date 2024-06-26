from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Ads
from boards.models import Category
from .forms import AdsForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@method_decorator(login_required, name="dispatch")
class AdsListView(ListView):
    model = Ads
    template_name = "ads/ad_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AdsForm()
        context["category_list"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("ads:list")


@method_decorator(login_required, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    form_class = AdsForm
    template_name = "ads/ad_list.html"

    def get_success_url(self):
        return reverse_lazy("ads:list")

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, "403.html")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads
    form_class = AdsForm
    template_name = "ads/edit.html"

    def get_success_url(self):
        return reverse_lazy("ads:list")

    def get_object(self, queryset=None):
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return get_object_or_404(Ads, pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ads"] = self.get_object()
        context["is_iterable"] = False
        context["category_list"] = Category.objects.all()
        return context


@method_decorator(login_required, name="dispatch")
class AdsDeleteView(DeleteView):
    model = Ads
    template_name = "ads/delete.html"

    def get_success_url(self):
        return reverse("ads:list")

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not self.request.user.is_superuser:
            raise PermissionDenied()
        return obj
