from django.shortcuts import render, redirect

from django.http import HttpResponse

# importing our forms
from .forms import CreateUserForm, LoginForm, NotePostForm, NoteUpdateForm, UpdateUserForm

from django.contrib.auth.models import auth

from django.contrib.auth import authenticate

# login_required decorator that is used to protect routes
from django.contrib.auth.decorators import login_required

# import for django messages
from django.contrib import messages

# import model
from .models import Notes

# home view


def home(request):
    return render(request, 'index.html')


# - Register

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your account was created Successfully.")
            return redirect('my-login')

    context = {'form': form}

    return render(request, 'register.html', context)


# - login

def my_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            # if the form is valid we want
            # to get the user and authenticate
            # that user.
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'my-login.html', context=context)


# - Dashboard
# (@login_required) will protect the route
# make sure the user is authenticated before
# they can access their dashboard. They will
# be redirected to the my-login url if not
# authenticated.
@login_required(login_url='my-login')
def dashboard(request):
    return render(request, 'profile/dashboard.html')


# - logout

def user_logout(request):
    auth.logout(request)
    return redirect('my-login')


@login_required(login_url='my-login')
def post_notes(request):
    form = NotePostForm()

    if request.method == "POST":
        form = NotePostForm(request.POST)

        if form.is_valid():
            # the trick is in this case we also want
            # to send our foreign key. commit=False
            # will hold off on saving until we do a
            # specific thing, in this case getting our
            # user instance.
            note = form.save(commit=False)

            note.user = request.user
            # so now after setting the user we can save
            note.save()

            return redirect('my-notes')

    context = {'form': form}

    return render(request, 'profile/post-notes.html', context=context)


@login_required(login_url='my-login')
def my_notes(request):

    current_user = request.user.id
    notes = Notes.objects.all().filter(user=current_user)
    context = {'notes': notes}

    return render(request, 'profile/my-notes.html', context=context)


@login_required(login_url='my-login')
def update_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NoteUpdateForm(instance=note)

    if request.method == 'POST':
        form = NoteUpdateForm(request.POST, instance=note)

        if form.is_valid():
            form.save()

            return redirect('my-notes')

    context = {'form': form}

    return render(request, 'profile/update-note.html', context=context)


@login_required(login_url='my-login')
def delete_note(request, pk):
    note = Notes.objects.get(id=pk)

    if request.method == 'POST':
        note.delete()

        return redirect('my-notes')

    # context = {'note': note}
    return render(request, 'profile/delete-note.html')


@login_required(login_url='my-login')
def profile_management(request):
    form = UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'profile/profile-management.html', context=context)
