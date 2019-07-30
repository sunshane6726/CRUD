from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog
# Create your views here.

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs': blogs})

def create(request):
    # 새로운 데이터 새로운 블로그 글을 저장하는 역할 REQUEST== POST
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False) # 아직 저장 x timezone 후에 save() 저장
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    # 글쓰기 페이지를 띄어주는 역할  == GET (REQUEST) !== POST
    
    else:
        # 단순히 입력받을 수 있는 form을 띄워주라
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form': form })

def update(request, pk):
    # 어떤 블로그를 수정할지 블로그 객체를 갖고 오기
    blog = get_object_or_404(Blog, pk = pk)
    # 해당하는 블로그 객체 pk 에 맞는 입력공간
    form = NewBlog(request.POST, instance=blog) # 두번째 인자 instance => pk 번째에 해당하는 객체를 입력하는 공간
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'viewcrud/new.html', {'form': form})

def delete(request, pk):
    blog = get_object_or_404(Blog,pk = pk )
    blog.delete()
    return redirect('home')
