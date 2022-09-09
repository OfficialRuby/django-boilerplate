from allauth.account.signals import user_signed_up, user_logged_in
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up_signal_handler(request, **kwargs):
    user = kwargs.get('user')
    print(f'{user} Just Logged In')


@receiver(user_logged_in)
def user_signed_in_signal_handler(request, **kwargs):
    print('\n\n')
    print(request.user)
    print(kwargs.get('user'))
    print('\n\n')
