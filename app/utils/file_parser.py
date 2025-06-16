import fitz
import os
from typing import List, Tuple


def parse_file(filename: str, content: bytes) -> List[Tuple[int, str]]:
    if filename.endswith(".txt"):
        return [(1, content.decode("utf-8"))]

    elif filename.endswith(".pdf"):
        temp_path = "temp.pdf"
        with open(temp_path, "wb") as f:
            f.write(content)
        doc = fitz.open(temp_path)

        pages = []
        for i, page in enumerate(doc, start=1):
            pages.append((i, page.get_text()))

        doc.close()
        os.remove(temp_path)
        return pages

    else:
        return []
