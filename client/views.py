from django.contrib import messages
from django.shortcuts import redirect
from client.models import payment_details

def index(request):
    return render(request,'home/index.html')

def client_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        registration(name=name, email=email,phone=phone,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request,'client/client_RL.html')
    return render(request,'client/client_RL.html')

def client_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = registration.objects.get(email=email, password=password)
            if s.approve:
                messages.info(request, "Client Login Successful")
                request.session['user_id'] = s.client_id
                print(request.session['user_id'])
                s.login = True
                s.logout = False
                s.save()
                return redirect("/client_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request, "client/client_RL.html")

        except registration.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request, "client/client_RL.html")



def client_logout(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        try:
            s = registration.objects.get(client_id=user_id)
            s.logout = True
            s.login = False
            s.save()
            del request.session['user_id']
            messages.success(request, 'Logout successful')
            return redirect('/')
        except registration.DoesNotExist:
            messages.error(request, 'User not found')

        request.session.pop('user_id', None)
    else:
        messages.info(request, 'Logout successful')

    return redirect('/')

def client_home(request):
    return render(request,"client/client_home.html")

def client_req(request):
    try:
        data = registration.objects.get(login=True)
        d = data.client_id
        p_data = requirements.objects.get(client_id=d)
        messages.info(request, "Record Already Uploaded!")
        return redirect("/client_home/")
    except:
        data=registration.objects.get(login=True)
        d=data.client_id
        if request.method=="POST":
            client_id=d
            antibiotics_name=request.POST['antibiotics_name']
            quantity=request.POST['quantity']
            bacteria=request.POST['bacteria']
            withdrawal_reason=request.POST['withdrawal_reason']
            chemical=request.POST['chemical']
            requirements(client_id=client_id, antibiotics_name=antibiotics_name,quantity=quantity,bacteria=bacteria,withdrawal_reason=withdrawal_reason,chemical=chemical).save()
            messages.info(request,f"{client_id} Requirement Upload Successful")
            return redirect("/client_home/")
        return render(request,'client/client_req.html',{'d':d})

def payment(request):
    client_id = None
    amount = None
    try:
        client = registration.objects.get(login=True)
        client_id = client.client_id
        amount = client.amount
        data1 = client.pay

    except registration.DoesNotExist:
        pass
    return render(request, 'client/payment.html', {'client_id': client_id, 'amount':amount,'data1':data1})

def process_payment(request):
    try:
        data = registration.objects.get(login=True)
        data1 = data.client_id
        data3 = data.amount
        if request.method == 'POST':
            client_id = data1
            amount = data3
            name = request.POST['name']
            cvv = request.POST['cvv']
            payment_details(client_id=client_id,amount=amount,name=name,cvv=cvv).save()

            a = registration.objects.get(login=True)
            a.pay = True
            a.save()
            messages.info(request, f"{client_id} Payment Successful")
            return redirect('/client_home/')
    except:
        messages.info(request, f"Amount No Yet Fixed by Admin!")
    return render(request, 'client/payment.html')


#
# def client_checkpoints(request):
#     try:
#         data = registration.objects.get(login=True)
#         client_id = data.client_id
#         data1 = requirements.objects.get(client_id=client_id)
#         return render(request, "client/client_checkpoints.html", {'data': data, 'data1': data1})
#     except:
#         messages.info(request, "Records Not Yet Uploaded")
#         return redirect('/client_home/')




from django.shortcuts import render, get_object_or_404
from .models import registration, requirements

def client_checkpoints(request):
    data = get_object_or_404(registration, login=True)
    client_id = data.client_id
    datas = data.pay
    data1 = requirements.objects.filter(client_id=client_id)
    return render(request, "client/client_checkpoints.html", {'data': data, 'data1': data1,'datas':datas})