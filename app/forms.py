from django import forms
g=[('Male','Female'),('male','female')]
c=[]
class Studentform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    gender=forms.ChoiceField(choices=g)
    #gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    