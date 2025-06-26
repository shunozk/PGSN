import json

class Term:
    def __init__(self, term_id, term_type, content):
        self.id = term_id
        self.type = term_type
        self.content = content

    def to_json(self):
        return {
            "id": self.id,
            "type": self.type,
            "content": self.content
        }

    @classmethod
    def from_json(cls, json_dict):
        return cls(
            term_id=json_dict["id"],
            term_type=json_dict["type"],
            content=json_dict["content"]
        )
