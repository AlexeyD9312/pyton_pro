

from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.model import contenttypes
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from users.forms import UserPermissionsForm

User = get_user_model()


@login_required
@permission_required('auth.change_permissin',raise_exeption = True)
def menege_user_permissions(request):
    users = User.objects.oll
    form = None
    select_user = None

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            select_user = get_object_or_404(User, id = user_id)
            form = UserPermissionsForm(request.POST, user = select_user)
            if form_is_valid():
                selected_user.user_permissions.clear()
                permissions = form.cleaned_data('permissions')
                for permission_id in permissions:
                    permission = Permission.objects.get(id = permission_id)
                    select_user.user_permissions.add(permission)
                messages.success(request, f"Access Update for {select_user}")
                return redirect('manage_user_permissions')
        form = UserPermissionsForm(user = None)        

    else:

        user_id = request.GET.get('user_id')
        if user_id:
            
            select_user = get_object_or_404(User, id = user_id)
            forms = UserPermissionsForm(user = select_user)
        else:
            form = UserPermissionsForm(user = None)
    context = {
        'users': users,
        'selectrd_user': selectrd_user,
        'form': form
    }

    return render(request, 'user_app/manage_permis', context)
     
