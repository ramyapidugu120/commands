# scheduler/tasks.py
from django.core.mail import send_mail
# import logging

# logger = logging.getLogger(__name__)

def send_daily_email():
    send_mail(
        'Daily Update',
        'This is your daily update email.',
        'piduguramya14e@gmail.com',         # Replace with your "from" email
        ['piduguramya14e@gmail.com'],         # Replace with your recipient list
        fail_silently=False,
    )
    # logger.info("Daily email sent.")
