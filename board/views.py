from django.shortcuts import render,redirect
from .models import Board,Comment
from django.http import Http404,HttpResponse
from django.core.paginator import Paginator
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from .forms import BoardForm,WriteForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required

# Create your views here.





def board_detail(request,pk):

    board = Board.objects.get(pk=pk)


    if request.method == 'POST':
        if str(request.user) == "AnonymousUser":
            return redirect('/login')
        Comment.objects.create(
            board = board,
            author = request.user,
            text=request.POST['text']

            )
        # print(board.pk)
        return redirect(f'/detail/{board.pk}')




    return render(request,'board_detail.html',{'board':board})

def comment_delete(request,pk):
    commen = Comment.objects.get(pk=pk)
    if commen.author == request.user:
        commen.delete()
        return redirect(f'/detail/{commen.board.id}')
    else:
        return redirect(f'/detail/{commen.board.id}')

@login_required
def board_write(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login/')

    if request.method == "POST":

        form = WriteForm(request.POST)
        if form.is_valid():
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = request.user
            board.save()

            return redirect('/list')
    else:
        form = BoardForm()
    return render(request,'board_write.html',{'form':form})

def board_list(request):

    all_board = Board.objects.all().order_by('-id')
    # comment_count = Comment.objects.filter()



    page = int(request.GET.get('p',1))
    paginator = Paginator(all_board,20)

    boards = paginator.get_page(page)

    return render(request,'board_list.html',{'boards':boards})


class boardUpdateView(UpdateView):
    model = Board
    form_class = BoardForm
    template_name = "board_update.html"
    success_url = reverse_lazy('list')

    def get_queryset(self):
        base_qs = super(boardUpdateView, self).get_queryset()
        return base_qs.filter(writer=self.request.user)


def board_delete(request,pk):
    boards = Board.objects.get(pk=pk)
    if boards.writer == request.user:
        boards.delete()
        return redirect('/list')
    else:
        return render(request,'registration/index.html')







# def search(request):
#     q = request.GET.get('q')
#
#     if q:
#         title = BoardDocument.search().query("match",title=q)
#
#     else:
#         boards = ' '
#
#     return render(request,'board_list.html',{'boards':title})