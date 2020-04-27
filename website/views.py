from django.shortcuts import render 
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def blog_details(request):
    return render(request, 'blog-details.html', {})


def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email
        send_mail(
            'a message from ' + message_name, # subject
            message, # message
            message_email, # from mail
            ['univreno@gmail.com', 'viralisting@gmail.com'], # To mail
        )

        return render(request, 'contact.html', {'message_name':  message_name })

    else:
        return render(request, 'contact.html', {}) 


def appointment(request):
    if request.method == 'POST':
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_day = request.POST['your-day']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']
        
        '''appointment_message = 'Name: ' + your_name + '\n' + 'Phone: ' + your_phone + '\n' + 'Email: ' + your_email + '\n' + 'Address: ' + your_address + '\n' + 'Day: ' + your_day + '\n' + 'Time: ' + your_time + '\n' + 'Message: ' + your_message
        # send an email
        send_mail(
            'Appointment Request', # subject
            appointment_message, # message
            your_email, # from mail
            ['univreno@gmail.com', 'viralisting@gmail.com'], # To mail
        )'''
        
        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_day': your_day,
            'your_time': your_time,
            'your_message': your_message,
        })

    else:
        return render(request, 'home.html', {}) 