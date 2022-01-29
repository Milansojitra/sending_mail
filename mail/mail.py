from django.conf import settings
from django.core.mail import send_mail


def mail_it(Subject, message, to):
    try:
        send_mail(Subject, message, settings.EMAIL_HOST_USER, [to], fail_silently=False)
        return "done"
    except Exception as e:
        return e