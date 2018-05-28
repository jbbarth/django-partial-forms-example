from django.forms import ModelForm

from .models import Pirate


class PirateForm(ModelForm):
    class Meta:
        model = Pirate
        fields = ("name", "is_captain")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cleanup_missing_keys(kwargs.get("data"))

    def cleanup_missing_keys(self, data):
        """
        Removes missing keys from fields on form submission.
        This avoids resetting fields that are not present in
        the submitted data, which may be the sign of a buggy
        or incomplete template.
        Note that this cleanup relies on the HTML form being
        patched to send all keys, even for checkboxes, via
        input[type="hidden"] fields or some JS magic.
        """
        if data is None:
            # not a form submission, don't modify self.fields
            return

        got_keys = data.keys()
        field_names = self.fields.keys()
        for missing in set(field_names) - set(got_keys):
            del self.fields[missing]
