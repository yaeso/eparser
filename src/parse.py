import logging
import os

# import xml.etree.ElementTree as ET
from lxml import etree as ET
from ebook import eBook


def extract_metadata(opf_file_path: str, name: str) -> dict:
    """Extracts eBook metadata from content.opf file."""
    tree = ET.parse(opf_file_path)
    root = tree.getroot()

    metadata = {}
    ns = {
        "dc": "http://purl.org/dc/elements/1.1/",
        "opf": "http://www.idpf.org/2007/opf",
    }

    # Try to extract metadata from OEBPS format
    for dc in root.findall(".//{http://purl.org/dc/elements/1.1/}*", ns):
        tag = dc.tag.replace("{http://purl.org/dc/elements/1.1/}", "")
        if tag == "subject" and dc.text is not None:
            if "Genres" not in metadata:
                metadata["Genres"] = []
            genre = dc.text.strip()
            if genre not in metadata["Genres"]:
                metadata["Genres"].append(genre)
        elif tag == "creator" and dc.text is not None:
            metadata["Author"] = dc.text.strip()
        else:
            metadata[tag] = dc.text

    if not metadata:
        # Try to extract metadata from Standard format
        for meta in root.findall(".//opf:meta[@property]", ns):
            property = meta.get("property")
            content = meta.text
            if property and content:
                metadata[property] = content

    return metadata


def parse(filenames: list[str], directory_path: str, standard: bool = False) -> eBook:
    """Parses .xhtml files in the extracted folder and stores metadata in an eBook."""
    ebook = eBook()
    chapter_number = 1

    for filename in filenames:
        file_path = os.path.join(directory_path, filename)

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            chapter_contents = "\n".join(
                [
                    element.text.strip()
                    for element in root.iter("{http://www.w3.org/1999/xhtml}p")
                    if element.text
                ]
            )

            ebook.set_chapters(chapter_number, chapter_contents)
            chapter_number += 1

        except Exception as error:
            logging.error(error)

    return ebook
