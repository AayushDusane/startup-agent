def parse_title(raw_text):
    """
    Example formats:
    'Stripe — Software Engineer'
    'OpenAI — Research Intern'
    """
    company = ""
    role = raw_text

    if "—" in raw_text:
        parts = raw_text.split("—", 1)
        company = parts[0].strip()
        role = parts[1].strip()

    return company, role
