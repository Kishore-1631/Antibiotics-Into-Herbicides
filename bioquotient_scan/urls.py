from django.urls import path
from bioquotient_scan import views
urlpatterns=[
    path('bioquotient_scan_RL/',views.bioquotient_scan_RL),
    path('bioquotient_scan_login/',views.bioquotient_scan_login),
    path('bioquotient_scan_logout/',views.bioquotient_scan_logout),
    path('bioquotient_home/',views.bioquotient_home),
    path('bioherb_report/',views.bioherb_report),
    path('bioquotient_scan/',views.bioquotient_scan),
    path('bqsresultprocess/<str:client_id>/',views.bqsresultprocess),
    path('outcome_visual/',views.outcome_visual)
]