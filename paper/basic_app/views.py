from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from basic_app.models import Exam
from basic_app.forms import ExamForm
from django.http import HttpResponse
from django.http import FileResponse, HttpResponseRedirect,HttpResponse
from django.utils.text import slugify
import os,re
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.utils import timezone
from basic_app.forms import UserForm,ExamForm
from django.contrib.auth import authenticate,login,logout

class AboutView(TemplateView):
    template_name='about.html'

class ExamListView(ListView):
    model=Exam
    template_name='exam_list.html'

    def get_queryset(self):
        return Exam.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


##class UploadPaper(LoginRequiredMixin,CreateView):
class UploadPaper(LoginRequiredMixin,CreateView):
    login_url='/login/'
    #redirect_field_name='basic_app/successfull_submission.html'   #not working

    model=Exam
    template_name='upload.html'

    form_class=ExamForm

class ExamUpdateView(LoginRequiredMixin,UpdateView):#By default template_name=Exam_form.html
    login_url = '/login/'
    redirect_field_name = 'basic_app/successfull_submission.html'

    form_class = ExamForm

    model = Exam    #context_object_name are derived from model name
    #fields will be provided from form_class attr

class DraftListView(LoginRequiredMixin,ListView): #template_name is exam_draft_list.html
    login_url = '/login/'
    redirect_field_name = 'basic_app/successfull_submission.html'

    model = Exam    #context_object_name are derived from model name
    template_name='show_precised_list.html' #not working
    def get_queryset(self):         #in the Exam_draft_list only satisfied condition objects will be passed
        return Exam.objects.filter(published_date__isnull=True).order_by('file')


class ExamDeleteView(LoginRequiredMixin,DeleteView):#By default template_name=exam_confirm_delete.html
    model = Exam    #context_object_name are derived from model name
    #template_name='exam_confirm_delete.html'
    success_url = reverse_lazy('exam_list')


@staff_member_required
def paper_publish(request, pk):
    paper = get_object_or_404(Exam, pk=pk)
    paper.publish()
    return redirect('exam_list')

def download_item(request, pk):
    item = get_object_or_404(Exam, pk=pk)
    file_name, file_extension = 	 os.path.splitext(item.file.file.name)
    file_extension = file_extension[1:] # removes dot
    response = FileResponse(item.file.file,
        content_type = "file/%s" % file_extension)
    response["Content-Disposition"] = "attachment;"\
        "filename=%s.%s" %(slugify(item.file.name)[:-(len(file_extension))], file_extension)
    return response



def register(request):

        registered=False

        if request.method=="POST":
            user_form=UserForm(data=request.POST)


            if user_form.is_valid():
                user=user_form.save()
                user.set_password(user.password)    #hashing
                user.save()
                registered=True
            else:
                print(user_form.errors)
        else:
            user_form=UserForm()
        return render(request,'basic_app/registration.html',{'user_form':user_form,'registered':registered})


#def show_precised_list(request):
#    return render(request,'basic_app/show_precised_list.html')

class PrescisedListView(ListView):
    model=Exam

    template_name='show_precised_list.html'

    def get_queryset(self):
        return Exam.objects.filter(published_date__lte=timezone.now(),branch=self.kwargs['branch'],semester=self.kwargs['semester']).order_by('-year')













def tryit(request):
    return render(request,'basic_app/try.html')

#############################################################
#############################################################
@login_required
def upload_paper(request):
    if request.method == 'Exam':
        form = ExamForm(request.Exam, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return render(request,'basic_app/successfull_submission.html')
    else:
        form = ExamForm()
    return render(request, 'upload.html', {'form': form})
