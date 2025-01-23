from typing import List, Optional, Tuple, Dict, Union
from langdetect import detect, LangDetectException
from pathlib import Path
from collections import Counter

from Log.logger_config import logger, error_handler
from Functionality.count_logic import file_walker
from Functionality.empty_file import is_empty_file
from Const.const import COMMENT_PATTERN

@error_handler
def is_comment_only(file_path: str) -> bool:
    """Vérifie si un fichier ne contient que des commentaires."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            # Ignorer les lignes vides en plus des commentaires
            non_comment_lines = [line for line in lines 
                               if not COMMENT_PATTERN.match(line.strip()) 
                               and line.strip()]
            return len(non_comment_lines) == 0
    except Exception as e:
        logger.error(f"\nErreur lors de la lecture du fichier {file_path}: {str(e)}\n")
        return False
    
def is_comment_only_list(file_paths: List[str]) -> List[str]:
    """Retourne la liste des fichiers qui ne contiennent que des commentaires."""
    comment_only_files = []
    for file_path in file_paths:
        if is_empty_file(file_path):
            continue
        if is_comment_only(file_path):
            comment_only_files.append(file_path)
    return comment_only_files
    
@file_walker
def count_comment_only_files(file_path: Path) -> int:
    """
    Compte le nombre de fichiers contenant uniquement des commentaires.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        int: 1 si le fichier contient uniquement des commentaires, 0 sinon
    """
    return 1 if is_comment_only(file_path) and not is_empty_file(file_path) else 0
    

@error_handler
def detect_comment_language(file_path: str) -> Optional[str]:
    """Détecte la langue des commentaires dans un fichier."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            comments = [line.strip() for line in f 
                       if COMMENT_PATTERN.match(line.strip())]

        if comments:
            try:
                comments_text = ' '.join(comments)
                return detect(comments_text)
            except LangDetectException:
                logger.warning(f"\nImpossible de détecter la langue dans {file_path}\n")
                return "Unknown"
        return None
    except Exception as e:
        logger.error(f"\nErreur lors de la lecture du fichier {file_path}: {str(e)}\n")
        return None
    
def count_comment_language_en_fr(project_path: Union[str, Path]) -> Dict[str, int]:
    """
    Compte le nombre de fichiers par langue de commentaires (français/anglais).
    
    Args:
        project_path (Union[str, Path]): Chemin du projet à analyser
        
    Returns:
        Dict[str, int]: Dictionnaire contenant le compte pour chaque langue
    """
    try:
        project_path = Path(project_path)
        if not project_path.exists():
            raise FileNotFoundError(f"\nProject path does not exist: {project_path}\n")

        comment_languages = Counter()
        
        for file_path in project_path.rglob('*'):
            if file_path.is_file():
                lang = detect_comment_language(file_path)
                if lang in ['en', 'fr']:
                    comment_languages[lang] += 1
                    
        return dict(comment_languages)
    
    except Exception as e:
        logger.error(f"\nError counting comment languages: {str(e)}\n")
        return {"en": 0, "fr": 0}
    
@error_handler
def detect_comment_blocks(file_path: str) -> List[Tuple[int, int]]:
    """Détecte les blocs de commentaires consécutifs dans un fichier et leurs lignes."""
    try:
        comment_blocks = []
        current_block = []
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                if COMMENT_PATTERN.match(line.strip()):
                    if not current_block:
                        current_block = [line_num]
                elif current_block:
                    current_block.append(line_num - 1)
                    comment_blocks.append(tuple(current_block))
                    current_block = []

            # Gérer le cas où le fichier se termine par un commentaire
            if current_block:
                current_block.append(line_num)
                comment_blocks.append(tuple(current_block))
        
        return comment_blocks
    except Exception as e:
        logger.error(f"\nErreur lors de la lecture du fichier {file_path}: {str(e)}\n")
        return []
    
def get_number_of_comment_only_files(file_path: Path) -> int:
    """
    Getter pour récupérer le nombre de fichiers contenant uniquement des commentaires.
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        int: Nombre de fichiers contenant uniquement des commentaires
    """
    return count_comment_only_files(file_path) + " comment-only files\n"

def get_comment_languages(file_path: Path) -> Dict[str, int]:
    """
    Getter pour récupérer le nombre de fichiers par langue de commentaires (français/anglais).
    
    Args:
        file_path (Path): Chemin du fichier à vérifier
        
    Returns:
        Dict[str, int]: Dictionnaire contenant le compte pour chaque langue
    """
    return count_comment_language_en_fr(file_path) + " comment languages\n"