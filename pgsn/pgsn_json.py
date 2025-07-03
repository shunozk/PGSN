import json
from typing import Any
from pgsn import gsn_term
from pgsn.gsn_term import Term, goal, strategy, evidence, variable

def term_to_dict(term: Term) -> dict:
    """
    TermオブジェクトをJSONに変換できる辞書形式にする。
    """
    match term:
        case gsn_term.Goal(description=d, support=s):
            return {
                "type": "goal",
                "description": term.description,
                "support": term_to_dict(term.support) if term.support else None
            }
        case gsn_term.Strategy(description=d, sub_goals=sgs):
            return {
                "type": "strategy",
                "description": term.description,
                "sub_goals": [term_to_dict(g) for g in term.sub_goals]
            }
        case gsn_term.Evidence(description=d):
            return {
                "type": "evidence",
                "description": term.description
            }
        case gsn_term.Variable(name=n):
            return {
                "type": "variable",
                "name": n
            }
        case _:
            raise ValueError(f"未対応のTerm型: {type(term)}")

def term_from_dict(data: dict) -> Term:
    """
    JSONの辞書形式からTermオブジェクトに復元する。
    """
    t = data["type"]
    if t == "goal":
        return goal(
            description=data["description"],
            support=term_from_dict(data["support"]) if data["support"] else None
        )
    elif t == "strategy":
        return strategy(
            description=data["description"],
            sub_goals=[term_from_dict(g) for g in data["sub_goals"]]
        )
    elif t == "evidence":
        return evidence(description=data["description"])
    elif t == "variable":
        return variable(data["name"])
    else:
        raise ValueError(f"未知のtype: {t}")

def save_term_to_file(term: Term, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(term_to_dict(term), f, ensure_ascii=False, indent=2)

def load_term_from_file(filename: str) -> Term:
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return term_from_dict(data)
