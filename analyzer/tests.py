from django.test import TestCase
from .utils import analyze_resume


class ResumeAnalyzerTest(TestCase):

    def test_python_match(self):

        resume = """
        Python Django SQL React
        """

        jd = """
        Python Django SQL React
        """

        score, matched, missing = analyze_resume(
            resume,
            jd
        )

        self.assertEqual(score, 100)

    def test_java_no_match(self):

        resume = """
        Java Spring Boot
        """

        jd = """
        Python Django SQL
        """

        score, matched, missing = analyze_resume(
            resume,
            jd
        )

        self.assertEqual(score, 0)
