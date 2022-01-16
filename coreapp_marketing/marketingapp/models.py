from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING



# Create your models here.

# registration details
class marketing_reg_details(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    designation = models.CharField(max_length=200) # marketing TL / data collector / marketing executive

# product details
class Products(models.Model):
    productname = models.CharField(max_length=200)
    date = models.DateField()   # Will clarify what date it is
    target = models.IntegerField()
    description = models.TextField()

# recruitment details
class Recruitments(models.Model):
    jobpostname = models.CharField(max_length=200)
    date = models.DateField()
    vacancies = models.IntegerField()
    qualifications = models.CharField(max_length=200)
    jobdescription = models.TextField()


#product task shared to data collector
class TL_prod_to_datacollect(models.Model):
    product = models.ForeignKey(Products, on_delete=CASCADE)
    collector = models.ForeignKey(marketing_reg_details, on_delete=CASCADE)

#recruitment task shared to data collector
class TL_recr_to_datacollect(models.Model):
    recruitment = models.ForeignKey(Recruitments, on_delete=CASCADE)
    collector = models.ForeignKey(marketing_reg_details, on_delete=CASCADE)    

#data collected on each product
class prod_datacollected(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phno = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    product = models.ForeignKey(Products, on_delete=CASCADE)
    exec_assigned = models.ForeignKey(marketing_reg_details, on_delete=DO_NOTHING, null=True)    
    status = models.BooleanField(null=True)

#data collected on each job applicant
class jobapplicant_datacollected(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phno = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    fresher_or_exp = models.CharField(max_length=200) # Will confirm whether  it is simply 'experienced' or '2 years experience'
    recruitment = models.ForeignKey(Recruitments, on_delete=CASCADE)
    exec_assigned = models.ForeignKey(marketing_reg_details, on_delete=DO_NOTHING, null=True)    
    status = models.BooleanField()    

# Have some doubts regarding the existing reports table structure. Will give answer tomorrow. For  now, work with the following table:

#report issues model
class hr_report(models.Model):
    issue = models.TextField()
    reported_date = models.DateField()
    reported_by = models.ForeignKey(marketing_reg_details, on_delete=CASCADE)
    hr_reply = models.TextField()


#attendance
class attendance(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=200)
    logintime = models.CharField(max_length=200)
    logouttime = models.CharField(max_length=200)
    reg = models.ForeignKey(marketing_reg_details, on_delete=CASCADE) # Will automatically turn into reg_id in database    

