from django.db import models
from django.utils import timezone
import re

# Create your models here.
class Person(models.Model):
    dna = models.CharField(max_length=42, unique=True)
    is_mutant = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.dna
    
    @staticmethod
    def isMutant(cadenas):
        n = len(cadenas)
        for i in range(n):
            if(re.search(r'(.)\1{3}', cadenas[i])):
                return True
            for j in range(len(cadenas[i])):
                if i < n-3 and j < len(cadenas[i])-3:
                    if len(set(cadenas[i+k][j+k] for k in range(4))) == 1:
                        return True
                if i < n-3 and j >= 3:
                    if len(set(cadenas[i+k][j-k] for k in range(4))) == 1:
                        return True
        return False
    
class Stats(models.Model):
    count_mutant_dna = models.IntegerField(default=0)
    count_human_dna = models.IntegerField(default=0)
    ratio = models.FloatField(default=0)

    @classmethod
    def get_instance(cls):
        instance, _ = cls.objects.get_or_create(id=1)
        return instance

    def save(self, *args, **kwargs):
        self.id = 1
        super().save(*args, **kwargs)

    def update_data(self, is_mutante):
        if is_mutante:
            self.count_mutant_dna += 1
        else:
            self.count_human_dna += 1

        if (self.count_human_dna > 0):
            self.count_human_dna = self.count_mutant_dna / self.count_human_dna

        self.save()