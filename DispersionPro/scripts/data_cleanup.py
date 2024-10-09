# scripts/data_cleanup.py

import os

def clean_old_logs(log_dir, days_old):
    """
    Deletes log files older than a specified number of days.

    Parameters:
    log_dir: str - Directory containing log files.
    days_old: int - Number of days.

    Returns:
    None
    """
    import time
    now = time.time()
    cutoff = now - (days_old * 86400)

    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)
        if os.path.isfile(file_path):
            if os.stat(file_path).st_mtime < cutoff:
                os.remove(file_path)
                print(f"Deleted old log file: {file_path}")

if __name__ == '__main__':
    clean_old_logs('logs/', 30)
