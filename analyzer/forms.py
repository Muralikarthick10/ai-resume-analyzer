from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField(
        label="Upload Resume (PDF)"
    )

    job_description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows':8,
                'placeholder':'Paste Job Description Here'
            }
        )
    )