from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import TemplateView, FormView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, get_object_or_404
from .models import Member
from .forms import MemberUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# email check start
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User

# email check end


# 登入
class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


# 登出
class LogoutView(TemplateView):
    template_name = "registration/logout.html"

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "登出成功！")
        return redirect("index")


# 註冊
class RegisterView(FormView):
    template_name = "registration/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("members:login")

    def form_valid(self, form):
        # 驗證信箱是否被註冊過
        email = form.cleaned_data.get("email")
        if Member.objects.filter(email=email).exists():
            messages.error(self.request, "此電子郵件已被註冊！！！")
            return self.form_invalid(form)
        # 創建一個尚未驗證成功的帳號，生成唯一的連結
        user = form.save(commit=False)
        user.is_active = False  # is_activate db column，預設尚未驗證
        user.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        link = self.request.build_absolute_uri(
            reverse("members:activate", kwargs={"uidb64": uid, "token": token})
        )
        # 發送郵件
        send_mail(
            "Diswork會員驗證信件",
            "點擊此連結驗證您的帳戶： {}".format(link),
            "dali175666@gmail.com",
            [user.email],
            fail_silently=False,
        )
        messages.success(self.request, "請至您的註冊信箱查看信件並完成註冊。")
        return super().form_valid(form)


# user profile
class ProfileView(DetailView):
    model = Member
    template_name = "registration/profile.html"
    context_object_name = "member"


# 編輯會員資料
@method_decorator(login_required, name="dispatch")
class MemberUpdateView(UpdateView):
    model = Member
    form_class = MemberUpdateForm
    template_name = "registration/edit.html"
    context_object_name = "member"

    def get_success_url(self):
        return reverse_lazy("members:profile", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        return Member.objects.get(pk=pk)


# mail驗證 2024/5/9 增加 -- Jeter
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Member.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "您的帳號已驗證成功！")
        return redirect("members:login")
    else:
        messages.error(request, "驗證連結無效！")
        return redirect("members:register")
