from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from user.models import User
from tag.models import Tag
from .models import Board
from .forms import BoardForm
# Create your views here.


# 정보를 얻는 디테일이 필요
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login/')
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            # id 가 생성됨.
            # 이 이후에 태그 추가 가능
            board.save()

            for tag in tags:
                # 태그 가져오기 - Tag.objects.get(조건)
                # 태그 생성 - a = Tag() 클래스 생성 a.save()
                if not tag:
                    continue

                # name=tag 조건을 일치하는 모델이 있으면 가져오고 없으면 생성
                # default = ('writer') 같은 조건 추가 가능
                # created 는 True or False
                _tag, created = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_list(request):
    # -id -> 최신 정보순
    all_boards = Board.objects.all().order_by('-id')
    # 페이지가 없으면 첫번째 페이지
    page = int(request.GET.get('p', 1))
    # 한페이지 두개씩 나오게 설정
    paginator = Paginator(all_boards, 2)
    boards = paginator.get_page(page)

    # boards 변수안에 페이지에 대한 모든 정보들이 들어있음
    return render(request, 'board_list.html', {'boards': boards})
