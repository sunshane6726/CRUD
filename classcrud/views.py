from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView # 데이터 보여주기
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # 데이터추가
from .models import ClassBlog
# Create your views here.
# html 규약을 정해진대로 작성해야한다.
class BlogView(ListView): # html 템플릿 : 블로그 리스트를 담은 html : (소문자모델)_list.html
    template_name = 'classcrud/list.html'
    context_object_name = 'blog_list'
    model = ClassBlog

class BlogCreate(CreateView): # html : form(입력공간)을 갖고 있는 html :(소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DetailView): # html : 상세 페이지를 담은 html :(소문자모델)_detail.html
    context_object_name = 'blogpost'
    model = ClassBlog


class BlogUpdate(UpdateView): # html : 입력공간 : (소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView): # html : 지울꺼야? 하는 확인페이지를 담는다. html: (소문자모델)_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')

# defalut 값을 작성해야한다. ㄷㄷ 
