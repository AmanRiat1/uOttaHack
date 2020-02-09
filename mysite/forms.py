from django import forms

<<<<<<< HEAD
gender = [('male', 'M'), ('female', 'F')]
response = [('yes', 'Y'), ('no', 'N')]
rating = [('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5')]

class ContactForm(forms.Form):
    gender_choice = forms.CharField(label="Gender:", widget=forms.Select(choices=gender))
    age = forms.CharField(max_length=254)
    family_size = forms.CharField(max_length=254)
    mother_education = forms.CharField(max_length=254)
    father_education = forms.CharField(max_length=254)
    travel_time_to_school = forms.CharField(max_length=254)
    study_time = forms.CharField(max_length=254)
    failures = forms.CharField(max_length=254)
    family_support = forms.CharField(label="Family Support:", widget=forms.Select(choices=response))
    internet = forms.CharField(label="Internet:", widget=forms.Select(choices=response))
    relationship = forms.CharField(label="Relationship:", widget=forms.Select(choices=response))
    family_relationship_quality = forms.CharField(label="Family Relationship Quality:", widget=forms.Select(choices=rating))
    time_after_school = forms.CharField(label="Free Time After School:", widget=forms.Select(choices=rating))
    going_out = forms.CharField(label="Going Out With Friends:", widget=forms.Select(choices=rating))
    health = forms.CharField(label="Health Status:", widget=forms.Select(choices=rating))
=======

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
>>>>>>> 1f38fe73826e331bab3ead3d8d7ffbcaba85a3fe

