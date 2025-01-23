from typing import Union, List
import os
from pathlib import Path

from Log.logger_config import logger, error_handler
from Functionality.count_logic import file_walker
from Functionality.empty_file import is_empty_file
from Functionality.comment_file import is_comment_only

@error_handler
def is_test_file(file_path: str) -> bool:
    """
    Vérifie si le fichier est un fichier de test basé sur son nom et son extension.
    Supporte les conventions de test pour Angular, Java, Python et autres frameworks courants.
    
    Args:
        file_path (str): Chemin du fichier à vérifier
    
    Returns:
        bool: True si c'est un fichier de test, False sinon
    """
    # Obtenir le nom du fichier en minuscules pour une comparaison insensible à la casse
    file_name = os.path.basename(file_path).lower()
    
    # Liste des patterns pour les fichiers de test
    test_patterns = [
        # Angular / TypeScript
        '.spec.ts',
        '.test.ts'
    ]
    
    # Vérifier le contenu du fichier pour les annotations/imports de test
    test_indicators = [
        # Java
        '@Test',
        'import org.junit',
        'import org.testng',
        'extends TestCase',
        # Angular/Jest
        'describe(',
        'it(',
        'beforeEach(',
        'afterEach('
    ]
    
    # Vérifier d'abord le nom du fichier
    for pattern in test_patterns:
        if file_name.endswith(pattern) or pattern in file_name:
            return True
    
    # Si le nom ne correspond pas, vérifier le contenu du fichier
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            for indicator in test_indicators:
                if indicator in content:
                    return True
    except Exception as e:
        logger.error(f"\nErreur lors de la lecture du fichier {file_path}: {str(e)}\n")
        return False
    
    # Vérifier si le fichier est dans un répertoire de test
    dir_path = os.path.dirname(file_path).lower()
    test_directories = ['test', 'tests', 'spec', 'specs', 'e2e']
    return any(test_dir in dir_path.split(os.sep) for test_dir in test_directories)

def is_test_file_list(files_list: List[str]) -> List[str]:
    """
    Vérifie si les fichiers de la liste sont des fichiers de test.
    
    Args:
        files_list (list): Liste de chemins de fichiers à vérifier
        
    Returns:
        list: Liste des fichiers de test
    """
    return [file for file in files_list if is_test_file(file)]

@file_walker
def count_test_files(project_path: Union[str, Path]) -> int:
    """
    Compte le nombre de fichiers de test dans le projet.
    
    Args:
        project_path (Union[str, Path]): Chemin du projet à analyser
        
    Returns:
        int: Nombre de fichiers de test dans le projet
    """
    return 1 if is_test_file(project_path) else 0

def count_empty_test_files(file_list: List[str]) -> int:
    """
    Compte le nombre de fichiers de test vides dans le projet.
    
    Args:
        file_list (List[str]) : Liste des chemin de fichier à vérifier
        
    Returns:
        int: Nombre de fichiers de test vides
    """
    empty_test_files = 0
    for file in file_list:
        if is_test_file(file) and is_empty_file(file):
            empty_test_files += 1
    return empty_test_files

def count_comment_only_test_files(file_list: List[str]) -> int:
    """
    Compte le nombre de fichiers de test contenant uniquement des commentaires.
    
    Args:
        file_list (List[str]) : Liste des chemin de fichier à vérifier
        
    Returns:
        int: Nombre de fichiers de test contenant uniquement des commentaires
    """
    comment_only_test_files = 0
    for file in file_list:
        if is_test_file(file) and is_comment_only(file) and not is_empty_file(file):
            comment_only_test_files += 1
    return comment_only_test_files

def pourcentage_test_file(first_total: int, second_total: int) -> float:
    """
    Calcule le pourcentage de fichiers de test dans le projet.
    
    Args:
        first_total (List[str]): Nombre de fichiers de test
        second_total (List[str]): Nombre total de fichiers

    Returns:
        float: Pourcentage de fichiers de test
    """
    if second_total == 0:
        return 0.0

    return round((first_total / second_total) * 100, 2)