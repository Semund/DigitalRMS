from django import forms

from .models import Booking, Guest, Room


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ('first_name', 'last_name', 'additional_name',
                  'passport_number', 'date_of_issue', 'birth_date', 'phone', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Иван', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Иванов', 'class': 'form-control'}),
            'additional_name': forms.TextInput(attrs={'placeholder': 'Иванович', 'class': 'form-control'}),
            'passport_number': forms.TextInput(attrs={'placeholder': '99 99 999999', 'class': 'form-control'}),
            'date_of_issue': forms.DateInput(attrs={'max': "9999-12-12", 'class': 'form-control', 'type': 'date'}),
            'birth_date': forms.DateInput(attrs={'max': "9999-12-12", 'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 999 999 99 99', 'class': 'form-control', 'type': 'tel'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@email.com', 'class': 'form-control'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('checkin_date', 'checkout_date')
        widgets = {
            'checkin_date': forms.DateInput(attrs={'max': "9999-12-12", 'class': 'form-control', 'type': 'date'}),
            'checkout_date': forms.DateInput(attrs={'max': "9999-12-12", 'class': 'form-control', 'type': 'date'}),
        }


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('number',)

        widgets = {
            'number': forms.NumberInput(attrs={'max': 9999, 'class': 'form-control'})
        }
