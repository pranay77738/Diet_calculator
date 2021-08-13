from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class FoodItemsForm(ModelForm):
    class Meta:
        model=FoodItems
        fields='__all__'

class addUserFoodItem(ModelForm):
    class Meta:
        model=UserFoodItem
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']