from __future__ import annotations
from utils import get_ebook
from ebook import eBook

import timeit


def benchmark_process(
    epub_path: str,
    ebook_name: str,
    standard: bool = False,
    out_directory: str | None = None,
) -> eBook:
    """
    Benchmarks process for different EPUB sizes and formats.

    Process time is determined by the number and size of .xhtml/html files.
    """

    epub_process: eBook = get_ebook(epub_path, ebook_name, standard, out_directory)
    return epub_process


if __name__ == "__main__":
    start_time = timeit.default_timer()
    ebook1 = benchmark_process("tests/test-epubs/small-standard.epub", "Poetry", True)
    print("\nSmall Standard EPUB Process: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    ebook2 = benchmark_process(
        "tests/test-epubs/small-act-standard.epub", "The-Jew-Of-Malta", True
    )
    print("\nSmall (Act) Standard EPUB Process: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    ebook3 = benchmark_process(
        "tests/test-epubs/medium-standard.epub", "The-Mystery-of-the-Yellow-Room", True
    )
    print("\nMedium Standard EPUB Process: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    ebook4 = benchmark_process(
        "tests/test-epubs/large-standard.epub", "The-Diary", True
    )
    print("\nLarge Standard EPUB Process: ", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    ebook5 = benchmark_process("tests/test-epubs/large.epub", "Viewpoint")
    print("\nLarge Non-Standard EPUB Process: ", timeit.default_timer() - start_time)

    for key, value in ebook5.ebook.items():
        if key == "Chapters":
            # first_chapter = next(iter(value.values()), None)
            # print(f"\nChapter 1 Contents:\n{first_chapter}")
            break

        print(f"\n{key}: {value}")
