from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class CompanyListView(ListView):
    model = Company
    # default template file is company_list.html


class CompanyDetailView(DetailView):
    model = Company
    # default template file is company_detail.html


class CompanyCreateView(CreateView):
    model = Company
    fields = ('name', 'location', 'ceo')
    # default template file is company_form.html


class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('name', 'ceo')


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('/')
