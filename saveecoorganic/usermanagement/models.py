from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ("Active", "Active"),
    ("Pending", "Pending"),
    ("Blocked", "Blocked"),
)
MARITAL_STATUS_CHOICES = (
    ("Married", "Married"),
    ("Un-Married", "Un-Married"),
)

GENDER_CHOICES = (
    ("M", "Male"),
    ("F", "Female"),
)

Relation = (
    ("mother", "Mother"),
    ("father", "Father"),
    ("others", "others"),
)



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UserBaseModel(BaseModel):
    name = models.CharField(max_length=255)  # Required
    mobile = models.CharField(max_length=255)  # Required
    alt_mobile = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    gen_info_complete = models.BooleanField(default=False)
    kyc_done = models.BooleanField(default=False)
    is_number_verified = models.BooleanField(default=False)

    class Meta:
        abstract = True



class UserAccount(UserBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    sponsor = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="Placement",
        blank=True,
        null=True,
    )  # Required
    referral = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="Direct", blank=True, null=True
    )  # Required
    position = models.CharField(max_length=6)  # Required
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Active")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    dob = models.DateField(null=True, blank=True)
    father = models.CharField(max_length=255, null=True, blank=True)
    is_married = models.CharField(
        max_length=12, choices=MARITAL_STATUS_CHOICES, default="Un-Married"
    )
    anniversary = models.DateField(null=True, blank=True)
    nominee_name = models.CharField(max_length=255, null=True, blank=True)
    relation = models.CharField(max_length=10, choices=Relation, default="mother")
    bank_name = models.CharField(max_length=255 , null=True, blank=True)
    account_holder_name = models.CharField(max_length=255 , null=True, blank=True)
    account_number = models.CharField(max_length=255 , null=True, blank=True)
    ifsc_code = models.CharField(max_length=255, null=True, blank=True)
    branch = models.CharField(max_length=255, null=True, blank=True)
    pan = models.CharField(max_length=255, null=True, blank=True)
    aadhar = models.CharField(max_length=255, null=True, blank=True)
    pan_image = models.ImageField(upload_to="kyc_images/" , null=True, blank=True)
    aadhar_image = models.ImageField(upload_to="kyc_images/" , null=True, blank=True)

    def __str__(self):
        return self.user.username

class MixMatchingCount(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    left_count = models.IntegerField(default=0)
    right_count = models.IntegerField(default=0)
    left_pair = models.IntegerField(default=0)
    right_pair = models.IntegerField(default=0)
    total_pair = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class UserWallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    wallet_amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username

class StoreDetails(UserBaseModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    proprietor_name = models.CharField(max_length=100, default="Save Eco Organic")
    mobile = models.CharField(max_length=255)  # Required
    alt_mobile = models.CharField(max_length=255, blank=True, null=True)
    gst = models.CharField(max_length=255, null=True)
    gst_doc = models.FileField(null=True, upload_to="store/")
    lat_long = models.CharField(max_length=255, null=True)
    is_number_verified = models.BooleanField(default=False)
    store_under = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name="stores",
        blank=True,
        null=True,
        limit_choices_to={"store": True},
    )

    ROLE_CHOICES = (
        ("EC", "ECO CENTER"),
        ("ST", "STOCKIST"),
        ("DS", "DISTRIBUTOR"),
    )

    role = models.CharField(choices=ROLE_CHOICES, default="EC", max_length=20)
    def __str__(self):
        return self.user.username