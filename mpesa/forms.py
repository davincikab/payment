from django import forms

class MpesaPaymentForm(forms.Form):
    amount = forms.IntegerField(label="Amount", required=True)
    phone_number = forms.CharField(label="Phone Number", max_length=12, required=True,
        help_text="Phone Number format: 254700111222",
        widget=forms.TextInput(attrs={
            'placeholder':'254700111222',
            'pattern':r'254([0-9]{9})'
        })
    )
    home = forms.CharField(
        label="Children's Home", max_length=50, required=False,
        widget=forms.TextInput(attrs={
            'disabled':True
        })
    )
