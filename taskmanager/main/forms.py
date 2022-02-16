from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task 
        fields = ["title", "task"]

        widgets = {
            "title": TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'Add task\'s name'
        }),
            "task": Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Add task\'s description'
        })
    }
