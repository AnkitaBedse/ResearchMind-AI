def clean_text(text: str):

    text = text.strip()

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = " ".join(line.strip().split())

        if line:
            cleaned_lines.append(line)

    cleaned_text = "\n".join(cleaned_lines)

    return cleaned_text