from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(min_length = 3, max_length = 100)
	# specify labels 
	email = forms.EmailField(required = False, label='your email') 
	message = forms.CharField(widget=forms.Textarea)
	
	# run extra validation errors using function
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message 