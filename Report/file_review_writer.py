import datetime
import os

from Log.logger_config import logger, error_handler
from Report.summary_writer import write_summary
    
def get_current_datetime():
    """Obtenir la date et l'heure actuelles"""
    return datetime.datetime.now().strftime("%d-%m-%Y-%H-%M")

def generate_output_filename(config) -> str:
    """Générer le nom du fichier de sortie"""
    return f"review_results_{get_current_datetime()}.{config.get('format')}"

def write_results(results, report_file) -> None:
    """Écrire les résultats dans le fichier de rapport"""
    report_file.write("\n=== Results ===\n\n")
    for file, result in sorted(results.items()):
        report_file.write(f"{file} : {result}\n")
    report_file.write("\n" + "=" * 18 + "\n\n")

def write_report(results, statistics, config) -> None:

    try:
        os.makedirs(config.get("outputDir"), exist_ok=True)
        output_file_name = os.path.join(config.get("outputDir"), generate_output_filename(config))

        with open(output_file_name, 'w', encoding='utf-8') as report_file:
            report_file.write("=== Code Review Report ===\n\n")
            write_summary(statistics, report_file)
            write_results(results, report_file)


    except Exception as e:
        logger.error(f"Erreur lors de l'écriture du rapport : {str(e)}")