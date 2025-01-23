from Functionality.empty_file import is_empty_files_list
from Functionality.comment_file import is_comment_only_list
from Functionality.todo_file import check_todo_files
from Functionality.file_logic import get_valid_files_list
from Functionality.test_file import count_empty_test_files, pourcentage_test_file, is_test_file_list, count_comment_only_test_files

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

    if features.get("detectTodo"):
        todo_files = check_todo_files(valid_files)
        for file, todos in todo_files.items():
            results[file] = f"TODOs: {todos}"
        statistics["todo_files"] = len(todo_files)

    if features.get("detectTestFiles"):
        test_files = is_test_file_list(valid_files)
        empty_test_files = count_empty_test_files(test_files)
        comment_only_test_files = count_comment_only_test_files(test_files)
        for file in test_files:
            results[file] = "Test file"
        
        statistics["total_test_files"] = len(test_files)
        statistics["total_empty_test_files"] = empty_test_files
        statistics["percentage_empty_test_files"] = pourcentage_test_file(statistics["total_empty_test_files"], statistics["total_test_files"])
        statistics["total_comment_only_test_files"] = comment_only_test_files
        statistics["pourcentage_comment_only_test_files"] = pourcentage_test_file(statistics["total_comment_only_test_files"], statistics["total_test_files"])


    if features.get("test"):
        print("Test mode is enabled")


    return results, statistics