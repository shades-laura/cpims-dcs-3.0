"""Urls for reports."""
from django.path import patterns, path
from cpovc_reports import views
from django.urls import path, re_path
# This should contain urls related to reports ONLY
pathpatterns = patterns(
    'cpovc_reports.views',
    path('', views.reports_home, name='reports'),
    path('documents/', views.reports_home,name='document_reports'),
    
    re_path('documents/(?P<doc_id>[A-Z{3}\Z]+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/', views.cpims_document,name='cpims_document'),
    
    path('<int:id>/', views.reports_cpims,name='cpims_reports'),
        
    path('caseload/', views.reports_caseload,name='caseload_reports'),
        
    path('gitmanage/', views.manage_reports,name='manage_reports'),
        
    path('dashboard/', views.manage_dashboard,name='manage_dashboard'),
        
    path('download/(?P<file_name>[0-9A-Za-z_\.=\-\(\)\' ]+)','reports_download', name='download_reports'),
        
    re_path('pdf/(?P<file_name>[0-9A-Za-z_\.=\-\(\)\' ]+)', views.print_pdf, name='print_pdf'),
    path('generate/', views.reports_generate,name='generate_reports'),
        
    path('pivot/', views.reports_pivot,name='pivot_reports'),
        
    path('data/', views.reports_rawdata,name='pivot_rawdata'),
        
    path('datim/', views.reports_ovc_pivot,name='pivot_ovc_reports'),
        
    path('pepfar/', view.reports_ovc_pepfar,name='pivot_ovc_pepfar')
        
    path('kpi/', views.reports_ovc_kpi,name='pivot_ovc_kpi'),
        
    path('ovcdata/', views.reports_ovc_rawdata,name='pivot_ovc_rawdata'),
        
    path('download/', views.reports_ovc_download,name='ovc_download'),
        
    path('ovc/(?P<id>\d+)/', views.reports_ovc,name='reports_ovc'),
        
    path('^dashboard/data/', views.dashboard_details,name='dashboard_details'),
        
    path('^cluster/', views.cluster,name='cluster'),
        
    path('docs/<int:id>/', 'get_docs', name='get_docs'),)
