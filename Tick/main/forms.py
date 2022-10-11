from logging import PlaceHolder
from tkinter import Widget
from django import forms
from .models import Profile,BlogPost,Comment_post


class PostForm(forms.ModelForm):  
    class Meta:
        model=BlogPost
        fields=("Title","Author","Body")
        
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        [
        self.fields['Title'].widget.attrs.update({'class': 'form-control'}),
        self.fields['Author'].widget.attrs.update({'class': 'form-control','id':'author'}),
        self.fields['Body'].widget.attrs.update({'class': 'form-control'}),
        
        ]
        # widgets = {
        #     'Title':forms.TextInput(attrs ={'class':'form-control'}),
        #     'Author':forms.ChoiceField(attrs={'class':'form-control'}),
        #     'Body':forms.Textarea(attrs={'class':'form-control'}),
        # }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields= '__all__'  
        



class CommentForm(forms.ModelForm): 
    Title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    Author=forms.CharField(widget=forms.Select(attrs={'class': 'form-control', 'id':'author'}))
    Body=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model=Comment_post
        fields=("Title","Author","Body")
        #fields='__all__'
        
    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     [
    #     self.fields['Title'].widget.attrs.update({'class': 'form-control'}),
    #     self.fields['Author'].widget.attrs.update({'class': 'form-control','id':'author'}),
    #     self.fields['Body'].widget.attrs.update({'class': 'form-control'}),
        
    #     ]
        # widgets = {
        #     'Title':forms.TextInput(attrs ={'class':'form-control'}),
        #     'Author':forms.ChoiceField(attrs={'class':'form-control'}),
        #     'Body':forms.Textarea(attrs={'class':'form-control'}),
        # } 