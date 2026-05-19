def extract_sections(text):

    sections = {
        "abstract": "",
        "methodology": "",
        "conclusion": ""
    }

    lower_text = text.lower()

    if "abstract" in lower_text:
        start = lower_text.find("abstract")
        sections["abstract"] = text[start:start+3000]

    if "methodology" in lower_text:
        start = lower_text.find("methodology")
        sections["methodology"] = text[start:start+5000]

    if "conclusion" in lower_text:
        start = lower_text.find("conclusion")
        sections["conclusion"] = text[start:start+3000]

    return sections
