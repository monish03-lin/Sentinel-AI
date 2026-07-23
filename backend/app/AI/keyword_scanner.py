import ahocorasick
import json
import re
from pathlib import Path
from dataclasses import dataclass
from typing import List, Set

def load_keywords_config(file_name: str ="keydictionary.json") -> dict:
    base_path= Path(__file__).parent
    file_path=base_path / file_name
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return {}

KEYWORDS_CATEGORIES = load_keywords_config()

@dataclass
class KeywordScanResult:
    """
    Stores the output of the keyword scanner.
    """

    detected_categories: List[str]
    matched_keywords: List[str]
    score: int


def build_automaton(categories_dict: dict) -> ahocorasick.Automaton:
    automaton = ahocorasick.Automaton()
    for category, items in categories_dict.items():
                 for key in items:
                    phrase=key["text"].lower()
                    automaton.add_word(phrase, (phrase, key["weight"], category))
    automaton.make_automaton()
    return automaton

AUTOMATON = build_automaton(KEYWORDS_CATEGORIES)

def scan_keywords(text: str) -> KeywordScanResult:
    if not text:
        return KeywordScanResult([], [], 0)

    text = text.lower()

    detected_categories: Set[str] = set()
    matched_keywords: Set[str] = set()

    score = 0

    for end_index, (phrase, weight, category) in AUTOMATON.iter(text):
                 start_index= end_index - len(phrase) +1
                 left_boundary = (start_index == 0 or not text[start_index - 1].isalnum())
                 right_boundary = (end_index == len(text)-1 or not text[end_index + 1]. isalnum())
                 if left_boundary and right_boundary:
                    if phrase not in matched_keywords:
                        matched_keywords.add(phrase)
                        if category not in detected_categories:
                            detected_categories.add(category)
                            score+= 10
                     
                        score+=weight

    return KeywordScanResult(
        detected_categories=sorted(detected_categories),
        matched_keywords=sorted(matched_keywords),
        score=score,
    )

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                