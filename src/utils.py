from __future__ import annotations
from file import extract, get_files
from parse import extract_metadata, parse
from ebook import eBook


# Consider renaming to create_ebook
def get_ebook(
    epub_file_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str | None = None,
) -> eBook:
    """Creates an eBook from EPUB."""
    filenames, file_path, opf_file_path = process_epub(
        epub_file_path, ebook_name, standard, out_directory
    )
    metadata = extract_metadata(opf_file_path, ebook_name)
    ebook = parse(filenames, file_path, standard)
    set_metadata(ebook, metadata)

    return ebook


def process_epub(
    epub_file_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str | None = None,
) -> tuple[list[str], str, str | None]:
    """Handles the extraction process for EPUB."""
    extract(epub_file_path, ebook_name, out_directory)
    filenames, file_path, opf_file_path = get_files(ebook_name, standard, out_directory)

    return filenames, file_path, opf_file_path


def set_metadata(ebook: eBook, metadata: dict) -> eBook:
    """Sets eBook metadata."""
    ebook.set_title(metadata.get("title") or metadata.get("Title"))
    ebook.set_author(metadata.get("Author") or metadata.get("author"))

    # Potentially change Genres to Subjects
    ebook.set_genres(metadata.get("Genres"))
    ebook.set_description(metadata.get("description"))

    return ebook
