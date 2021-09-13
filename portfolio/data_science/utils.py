"""
Utils
"""
import os

SKILL_CATEGORY_CHOICES = (
    ("technical", "Technical"),
    ("cloud", "Cloud"),
    ("soft", "Soft"),
    ("other", "Other"),
    ("highlight", "Highlight"),
    ("framework", "Framework")
)

def get_upload_path(instance, filename):
    """
    Get File Upload path
    :return:
    """
    return os.path.join(
        instance.professional.user.username,
        filename,
    )