# _*_ coding:utf-8 _*_

from models import *
from django.views.generic import list_detail
from forms import *
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

ITEMS_PER_PAGE = 2    #每页容纳的留言对象数目

def msg_list_page(request):
    return list_detail.object_list(
        request,
        queryset = Msg.objects.order_by('-id'),
        paginate_by = ITEMS_PER_PAGE,
        template_name = 'msg_list_page.html',
        template_object_name = 'msg'
    )

def register_page(request):
    #如果是通过POST方法提交表单数据
    if request.method == 'POST':
        error = {'success':'','error':''}
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = form.cleaned_data['email']
            )
#            error['success'] = "注册成功！"
        else:     #输入有错误，注册失败页面
            return HttpResponseRedirect('/accounts/register/fail/')
         #跳转到注册成功页面
        return HttpResponseRedirect('/accounts/register/success/')
#        return HttpResponseRedirect('/accounts/register/login/')

    else:
        form = RegistrationForm()

        variables = RequestContext(request,{'form':form})
        return render_to_response('registration/register.html',variables)

@login_required
def msg_post_page(request):
    if request.method == 'POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = Msg(
                title=form.cleaned_data['title'],
                content = form.cleaned_data['content'],
                user = request.user,
                ip = request.META['REMOTE_ADDR'])
            newmessage.save()
            return HttpResponseRedirect('/')
    else:
        form = MsgPostForm()
        variables = RequestContext(request,{'form':form})
        return render_to_response('msg_post_page.html',variables)

def user_msg_list_page(request,username):
    user = get_object_or_404(User,username=username)
    return list_detail.object_list(
        request,
        queryset=user.msg_set.order_by('-id'),
        paginate_by=ITEMS_PER_PAGE,
        template_name='user_msg_list_page.html',
        template_object_name='msg',
        extra_context={'username':username}
    )

def msg_detail_page(request,message_id):
    msg = get_object_or_404(Msg,id=message_id)
    msg.clickcount += 1
    msg.save()
    return list_detail.object_detail(
        request,
        queryset=Msg.objects.all(),
        object_id=message_id,
        template_name='msg_detail_page.html',
        template_object_name='msg'
    )