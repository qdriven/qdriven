# Live README feeds

Two blocks in `README.md` are generated from RSS. Do not edit them by hand — the next run overwrites whatever is between the markers.

| README section | Markers | Script | Workflow |
|----------------|---------|--------|----------|
| Tech Wire | `<!-- NEWS:START -->` … `<!-- NEWS:END -->` | `.github/scripts/update_news.py` | `.github/workflows/news-ticker.yml` |
| Latest Posts | `<!-- BLOG:START -->` … `<!-- BLOG:END -->` | `.github/scripts/update_blog.py` | `.github/workflows/blog-feed.yml` |

Headings, captions, and anything **outside** the markers stay as you wrote them. If a pair of markers is missing, that script prints a warning and skips the update.

Both jobs are **paused**. The workflow files keep a no-op stub so GitHub still accepts them; the real `on` / `jobs` blocks are commented out.

Uncomment those blocks in `.github/workflows/news-ticker.yml` and `.github/workflows/blog-feed.yml` when you uncomment the README sections. Both jobs need `contents: write`. Scheduled runs only fire on the default branch.

---

## Generate locally

From the repo root:

```bash
python3 -m pip install feedparser
python3 .github/scripts/update_news.py
python3 .github/scripts/update_blog.py
```

Then check **Tech Wire** and **Latest Posts** in `README.md`.

---

## Generate on GitHub

Currently paused. After you restore the commented job in each workflow file, it runs every 6 hours UTC (`0 */6 * * *`) and can also be run by hand.

1. Uncomment the original `on` / `jobs` block in the workflow file (and remove the `paused` stub)
2. Open the repo on GitHub → **Actions**
3. Select **Tech News Ticker** or **Blog Feed**
4. Click **Run workflow** → **Run workflow**

If the README changed, the workflow commits and pushes:

- Tech Wire → `chore: update tech news ticker`
- Latest Posts → `chore: update blog feed`

No commit means the feed returned the same content as last time.

---

## Tech Wire

Pulls community RSS feeds, keeps up to **10** rows, and writes a markdown table.

### Current sources

Defined in `NEWS_SOURCES` inside `update_news.py`:

| Category | Feed | Items taken |
|----------|------|-------------|
| Tech | [Hacker News frontpage](https://hnrss.org/frontpage?count=5) | 5 |
| Dev | [Dev.to](https://dev.to/feed) | 5 |
| GitHub | [GitHub Blog](https://github.blog/feed/) | 5 |

Order is source order (HN, then Dev.to, then GitHub Blog), not recency. Combined list is then truncated to 10.

### Change sources

Edit `NEWS_SOURCES` in `.github/scripts/update_news.py`:

```python
{
    "name": "Your Source",
    "url": "https://example.com/feed.xml",
    "category": "ShortLabel"
}
```

`category` is the first table column. Any RSS or Atom URL that `feedparser` can read works.

To change how many rows appear, edit `all_news[:10]` in `fetch_all_news()`. Per-source cap is `feed.entries[:5]`.

---

## Latest Posts

Pulls **your** blog RSS/Atom feed and writes up to **5** posts as a markdown list.

### Current source

`BLOG_FEED_URL` in `.github/scripts/update_blog.py`:

```python
BLOG_FEED_URL = "https://qdriven.github.io/blog/feed.xml"
```

If that URL is empty or unreachable, README shows: *No posts available yet. Check back soon!*

### Point it at a real feed

```python
BLOG_FEED_URL = "https://qdriven.github.io/blog/feed.xml"  # Jekyll / Hugo
# BLOG_FEED_URL = "https://dev.to/feed/qdriven"            # Dev.to
# BLOG_FEED_URL = "https://medium.com/feed/@qdriven"       # Medium
```

To show more or fewer posts, change `limit=5` on `fetch_posts()`.

---

## Troubleshooting

| Symptom | What to check |
|---------|----------------|
| Table or list did not change | Run the matching script locally. Confirm the RSS URL responds. |
| Latest Posts still empty | `BLOG_FEED_URL` 404s or has no entries. Open the URL in a browser. |
| Action ran but no commit | Feed content matches the last commit. That is expected. |
| Action skipped on a branch | Schedules only fire on the default branch. Use **Run workflow** there. |
| Dates look truncated (`Thu, 03 Sep 202`) | The feed date did not match `%a, %d %b %Y %H:%M:%S %Z`, so the script keeps the first 15 characters. Fix the parser in the script if you want a full date. |
