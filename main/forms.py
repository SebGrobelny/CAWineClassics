from django import forms

# from .models import Request
from .models import Contact


SINGLE = (
    ('individual', 'Individual'),
    ('distributer', 'Distributer'),
    ('winery', 'Winery'),
    ('broker', 'Broker'),

)
MULTIPLE = (
    ('bulk', 'Bulk'),
    ('still wine', 'Still Wine'),
    ('shiners', 'Shiners'),
    ('custom program', 'Custom Program'),
)


class ContactForm(forms.ModelForm):
	
	single = forms.ChoiceField(
    	required = True,
    	choices=SINGLE,
    )
	multiple = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=MULTIPLE,
    )
	looking = forms.CharField(
        max_length = 500,
        widget = forms.Textarea,
    )
	hear = forms.CharField(
        max_length = 500,
        widget = forms.Textarea,
    )
	address2 = forms.CharField(
    	required = False,
    )

	class Meta:
		model = Contact 
		fields = ('name', 'email', 'phone', 'address1', 'address2', 'country', 'state', 'zipcode', 'single', 'multiple','looking','hear')
        # widgets = {
        #     'looking' : forms.Textarea(attrs={
        #         'rows': '5',
        #         'cols': '90',
        #         'maxlength': '500'}),
        #     'hear' : forms.Textarea(attrs={
        #         'rows': '5',
        #         'cols': '90',
        #         'maxlength': '500',
        #     })
        #     }


	# first_name = forms.CharField(max_length=100)
	# last_name = forms.CharField(max_length=100)
	# email = forms.CharField(max_length=100)
	# phone = forms.CharField(max_length=100)
	# address1 = forms.CharField(max_length=100)
	# address2 = forms.CharField(required = False, max_length=100)
	# country = forms.CharField(max_length=100)
	# state = forms.CharField(max_length=100)
	# zipcode = forms.CharField(max_length=100)
	# single = forms.ChoiceField(
 #    	required = True,
 #    	choices=SINGLE,
 #    )
	# multiple = forms.MultipleChoiceField(
 #        required=True,
 #        widget=forms.CheckboxSelectMultiple,
 #        choices=MULTIPLE,
 #    )

	# def __init__(self, *args, **kwargs):
	# 	super(RequestForm, self).__init__(*args, **kwargs)
 #    	self.fields['name'].required = True
 #    	self.fields['email'].required = True
 #    	self.fields['phone'].required = True
 #    	self.fields['address1'].required = True
 #    	self.fields['country'].required = True
 #    	self.fields['state'].required = True
 #    	self.fields['zipcode'].required = True
 #    	self.fields['single'].required = True


	# class Meta:
	# 	model = Request
	# 	looking = forms.CharField(widget=forms.Textarea)
	# 	hear = forms.CharField(widget=forms.Textarea)
	# 	single = forms.MultipleChoiceField(
 #        required=True,
 #        widget=forms.CheckboxSelectMultiple,
 #        choices=SINGLE,
 #    )
	# 	multiple = forms.MultipleChoiceField(
 #        required=True,
 #        widget=forms.CheckboxSelectMultiple,
 #        choices=MULTIPLE,
 #    )
		#fields = ('name', 'email', 'phone', 'address1', 'address2', 'country', 'state', 'zipcode', 'single', 'multiple','looking','hear')




# class ContactForm(forms.ModelForm):

# 	def __init__(self, *args, **kwargs):
# 		super(ContactForm, self).__init__(*args, **kwargs)
#     	self.fields['name'].required = True
#     	self.fields['email'].required = True
#     	self.fields['phone'].required = True
#     	self.fields['address1'].required = True
#     	self.fields['country'].required = True
#     	self.fields['state'].required = True
#     	self.fields['zipcode'].required = True
#     	self.fields['single'].required = True

# 	class Meta:
# 		model = Contact
# 		fields = ('name', 'email', 'phone', 'address1', 'address2', 'country', 'state', 'zipcode', 'single', 'multiple','looking','hear')