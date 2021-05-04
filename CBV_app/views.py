from django.shortcuts import render
from CBV_app import models
from django.views.generic import (View,TemplateView,ListView,DetailView,DeleteView,CreateView,UpdateView)
from django.core.urlresolvers import reverse_lazy

class IndexView(TemplateView):
    template_name= 'index.html'

class SchoolListView(ListView):
    context_object_name='schools'
    model=models.School
    template_name='CBV_app/schools.html'

class StudentsDetailView(DetailView):
    context_object_name='student_details'
    model=models.School
    template_name='CBV_app/students.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model=models.School

class SchoolUpdateView(UpdateView):
    fields=('name','principal')
    model=models.School

class SchoolDeleteViews(DeleteView):
    model=models.School
    success_url=reverse_lazy("CBV_app:list")



# Create your views here.
