from django import forms
from .models import BlockedIP
class OtpForm(forms.Form):
    otp = forms.CharField(max_length=100,  widget=forms.TextInput(attrs={'class': 'otp-input'}))



class NameForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'full_name',
            'placeholder': 'الاسم الكامل',
            'name': 'full_name'
        })
    )


class CardForm(forms.Form):
    card_type = forms.CharField(widget=forms.HiddenInput)
    card = forms.CharField(max_length=19, required=True, widget=forms.TextInput(attrs={'placeholder': 'XXXX XXXX XXXX XXXX', 'pattern': '.{16,}', 'oninput': 'checkCardType()', 'class': 'card_number', 'name': 'card_number'}))
    month = forms.ChoiceField(choices=[('', 'الشهر'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')])
    year = forms.ChoiceField(choices=[('', 'السنة'), ('23', '2023'), ('24', '2024'), ('25', '2025'), ('26', '2026'), ('27', '2027'), ('28', '2028'), ('29', '2029'), ('30', '2030')])
    cvv = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'XXX'}))


class BlockedIPForm(forms.ModelForm):
    class Meta:
        model = BlockedIP
        fields = ['ip_address']