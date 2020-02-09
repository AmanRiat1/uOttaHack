from django import forms

gender = [('male', 'M'), ('female', 'F')]
response = [('1', 'yes'), ('0', 'no')]
time = [('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four')]
education = [('0', 'zero'),('1', 'zero'), ('2', 'two'), ('3', 'three'), ('4', 'four')]
rating = [('1', 'one'), ('2', 'two'), ('3', 'three'), ('4', 'four'), ('5', 'five')]

class ContactForm(forms.Form):
    gender_choice = forms.CharField(label="Gender:", widget=forms.Select(choices=gender))
    age = forms.CharField(max_length=254)
    family_size = forms.CharField(max_length=254)
    pstatus = forms.CharField(label="Health Status:", widget=forms.Select(choices=response))
    mother_education = forms.CharField(label="Mother's Education:", widget=forms.Select(choices=education))
    father_education = forms.CharField(label="Father's Education:", widget=forms.Select(choices=education))
    travel_time_to_school = forms.CharField(label="Travel Time To School:", widget=forms.Select(choices=time))
    study_time = forms.CharField(label="Study Time To School:", widget=forms.Select(choices=time))
    failures = forms.CharField(max_length=254)
    family_support = forms.CharField(label="Family Support:", widget=forms.Select(choices=response))
    internet = forms.CharField(label="Internet:", widget=forms.Select(choices=response))
    relationship = forms.CharField(label="Relationship:", widget=forms.Select(choices=response))
    family_relationship_quality = forms.CharField(label="Family Relationship Quality:", widget=forms.Select(choices=rating))
    time_after_school = forms.CharField(label="Free Time After School:", widget=forms.Select(choices=rating))
    going_out = forms.CharField(label="Going Out With Friends:", widget=forms.Select(choices=rating))
    health = forms.CharField(label="Health Status:", widget=forms.Select(choices=rating))
    absences = forms.CharField(max_length=254)

