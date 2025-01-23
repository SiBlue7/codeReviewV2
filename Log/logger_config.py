# File/logger_config.py

import logging
import traceback

from pathlib import Path
from logging.handlers import RotatingFileHandler
from functools import wraps

def setup_logging(verbose: bool = False) -> logging.Logger:
    """
    Configuration du système de logging avec propagation des erreurs
    """
    # Créer le logger principal
    logger = logging.getLogger('CodeReview')
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)
    
    # S'assurer que le logger n'a pas déjà des handlers
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s\n'
            'Additional Info: %(pathname)s:%(lineno)d',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Log console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # Créer le dossier Log s'il n'existe pas
        log_dir = Path('Log')
        log_dir.mkdir(exist_ok=True)

        # Log fichier avec rotation
        file_handler = RotatingFileHandler(
            log_dir / 'code_review.log', 
            maxBytes=1_048_576,  # 1 MB
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Configurer la propagation des logs
    logger.propagate = True
    
    return logger

def error_handler(func):
    """
    Décorateur pour gérer et logger les erreurs des fonctions
    """
    logger = logging.getLogger('CodeReview')
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Capture la stack trace complète
            stack_trace = traceback.format_exc()
            # Log l'erreur avec la stack trace
            logger.error(f"Error in {func.__name__}: {str(e)}\nStack trace:\n{stack_trace}")
            raise
    return wrapper

# Créer une instance du logger par défaut
logger = logging.getLogger('CodeReview')