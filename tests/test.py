# ruff: noqa
import os
import sys
import unittest

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "eparser"))
)

from ebook import eBook
from utils import *

TEST_EPUB_PATH = "tests/test-epubs/large.epub"
TEST_EPUB_NAME = "Viewpoint"


def create_test_ebook() -> eBook:
    """Creates a test eBook using Viewpoint."""
    test_ebook = eBook()
    test_ebook.set_title("Omniscient Reader's Viewpoint")
    test_ebook.set_author("Sing-shong (싱숑)")
    test_ebook.set_description(
        "Only I know the end of this world. One day our MC finds himself stuck in the world of his favorite webnovel. What does he do to survive? It is a world struck by catastrophe and danger all around. His edge? He knows the plot of the story to end. Because he was the sole reader that stuck with it. Read his story to see how he survives!"
    )
    test_ebook.set_genres(
        ["Game Elements", "Apocalypse", "Adventure", "Action", "Korean"]
    )

    return test_ebook


class TestMetadata(unittest.TestCase):
    """Verify if eBook obtains metadata correctly."""

    def test_title(self):
        ebook: eBook = get_ebook(TEST_EPUB_PATH, TEST_EPUB_NAME)
        test_ebook: eBook = create_test_ebook()
        self.assertEqual(ebook.get_title(), test_ebook.get_title())

    def test_author(self):
        ebook: eBook = get_ebook(TEST_EPUB_PATH, TEST_EPUB_NAME)
        test_ebook: eBook = create_test_ebook()
        self.assertEqual(ebook.get_author(), test_ebook.get_author())

    def test_description(self):
        ebook: eBook = get_ebook(TEST_EPUB_PATH, TEST_EPUB_NAME)
        test_ebook: eBook = create_test_ebook()
        self.assertEqual(ebook.get_description(), test_ebook.get_description())

    def test_genres(self):
        ebook: eBook = get_ebook(TEST_EPUB_PATH, TEST_EPUB_NAME)
        test_ebook: eBook = create_test_ebook()
        self.assertListEqual(ebook.get_genres(), test_ebook.get_genres())


if __name__ == "__main__":
    unittest.main()

# Test extraction

# Test parsing

# Test eBook methods
