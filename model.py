import typing as t


class UserAnswers():
    def __init__(self, name: str, username: str):
        self.name = name
        self.username = username
        self.city = None
        self.place = None
        self.dog_place = None
        self.children = None
        self.other_animals = None
        self.dog_experience = None
        self.dog_choice = None
        self.contact_number = None

    def to_list(self) -> list[t.Any]:
        return [
            self.username,
            self.name,
            self.city,
            self.place,
            self.dog_place,
            self.children,
            self.other_animals,
            self.dog_experience,
            self.dog_choice,
            self.contact_number,
        ]
