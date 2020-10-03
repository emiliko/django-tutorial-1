from django import forms
from .models import Topic

# ModelForm associated with Topic model
class NewTopicForm(forms.ModelForm):
    # refers to the message in the Post we want to save
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
        )

    class Meta:
        model = Topic
        fields =['subject', 'message'] # subject refers to the subject dield in the Topic class


