from django.shortcuts import render
from .models import UserProfile
from .forms import UserProfileForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .tables import UserProfileTable
from django_tables2 import RequestConfig
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden

# Create your views here.


def user_form_view(request):

  if request.user.is_staff or request.user.is_superuser:
     if request.method == 'POST':
         form = UserProfileForm(request.POST)
         if form.is_valid():
                 instance, created = UserProfile.objects.get_or_create(first_name=form.cleaned_data['first_name'],
                                                                       last_name=form.cleaned_data['last_name'],
                                                                       iban=form.cleaned_data['iban'])
                 instance.save()
                 messages.add_message(request,
                                      messages.SUCCESS,
                                      '%(instance)s was successfully added' % {'instance': instance})
                 return HttpResponseRedirect(reverse('user_form_view'))

     else:
         form = UserProfileForm()


     user_profile_table = UserProfileTable(UserProfile.objects.all())
     RequestConfig(request).configure(user_profile_table)

     return render(request, 'landing.html', {'form': form,
                                             'user_profile_table': user_profile_table,
                                             'objects': UserProfile.objects.all()
                                            }
                   )
  else:
      raise PermissionDenied


def delete_profile_view(request, pk=None):

    if request.user.is_staff or request.user.is_superuser:
        instance = get_object_or_404(UserProfile, pk=pk)
        instance.delete()
        messages.add_message(request,
                             messages.INFO,
                             '%(instance)s was successfully deleted' % {'instance': instance})

        return HttpResponseRedirect(reverse('user_form_view'))

    else:
        raise PermissionDenied


def update_profile_view(request, pk=None):

   if request.user.is_staff or request.user.is_superuser:
       instance = get_object_or_404(UserProfile, pk=pk)
       form = UserProfileForm(data=request.POST or None, instance=instance)

       if form.is_valid():
               form.save()
               messages.add_message(request,
                                messages.INFO,
                                '%(instance)s was successfully updated' % {'instance': instance})
               return HttpResponseRedirect(reverse('user_form_view'))

       return render(request, 'partials/modal_update.html', {'form': form,
                                                             'instance': instance
                                                            })
   else:
       raise PermissionDenied

