from django.contrib import messages
from django.shortcuts import render,redirect
from bioherb_analysis.models import employee
from client.models import requirements,registration
from django.core.files.base import ContentFile
from io import BytesIO
import matplotlib.pyplot as plt

def bioquotient_scan_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "bioquotient_scan/bioquotient_scan_RL.html")
    return render(request,"bioquotient_scan/bioquotient_scan_RL.html")

def bioquotient_scan_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)

            if s.accept:
                messages.info(request, "BioQuotient Scan Login Successful")

                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/bioquotient_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request,"bioquotient_scan/bioquotient_scan_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request,"bioquotient_scan/bioquotient_scan_RL.html")


def bioquotient_scan_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')

def bioquotient_home(request):
    return render(request,'bioquotient_scan/bioquotient_home.html')

def bioherb_report(request):
    data=requirements.objects.filter(bha_approve=True )
    return render(request,"bioquotient_scan/bioherb_report.html",{'data':data})

def bioquotient_scan(request):
    data=requirements.objects.filter(bha_approve=True )
    return render(request,"bioquotient_scan/bioquotient_scan.html",{'data':data})

import pandas as pd
def bqsresultprocess(request, client_id):
    data = requirements.objects.filter(client_id=client_id)
    csv_path = r'C:\FinalYearProject\source\AI - Herbicides\Herbicide\LD50.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        for i in data:
            if (i.antibiotics_name) == (row['failed_antibiotics']):
                i.herbicide_concentration = row['herbicide_concentration']
                i.average_weight = row['average_weight']
                i.cell_viability = row['cell_viability']
                i.growth_inhibitions = row['growth_inhibition']
                i.reactive_oxygen_species = row['reactive_oxygen_species']
                i.residual_activity = row['residual_activity']
                i.membrane_permeability = row['membrane_permeability']
                d=i.herbicide_concentration/i.average_weight*100
                i.LD50=d
                i.protein_folding = row['protein_folding']
                i.metabolic_activity =row['metabolic_activity']
                i.cellular_apoptosis =row['cellular_apoptosis']
                if i.LD50>50:
                    i.LD50_range="Low Toxocity"
                elif i.LD50==50:
                    i.LD50_range = "Moderate Toxocity"
                else:
                    i.LD50_range = "High Toxocity"
                i.save()

                # Plotting
                plt.plot(['Herbicide Concentration', 'Average Weight', 'LD50'],
                         [i.herbicide_concentration, i.average_weight, i.LD50],
                         marker='o', linestyle='--', color='r')

                plt.title('BioHerb Analysis')
                plt.xlabel('Parameters')
                plt.ylabel('Values')

                for j, txt in enumerate([i.herbicide_concentration, i.average_weight,i.LD50]):
                    plt.annotate(f'{txt:.2f}', (j, txt), textcoords="offset points", xytext=(0, 10), ha='center')

                # Saving the plot
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                i.bioquotient_scan_plot.save('bioquotient_scan.png', ContentFile(buffer.getvalue()))
                i.save()
    d = registration.objects.get(client_id=client_id)
    d.bqsdone = True
    d.save()
    data1 = requirements.objects.get(client_id=client_id)
    data1.bqsdone2 = True
    data1.save()

    messages.info(request, f"BioQuotient Scan Processed Successfully for {client_id}")
    return render(request, r'bioquotient_scan\bioquotient_scan.html')

def outcome_visual(request):
    data=requirements.objects.all()
    return render(request,"bioquotient_scan/outcome_visual.html",{'data':data})