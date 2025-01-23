from pathlib import Path
from typing import List, Iterator

from Log.logger_config import setup_logging, logger


def check_valid_files(project_path, valid_extensions) -> Iterator[Path]:
    """Filtre les fichiers valides une seule fois"""
    try:
        base_path = Path(project_path).resolve()  # resolve() normalise le chemin
        if not base_path.exists():
            logger.error(f"Le dossier du projet n'existe pas : {base_path}")
            return iter([])

        return (
            file
            for file in Path(project_path).rglob("*")
            if file.suffix in valid_extensions
        )

    except Exception as e:
            logger.error(f"Erreur lors de la recherche des fichiers : {str(e)}")

def get_valid_files_list(project_path, valid_extensions) -> List[str]:
    """Filtre les fichiers valides et les renvoie sous forme de liste"""
    return [str(file.absolute()) for file in check_valid_files(project_path, valid_extensions)]

def print_valid_files_list(valid_files: List[str]) -> None:
    """Affiche la liste des fichiers valides"""
    print("Fichiers valides :")
    for file in valid_files:
        print(file)