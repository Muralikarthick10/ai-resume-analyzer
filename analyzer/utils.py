skills = [
    "python",
    "django",
    "flask",
    "java",
    "spring",
    "spring boot",
    "hibernate",
    "mysql",
    "postgresql",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "bootstrap",
    "git",
    "github",
    "rest api"
]


def analyze_resume(resume_text, jd):

    resume_text = resume_text.lower()
    jd = jd.lower()

    # Skills found in Job Description
    jd_skills = []

    for skill in skills:
        if skill in jd:
            jd_skills.append(skill)

    # Matched Skills
    matched = []

    for skill in jd_skills:
        if skill in resume_text:
            matched.append(skill)

    # Missing Skills
    missing = []

    for skill in jd_skills:
        if skill not in matched:
            missing.append(skill)

    # ATS Score based on JD requirements
    if len(jd_skills) > 0:
        score = round(
            (len(matched) / len(jd_skills)) * 100
        )
    else:
        score = 0

    print("JD Skills:", jd_skills)
    print("Matched:", matched)
    print("Missing:", missing)
    print("Score:", score)

    return score, matched, missing


def detect_sections(resume_text):

    text = resume_text.lower()

    sections = {
        "Education": "education" in text,
        "Skills": "skills" in text,
        "Projects": "project" in text,
        "Experience": "experience" in text,
        "Certifications":
            "certification" in text
            or "certificate" in text
    }

    return sections