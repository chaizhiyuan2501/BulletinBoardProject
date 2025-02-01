from django import forms
from .models import Themes,Comments

class CreateThemeForm(forms.ModelForm):
    title = forms.CharField(label="タイトル")

    class Meta:
        model = Themes
        fields = ("title",)

class DeleteThemeForm(forms.ModelForm):
    
    class Meta:
        model = Themes
        fields = []

class PostCommentForm(forms.ModelForm):
    # rows:行数     cols:列数
    comment = forms.CharField(label="",widget=forms.Textarea(attrs={'rows':5,"cols":'60'}))

    class Meta:
        model = Comments
        fields = ("comment",)