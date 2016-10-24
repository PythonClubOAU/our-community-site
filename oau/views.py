from django.shortcuts import render
from .forms import ContactForm, UserForm
from .models import Event, Member
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context


def queries(query_for):
    if query_for not in ['member', 'event']:
        return False
    else:
        if query_for == "member":
            member_list = Member.objects.get(display_image=True)
            if not member_list:
                return False
            else:
                return member_list
        else:
            if query_for == "event":
                club_list = Event.objects.get(event="PYT")
                general_list = Event.objects.get(event="GEN")
                if not club_list and not general_list:
                    return False
                else:
                    return club_list, general_list


def handle_uploaded_file(file):
    with open(file, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def index(request):
    form = ContactForm()
    userform = UserForm()
    members = queries('members')
    # club_events, general_events = queries('events')
    if request.method == 'POST':
        if request.POST['contact'] == "contact":
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                context = Context({
                    "name": form.cleaned_data['name'],
                    "email": form.cleaned_data['email'],
                    "message": form.cleaned_data['message']
                })
                email_message = get_template('ClubPython/contact_email.html').render(context)
                send_mail(settings.EMAIL_MESSAGE['email_subject_for_contact'], email_message, settings.EMAIL_HOST_USER,
                          settings.TO_EMAILS, fail_silently=False)
                message = settings.MESSAGES['successful_contact']
                return render(request, 'ClubPython/index.html', {'form': form, 'message': message})
            else:
                error = settings.MESSAGES['error_message_for_registration']
                return render(request, 'ClubPython/index.html', {'form': form, 'error': error})
        else:
            userform = UserForm(request.POST, request.FILES)
            if userform.is_valid():
                userform.save()
                context = Context({
                    "name": userform.cleaned_data['name'],
                    "email": userform.cleaned_data['email'],
                    "message": userform.cleaned_data['message']
                })
                email_message = get_template('ClubPython/registration_email.html').render(context)
                send_mail(settings.EMAIL_MESSAGE['email_subject_for_contact'], email_message, settings.EMAIL_HOST_USER,
                          settings.TO_EMAILS, fail_silently=False)
                message = settings.MESSAGES['successful_registration']
                return render(request, 'ClubPython/index.html', {'userform': userform, 'message': message})
            else:
                error = settings.MESSAGES['error_message_for_contact']
                return render(request, 'ClubPython/index.html', {'form': form, 'error': error})

    return render(request, 'ClubPython/index.html', {'form': form,'members': members, 'userform': userform})
