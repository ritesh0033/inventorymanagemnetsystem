from django import forms
from users.models import User 
from users.models import Role  

class UserSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}),label="Confirm Password",)

    class Meta:
        model = User
        fields = ["name", "email", "password", "confirm_password", "role"]
        widgets = {"password": forms.PasswordInput(attrs={"placeholder": "Enter Password"}),
                   }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match!")

        return cleaned_data
