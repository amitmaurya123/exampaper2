from django.conf.urls import url
from basic_app import views
urlpatterns=[

    url(r'^register/$',views.register,name='register'),

    url(r'^$',views.ExamListView.as_view(),name='exam_list'),
    url(r'^upload_file/',views.UploadPaper.as_view(),name='upload_paper'),
    url(r'^about/',views.AboutView.as_view(),name='about'),
    url(r'^pdf/(?P<pk>\d+)/download/$', views.download_item, name='pdf_download'),
    #url(r'^cv/pdfs/(?P<filename>)/$', 'views.pdf_download',name="pdf_download"),
    #('ques_detail/<int:pk>/',views.ques_detail,name='ques_detail')
    url(r'^drafts/paper/$', views.DraftListView.as_view(), name='paper_draft_list'),
    url(r'^paper/(?P<pk>\d+)/publish/$', views.paper_publish, name='paper_publish'),
    url(r'^paper/(?P<pk>\d+)/remove/$', views.ExamDeleteView.as_view(), name='paper_remove'),
    url(r'^paper/(?P<pk>\d+)/edit/$', views.ExamUpdateView.as_view(), name='paper_edit'),

    url(r'^try/$',views.tryit,name='try'),

    url(r'^show/(?P<branch>[-\w]+)/(?P<semester>\d+)/$',views.PrescisedListView.as_view(),name='show_precised_list'),

]
