from django import forms
from booking.models import Booking
from datetime import datetime


class DateTimeWidget(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(attrs={'type': 'date'}),
                   forms.TextInput(attrs={'type': 'time'})]
        super(DateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time()]
        else:
            return ['', '']


class DateTimeField(forms.fields.MultiValueField):
    widget = DateTimeWidget

    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.DateField(),
                       forms.fields.TimeField()]
        super(DateTimeField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        return datetime.strptime("{}T{}".format(*values), "%Y-%m-%dT%H:%M:%S")


class BookingForm(forms.ModelForm):
    start = DateTimeField()
    end = DateTimeField()
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'bookable': forms.HiddenInput(),
        }


    def clean(self):
        cleaned_data = super().clean()
        bookable = cleaned_data.get("bookable")
        start = cleaned_data.get("start")
        end = cleaned_data.get("end")

        if bookable and start and end:
            overlapping = Booking.objects.filter(
                bookable=bookable, start__lt=end, end__gt=start)
            if overlapping:
                warning = "Error: Requested booking is overlapping with following bookings: "
                for booking in overlapping:
                    warning = warning + str(booking)
                raise forms.ValidationError(warning)
