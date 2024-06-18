from django.shortcuts import render, redirect
from bioherb_analysis.models import *

from django.contrib import messages
from django.core.files.base import ContentFile
from io import BytesIO
import matplotlib.pyplot as plt


# Create your views here.
from client.models import requirements, registration


def bioherb_analysis_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "bioherb_analysis/bioherb_analysis_RL.html")
    return render(request,"bioherb_analysis/bioherb_analysis_RL.html")

def bioherb_analysis_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)

            if s.grant:
                messages.info(request, "BioHerb Analysis Login Successful")

                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/bioherb_analysis_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request,"bioherb_analysis/bioherb_analysis_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request,"bioherb_analysis/bioherb_analysis_RL.html")


def bioherb_analysis_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')

def bioherb_analysis_home(request):
    return render(request,'bioherb_analysis/bioherb_home.html')

def outlook_requisites(request):
    data = requirements.objects.all()
    return render(request,'bioherb_analysis\outlook_requisites.html',{'data':data})

def actionable_requisites(request):
    data = requirements.objects.all()
    return render(request,r'bioherb_analysis\actionable_requisites.html',{'data':data})

import pandas as pd
def bharesultprocess(request, client_id):
    data = requirements.objects.filter(client_id=client_id)
    csv_path = r'C:\FinalYearProject\source\AI - Herbicides\Herbicide\IC50 and Growth Inhibition.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        for i in data:
            if (i.antibiotics_name) == (row['failed_antibiotics']):
                i.Dl = row['Dl']
                i.Du = row['Du']
                i.Pl = row['Pl']
                i.Pu = row['Pu']
                i.target_weed = row['target_weed']
                i.growth_of_treated_sample = row['growth_of_treated_sample']
                i.growth_of_control_sample = row['growth_of_control_sample']
                d=i.Dl+(i.Dl-i.Du) * (50-i.Pl)/(i.Pl-i.Pu)
                i.IC50=d
                e=i.growth_of_control_sample - i.growth_of_treated_sample
                i.growth_inhibition=e
                i.hill_coefficient = row['hill_coefficient']
                i.confidence_interval =row['confidence_interval']
                i.save()

                # Plotting
                plt.plot(['Dl', 'Du', 'Pl', 'Pu','IC50'],
                         [i.Dl, i.Du, i.Pl,
                          i.Pu,i.IC50],
                         marker='o', linestyle='--', color='g')

                plt.title('BioHerb Analysis')
                plt.xlabel('Parameters')
                plt.ylabel('Values')

                for j, txt in enumerate([i.Dl, i.Du,
                                         i.Pl, i.Pu,i.IC50]):
                    plt.annotate(f'{txt:.2f}', (j, txt), textcoords="offset points", xytext=(0, 10), ha='center')

                # Saving the plot
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                i.bioherb_analysis_plot.save('bioherb_analysis.png', ContentFile(buffer.getvalue()))
                i.save()
    d=registration.objects.get(client_id=client_id)
    d.bhadone=True
    d.save()
    data1 = requirements.objects.get(client_id=client_id)
    data1.bhadone1=True
    data1.save()
    messages.info(request, f"Requisites Processed Successfully for {client_id}")
    return render(request, r'bioherb_analysis\actionable_requisites.html')




def inspect_findings(request):
    data = requirements.objects.filter(bhadone1=True)
    return render(request,'bioherb_analysis\inspect_findings.html',{'data':data})
