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

    def get_title(self) -> str:
        return self.ebook["Title"]

    def set_author(self, author) -> None:
        self.ebook["Author"] = author

    def get_author(self) -> str:
        return self.ebook["Author"]

    def set_description(self, description) -> None:
        self.ebook["Description"] = description

    def get_description(self) -> str:
        return self.ebook["Description"]

    def set_genres(self, genres) -> None:
        self.ebook["Genres"] = genres

    def get_genres(self) -> list[str]:
        return self.ebook["Genres"]

    def set_chapters(self, chapter_number, chapter_contents) -> None:
        self.ebook["Chapters"][chapter_number] = chapter_contents

    def get_chapter(self, chapter_number) -> str:
        return self.ebook["Chapters"].get(chapter_number)
