from django import forms

from QandA_app.models import Question


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields ="__all__"