from django.shortcuts import render
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect, reverse
from booking.models import *
import pytz
from fars.settings import TIME_ZONE
from datetime import datetime


class DashboardView(View):
    template = 'dashboard.html'
    context = {}

    def get(self, request):
        now = pytz.timezone(TIME_ZONE).localize(datetime.now())

        return render(request, self.template, context=self.context)


    def post(self, request):
        username = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username=username, password=pw)
        postdata = request.POST.copy()
        try:
            postdata['user'] = user.id
        except AttributeError:
            postdata['user'] = -1
            self.context['errors'] = 1
            self.context['credential_error'] = 1
        form = BookingForm(postdata, instance=Booking())
        if form.is_valid():
            form.save()
            return redirect('tablet')
        self.context['errors'] = 1
        status = 400

        self.context['bookform'] = form
        return render(request, self.template, context=self.context, status=status)
