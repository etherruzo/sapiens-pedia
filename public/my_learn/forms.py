from django import forms


TAGS = (
    ('', 'Choose...'),
    ('leisure', 'leisure'),
    ('work', 'work'),
    ('life', 'life')
)

class ContactForm(forms.Form):
#    name = forms.CharField(label="Name", required=True)
#    email = forms.EmailField(label="Email", required=True)
#    subject = forms.CharField(label="Subject", required=True)
    learning_1 = forms.CharField(label="learning_1", widget=forms.Textarea, required=True)
    learning_2 = forms.CharField(label="learning_2", widget=forms.Textarea, required=True)
    learning_3 = forms.CharField(label="learning_3", widget=forms.Textarea, required=True)
    tag1 = forms.ChoiceField(label="tag1", required=True,choices=TAGS)
    tag2 = forms.ChoiceField(label="tag2", required=True,choices=TAGS)
    tag3 = forms.ChoiceField(label="tag3", required=True,choices=TAGS)
    #public1 = forms.ChoiceField(label="tag1", required=True)
    #public2 = forms.ChoiceField(label="tag2", required=True,choices=TAGS)
    #public3 = forms.ChoiceField(label="tag3", required=True,choices=TAGS)
