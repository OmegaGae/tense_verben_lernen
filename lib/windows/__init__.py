"""WINDOWS package"""
# import sys
# from pathlib import Path

# path_test = Path(__file__).resolve().parents[1]
# sys.path.append(str(path_test))

from lib.windows.templates import (
    check_input,
    create_frame,
    create_label,
    create_photo_label,
    create_text,
    create_entry,
    create_progress_bar,
    create_button,
    GamePresentationTemplate,
    GamePageTemplate,
    GameStateTemplate,
    GameSuccessTemplate,
    GameFailedTemplate,
    GameConclusionTemplate,
)


__all__ = [
    check_input,
    create_frame,
    create_label,
    create_photo_label,
    create_text,
    create_entry,
    create_progress_bar,
    create_button,
    GamePresentationTemplate,
    GamePageTemplate,
    GameStateTemplate,
    GameFailedTemplate,
    GameSuccessTemplate,
    GameConclusionTemplate,
]
