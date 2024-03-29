from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
from board.models import Board,Comment
from django.core.paginator import Paginator
from .forms import RegisterForm


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {'parm1': 'hello', 'parm2': 'django', 'auth': request.user.is_authenticated}
        print(request.user)
        return render(request, 'registration/index.html', context=context)


@login_required
def profile(request):
    myboards = Board.objects.filter(writer=request.user).order_by('-id')
    mycomments = Comment.objects.filter(author=request.user).order_by('-id')

    page = int(request.GET.get('p', 1))
    paginator = Paginator(myboards, 5)

    boards = paginator.get_page(page)

    pages = int(request.GET.get('p', 1))
    paginators = Paginator(mycomments, 5)

    comments = paginators.get_page(pages)

    return render(request, 'registration/profile.html',{'myboards':boards,'mycomments':comments})


def register(request):

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()

    return render(request, 'registration/register.html',{'form':user_form})