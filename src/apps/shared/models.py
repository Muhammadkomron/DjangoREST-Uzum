from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def delete(self, using=None, keep_parents=False):
        """object instance never gets deleted really"""
        self.is_active = False
        self.save()

    class Meta:
        abstract = True


class LanguageChoices(models.TextChoices):
    RU = "🇷🇺 Русский", "ru"
    UZ = "🇺🇿 O`zbekcha", "uz"
