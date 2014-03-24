


from django.shortcuts import HttpResponse, render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from forms import RegistrationForm
from forms import AuthenticateForm
from forms import PostDonationForm
from django.contrib.auth.decorators import login_required
from models import UserProfile
from models import Post
from models import ProfileFeedback
from models import Message
from models import PostFeedback
from django.views.generic import ListView
from django.views.generic import View
from inspect import getmembers
from pprint import pprint









# Create your views here.



class IndexView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'


    def get_queryset(self, *args, **kwargs):
        return Post.objects.all()

    def get_context_data(self,**kwargs):

        context = super(IndexView, self).get_context_data(**kwargs)

        context['auth_form']  = kwargs.get('auth_form',None) or AuthenticateForm()

        return context








def index(request, auth_form = None):

    # if not request.user.is_authenticated():

    auth_form = auth_form or AuthenticateForm()

    # return IndexView.as_view()

    post_list =  Post.objects.all()


    # print(auth_form.error_messages())


    return render(request, 'home.html',{'post_list':post_list, 'user':request.user, 'auth_form':auth_form})


@login_required()
def my_donation_view(request):

    post_list = Post.objects.all().filter(user=request.user)

    return render(request, 'home.html',{'post_list':post_list, 'user':request.user})


def donation_view(request, auth_form = None):

    post_list = Post.objects.all().filter(post_type="make donation")

    return render(request, 'donations.html',{'post_list':post_list, 'user':request.user, 'auth_form':auth_form})


def request_donation_view(request, auth_form = None):

    post_list = Post.objects.all().filter(post_type="take donation")

    return render(request, 'requests.html',{'post_list':post_list, 'user':request.user, 'auth_form':auth_form})





def register(request,register_form=None):

    if request.method == "GET":

        # print(register_form)

        register_form = register_form or RegistrationForm()

        print(register_form)

        return render(request, 'register.html', {'register_form':register_form})

    if request.method == 'POST':

        register_form=RegistrationForm(data=request.POST)

        if register_form.is_valid():

            username = register_form.clean_username()
            password = register_form.clean_password2()

            register_form.save()

            user = authenticate(username=username, password=password)

            userprofile = UserProfile(user=user)

            userprofile.save()

            login(request,user)

            return redirect('/')

        else:

            return register(request,register_form=register_form)


def login_view(request):

    if request.method=="POST":
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return index(request, auth_form=form)
        else :
            return index(request, auth_form=form)

    return redirect('/')


@login_required()
def logout_view(request):
    logout(request)
    return redirect('/')




@login_required()
def post_donation_view(request, post_donation_form=None):
    post_donation_form = post_donation_form or PostDonationForm()
    return render(request,'post_donation.html',{'post_donation_form': post_donation_form })




@login_required()
def submit_donation_view(request):

    userprofile = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PostDonationForm(data=request.POST)

        if form.is_valid():
            post=form.save(commit=False)
            post.user=UserProfile(user=request.user)
            post.user_id= User.objects.get(username=request.user).pk
            print post.user_id
            post.save()
            # form.save_m2m()
            redirect('/')
        else :
            post_donation_view(request, form)
    # print request

    return redirect('/')


def post_detail_view(request,pk=1,auth_form=None):
    auth_form = auth_form or AuthenticateForm()
    post = Post.objects.get(pk=pk)
    return render(request,'donation_detail.html',{'post':post, 'user':request.user, 'auth_form': auth_form})


@login_required()
def profile_detail_view(request,username=None,auth_form=None):

    auth_form = auth_form or AuthenticateForm()
    user = User.objects.get(username=username)
    UserProfile.objects.get_or_create(user=user)
    profile = UserProfile.objects.get(user=user)
    profile_feedback = ProfileFeedback.objects.all().filter(user=user)

    return render(request, 'profile.html', {'profile':profile, 'user':request.user, 'auth_form': auth_form, 'profile_feedback': profile_feedback})


@login_required()
def my_profile(request):

    auth_form = AuthenticateForm()
    user = User.objects.get(username=request.user)
    UserProfile.objects.get_or_create(user=user)
    profile = UserProfile.objects.get(user=user)
    profile_feedback = ProfileFeedback.objects.all().filter(user=user)

    return render(request, 'my_profile.html', {'profile':profile, 'user':request.user, 'auth_form': auth_form, 'profile_feedback': profile_feedback})



def all_users_view(request,auth_form = None):

    auth_form = auth_form or AuthenticateForm()

    user_list = User.objects.all()

    return render(request, 'users.html', {'user_list':user_list, 'auth_form': auth_form})





def add_profile_feedback(request):

    # print('hic')
    #
    feedback=ProfileFeedback()
    #
    feedback.message=request.POST['message']
    feedback.feedback_sender=request.user or "Annonymous"
    feedback.user = User.objects.get(username=request.POST['profile'])

    feedback.save()


    # pprint(getmembers(feedback))
    return HttpResponse("success")

@login_required()
def my_messages(request):

    # print('hic')
    #
    messages = Message.objects.filter(Q(sender=User.objects.get(username=request.user)) | Q(receiver=request.user))
    auth_form = AuthenticateForm()

    profile=User.objects.all().get(username=request.user)




    return render(request, 'all_message.html', {'messages':messages, 'profile':profile, 'auth_form':auth_form })


from forms import UserProfileUpdateForm

@login_required()
def update(request):

    # print('hic')
    #
    auth_form = AuthenticateForm()
    update_form = UserProfileUpdateForm()
    return render(request, 'update.html', {'update_form':update_form, 'auth_form':auth_form })


def update_profile(request):



    pass




from django.db.models import Q

class send_message(View):

    def get(self, request, **kwargs):


        # print (request.user)
        # print (kwargs['receiver'])

        messages = Message.objects.filter(Q(sender=request.user, receiver=kwargs['receiver']) | Q(sender=User.objects.get(username=kwargs['receiver']), receiver=request.user))



        # print messages1
        # print messages2
        # print messages

        profile = User.objects.filter(username=kwargs['receiver'])[0]



        auth_form = AuthenticateForm()


        # print profile

        return render(request, 'message.html', {'messages':messages, 'profile':profile, 'auth_form':auth_form })



    def post(self, request, **kwargs):

        file = request.FILES.get('file')
        content = request.POST.get('message')
        sender = request.user
        message = Message()

        message.file=file


        print message.file

        message.content=content
        message.receiver = kwargs['receiver']
        message.sender=sender
        message.sender_full_name=User.objects.get(username=sender).get_full_name
        message.save()

        print message

        print message.file


        # print (request.user)

        messages = Message.objects.filter(Q(sender=request.user, receiver=kwargs['receiver']) | Q(sender=User.objects.get(username=kwargs['receiver']), receiver=request.user))


        profile = User.objects.filter(username=kwargs['receiver'])[0]

        # print profile

        auth_form = AuthenticateForm()

        return render(request, 'message.html', {'messages':messages, 'profile':profile ,'auth_form':auth_form})





