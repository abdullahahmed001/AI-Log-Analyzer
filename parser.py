def analyze_logs(filepath):

    errors = []
    warnings = []

    with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:

            line = line.strip().upper()

            if "ERROR" in line:
                errors.append(line)

            elif "WARNING" in line:
                warnings.append(line)

    return {
        "total_lines": len(errors) + len(warnings),
        "errors": errors,
        "warnings": warnings,
        "error_count": len(errors),
        "warning_count": len(warnings)
    }