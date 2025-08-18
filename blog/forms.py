from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["full_name", "email", "content"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Your Name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your Email"}),
            "content": forms.Textarea(attrs={"placeholder": "Your Comment", "rows": 5}),
        }
