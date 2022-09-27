from django import forms


class SignupForm(forms.Form):
    """
    A class for the Signup form
    """
    first_name = forms.CharField(
        max_length=30, label='First name',
        widget=forms.TextInput(attrs={'placeholder': 'First name'})
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name'].capitalize()
        user.save()
