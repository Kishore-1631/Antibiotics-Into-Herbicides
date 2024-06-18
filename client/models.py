from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    approve = models.BooleanField(null=True, default=False)
    reject = models.BooleanField(null=True, default=False)
    client_id = models.CharField(null=True, max_length=50)
    status=models.CharField(null=True,max_length=50, default="Pending")

    login = models.BooleanField(null=True, default=False)
    logout = models.BooleanField(null=True, default=False)

    #BioHerb Analysis
    bhadone = models.BooleanField(null=True, default=False)

    #BioQuotient Scan
    bqsdone = models.BooleanField(null=True, default=False)


    #HerbiConversion Nexus
    hcndone = models.BooleanField(null=True, default=False)

    finalreport = models.BooleanField(default=False)
    amount = models.CharField(null=True, max_length=10)
    pay = models.BooleanField(default=False, null=True)
    payamt= models.BooleanField(default=False, null=True)


class payment_details(models.Model):
    client_id=models.CharField(null=True, max_length=50)
    name=models.CharField(null=True, max_length=50)
    amount=models.PositiveBigIntegerField()
    cvv=models.PositiveBigIntegerField()

class requirements(models.Model):
    client_id = models.CharField(null=True, max_length=50)
    antibiotics_name = models.CharField(max_length=250)
    quantity = models.PositiveBigIntegerField()
    bacteria = models.CharField(max_length=250)
    withdrawal_reason = models.CharField(max_length=450)
    chemical=models.CharField(max_length=450,null=True)
    #BioHerb Analysis
    Dl= models.PositiveBigIntegerField(null=True)
    Du= models.PositiveBigIntegerField(null=True)
    Pl= models.PositiveBigIntegerField(null=True)
    Pu= models.PositiveBigIntegerField(null=True)
    target_weed= models.CharField(null=True, max_length=50)
    growth_of_treated_sample= models.PositiveBigIntegerField(null=True)
    growth_of_control_sample= models.PositiveBigIntegerField(null=True)
    IC50=models.PositiveBigIntegerField(null=True)
    growth_inhibition=models.PositiveBigIntegerField(null=True)
    hill_coefficient = models.PositiveBigIntegerField(null=True)
    confidence_interval= models.CharField(null=True, max_length=50)
    bioherb_analysis_plot = models.ImageField(upload_to='Bioherb_Analysis/', null=True)

    bha_approve=models.BooleanField(null=True, default=False)
    bha_reject = models.BooleanField(null=True, default=False)

    #BioQuotient Scan
    herbicide_concentration= models.PositiveBigIntegerField(null=True)
    average_weight= models.PositiveBigIntegerField(null=True)
    cell_viability= models.PositiveBigIntegerField(null=True)
    growth_inhibitions= models.PositiveBigIntegerField(null=True)
    reactive_oxygen_species= models.CharField(null=True, max_length=50)
    residual_activity= models.PositiveBigIntegerField(null=True)
    membrane_permeability= models.CharField(null=True, max_length=50)
    protein_folding= models.CharField(null=True, max_length=50)
    metabolic_activity= models.CharField(null=True, max_length=50)
    cellular_apoptosis= models.PositiveBigIntegerField(null=True)
    LD50=models.PositiveBigIntegerField(null=True)
    LD50_range= models.CharField(null=True, max_length=50)
    bioquotient_scan_plot = models.ImageField(upload_to='BioQuotient_Scan/', null=True)

    bqs_approve=models.BooleanField(null=True, default=False)
    bqs_reject = models.BooleanField(null=True, default=False)

    #HerbiConversion Nexus
    herbiconversion_pert = models.FloatField(null=True)

    antibiotic_candidate= models.CharField(null=True, max_length=250)
    target_weeds = models.CharField(null=True, max_length=250)
    mechanism_of_action_Herbicidal= models.CharField(null=True, max_length=250)
    stage_of_development= models.CharField(null=True, max_length=250)
    key_modifications= models.CharField(null=True, max_length=250)
    environmental_considerations= models.CharField(null=True, max_length=250)
    potential_challenges= models.CharField(null=True, max_length=250)
    materials_needed= models.CharField(null=True, max_length=250)
    duration= models.CharField(null=True, max_length=250)

    hcn_approve = models.BooleanField(null=True, default=False)
    hcn_reject = models.BooleanField(null=True, default=False)

    # FINAL Result
    final_report = models.FileField(upload_to='Final_Report/', null=True)
    report_view = models.BooleanField(null=True, default=False)

    finalreportapprove= models.BooleanField(null=True, default=False)
    finalreportreject= models.BooleanField(null=True, default=False)

    payamt = models.BooleanField(default=False, null=True)

    # BioHerb Analysis
    bhadone1 = models.BooleanField(null=True, default=False)

    # BioQuotient Scan
    bqsdone2 = models.BooleanField(null=True, default=False)

    # HerbiConversion Nexus
    hcndone3 = models.BooleanField(null=True, default=False)