# from __future__ import absolute_import,unicode_literals
# from django.core.mail import EmailMessage
# from bauss.celery import app

# @app.task(name='celery_verify_email', bind=True)
# def celery_verify_email(self,mail_subject, html_message,to_email):
#     try:
#         message = EmailMessage(mail_subject, html_message,  to=[to_email])
#         message.content_subtype = 'html' # this is required because there is no plain text email message
#         message.send()
#     except:
#         pass