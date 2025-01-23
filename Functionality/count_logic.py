from pathlib import Path
from typing import Dict, Union, Any
from functools import wraps
from Log.logger_config import logger, error_handler

import concurrent.futures

@error_handler
def file_walker(func):
    @wraps(func)
    def wrapper(project_path: Union[str, Path]) -> Any:
        try:
            project_path = Path(project_path)
            if not project_path.exists():
                raise FileNotFoundError(f"\nProject path does not exist: {project_path}\n")
            
            # Traitement parallèle
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = [
                    executor.submit(func, file_path)
                    for file_path in project_path.rglob('*')
                    if file_path.is_file()
                ]
                return sum(future.result() for future in concurrent.futures.as_completed(futures))
                
        except Exception as e:
            logger.error(f"\nError in {func.__name__}: {str(e)}\n")
            return 0
    return wrapper