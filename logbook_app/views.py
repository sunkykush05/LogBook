from django.shortcuts import render, redirect, get_object_or_404
from logbook_app.forms import InventoryForm, InventorySearchForm, AttorneyForm, AttorneySearchForm
from .models import InventoryModel, AttorneyModel
from django.contrib import messages
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required, user_passes_test




# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/home-page/')
def add_logbook(request):
    if request.method == 'POST':
        inventory = InventoryForm(request.POST)
        if inventory.is_valid():
            inventory.save()
            messages.success(request, 'Data Submitted')
            inventory = InventoryForm()
    else:
        inventory = InventoryForm()
    
    return render(request, 'add-logbook.html', {'invt':inventory})

@login_required
def add_info(request):
    if request.method == 'POST':
        attorney = AttorneyForm(request.POST)
        if attorney.is_valid():
            attorney.save()
            messages.success(request, 'Data Submited')
            attorney = AttorneyForm()
    else:
        attorney = AttorneyForm()
    
    return render(request, 'add-info.html', {'attn':attorney})

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/home-page/')
def view_logbook(request):
    title = 'List of Data' 
    queryset = InventoryModel.objects.all().order_by('-entry_date')
    form = InventorySearchForm(request.POST)
    context = {
                    "title": title,
                    "queryset": queryset,
                    "form": form,
                    }

    if request.method == 'POST':
        queryset = InventoryModel.objects.all().order_by('-updated_date').filter(file_no__icontains=form['file_no'].value(),case_no__icontains=form['case_no'].value())
        context = {
                    "title": title,
                    "queryset": queryset,
                    "form": form,
                    }
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Data list.csv"'
            writer = csv.writer(response)
            writer.writerow(['ENTRY_DATE', 'UPDATED_DATE', 'FILE_NO', 'CASE_NO', 'COURT', 
                                'COURT_NO', 'NO_MALE SUSPECT', 'NO_FEMALE SUSPECT', 'NO_UNDERAGE_MALE SUSPECT', 
                                'NO_UNDERAGE_FEMALE SUSPECT', 'ASSIGNED TO', 'AGENCY', 'DATE REQUEST', 
                                'STATUTORY DEADLINE', 'BAIL GRANTED', 'IN CUSTODY', 'DATE OF REMAND', 
                                'PLACE OF REMAND', 'DATE OF ADVICE', 'CASE TO ANSWER', 'ENTRY OFFICER', 'UPDATED BY'])
            instance = queryset
            for row in instance:
                writer.writerow([row.entry_date, row.updated_date, row.file_no,  row.case_no,  row.court,  
                                    row.court_no,  row.male_suspect, row.female_suspect, row.male_underage_suspect, 
                                    row.female_underage_suspect, row.assigned_to, row.agency, row.date_of_request, 
                                    row.date_of_receipt, row.st_deadline, row.bail_granted, row.in_custody, row.date_of_remand, 
                                    row.place_of_remand, row.date_of_advice, row.case_to_answer, row.entry_made_by, row.update_made_by])
            return response
    return render(request, 'view-logbook.html', context)

@login_required
def view_info(request):
    title = 'List of Data' 
    queryset = AttorneyModel.objects.all()
    form = AttorneySearchForm(request.POST)
    context = {
                    "title": title,
                    "queryset": queryset,
                    "form": form,
                    }

    if request.method == 'POST':
        queryset = AttorneyModel.objects.all().order_by('-updated_date').filter(file_no__icontains=form['file_no'].value(),case_no__icontains=form['case_no'].value())
        context = {
                    "title": title,
                    "queryset": queryset,
                    "form": form,
                    }
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Data list.csv"'
            writer = csv.writer(response)
            writer.writerow(['ENTRY_DATE', 'UPDATED_DATE', 'FILE_NO', 'CASE_NO', 'CASE_NAME', 'COURT', 
                            'AGENCY', 'NO_DEFENDANT_MALE', 'NO_DEFENDANT_FEMALE', 'NO_UNDERAGE_MALE', 
                            'NO_UNDERAGE_FEMALE', 'NO_PWDS_MALE', 'NO_PWDS_FEMALE', 
                            'COUNSEL_NAME', 'COUNSEL_TELEPHONE', 'ADJOURN_DATE', 'REASON_FOR_ADJOURNMENT', 
                            'STAGE_OF_PROCEEDINGS', 'IS DEFENDANT IN CUSTODY', 'HAS BAIL BEEN REVOKED', 'DISPOSAL', 
                            'LEAD COUNSEL', 'ENTRY_BY','UPDATED_BY'])
            instance = queryset
            for row in instance:
                writer.writerow([row.entry_date, row.updated_date, row.file_no,  row.case_no,  row.case_name, row.court,  
                                row.agency,  row.no_defendant_male, row.no_defendant_female, row.no_underage_male, 
                                row.no_underage_female, row.no_pwds_male, row.no_pwds_female, 
                                row.counsel_name, row.counsel_telephone, row.adjourn_date, row.reason_for_adjournment, 
                                row.stage_of_proceedings, row.is_defendant_in_custody, row.has_bail_been_revoked, row.disposal, 
                                row.lead_counsel, row.entry_made_by, row.update_made_by])
            return response
    return render(request, 'view-info.html', context)



@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='/home-page/')
def edit_logbook(request, id=None):  
    instance = get_object_or_404(InventoryModel, id=id)
    inventory = InventoryForm(request.POST or None, instance=instance)
    if inventory.is_valid():
        instance = inventory.save(commit=False)
        instance.save()
        return redirect('/view-page')
    context = {
            "title": 'Edit ' + str(instance.file_no),
            "instance": instance,
            "invt": inventory,
        }
    return render(request, "add-logbook.html", context)


@login_required
def edit_info(request, id=None):  
    instance = get_object_or_404(AttorneyModel, id=id)
    attorney = AttorneyForm(request.POST or None, instance=instance)
    if attorney.is_valid():
        instance = attorney.save(commit=False)
        instance.save()
        return redirect('/view-infopage')
    context = {
            "title": 'Edit ' + str(instance.file_no),
            "instance": instance,
            "attn": attorney,
        }
    return render(request, "add-info.html", context)



@login_required
def delete_logbook(request, id=None):  
    instance = get_object_or_404(InventoryModel, id=id)
    instance.delete()
    return redirect("/view-page")
    
@login_required
def delete_info(request, id=None):  
    instance = get_object_or_404(AttorneyModel, id=id)
    instance.delete()
    return redirect("/view-infopage")

