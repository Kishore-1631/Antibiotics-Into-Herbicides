from django.contrib import messages
from django.shortcuts import render,redirect
from sklearn.model_selection import train_test_split

from bioherb_analysis.models import employee
from client.models import requirements, registration


def herbiconversion_nexus_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "herbiconversion_nexus/herbiconversion_nexus_RL.html")
    return render(request,"herbiconversion_nexus/herbiconversion_nexus_RL.html")

def herbiconversion_nexus_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)

            if s.admit:
                messages.info(request, "HerbiConversion Nexus Login Successful")

                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/herbiconversion_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request,"herbiconversion_nexus/herbiconversion_nexus_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request,"herbiconversion_nexus/herbiconversion_nexus_RL.html")


def herbiconversion_nexus_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'HerbiConversion Nexus Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'HerbiConversion Nexus Logout successful')
        return redirect('/')

def herbiconversion_home(request):
    return render(request,'herbiconversion_nexus/herbiconversion_home.html')

def bioquotient_report(req):
    data=requirements.objects.filter(bqs_approve=True)
    return render(req,"herbiconversion_nexus/bioquotient_scan_report.html",{'data':data})

def herbi_conversion(req):
    data=requirements.objects.filter(bqs_approve=True)
    return render(req,"herbiconversion_nexus/herbi_conversion.html",{'data':data})



from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

def herbi_conversion_process(request, client_id):
    con = requirements.objects.get(client_id=client_id)
    IC50 = con.IC50
    growth_inhibition = con.growth_inhibition
    LD50 = con.LD50
    growth_inhibitions = con.growth_inhibitions

    file_path = r'C:\FinalYearProject\source\AI - Herbicides\Herbicide\Herbi Testing.csv'

    dataset = pd.read_csv(file_path)

    X = dataset[['IC50', 'growth_inhibition', 'LD50', 'growth_inhibitions']]
    y = dataset['herbiconversion']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    svr_regressor = SVR(kernel='linear')
    svr_regressor.fit(X_train, y_train)
    input_data = pd.DataFrame([[IC50, growth_inhibition, LD50, growth_inhibitions]],
                              columns=['IC50', 'growth_inhibition', 'LD50', 'growth_inhibitions'])
    prediction = svr_regressor.predict(input_data)
    print(prediction)
    mse = mean_squared_error(y_test, svr_regressor.predict(X_test))
    print(f'Mean Squared Error: {mse}')
    fprediction = float(round(prediction[0], 2))
    print('fprediction', fprediction)



    csv_path = r'C:\FinalYearProject\source\AI - Herbicides\Herbicide\Herbicide Conversion.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():

        print("1",con.antibiotics_name)
        print("2",row['failed_antibiotics'])
        if (con.antibiotics_name) == (row['failed_antibiotics']):
            con.antibiotic_candidate = row['antibiotic_candidate']
            con.target_weeds = row['target_weeds']
            con.mechanism_of_action_Herbicidal = row['mechanism_of_action_Herbicidal']
            con.stage_of_development = row['stage_of_development']
            con.key_modifications = row['key_modifications']
            con.environmental_considerations = row['environmental_considerations']
            con.potential_challenges = row['potential_challenges']
            con.materials_needed = row['materials_needed']
            con.duration = row['duration']
            con.save()

    con.herbiconversion_pert = fprediction
    con.save()

    d = registration.objects.get(client_id=client_id)
    d.hcndone = True
    d.save()
    data1 = requirements.objects.get(client_id=client_id)
    data1.hcndone3 = True
    data1.save()

    messages.success(request, f'HerbiConversion Analysed Successfully for {client_id}')
    return redirect('/herbi_conversion/')


def wrap_up_report(request):
    data=requirements.objects.all()
    return render(request,"herbiconversion_nexus/wrap_up_report.html",{'data':data})