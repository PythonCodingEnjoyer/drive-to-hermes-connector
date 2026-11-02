"""Read-only checks for the public informational site (no credentials)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import unittest

ROOT = Path(__file__).resolve().parents[1] / "docs"
PAGES = ("index.html", "privacy.html", "terms.html")


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.tags = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a":
            self.links.append(attrs.get("href", ""))


class PublicSiteTests(unittest.TestCase):
    def test_informational_pages_are_complete_and_interlinked(self):
        for name in PAGES:
            with self.subTest(page=name):
                path = ROOT / name
                self.assertTrue(path.is_file(), f"Missing public page: {name}")
                text = path.read_text(encoding="utf-8")
                page = Page(text)
                self.assertIn("drive-to-hermes-connector", text)
                self.assertIn('lang="ru"', text)
                self.assertIn('name="viewport"', text)
                self.assertEqual(page.tags.count("h1"), 1)
                self.assertIn("main", page.tags)
                self.assertNotIn("script", page.tags)
                self.assertNotIn("form", page.tags)
                self.assertTrue(set(PAGES).issubset(page.links))
                for href in page.links:
                    parts = urlsplit(href)
                    if not parts.scheme and not parts.netloc:
                        destination = ROOT / (parts.path or name)
                        self.assertTrue(destination.is_file(), f"Broken link: {href}")
                        if parts.fragment:
                            target = Page(destination.read_text(encoding="utf-8"))
                            self.assertIn(parts.fragment, target.ids)


if __name__ == "__main__":
    unittest.main(verbosity=2)
