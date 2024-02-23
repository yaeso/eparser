class eBook:
    def __init__(
        self, title=None, author=None, description=None, genres=[], chapters={}
    ) -> None:
        self.ebook = {
            "Title": None,
            "Author": None,
            "Description": None,
            "Genres": [],
            "Chapters": {},
        }

    def set_title(self, title) -> None:
        self.ebook["Title"] = title

    def set_author(self, author) -> None:
        self.ebook["Author"] = author

    def set_description(self, description) -> None:
        self.ebook["Description"] = description

    def set_genres(self, genres) -> None:
        self.ebook["Genres"] = genres

    def set_chapters(self, chapter_number, chapter_contents) -> None:
        self.ebook["Chapters"][chapter_number] = chapter_contents
