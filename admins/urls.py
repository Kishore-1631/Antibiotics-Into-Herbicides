
from django.urls import path
from admins import views

urlpatterns = [
    path('admins_login/', views.admins_login),
    path('admins_logout/',views.admins_logout),
    path('admins_home/', views.admins_home),
    path('client_reg/', views.client_reg),
    path('approve/<int:id>/', views.approve),
    path('reject/<int:id>/', views.reject),
    path('bioherb_analysis_reg/',views.bioherb_analysis_reg),
    path('grant/<int:id>/', views.grant),
    path('revoke/<int:id>/', views.revoke),
    path('bioquotient_scan_reg/',views.bioquotient_scan_reg),
    path('accept/<int:id>/', views.accept),
    path('decline/<int:id>/', views.decline),
    path('herbiconversion_nexus_reg/',views.herbiconversion_nexus_reg),
    path('admit/<int:id>/', views.admit),
    path('deny/<int:id>/', views.deny),
    path('bioherb_analysis_report/',views.bioherb_analysis_report),
    path('bha_approve/<str:client_id>/',views.bha_approve),
    path('bioquotient_scan_report/',views.bioquotient_scan_report),
    path('bqs_approve/<str:client_id>/',views.bqs_approve),
    path('herbiconversion_nexus_report/', views.herbiconversion_nexus_report),
    path('hcn_approve/<str:client_id>/', views.hcn_approve),
    path('report_view/',views.report_view),
    path('view_final_report/<str:client_id>/',views.view_final_report),
    path('finalreportapprove/<str:client_id>/',views.finalreportapprove),
    path('read/<str:client_id>/',views.read),
    path('payslip/',views.payslip),
    path('invoice/<str:client_id>/',views.invoice)




]
