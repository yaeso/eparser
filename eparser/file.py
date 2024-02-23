import logging
import os
import patoolib


def extract(
    epub_file_path: str, ebook_name: str, out_directory: str | None = None
) -> None:
    """Unzips an EPUB file and extracts its contents."""
    if out_directory is None:
        out_directory = default_path(ebook_name)

    try:
        # Verbosity set to -1 ignores patoolib prints
        patoolib.extract_archive(epub_file_path, outdir=out_directory, verbosity=-1)
    except FileNotFoundError:
        logging.error(f"ERROR: EPUB file not found:\n{epub_file_path}")
    except Exception as error:
        logging.error(error)

    oebps_path = os.path.join(out_directory, "OEBPS")
    if not os.path.exists(oebps_path):
        os.makedirs(oebps_path)


def default_path(ebook_name: str) -> str:
    """Sets the default extraction path."""
    current_path = os.getcwd()
    epub_directory = os.path.join(current_path, "extracted-epubs", ebook_name)

    if not os.path.exists(epub_directory):
        try:
            os.makedirs(epub_directory)
        except OSError as error:
            logging.error(error)

    return epub_directory


def get_files(
    ebook_name: str, standard: bool = False, directory_path: str | None = None
) -> tuple[list[str], str, str | None]:
    """Obtains chapter filenames from the OEBPS folder and stores them in a list."""

    # Cleaning up the function -- also try to remember the steps
    if directory_path is None:
        directory_path = default_path(ebook_name)

    ebook_files = []
    opf_file_path = None

    if standard:
        content_path = os.path.join(directory_path, "epub")
        file_path = os.path.join(directory_path, "epub", "text")

        opf_file_path = os.path.join(content_path, "content.opf")
        ebook_files += [opf_file_path]

    else:
        # content.opf exists in OEBPS
        file_path = os.path.join(directory_path, "OEBPS")

    files = os.listdir(file_path)

    valid_prefixes = [ebook_name.lower(), "chap", "act"]
    valid_suffix = "html"
    content_opf = "content.opf"

    for filename in files:
        if (
            any(filename.startswith(prefix) for prefix in valid_prefixes)
            and filename.endswith(valid_suffix)
        ) or filename == content_opf:
            if filename == content_opf:
                opf_file_path = os.path.join(file_path, filename)
            ebook_files.append(filename)

    return sorted(ebook_files), file_path, opf_file_path
