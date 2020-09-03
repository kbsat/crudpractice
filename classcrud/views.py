from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

# generice view는 템플릿의 이름이 정의되어있다.
# 만약 임의의 이름의 템플릿을 사용하려면 작업이 필요.


class BlogView(ListView):   # html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    model = ClassBlog
    # template_name = 'classcrud/list.html'
    context_object_name = 'blog_list'


class BlogCreate(CreateView):   # html : form ( 입력 공간 )을 갖고 있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']  # 입력받을 필드
    success_url = reverse_lazy('list')  # redirection 용
    # redirection으로 다른 방법으로 get_absoulute_url(), reverse() 등 배워두면 유용


class BlogDetail(DetailView):   # html : 상세페이지를 담은 html : (소문자모델)_detail.html
    model = ClassBlog


class BlogUpdate(UpdateView):   # html : form ( 입력 공간 )을 갖고 있는 html : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')


class BlogDelete(DeleteView):   # html : 경고메세지를 담은 html : (소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')
