from django.forms import ModelForm

from .models import Pirate


class PirateForm(ModelForm):
    class Meta:
        model = Pirate
        fields = ("name", "is_captain")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        self.fields = ["name"]
        if user["role"] == "admin":
            self.fields.append("is_captain")

        super(PirateForm, self).__init__(*args, **kwargs)
