from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.departamento.models import Departamento
from applications.empleados.models import Empleado
# Create your views here.


class NewDepartamentoView(FormView):
    template_name = "departamento/new_departamento.html"
    form_class = NewDepartamentoForm
    success_url = "/"

    def form_valid(self, form):

        #Los 2 hacen lo mismo pero son ejeplos diferentes

        #Creo el departmaento
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shortname']
        )
        depa.save()

        #Creo el empleado
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=depa
        )
        return super(NewDepartamentoView, self).form_valid(form)