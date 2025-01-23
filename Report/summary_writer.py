from pathlib import Path

def write_summary(statistics: dict, report_file: Path) -> None:
    """Écrire le résumé des statistiques dans le fichier de rapport"""
    report_file.write("\n=== Statistics ===\n\n")
    for key, value in statistics.items():
        report_file.write(f"{key} : {value}\n")
    report_file.write("\n" + "=" * 18 + "\n\n")