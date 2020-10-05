from django import forms 
from django.forms import ModelForm
from .models import InventoryModel, AttorneyModel
from django.contrib.auth.forms import(AuthenticationForm)
from django.contrib.auth import authenticate





class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control', 'placeholder':'Enter Password'}, render_value=True))


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Please enter a correct USERNAME and PASSWORD")
            elif not self.user_cache.is_active:
                raise forms.ValidationError(_("This account is inactive."))
        return self.cleaned_data

    


class InventoryForm(forms.ModelForm):

    NCS = 'NS'
    POLICE = 'PL'
    DSS = 'DS'
    OTHERS = 'OT'
    AGENCY_CHOICE = [
        (NCS, 'NCS'),
        (POLICE, 'Police'),
        (DSS, 'DSS'),
        (OTHERS, 'Others'),
    ]


    YES = 'YS'
    NO = 'NO'
    TF_CHOICE = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    
    file_no = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'File Number'}))
    case_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Case Number'}))
    court = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Court'}))
    court_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Court Number'}))
    male_suspect = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    female_suspect = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    male_underage_suspect = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    female_underage_suspect = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    assigned_to = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name'}))
    agency = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=AGENCY_CHOICE))
    date_of_request = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    date_of_receipt = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    st_deadline = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    bail_granted = forms.CharField(required=False, widget=forms.Select(attrs={
        'class':'form-control'}, choices=TF_CHOICE))
    in_custody = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=TF_CHOICE))
    date_of_remand = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    place_of_remand = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=AGENCY_CHOICE))
    date_of_advice = forms.DateField(required=False, widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    case_to_answer = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=TF_CHOICE))
    entry_made_by = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name'}))
    update_made_by = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name'}))
    

    class Meta():
        model = InventoryModel
        fields = '__all__'

        

    # def clean_file_no(self): 
    #     file_no = self.cleaned_data.get('file_no')
    #     if (file_no == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     for instance in InventoryModel.objects.all():
    #         if instance.file_no == file_no:
    #             raise forms.ValidationError('File Number ' + file_no + ' Exist')
    #     return file_no

    # def clean_case_no(self): 
    #     case_no = self.cleaned_data.get('case_no')
    #     if (case_no == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     for instance in InventoryModel.objects.all():
    #         if instance.case_no == case_no:
    #             raise forms.ValidationError('Case Number ' + case_no + ' Exist')
    #     return case_no

    # def clean_court(self): 
    #     court = self.cleaned_data.get('court')
    #     if (court == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     return court

    # def clean_court_no(self): 
    #     court_no = self.cleaned_data.get('court_no')
    #     if (court_no == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     return court_no

    # def clean_entry_made_by(self): 
    #     entry_made_by = self.cleaned_data.get('entry_made_by')
    #     if (entry_made_by == ""):
    #         raise forms.ValidationError('This field cannot be left blank')
    #     return entry_made_by

class AttorneyForm(forms.ModelForm):

    NCS = 'NS'
    POLICE = 'PL'
    DSS = 'DS'
    OTHERS = 'OT'
    AGENCY_CHOICE = [
        (NCS, 'NCS'),
        (POLICE, 'Police'),
        (DSS, 'DSS'),
        (OTHERS, 'Others'),
    ]

    # DETAILS OF REMAND
    YES = 'YS'
    NO = 'NO'
    TF_CHOICE = [
        (YES, 'Yes'),
        (NO, 'No'),
    ]

    # ADJOURNMENT
    COURT_DID_NOT_SIT = 'CDN'
    ABSENT_PROSECUTION = 'ABP'
    ABSENT_COUNSEL = 'AC'
    ABSENT_DEFENDANT = 'AD'
    PROSECUTION_NOT_READY = 'PNR'
    REQUEST_PROSECUTION = 'PR'
    REQUEST_COUNSEL = 'RC'
    HEARD = 'HD'
    NOT_HEARD = 'NHD'
    ADJOURNMENT_CHOICE = [
        (COURT_DID_NOT_SIT, 'Court Did Not Sit'),
        (ABSENT_PROSECUTION, 'Absent Prosecution'),
        (ABSENT_COUNSEL, 'Absent Defence Counsel'),
        (ABSENT_DEFENDANT, 'Absent Defendant'),
        (PROSECUTION_NOT_READY, 'Prosecution Not Ready'),
        (REQUEST_PROSECUTION, 'Request Prosecution'),
        (REQUEST_COUNSEL, 'Request Counsel'),
        (HEARD, 'Heard'),
        (NOT_HEARD, 'Not Heard'),
    ]

    # STAGE OF PROCEEDINGS
    AWAITING_DPP_ADVICE = 'ADA'
    AWAITING_FILING_CHARGES = 'AFC'
    ARRAIGNMENT = 'AR'
    COMMENCEMENT_OF_TRIAL = 'CT'
    TRIAL_ONGOING = 'TO'
    TRIAL_WITHIN_TRIAL_ONGOING = 'TWTO'
    JUDGEMENT = 'JG'
    PROCEEDINGS_CHOICE = [
        (AWAITING_DPP_ADVICE, 'Awaiting DPP Legal Advice'),
        (AWAITING_FILING_CHARGES, 'Awaiting Filing of Charges/Information'),
        (ARRAIGNMENT, 'Arraignment'),
        (COMMENCEMENT_OF_TRIAL, 'Commencement of Trial'),
        (TRIAL_ONGOING, 'Trial Ongoing'),
        (TRIAL_WITHIN_TRIAL_ONGOING, 'Trial-within-Trial ongoing'),
        (JUDGEMENT, 'Judgment and Sentencing'),
    ]


     # DISCHARGE
    CONVICTION = 'CN'
    ACQUITTAL = 'AC'
    STRUCK_OUT = 'SO'
    DISMISSAL = 'DS'
    DISCHARGE_CHOICE = [
        (CONVICTION, 'Conviction'),
        (ACQUITTAL, 'Acquittal'),
        (STRUCK_OUT, 'Struck Out– Want Of Diligent Prosecution'),
        (DISMISSAL, 'Dismissal– No Case Submission'),
    ]


    file_no = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'File Number'}))
    case_no = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Case Number'}))
    case_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Case Name'}))
    court = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Court'}))
    agency = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=AGENCY_CHOICE))
    no_defendant_male = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Defendant'}))
    no_defendant_female = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Defendant'}))
    no_underage_male = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    no_underage_female = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of Suspect'}))
    no_pwds_male = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': '0','max': '100','class':'form-control', 'placeholder':'Number of PWDS'}))
    no_pwds_female = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class':'form-control', 'placeholder':'PWDS Female'}))
    counsel_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Counsel Name'}))
    counsel_telephone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Phone Number'}))
    adjourn_date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control', 'type':'date'}))
    reason_for_adjournment = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=ADJOURNMENT_CHOICE))
    stage_of_proceedings = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=PROCEEDINGS_CHOICE))
    is_defendant_in_custody = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=TF_CHOICE))
    has_bail_been_revoked = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=TF_CHOICE))
    disposal = forms.CharField(widget=forms.Select(attrs={
        'class':'form-control'}, choices=DISCHARGE_CHOICE))
    lead_counsel = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Lead Counsel'}))
    entry_made_by = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name'}))
    entry_updated_by = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder':'Enter Name'}))

    class Meta():
        model = AttorneyModel
        fields = '__all__'



class InventorySearchForm(forms.ModelForm):

    class Meta():
        model = InventoryModel
        fields = ['file_no', 'case_no', 'export_to_CSV']

class AttorneySearchForm(forms.ModelForm):
    
    class Meta():
        model = AttorneyModel
        fields = ['file_no', 'case_no', 'export_to_CSV']

        