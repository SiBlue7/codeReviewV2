from typing import List, Tuple
from pathlib import Path

from Log.logger_config import logger, error_handler
from Functionality.count_logic import file_walker

@error_handler
def check_todo(file_path: str) -> List[Tuple[int, str]]:
    """Recherche les lignes contenant des TODO dans un fichier."""
    TODO_PATTERNS = ['TODO', 'TO DO', 'todo']
    try:
        todo_lines = []
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for i, line in enumerate(f, start=1):
                if any(pattern in line for pattern in TODO_PATTERNS):
                    todo_lines.append((i, line.strip()))
        return todo_lines
    except Exception as e:
        logger.error(f"\nErreur lors de la lecture du fichier {file_path}: {str(e)}\n")
        return []
    
@file_walker
def count_todo_files(file_path: Path) -> int:
    """
    Compte le nombre de fichiers contenant des TODOs.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        int: 1 si le fichier contient des TODOs, 0 sinon
    """
    return 1 if check_todo(file_path) else 0