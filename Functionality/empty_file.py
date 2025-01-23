import os
from pathlib import Path
from typing import List

from Log.logger_config import error_handler, logger
from Functionality.count_logic import file_walker

@error_handler
def is_empty_file(file_path: str) -> bool:
    """Vérifie si un fichier est vide en vérifiant sa taille."""
    try:
        return os.stat(file_path).st_size == 0
    except OSError as e:
        logger.error(f"\nErreur lors de la vérification du fichier {file_path}: {str(e)}\n")
        raise

def is_empty_files_list(file_paths: List[str]) -> List[str]:
    """Vérifie quels fichiers sont vides dans une liste de chemins."""
    empty_files = []
    for file_path in file_paths:
        if is_empty_file(file_path):
            empty_files.append(file_path)
    return empty_files

@file_walker
def count_empty_files(file_path: Path) -> int:
    """
    Compte le nombre de fichiers vides dans le projet.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        int: 1 si le fichier est vide, 0 sinon
    """
    return 1 if is_empty_file(file_path) else 0

def get_number_of_empty_files(file_path: Path) -> int:
    """
    Getter pour récupérer le nombre de fichiers vides.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        int: Nombre de fichiers vides dans le projet
    """
    return count_empty_files(file_path) + " empty files\n"

def write_empty_files(file_path: List[str]) -> None:
    """
    Écrit la liste des fichiers vides dans un fichier.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
    """
    with open("empty_files.txt", "w") as f:
        f.write("Empty files detected:\n")
        for file in file_path:
            f.write(f"- {file}\n")
        f.write(f"Number of empty files: {len(is_empty_file)}\n")
    print(f"Empty files detected: {is_empty_file}\nNumber of empty files: {len(is_empty_file)}")