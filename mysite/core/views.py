from django.views.generic import TemplateView, CreateView, DetailView, FormView

from mysite.core.forms import BootstrapEventForm, XDSoftEventForm, FengyuanChenEventForm, DateForm
from mysite.core.models import Event


class HomeView(TemplateView):
    template_name = 'core/home.html'


class EventDetailView(DetailView):
    model = Event


class ManualFormView(FormView):
    form_class = DateForm
    template_name = 'core/manual.html'


class XDSoftDateTimePickerView(CreateView):
    model = Event
    form_class = XDSoftEventForm
    template_name = 'core/xdsoft_event_form.html'


class BootstrapDateTimePickerView(CreateView):
    model = Event
    form_class = BootstrapEventForm
    template_name = 'core/bootstrap_event_form.html'


class FengyuanChenDatePickerView(CreateView):
    model = Event
    form_class = FengyuanChenEventForm
    template_name = 'core/fengyuanchen_event_form.html'
