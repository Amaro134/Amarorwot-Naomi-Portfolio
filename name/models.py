from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('data', 'Data'),
        ('tools', 'Tools'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, default='Present')
    is_current = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return f"{self.title} at {self.company}"


class ExperienceBullet(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:60]


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=500, blank=True)
    github_url = models.CharField(max_length=500, blank=True)
    live_url = models.CharField(max_length=500, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Stat(models.Model):
    value = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value} {self.label}"
