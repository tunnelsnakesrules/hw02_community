from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class ChangeForm(PasswordChangeForm):
    model = User
    fields = ('current_password', 'new_password', 'new_password_again')

class ResetForm(PasswordResetForm):
    model = User
    fields = ('email')

class PswResetConf(SetPasswordForm):
    model = User
    fields = ('new_password1', 'new_password2')

