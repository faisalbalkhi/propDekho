from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from properties_engine.models import Property




class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

    #     widgets = {
    #         'cartegory': forms.Select(attrs={'class': 'selectpicker'}),
    #         'amenities': forms.Select(attrs={'class': 'selectpicker'}),
    #         'furnished': forms.Select(attrs={'class': 'selectpicker'}),
    #         'bhk': forms.Select(attrs={'class': 'selectpicker'}),
    #         'bhk_type': forms.TextInput(attrs={'class': 'form-control'}),
    #         'r_parking': forms.Select(attrs={'class': 'selectpicker'}),
    #         'a_status': forms.Select(attrs={'class': 'selectpicker'}),
    #         'p_tenant_type': forms.Select(attrs={'class': 'selectpicker'}),
    #         'brokerage': forms.Select(attrs={'class': 'selectpicker'}),
    #         'brokerage_charge': forms.TextInput(attrs={'class': 'form-control'}),
    #         'location': forms.TextInput(attrs={'class': 'form-control'}),
    #         'title': forms.Select(attrs={'class': 'selectpicker', 'data-style': 'select-with-transition', 'title': 'select User'}),
    #         'no_of_bedroom': forms.TextInput(attrs={'class': 'form-control'}),
    #         'no_of_bathroom': forms.TextInput(attrs={'class': 'form-control'}),
    #         'no_of_kitchen': forms.TextInput(attrs={'class': 'form-control'}),
    #         'author_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'rating': forms.TextInput(attrs={'class': 'form-control'}),
    #         'created_at' :forms.Select(attrs={'class': 'selectpicker'}),
    #         'description': forms.Textarea(attrs={'class': 'selectpicker'}),
    #         'area': forms.TextInput(attrs={'class': 'form-control'}),
    #         'available_form': forms.DateInput(attrs={'type': 'date','class': 'datepicker form-control', 'placeholder': 'YYYY-MM-DD'}),
    #     }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.fields['feature_image'].label = "Upload feature_image"
    #     self.fields['author_name'].label = "Upload author_name"
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('Save Change', 'Save Change'))
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('cartegory'),
    #             Column('amenities'),
    #             Column('furnished'),
    #         ),
            
    #         Row(
    #             Column('bhk'),
    #             Column('bhk_type'),
    #             Column('r_parking'),
    #         ),
    #         Row(
    #             Column('a_status'),
    #             Column('p_tenant_type'),
    #         ),
    #         Row(
    #             Column('brokerage'),
    #             Column('brokerage_charge'),
    #         ),
    #         Row(
    #             Column('feature_image'),
    #             Column('location'),
    #         ),
    #         Row(
    #             Column('title'),
    #             Column('p_tenant_type'),
    #         ),
    #         Row(
    #             Column('price'),
    #             Column('no_of_bedroom'),
    #         ),
    #         Row(
    #             Column('no_of_bathroom'),
    #             Column('no_of_kitchen'),
    #         ),
    #         Row(
    #             Column('author_image'),
    #             Column('author_name'),
    #         ),
    #         Row(
    #             Column('rating'),
    #             Column('created_at'),
               
    #         ),
    #         Row(
    #             Column('description'),
    #             Column('area'),
    #         ),
    #         Row(
    #             Column('available_form'),
                
    #         ),
            
    #     )