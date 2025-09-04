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


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={"id": "name", "placeholder": "Your Name"}),
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={"id": "email", "placeholder": "Your Email"}),
    )
    message_content = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "id": "message",
                "placeholder": "Write your message...",
                "rows": 5,
            }
        ),
    )
