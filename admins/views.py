import random
from django.contrib import messages
from django.shortcuts import render, redirect
from bioherb_analysis.models import employee
from client.models import registration, requirements

def admins_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=="admin" and password=="admin":
            messages.info(request,"Admin Login Successful")
            return redirect("/admins_home/")
        elif username !="admin" and password=="admin":
            messages.error(request, "Incorrect Username!")
            return render(request, 'admins/admins_login.html')
        elif username =="admin" and password!="admin":
            messages.error(request, "Incorrect Password!")
            return render(request, 'admins/admins_login.html')
        elif username !="admin" and password!="admin":
            messages.error(request, "Incorrect Username and Password!")
            return render(request, 'admins/admins_login.html')
        else:
            return render(request, 'admins/admins_login.html')
    return render(request, 'admins/admins_login.html')

def admins_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Admin Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Admin Logout successful')
        return redirect('/')

def admins_home(request):
    return render(request,'admins/admins_home.html')

def client_reg(request):
    data=registration.objects.all()
    return render(request,'admins/client_reg.html',{'data':data})

def approve(request, id):
    datas =registration.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.client_id = f"CLI-{p}"
    print(p)
    datas.approve = True
    datas.reject = False
    datas.save()
    messages.info(request, f"{datas.client_id} Approval Successful")
    return redirect('/admins_home/')

def reject(request, id):
    datas =registration.objects.get(id=id)
    datas.reject = True
    datas.approve = False
    datas.save()
    messages.info(request, "Client Registration Rejected")
    return redirect('/admins_home/')

#BioHerb Analysis
def bioherb_analysis_reg(request):
    data=employee.objects.filter(department="bioherb_analysis")
    return render(request,'admins/bioherb_analysis_reg.html',{'data':data})

def grant(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"BHA-{p}"
    print(p)
    d=datas.emp_id
    datas.grant = True
    datas.revoke = False
    datas.save()
    messages.info(request, f"{d} BioHerb Analysis Registration Approved Successfully")
    return redirect('/admins_home/')

def revoke(request, id):
    datas =employee.objects.get(id=id)
    datas.revoke = True
    datas.grant = False
    datas.save()
    messages.info(request, "BioHerb Analysis Registration Rejected")
    return redirect('/admins_home/')

#BioQuotient Scan
def bioquotient_scan_reg(request):
    data=employee.objects.filter(department="bioquotient_scan")
    return render(request,'admins/bioquotient_scan_reg.html',{'data':data})

def accept(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"BQS-{p}"
    print(p)
    d=datas.emp_id
    datas.accept = True
    datas.decline = False
    datas.save()
    messages.info(request, f"{d} BioQuotient Scan Registration Approved Successfully")
    return redirect('/admins_home/')

def decline(request, id):
    datas =employee.objects.get(id=id)
    datas.decline = True
    datas.accept = False
    datas.save()
    messages.info(request, "BioQuotient Scan Registration Rejected")
    return redirect('/admins_home/')


#HerbiConversion Nexus
def herbiconversion_nexus_reg(request):
    data=employee.objects.filter(department="herbiconversion_nexus")
    return render(request,'admins/herbiconversion_nexus_reg.html',{'data':data})

def admit(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"HCN-{p}"
    print(p)
    d=datas.emp_id
    datas.admit = True
    datas.deny = False
    datas.save()
    messages.info(request, f"{d} HerbiConversion Nexus Registration Approved Successfully")
    return redirect('/admins_home/')

def deny(request, id):
    datas =employee.objects.get(id=id)
    datas.deny = True
    datas.admit = False
    datas.save()
    messages.info(request, "HerbiConversion Nexus Registration Rejected")
    return redirect('/admins_home/')


#BioHerb Analysis Report
def bioherb_analysis_report(request):
    data = requirements.objects.all()
    return render(request,r'admins\bioherb_analysis_report.html',{'data':data})

def bha_approve(request, client_id):
    datas = requirements.objects.get(client_id=client_id)
    datas.bha_approve = True
    datas.bha_reject = False
    datas.save()
    messages.info(request, f"{datas.client_id} BioHerb Analysis Report Approved Successfully")
    return redirect('/admins_home/')

#BioQuotient Scan
def bioquotient_scan_report(request):
    data = requirements.objects.all()
    return render(request,r'admins\bioquotient_scan_report.html',{'data':data})

def bqs_approve(request, client_id):
    datas = requirements.objects.get(client_id=client_id)
    datas.bqs_approve = True
    datas.bqs_reject = False
    datas.save()
    messages.info(request, f"{datas.client_id} BioQuotient Scan Report Approved Successfully")
    return redirect('/admins_home/')


#Herbiconversion Nexus
def herbiconversion_nexus_report(request):
    data = requirements.objects.filter(hcndone3 = True)
    return render(request,r'admins\herbiconversion_nexus_report.html',{'data':data})

def hcn_approve(request, client_id):
    datas = requirements.objects.get(client_id=client_id)
    datas.hcn_approve = True
    datas.hcn_reject = False
    datas.save()
    d = registration.objects.get(client_id=client_id)
    d.status = "Awaiting Admin Authorization"
    d.save()
    messages.info(request, f"{datas.client_id} HerbiConversion Nexus Report Approved Successfully")
    return redirect('/admins_home/')

def report_view(request):
    data=requirements.objects.filter(hcn_approve = True)
    return render(request,"admins/final_report.html",{'data':data})


#Final Report
from django.core.files.base import ContentFile
def view_final_report(request, client_id):
    data = requirements.objects.get(client_id=client_id)

    title = "ANTIBIOTICS FAILURE INTO HERBICIDES"
    list_data = [
        f"Client.ID: {data.client_id}",
        "----------------------------------------------------",
        "REQUIREMENT ANALYSIS\n"
        "----------------------------------------------------",
        f"Antibiotics Name: {data.antibiotics_name}",
        f"Quantity: {data.quantity}",
        f"Bacteria : {data.bacteria}",
        f"Withdrawal Reason: {data.withdrawal_reason}",
        f"Chemical: {data.chemical}",
        "----------------------------------------------------",
        "BIOHERB ANALYSIS\n"
        "----------------------------------------------------",
        f"Dl: {data.Dl}",
        f"Du: {data.Du}",
        f"Pl: {data.Pl}",
        f"Pu: {data.Pu}",
        f"Target Weed: {data.target_weed}",
        f"Growth-Treated Sample: {data.growth_of_treated_sample}",
        f"Growth-Control Sample: {data.growth_of_control_sample}",
        f"IC50: {data.IC50}",
        f"Growth Inhibition: {data.growth_inhibition}",
        f"Hill Coefficient: {data.hill_coefficient}",
        f"Confidence Interval: {data.confidence_interval}",

        "----------------------------------------------------",
        "BIOQUOTIENT SCAN\n"
        "----------------------------------------------------",

        f"Herbicide Concentration: {data.herbicide_concentration}",
        f"Average Weight: {data.average_weight}",
        f"Cell Viability: {data.cell_viability}",
        f"Growth Inhibitions: {data.growth_inhibitions}",
        f"Reactive Oxygen Species: {data.reactive_oxygen_species}",
        f"Residual Activity: {data.residual_activity}",
        f"Membrane Permeability: {data.membrane_permeability}",
        f"Protein Folding: {data.protein_folding}",
        f"Metabolic Activity: {data.metabolic_activity}",
        f"Cellular Apoptosis: {data.cellular_apoptosis}",
        f"LD50: {data.LD50}",
        f"LD50 Range: {data.LD50_range}",

        "----------------------------------------------------",
        "HerbiConversion Nexus\n"
        "----------------------------------------------------",

        f"Herbiconversion Percentage Prediction: {data.herbiconversion_pert}",
        f"Antibiotic candidate: {data.antibiotic_candidate}",
        f"Target Weeds: {data.target_weeds}",
        f"Mechanism: {data.mechanism_of_action_Herbicidal}",
        f"Stage of Developement: {data.stage_of_development}",
        f"Key Modification: {data.key_modifications}",
        f"Environmental Considerations: {data.environmental_considerations}",
        f"Potential Challenges: {data.potential_challenges}",
        f"Materials Need: {data.materials_needed}",
        f"Duration: {data.duration}",

    ]
    content = f"{title}\n\n" + '\n'.join(list_data)

    file_content = ContentFile(content.encode('utf-8'))
    data.final_report.save(f"{title}_{data.client_id}.txt", file_content)
    data.report_view=True
    data.save()

    messages.info(request,"Report Generated Successfully")
    return redirect('/report_view/')


def finalreportapprove(request, client_id):
    datas = requirements.objects.get(client_id=client_id)
    datas.finalreportapprove = True
    datas.finalreportreject = False
    datas.save()
    data=registration.objects.filter(client_id=client_id)
    for i in data:
        i.status="Admin Approval Authorized"
        i.finalreport=True
        i.save()
    messages.info(request, f"{datas.client_id} Antibiotics Failure into Herbicides Report Approved Successfully")
    return redirect('/admins_home/')

import os
import pyttsx3
from django.shortcuts import redirect
def read(request, client_id):
    try:
        data = requirements.objects.get(client_id=client_id)
        title = "ANTIBIOTICS_FAILURE_INTO_HERBICIDES"
        file_name = f"{title}_{data.client_id}.txt"
        file_path = os.path.join(r'C:\FinalYearProject\source\AI - Herbicides\Herbicide\media\Final_Report', file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()
        speaker = pyttsx3.init()
        speaker.say(text_content)
        speaker.runAndWait()
        return redirect('/report_view/')
    except:
        print("Loop Running")
    return redirect('/report_view/')


def payslip(request):
    data=requirements.objects.filter(finalreportapprove=True)
    return render(request,'admins/payslip.html',{'data':data})


def invoice(request,client_id):
    d=registration.objects.get(client_id=client_id)

    if request.method == 'POST':
        amount=request.POST['amount']
        d.amount=amount
        d.status="Make Payment"
        d.payamt=True
        d.save()
        e = requirements.objects.get(client_id=client_id)
        e.payamt = True
        e.save()
        messages.info(request, f"Payslip sent to {client_id} successfully")
        return render(request, 'admins/payslip.html')
    return render(request,'admins/payslip.html')