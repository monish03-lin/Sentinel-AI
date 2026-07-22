import unittest
from dataclasses import dataclass
from typing import List, Set, Dict


from backend.app.AI.keyword_scanner import scan_keywords

# Import your main scanning function and data structures here
# from your_main_file import scan_keywords_aho, KeywordScanResult, KEYWORDS_CATEGORIES

class TestPhishingKeywordScanner(unittest.TestCase):
    
    def test_empty_text(self):
        """Test that an empty or blank string returns a zero score and empty lists."""
        result = scan_keywords("")
        self.assertEqual(result.score, 0)
        self.assertEqual(result.matched_keywords, [])
        self.assertEqual(result.detected_categories, [])

    def test_standalone_keyword_matching(self):
        """Test that valid standalone keywords trigger the correct weights and categories."""
        # 'urgent' is weight 2, category 'urgency' adds 10 base points = 12 total
        text = "Please review this urgent matter."
        result = scan_keywords(text)
        
        self.assertIn("urgent", result.matched_keywords)
        self.assertIn("urgency", result.detected_categories)
        self.assertEqual(result.score, 12)

    def test_substring_boundary_false_positive_prevention(self):
        """Test that words embedded inside other words (e.g., 'blog in' or 'surgent') are ignored."""
        # 'log in' and 'urgent' are hidden inside larger words here
        text = "I love reading your blogging website during a insurgent attack."
        result = scan_keywords(text)
        
        self.assertEqual(len(result.matched_keywords), 0)
        self.assertEqual(result.score, 0)

    def test_duplicate_keyword_deduplication(self):
        """Test that repeating the exact same keyword multiple times doesn't spam the score."""
        text = "Urgent! Urgent! This is an urgent request."
        result = scan_keywords(text)
        
        # 'urgent' should only appear once in matched_keywords
        self.assertEqual(result.matched_keywords.count("urgent"), 1 if "urgent" in result.matched_keywords else 0)
        # Should score base category (10) + weight (2) once = 12, not multiplied by 3
        self.assertEqual(result.score, 12)

    def test_multiple_categories(self):
        """Test an email containing triggers from different categories simultaneously."""
        text = "Urgent: Please update your password immediately to avoid account suspension."
        result = scan_keywords(text)
        
        # Should detect multiple distinct categories
        self.assertIn("urgency", result.detected_categories)
        self.assertIn("credential", result.detected_categories)
        self.assertIn("threat", result.detected_categories)
        
        # Score should be well above base since multiple critical triggers were hit
        self.assertGreater(result.score, 30)

if __name__ == "__main__":
    unittest.main()