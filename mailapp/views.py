from django.shortcuts import render

# Create your views here.

import csv
from django.shortcuts import render
from django.core.mail import send_mail

def logout(request):
    auth.logout(request)
    return render(request, 'newhomepage.html')
def send_emails(request):
    csv_file_path = r'Z:\pfsd\djangoproject\DjangoProject\TTM\static'
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            recipient_email = row['email']
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here
            send_mail(
                subject,
                message_body,
                'chaitu2514@gmail.com'
                [recipient_email],
                fail_silently=False,
            )
            print(f'Sent email to {recipient_email}')
    return render(request, 'Emails_sent_successfully.html')
