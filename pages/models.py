from django.db import models

class Header(models.Model):
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone Number",
        help_text="Enter phone number in international format (+XXX...)",
        default="+0123456789"
    )
    
    email = models.EmailField(
        verbose_name="Email Address",
        default="info@example.com"
    )
    
    facebook_url = models.URLField(
        verbose_name="Facebook URL",
        blank=True,
        null=True
    )
    
    twitter_url = models.URLField(
        verbose_name="Twitter URL",
        blank=True,
        null=True
    )
    
    linkedin_url = models.URLField(
        verbose_name="LinkedIn URL",
        blank=True,
        null=True
    )
    
    instagram_url = models.URLField(
        verbose_name="Instagram URL",
        blank=True,
        null=True
    )
    
    signup_url = models.URLField(
        verbose_name="Signup/Login URL",
        blank=True,
        null=True,
        default="/auth/login",
        help_text="Leave empty to hide signup link"
    )

    class Meta:
        verbose_name = "Header Settings"
        verbose_name_plural = "Header Settings"

    def __str__(self):
        return "Header Configuration"
    

class Footer(models.Model):
    newsletter_title = models.CharField(max_length=100, verbose_name="Newsletter Title")
    newsletter_description = models.TextField(verbose_name="Newsletter Description")
    address = models.TextField(verbose_name="Address")
    phone = models.CharField(max_length=20, verbose_name="Phone Number")
    map_link = models.URLField(verbose_name="Map Link", blank=True)
    copyright_text = models.TextField(verbose_name="Copyright Text")
    design_credit = models.TextField(verbose_name="Design Credit")
    
    class Meta:
        verbose_name = "Footer Settings"
        verbose_name_plural = "Footer Settings"

    def __str__(self):
        return "Footer Configuration"

class FooterLink(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=50, verbose_name="Link Title")
    url = models.CharField(max_length=200, verbose_name="Link URL")
    order = models.PositiveIntegerField(default=0, verbose_name="Order")

    class Meta:
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"
        ordering = ['order']

    def __str__(self):
        return self.title
