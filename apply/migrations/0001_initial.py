# Generated by Django 3.1.6 on 2021-02-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_num', models.IntegerField(verbose_name='모집 기수')),
                ('poster', models.ImageField(upload_to='season/poster', verbose_name='모집 포스터')),
                ('session_start_date', models.DateField(verbose_name='세션 시작일')),
                ('session_end_date', models.DateField(verbose_name='세션 종료일')),
                ('meeting_date1', models.DateField(blank=True, null=True, verbose_name='면접 후보일 1')),
                ('meeting_date2', models.DateField(blank=True, null=True, verbose_name='면접 후보일 2')),
                ('meeting_date3', models.DateField(blank=True, null=True, verbose_name='면접 후보일 3')),
                ('doc_screening_info', models.TextField(blank=True, null=True, verbose_name='서류전형 관련 추가 안내')),
                ('doc_screening_start', models.DateTimeField(verbose_name='서류전형 지원 시작일시')),
                ('doc_screening_end', models.DateTimeField(verbose_name='서류전형 지원 마감일시')),
                ('question1', models.TextField(verbose_name='서류전형 문제1')),
                ('question2', models.TextField(verbose_name='서류전형 문제2')),
                ('question3', models.TextField(verbose_name='서류전형 문제3')),
                ('question4', models.TextField(verbose_name='서류전형 문제4')),
                ('question5', models.TextField(verbose_name='서류전형 문제5')),
                ('coding_test', models.TextField(verbose_name='코딩테스트 문제')),
                ('doc_meeting_info', models.TextField(blank=True, null=True, verbose_name='면접전형 관련 추가 안내')),
                ('doc_result_start', models.DateTimeField(verbose_name='서류전형 결과 발표 시작일시')),
                ('doc_result_end', models.DateTimeField(verbose_name='서류전형 결과 발표 마감일시')),
                ('final_info', models.TextField(blank=True, null=True, verbose_name='최종발표 관련 추가 안내')),
                ('final_result_open', models.DateTimeField(verbose_name='최종발표 시작일시')),
                ('final_result_close', models.DateTimeField(verbose_name='최종발표 마감일시')),
                ('workshop_date', models.DateTimeField(verbose_name='워크샵 요일')),
                ('workshop_place', models.CharField(max_length=50, verbose_name='워크샵 장소')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image', verbose_name='코딩테스트 문제 관련 이미지')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='apply.season', verbose_name='모집 기수')),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('doc_pass', models.BooleanField(default=False, verbose_name='서류전형 합격')),
                ('meeting_date_time', models.DateTimeField(blank=True, null=True, verbose_name='지원자 면접시간')),
                ('final_pass', models.BooleanField(default=False, verbose_name='최종 합격')),
                ('school', models.CharField(max_length=20, verbose_name='학교')),
                ('major', models.CharField(max_length=20, verbose_name='전공')),
                ('major_grade', models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('5학년 이상', '5학년 이상'), ('졸업생', '졸업생'), ('대학원생', '대학원생')], max_length=10, verbose_name='전공 학년')),
                ('sub_major', models.CharField(blank=True, max_length=20, null=True, verbose_name='부전공')),
                ('sub_major_semester', models.IntegerField(blank=True, choices=[(1, '1학기'), (2, '2학기'), (3, '3학기'), (4, '4학기'), (5, '5학기'), (6, '6학기')], null=True, verbose_name='부전공 이수 학기')),
                ('address', models.CharField(max_length=100, verbose_name='거주지')),
                ('phone_number', models.CharField(max_length=15, verbose_name='전화번호')),
                ('avail_meeting_time', models.CharField(choices=[], max_length=30, verbose_name='면접 가능 일자')),
                ('answer1', models.TextField(verbose_name='서류전형 문제1 답안')),
                ('answer2', models.TextField(verbose_name='서류전형 문제2 답안')),
                ('answer3', models.TextField(verbose_name='서류전형 문제3 답안')),
                ('answer4', models.TextField(verbose_name='서류전형 문제4 답안')),
                ('answer5', models.TextField(verbose_name='서류전형 문제5 답안')),
                ('code', models.TextField(verbose_name='코딩테스트 답안')),
                ('participate_check', models.CharField(choices=[('예', '예'), ('아니오', '아니오')], max_length=10, verbose_name='모든 일정 참석 여부')),
                ('workshop_check', models.CharField(choices=[('예', '예'), ('아니오', '아니오')], max_length=10, verbose_name='워크샵 참석 여부')),
                ('info_check', models.CharField(choices=[('동의', '동의'), ('비동의', '비동의')], max_length=10, verbose_name='개인정보 이용 동의')),
                ('deposit_check', models.CharField(choices=[('동의', '동의'), ('비동의', '비동의')], max_length=10, verbose_name='보증금 납부 동의')),
                ('know_check', models.CharField(choices=[('sns', '피로그래밍 공식 SNS(예 - 페이스북, 인스타그램)'), ('cafe community', '네이버 카페/동아리 관련 커뮤니티(예 - 스펙업, 링커리어, 캠퍼스픽'), ('everytime', '에브리타임'), ('friends', '지인의 소개'), ('others', '기타')], max_length=50, verbose_name='피로그래밍 알게 된 경로')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='apply.season', verbose_name='모집기수')),
            ],
        ),
    ]
