from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import *
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.


#login form
class LoginView(FormView):
    template_name = 'login/login.html'
    form_class = LoginForm
    success_url = '/home/'

    

    def form_valid(self, form):

        uname = form.cleaned_data['username']
        pword = form.cleaned_data['password']
        print(uname,'88')


        user = authenticate(username=uname, password=pword)
        print(user,'3333333333')
        self.thisuser = user
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, self.template_name, {
                'error': 'Username you enter doesnot exist',
                'form': form
            })
        return super().form_valid(form)


class indexview(TemplateView):
    template_name = 'login/index.html'


#home view
class HomeView(TemplateView):
    template_name = 'admintemplates/adminhome.html'


#logout
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


#supplier list
class SupplierListView(TemplateView):
    template_name = 'supplier/supplierlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['suppliers'] = Supplier.objects.all()
        return context

#supplier add
class SupplierCreateView(CreateView):
    template_name = 'supplier/supplieradd.html'
    form_class = SupplierForm
    success_url = reverse_lazy('posapp:supplierlist')


#supplier update
class SupplierUpdateView(UpdateView):
    template_name = 'supplier/supplierupdate.html'
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy("posapp:supplierlist")

#supplier delete
class SupplierdeleteView(DeleteView):
    template_name = 'supplier/supplierdelete.html'
    model = Supplier
    form_class = SupplierForm
    success_url = reverse_lazy("posapp:supplierlist")