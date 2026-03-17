import re

def extract_medical_info(text):
    diseases = []
    medications = []
    lab_results = []

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        # ❌ Skip useless lines
        if any(word in line.lower() for word in [
            "method", "page", "range", "years", "day", "month"
        ]):
            continue

        # -------- LAB RESULTS --------
        lab_match = re.search(
            r"([A-Za-z ,()]+)\s+([\d.]+)\s*(mg/dl|gm/dl|IU/L)?",
            line
        )

        if lab_match:
            name = lab_match.group(1).strip()
            value = lab_match.group(2).strip()
            unit = lab_match.group(3) if lab_match.group(3) else ""

            # filter noise
            if len(name) > 3 and not name.lower().startswith(("test", "report")):
                lab_results.append(f"{name}: {value} {unit}")
            continue

        # -------- DISEASE --------
        if any(d in line.lower() for d in ["diabetes", "hypertension"]):
            diseases.append(line)

        # -------- MEDICATION --------
        if line.startswith("-") and len(line) < 40:
            medications.append(line.replace("-", "").strip())

    return {
        "diseases": diseases,
        "medications": medications,
        "lab_results": lab_results
    }