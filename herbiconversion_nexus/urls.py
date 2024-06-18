from django.urls import path
from herbiconversion_nexus import views
urlpatterns=[
    path('herbiconversion_nexus_RL/',views.herbiconversion_nexus_RL),
    path('herbiconversion_nexus_login/',views.herbiconversion_nexus_login),
    path('herbiconversion_nexus_logout/',views.herbiconversion_nexus_logout),
    path('herbiconversion_home/',views.herbiconversion_home),
    path('bioquotient_report/',views.bioquotient_report),
    path('herbi_conversion/',views.herbi_conversion),
    path('herbi_conversion_process/<str:client_id>/',views.herbi_conversion_process),
    path('wrap_up_report/',views.wrap_up_report)
]