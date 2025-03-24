from django.shortcuts import render
from .models import Empleado
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView)

# Create your views here.

class ListAllEmpleados(ListView):
    template_name = "empleado/list_all.html"
    paginate_by = 4
    ordering = ['first_name']
    model = Empleado
    context_object_name = "list_empleados"

class ListViewAreaEmpleado(ListView):
    """ List empleados de un area"""
    template_name = "empleado/list_by_area.html"

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name=area
    )

        return lista
    context_object_name = "list_empleados"


class ListViewTrabajoEmpleado(ListView):
    """ List empleado pr trabajo"""
    """ Recordar que es por numero del 0 al 3"""
    template_name = "empleado/list_by_trabajo.html"


    def get_queryset(self):
        trabajo = self.kwargs['trabajo']

        lista = Empleado.objects.filter(
            job=trabajo
        )


        return lista

class ListEmpleadosByKword(ListView):
    """ Lista de empleados por palabra clave"""
    template_name = "empleado/by_kword.html"
    context_object_name = "empleados"

    def get_queryset(self):
        print("*****************")
        palabra_clave = self.request.GET.get('kword',"")
        print("===========" , palabra_clave)
        lista = Empleado.objects.filter(
            first_name=palabra_clave
        )


        return lista

class ListHabilidadesEmpleados(ListView):
    template_name = "empleado/habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        idEmpleado = self.request.GET.get('idEmpleado',"")
        if idEmpleado == "":
            return []
        empleado = Empleado.objects.get(id=idEmpleado)
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleado/detail_empleado.html'
    def get_context_data(self, **kwargs):
        context = super (EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'empleado/success.html'

class UnsuccessView(TemplateView):
    template_name = 'empleado/unsuccess.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleado/add.html'
    fields = [
        'first_name',
        'last_name',
        'departamento',
        'job',
        'habilidades']
    success_url = reverse_lazy('empleados_app:correcto')
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado/update.html'
    fields = [
        'first_name',
        'last_name',
        'departamento',
        'job',
        'habilidades']
    success_url = reverse_lazy('empleados_app:correcto')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + " " + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado/delete.html'









