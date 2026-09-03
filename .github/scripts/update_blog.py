#!/usr/bin/env python3
"""
Blog Post Feed Updater
Fetches latest posts from a blog RSS feed and updates README.md
"""

import feedparser
import re
from datetime import datetime
from typing import List, Dict
import sys

BLOG_FEED_URL = "https://qdriven.github.io/blog/feed.xml"

START_MARKER = "<!-- BLOG:START -->"
END_MARKER = "<!-- BLOG:END -->"


def fetch_posts(url: str, limit: int = 5) -> List[Dict]:
    """Fetch latest blog posts from RSS feed."""
    try:
        feed = feedparser.parse(url)
        posts = []

        for entry in feed.entries[:limit]:
            try:
                pub_date = entry.get("published", "")
                if pub_date:
                    try:
                        date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date = date_obj.strftime("%b %d, %Y")
                    except Exception:
                        formatted_date = pub_date[:15]
                else:
                    formatted_date = datetime.now().strftime("%b %d, %Y")

                posts.append({
                    "title": entry.get("title", "Untitled"),
                    "link": entry.get("link", "#"),
                    "date": formatted_date,
                    "summary": entry.get("summary", "")[:120]
                })
            except Exception as e:
                print(f"Error parsing entry: {e}", file=sys.stderr)
                continue

        return posts
    except Exception as e:
        print(f"Error fetching blog feed: {e}", file=sys.stderr)
        return []


def format_posts_as_markdown(posts: List[Dict]) -> str:
    """Format blog posts as markdown list."""
    if not posts:
        return """*No posts available yet. Check back soon!*
"""

    markdown = ""
    for post in posts:
        summary = post["summary"].replace("\n", " ").strip()
        if summary:
            summary_html = f"<br/><small>{summary}...</small>" if len(summary) > 10 else ""
        else:
            summary_html = ""
        markdown += f"- [{post['title']}]({post['link']}) *{post['date']}*{summary_html}\n"

    return markdown


def update_readme(blog_markdown: str):
    """Update README.md with blog posts."""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        if START_MARKER not in content or END_MARKER not in content:
            print("Warning: Blog markers not found in README.md", file=sys.stderr)
            return

        pattern = f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}"
        replacement = f"{START_MARKER}\n{blog_markdown}\n{END_MARKER}"

        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)

        print("README.md updated with blog posts!")

    except Exception as e:
        print(f"Error updating README: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main execution function."""
    print("Starting blog feed update...")
    print(f"Fetching from: {BLOG_FEED_URL}")

    posts = fetch_posts(BLOG_FEED_URL)

    if not posts:
        print("Warning: No posts fetched", file=sys.stderr)
        posts = []

    blog_markdown = format_posts_as_markdown(posts)
    update_readme(blog_markdown)

    print(f"Update complete! Added {len(posts)} posts.")


if __name__ == "__main__":
    main()
