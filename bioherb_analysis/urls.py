from django.urls import path
from bioherb_analysis import views
urlpatterns=[
    path('bioherb_analysis_RL/',views.bioherb_analysis_RL),
    path('bioherb_analysis_home/', views.bioherb_analysis_home),
    path('bioherb_analysis_login/',views.bioherb_analysis_login),
    path('bioherb_analysis_logout/',views.bioherb_analysis_logout),
    path('outlook_requisites/',views.outlook_requisites),
    path('actionable_requisites/',views.actionable_requisites),
    path('bharesultprocess/<str:client_id>/',views.bharesultprocess),
    path('inspect_findings/',views.inspect_findings)
]