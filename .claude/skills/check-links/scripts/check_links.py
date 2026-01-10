#!/usr/bin/env python3
"""Check all internal links on the local Hugo site for broken links."""

import sys
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen


class LinkExtractor(HTMLParser):
    """Extract href attributes from anchor tags."""

    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value:
                    self.links.append(value)


def get_links(url: str) -> list[str]:
    """Fetch a page and extract all links."""
    try:
        with urlopen(url, timeout=10) as response:
            content = response.read().decode("utf-8", errors="ignore")
            parser = LinkExtractor()
            parser.feed(content)
            return parser.links
    except (HTTPError, URLError):
        return []


def is_internal(url: str, base_host: str) -> bool:
    """Check if URL is internal (same host or relative)."""
    parsed = urlparse(url)
    # Relative URLs or same host
    if not parsed.netloc:
        return True
    return parsed.netloc == base_host


def normalize_url(url: str) -> str:
    """Normalize URL for comparison (remove fragments)."""
    parsed = urlparse(url)
    # Remove fragment, keep path with trailing slash normalization
    path = parsed.path
    if not path.endswith("/") and "." not in path.split("/")[-1]:
        path = path + "/"
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def check_url(url: str) -> tuple[bool, int | str]:
    """Check if a URL is accessible. Returns (ok, status_or_error)."""
    try:
        with urlopen(url, timeout=10) as response:
            return True, response.status
    except HTTPError as e:
        return False, e.code
    except URLError as e:
        return False, str(e.reason)
    except Exception as e:
        return False, str(e)


def crawl(start_url: str) -> dict[str, list[tuple[str, int | str]]]:
    """
    Crawl site starting from start_url.

    Returns dict mapping source pages to list of (broken_link, error) tuples.
    """
    parsed_start = urlparse(start_url)
    base_host = parsed_start.netloc

    visited: set[str] = set()
    to_visit: list[tuple[str, str | None]] = [(start_url, None)]  # (url, referrer)
    broken: dict[str, list[tuple[str, int | str]]] = {}

    while to_visit:
        url, referrer = to_visit.pop(0)
        normalized = normalize_url(url)

        if normalized in visited:
            continue
        visited.add(normalized)

        # Check if page exists
        ok, status = check_url(url)
        if not ok:
            if referrer:
                if referrer not in broken:
                    broken[referrer] = []
                broken[referrer].append((url, status))
            continue

        # Get links from this page
        links = get_links(url)

        for link in links:
            # Skip non-http links
            if link.startswith(("mailto:", "tel:", "javascript:", "#")):
                continue

            # Resolve relative URLs
            full_url = urljoin(url, link)

            # Only follow internal links
            if not is_internal(full_url, base_host):
                continue

            normalized_link = normalize_url(full_url)
            if normalized_link not in visited:
                to_visit.append((full_url, url))

    return broken


def find_hugo_server() -> str | None:
    """Try common Hugo ports to find running server."""
    ports = [1313] + list(range(60420, 60440))  # Default + common dynamic range
    for port in ports:
        url = f"http://localhost:{port}/"
        try:
            with urlopen(url, timeout=2) as response:
                if response.status == 200:
                    return url
        except (HTTPError, URLError):
            continue
    return None


def main() -> int:
    """Main entry point."""
    start_url = find_hugo_server()

    if not start_url:
        print("Error: Cannot find Hugo server on common ports")
        print("Make sure Hugo server is running: cd hugo && hugo server")
        return 1

    print(f"Checking links starting from {start_url}")
    print("-" * 50)

    broken = crawl(start_url)

    if not broken:
        print("All links OK!")
        return 0

    print(f"\nFound broken links:\n")
    total_broken = 0

    for source, links in sorted(broken.items()):
        print(f"On page: {source}")
        for link, error in links:
            print(f"  -> {link} ({error})")
            total_broken += 1
        print()

    print(f"Total: {total_broken} broken link(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
