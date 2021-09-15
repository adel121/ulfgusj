from django import forms


class StudentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        Name = forms.CharField(label="Group Member Names",max_length=300, required = True)
        Gmail = forms.CharField(label="Enter Your Gmail",max_length=200, required = True)
        Email = forms.CharField(label="Enter Your Email ending with st.ul.edu.lb",max_length=200, required = True)
        #Discipline = forms.CharField(label="Discipline",max_length=10, choices=[("telecom","TELECOM"), ("power","POWER") ], required = True)
