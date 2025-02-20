from django.db import models

# 1️⃣ Hero Section
class HeroSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="Main Title")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtitle")
    background_image = models.ImageField(upload_to="uploads/hero/", verbose_name="Background Image")

    def __str__(self):
        return self.title

# 2️⃣ About Section
class AboutSection(models.Model):
    title = models.CharField(max_length=255, verbose_name="Section Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(upload_to="uploads/about/", blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.title

# 3️⃣ Activities Section
class Activity(models.Model):
    title = models.CharField(max_length=255, verbose_name="Activity Title")
    description = models.TextField(verbose_name="Activity Description")
    image = models.ImageField(upload_to="uploads/activities/", blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.title

# 4️⃣ Events Section
class Event(models.Model):
    title = models.CharField(max_length=255, verbose_name="Event Title")
    description = models.TextField(verbose_name="Event Description")
    date = models.DateTimeField(verbose_name="Event Date")
    image = models.ImageField(upload_to="uploads/events/", blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.title

# 5️⃣ Sermons (e.g., Friday Khutbah)
class Sermon(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sermon Title")
    speaker = models.CharField(max_length=255, verbose_name="Speaker Name")
    date = models.DateTimeField(verbose_name="Sermon Date")
    audio_file = models.FileField(upload_to="uploads/sermons/", blank=True, null=True, verbose_name="Audio File")
    description = models.TextField(verbose_name="Sermon Description")

    def __str__(self):
        return f"{self.title} - {self.speaker}"

# 6️⃣ Blog Section
class BlogPost(models.Model):
    title = models.CharField(max_length=255, verbose_name="Blog Title")
    content = models.TextField(verbose_name="Content")
    author = models.CharField(max_length=255, verbose_name="Author")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Published Date")
    image = models.ImageField(upload_to="uploads/blog/", blank=True, null=True, verbose_name="Image")

    def __str__(self):
        return self.title

# 7️⃣ Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    role = models.CharField(max_length=255, verbose_name="Role/Position")
    image = models.ImageField(upload_to="uploads/team/", blank=True, null=True, verbose_name="Profile Image")
    bio = models.TextField(verbose_name="Short Bio")

    def __str__(self):
        return self.name

# 8️⃣ Testimonials
class Testimonial(models.Model):
    name = models.CharField(max_length=255, verbose_name="Person's Name")
    feedback = models.TextField(verbose_name="Testimonial / Feedback")
    image = models.ImageField(upload_to="uploads/testimonials/", blank=True, null=True, verbose_name="Image (Optional)")

    def __str__(self):
        return self.name

    
# 9️⃣ Topbar / Header 
class Header(models.Model):
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    email = models.EmailField(blank=True, null=True, verbose_name="Email Address")

    def __str__(self):
        return "Website Topbar Settings"
    

# Navbar 
class NavbarItem(models.Model):
    title = models.CharField(max_length=255, verbose_name="Link Name")
    url = models.CharField(max_length=255, verbose_name="URL")

    def __str__(self):
        return self.title


