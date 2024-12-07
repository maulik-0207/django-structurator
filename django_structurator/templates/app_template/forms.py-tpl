"""
class ExampleModelForm(forms.ModelForm):
    field3 = forms.CharField(
        max_length= 100,
        required= True,
        label= "Full Name",
        help_text= "Enter your full name.",
        widget= forms.TextInput(attrs={"placeholder": "John Doe", "class": "form-control"}),
    )
    
    class Meta:
        model = ExampleModel
        fields = ["field1", "field2", "field3"]
        widgets = {
            "field1": forms.TextInput(attrs={"class": "form-control"}),
            "field2": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
        help_texts = {
            "field1": "Enter a value for field1.",
        }
        labels = {
            "field1": "Custom Label for Field1",
        }

    def clean_field1(self):    
        clean_field1 = self.cleaned_data.get("clean_field1")
        if not clean_field1.endswith("@domain.com"):
            raise forms.ValidationError("clean_field1 must be from domain.com")
        return clean_field1
    
    def clean(self):
        cleaned_data = super(ExampleModelForm, self).clean()
        field1 = cleaned_data.get("field1")
        field2 = cleaned_data.get("field2")

        if field1 == field2:
            self.add_error('field1',"field1 is not same as field2")
        return cleaned_data
    
    def save(self):
        # Override or write your own save method
        pass
"""
from django import forms
from .models import *  
# Create your forms here.

