from Functionality.empty_file import is_empty_files_list
from Functionality.comment_file import is_comment_only_list
from Functionality.file_logic import get_valid_files_list

def check_config(config):
    features = config.get("features", {})
    valid_files = get_valid_files_list(config.get("projectPath"), config.get("extensions"))

    results = {}
    statistics = {}

    if features.get("detectEmptyFiles"):
        empty_files = is_empty_files_list(valid_files)
        for file in empty_files:
            results[file] = "Empty file"
        statistics["empty_files"] = len(empty_files)
    
    if features.get("detectCommentOnlyFiles"):
        comment_files = is_comment_only_list(valid_files)
        for file in comment_files:
            results[file] = "Comment-only file"
        statistics["comment_files"] = len(comment_files)

    if features.get("test"):
        print("Test mode is enabled")


    return results, statistics