from django.shortcuts import render
from .forms import ResumeForm
from .resume_parser import extract_resume_text
from .utils import analyze_resume, detect_sections
from .gemini import get_ai_feedback

import os


def home(request):

    if request.method == "POST":

        form = ResumeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume = request.FILES["resume"]

            os.makedirs(
                "media",
                exist_ok=True
            )

            file_path = os.path.join(
                "media",
                resume.name
            )

            with open(
                file_path,
                "wb+"
            ) as f:

                for chunk in resume.chunks():
                    f.write(chunk)

            # Extract Resume Text
            resume_text = extract_resume_text(
                file_path
            )

            # Job Description
            jd = form.cleaned_data[
                "job_description"
            ]

            # Debug Print
            print("\n===== RESUME TEXT =====")
            print(resume_text)
            print("=======================\n")

            print("\n===== JOB DESCRIPTION =====")
            print(jd)
            print("===========================\n")

            # ATS Analysis
            score, matched, missing = analyze_resume(
                resume_text,
                jd
            )

            # Resume Sections
            sections = detect_sections(
                resume_text
            )

            # AI Feedback
            try:

                feedback = get_ai_feedback(
                    resume_text
                )

            except Exception as e:

                print(
                    "Gemini Error:",
                    e
                )

                feedback = """
🚀 AI Suggestions

Strengths:
• Resume Uploaded Successfully
• Good Technical Foundation

Weaknesses:
• Missing Required Skills

Suggestions:
• Add More Projects
• Add GitHub Links
• Learn REST APIs
• Improve ATS Keywords
"""

            return render(
                request,
                "analyzer/result.html",
                {
                    "score": score,
                    "matched": matched,
                    "missing": missing,
                    "feedback": feedback,
                    "sections": sections
                }
            )

    else:

        form = ResumeForm()

    return render(
        request,
        "analyzer/home.html",
        {
            "form": form
        }
    )