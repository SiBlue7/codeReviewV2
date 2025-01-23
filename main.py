import os
import json

from Log.logger_config import setup_logging
from Functionality.check_config import check_config
from Report.file_review_writer import write_report


def load_config(config_path="config.json"):
    if os.path.exists(config_path):
        with open(config_path, 'r') as file:
            return json.load(file)
    return {}

def code_review(config):
    """Fonction principale de revue de code"""
    results, statistics = check_config(config)

    write_report(results, statistics, config)


def main():
    """Point d'entrée principal"""
    try:

        # Configurer le logging
        logger = setup_logging(verbose=True)
        
        config = load_config()
        project_path = config.get("projectPath")

        logger.info(f"Starting code review for {project_path}")

        code_review(config)

        logger.info("Code review completed successfully")



    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

if __name__ == "__main__":
    main()