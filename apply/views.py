from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Season, Image, Applicant
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .forms import ApplyForm, ApplyConfirm
from django.contrib import messages

def main(request):

    try:
        season = Season.objects.order_by('-created_at').first()
    except ObjectDoesNotExist:
        msg = "모집 중인 기수가 없습니다"
        messages.error(request, msg)
        return redirect(reverse('main:main_page'))
    
    number = season.season_num
    img = season.poster
    now = timezone.now()
    print(now)
    if now<=season.doc_screening_end and now>=season.doc_screening_start:
        status = "doc"
        notify_date = None
    elif now<season.doc_result_start and now>season.doc_screening_end:
        status = "doc_result_waiting"
        notify_date = season.doc_result_start
    elif now>=season.doc_result_start and now<=season.doc_result_end:
        status = "doc_result"
        notify_date = None
    elif now>season.doc_result_end and now<season.final_result_open:
        status = "final_result_waiting"
        notify_date = season.final_result_open
    elif now>=season.final_result_open and now<=season.final_result_close:
        status = "final"
        notify_date = None
    else:
        msg = "지원 기간이 아닙니다!"
        messages.error(request, msg)
        return redirect(reverse('main:main_page'))

    print(img)

    ctx = {
        'number' : number,
        'img' : img,
        'status' : status,
        'notify_date' : notify_date,
    }
    return render(request, 'apply/apply_main.html', ctx)
    
def apply(request):
    try:
        season = Season.objects.order_by('-created_at').first()
    except ObjectDoesNotExist:
        msg = "모집 중인 기수가 없습니다"
        messages.error(request, msg)
        return redirect(reverse('apply:main'))
    print("왔다")
    now = timezone.now()
    if now<=season.doc_screening_end and now>=season.doc_screening_start:
        print("여기도")
        status = "doc"
        if request.method == 'POST':
            form = ApplyForm(request.POST)
            if form.is_valid():
                new_applicant = Applicant(**form.cleaned_data)
                new_applicant.season = season
                new_applicant.save()
                msg = "지원이 완료되었습니다! 지원 상태 확인을 통해서 추가 확인 해주세요!"
                print(msg)
                messages.success(request, msg)
            else:
                msg = "오류가 발생했습니다. 지원서를 다시 작성해주세요"
                messages.error(request, msg)
            
            return redirect(reverse('apply:main'))
        else:
            form = ApplyForm()
            ctx ={
                'form':form,
            }
            return render(request, 'apply/application.html', ctx)
    else:
        msg = "지금은 지원 기간이 아닙니다!"
        messages.error(request, msg)
    
        return redirect(reverse('apply:main'))


def applyConfirm(request):
    season = Season.objects.order_by('-created_at').first()
    if request.method == 'GET':
        form = ApplyConfirm()
        ctx={
            'form':form,
        }
        return render(request, 'apply/applyconfirm.html', ctx)
    else:
        form = ApplyConfirm(request.POST)
        print(form)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            phone_number = form.cleaned_data.get('phone_number')
            print(name, phone_number)
            try:
                applicant = Applicant.objects.get(season__season_num = season.season_num, name=name, phone_number=phone_number)
                print(applicant)
                apply_date = applicant.created_at.date()
                msg = f'{name}님의 {apply_date} 피로그래밍 서류 전형 지원 이력이 확인되었습니다'
            except ObjectDoesNotExist:
                msg = "서류전형 지원 이력이 없습니다! 피로그래밍에 지원해주세요"

            messages.error(request, msg)
            return redirect(reverse('apply:applyconfirm'))
        else:
            msg = "확인에 오류가 있습니다! 다시 입력해 주세요"
            messages.error(request, msg)
            return redirect(reverse('apply:applyconfirm'))
