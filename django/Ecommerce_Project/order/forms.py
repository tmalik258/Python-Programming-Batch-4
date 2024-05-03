from django import forms

from .models import Order

class AddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('__all__')
        exclude = ('user', 'total_amount', 'is_placed', 'is_canceled', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'required': True
            })
        
        self.fields['address_line_2'].widget.attrs.update({
            'required': False
        })
        self.fields['address_line_2'].help_text = 'Optional'