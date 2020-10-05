from django.db import models
from datetime import date

# Create your models here.

class InventoryModel(models.Model):
    # GENERAL INFORMATION
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
    
    # CASE DETAILS
    entry_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    file_no = models.CharField(max_length=25, blank=True)
    case_no = models.CharField(max_length=25, blank=True)
    court = models.CharField(max_length=100, blank=True)
    court_no = models.CharField(max_length=15, blank=True)
    male_suspect = models.IntegerField()
    female_suspect = models.IntegerField()
    male_underage_suspect = models.IntegerField()
    female_underage_suspect = models.IntegerField()
    assigned_to = models.CharField(max_length=150)

    # GENERAL INFORMATION
    agency = models.CharField(max_length=4, choices=AGENCY_CHOICE)
    date_of_request = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    date_of_receipt = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    st_deadline = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)

    # DETAILS OF REMAND
    bail_granted = models.CharField(max_length=2, choices=TF_CHOICE)
    in_custody = models.CharField(max_length=2, choices=TF_CHOICE)
    date_of_remand = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    place_of_remand = models.CharField(max_length=4, choices=AGENCY_CHOICE)

    # OUTCOME/UPDATE
    date_of_advice = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    case_to_answer = models.CharField(max_length=2, choices=TF_CHOICE)
    entry_made_by = models.CharField(max_length=200)
    update_made_by = models.CharField(max_length=200)

    export_to_CSV = models.BooleanField(default=False)



    def __str__(self):
        return self.file_no






class AttorneyModel(models.Model):
    # GENERAL INFORMATION
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

    # CASE DETAILS
    entry_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    file_no = models.CharField(max_length=25, blank=True)
    case_no = models.CharField(max_length=25, blank=True)
    case_name = models.CharField(max_length=25, blank=True)
    court = models.CharField(max_length=15, blank=True)
    

    # GENERAL INFORMATION
    agency = models.CharField(max_length=4, choices=AGENCY_CHOICE)
    no_defendant_male = models.IntegerField()
    no_defendant_female = models.IntegerField()
    no_underage_male = models.IntegerField()
    no_underage_female = models.IntegerField()
    no_pwds_male = models.IntegerField()
    no_pwds_female = models.IntegerField()
    counsel_name = models.CharField(max_length=150)
    counsel_telephone = models.CharField(max_length=14)

    # ADJOURNMENT
    adjourn_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    reason_for_adjournment = models.CharField(max_length=4, choices=ADJOURNMENT_CHOICE)
    
    # STAGE OF PROCEEDINGS
    stage_of_proceedings = models.CharField(max_length=4, choices=PROCEEDINGS_CHOICE)

    # DISCHARGE
    is_defendant_in_custody = models.CharField(max_length=2, choices=TF_CHOICE)
    has_bail_been_revoked = models.CharField(max_length=2, choices=TF_CHOICE)
    disposal = models.CharField(max_length=2, choices=DISCHARGE_CHOICE)

    # DISCHARGE
    lead_counsel = models.CharField(max_length=200)
    entry_made_by = models.CharField(max_length=200)
    entry_updated_by = models.CharField(max_length=200)

    export_to_CSV = models.BooleanField(default=False)

    

    def __str__(self):
        return self.file_no

    
    

    
    