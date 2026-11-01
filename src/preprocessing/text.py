"""Small public cleaning example; original text remains untouched."""
import re

def clean_caption(caption):
    # Preserve Bengali letters and combining marks, Latin letters, and spaces.
    if not isinstance(caption, str):
        raise TypeError("Caption must be text")
    caption = re.sub(r"[^a-zA-Z\u0980-\u09FF\s]", " ", caption)
    return " ".join(caption.split())
