import abc


class AutoDocumentedObject(abc.ABC):
    def get_underline(
        self, word_to_underline: str, underline_charachter: str = "="
    ) -> str:
        return len(word_to_underline) * underline_charachter

    @abc.abstractmethod
    def export(self, path: str):
        ...
