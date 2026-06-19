from django.db import models


class ResumeAnalysis(models.Model):

    score = models.IntegerField()

    matched_skills = models.TextField()

    missing_skills = models.TextField()

    feedback = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"ATS Score {self.score}"