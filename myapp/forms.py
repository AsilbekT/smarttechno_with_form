from myapp.models import MxikObject
from django import forms

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput
                           (attrs={'class': 'form-control',
                                   'id': 'name', "name": "name", "placeholder": _("Ваше имя")}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
                            'class': "form-control", "name": "email", "placeholder": _("Ваша электронная почта")}))
    text = forms.CharField(widget=forms.Textarea
                           (attrs={'class': 'form-control', "cols": "30", "rows": "10", "placeholder": _("Текст")}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)


class MxikForm(forms.ModelForm):
    class Meta:
        model = MxikObject
        fields = ("mxik_options", "mxik_input",)

    def save_and_get_id(self):
        instance = self.save()
        return instance.id
