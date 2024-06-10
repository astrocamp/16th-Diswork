from django.views.generic import ListView, DeleteView
from .models import Friend
from members.models import Member
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from lib.paginate_que import paginate_queryset
from django.db.models import Q


@method_decorator(login_required, name="dispatch")
class MemberListView(ListView):
    model = Member
    template_name = "friends/search_list.html"
    context_object_name = "search_list"
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset().exclude(username=self.request.user)
        keyword = self.request.GET.get("username", "").strip()
        if keyword:
            return query.filter(username__icontains=keyword)
        return query
    

@method_decorator(login_required, name="dispatch")
class FriendListView(ListView):
    model = Friend
    paginate_by = 5

    def get_queryset(self):
        user = self.request.user
        return Friend.objects.filter(sender=user, status="2") | Friend.objects.filter(
            receiver=user, status="2"
        )


@method_decorator(login_required, name="dispatch")
class FriendDeleteView(DeleteView):
    model = Friend
    template_name = "friends/confirm_delete.html"
    success_url = reverse_lazy("friends:friend_list")


@login_required
def send_friend_request(req, receiver_id):
    members = Member.objects.exclude(id=req.user.id)
    page_number = req.POST.get("page")
    page_obj, is_paginated  = paginate_queryset(members, page_number, 5)
    sender_id = req.user.id
    receiver_exists = Member.objects.filter(id=receiver_id).exists()

    if req.method == "POST":
        is_friend = Friend.objects.filter(Q(sender_id=sender_id, receiver_id=receiver_id) | Q(sender_id=receiver_id, receiver_id=sender_id)).exists()
        friend = Friend.objects.filter(Q(sender_id=sender_id, receiver_id=receiver_id) | Q(sender_id=receiver_id, receiver_id=sender_id)).first()
        if is_friend:
            if friend.status == "2":
                messages.error(req, "己經是好友了。")
            elif friend.receiver_id == req.user.id:
                messages.error(req, "對方己發送好友通知，請到等待中加好友!")        
            else:    
                messages.error(req, "好友邀請已經發送過了！")
        else:
            Friend.objects.create(sender_id=sender_id, receiver_id=receiver_id)
    else:
        if not receiver_exists:
            messages.error(req, "沒有這個使用者!")
        elif sender_id == receiver_id:
            messages.error(req, "不能加自己為好友!")
    redirect_url = reverse("friends:member_list")
    
    if is_paginated:
            redirect_url += f"?page={page_number}"

    return redirect(redirect_url)       



@login_required
def accept_friend_request(req, friend_request_id):
    try:
        friend_request = Friend.objects.get(id=friend_request_id, status="1")
    except Friend.DoesNotExist:
        messages.error(req, "好友邀請已經發送過了！")
        return render(req, "friends/search_list.html")

    if friend_request.receiver == req.user:
        sender = friend_request.sender
        receiver = friend_request.receiver

        if not Friend.objects.filter(sender=receiver, receiver=sender).exists():
            receiver.friends.add(sender)
            sender.friends.add(receiver)

        friend_request.status = "2"
        friend_request.save()

        messages.success(req, "好友邀請已接受")
        return render(req, "friends/friend_list.html")
    else:
        messages.error(req, "好友邀請已接受")
        return render(req, "friends/friend_list.html")


@login_required
def reject_friend_request(req, friend_request_id):
    if req.method == "POST":
        friend_request = get_object_or_404(Friend, id=friend_request_id, status="1")
        if friend_request.receiver == req.user:
            friend_request.status = "3"
            friend_request.save()
    return redirect("friend_requests")


@login_required
def friend_requests(req):
    received_requests = Friend.objects.filter(receiver=req.user, status="1")
    return render(
        req, "friends/friend_requests.html", {"received_requests": received_requests}
    )
