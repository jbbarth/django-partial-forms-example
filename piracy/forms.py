from django.forms import ModelForm

from .models import Pirate


class PirateForm(ModelForm):
    class Meta:
        model = Pirate
        fields = ("name", "is_captain")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(PirateForm, self).__init__(*args, **kwargs)

        if user["name"] != "Alice":
            del self.fields["is_captain"]
