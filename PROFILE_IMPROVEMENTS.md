# GitHub Profile Improvements Documentation

This document outlines the structure and improvements applied to the qdriven GitHub profile.

## Structure

### Directory Layout

```
qdriven/
├── README.md                         # Main profile page
├── Public/                           # Images, GIFs, screenshots for README
│   ├── .gitkeep
│   └── README.md                     # Usage instructions
├── all.md                            # Project inventory (internal reference)
├── simplify-prompts.md               # Profile writing prompts
├── references.md                     # Reference links
├── self-fulfill.yaml                 # Misc config
├── .gitattributes                    # LFS tracking for gif/png/jpg
├── PROFILE_IMPROVEMENTS.md           # This file
├── PIN_PROJECTS_GUIDE.md             # How to pin repos
├── .github/
│   ├── dependabot.yml                # Dependency management
│   ├── news-template.md              # News section template
│   ├── scripts/
│   │   ├── update_news.py            # Tech news fetcher (HN/Dev.to/GitHub Blog)
│   │   └── update_blog.py            # Blog RSS fetcher
│   └── workflows/
│       ├── news-ticker.yml           # Auto-update tech news (6h)
│       ├── blog-feed.yml             # Auto-update blog posts (6h)
│       ├── profile-3d.yml            # 3D contribution graph (daily)
│       ├── update-readme.yaml        # Auto-update activity (24h)
│       ├── smoke.yml                 # PR quality check
│       └── dependabot-automerge.yml  # Auto-merge dependabot PRs
└── assets/
    └── me-notion-png.png             # Old avatar (move to Public/ if preferred)
```

### What Each Section Does

| README Section | Purpose |
|---|---|
| Badges + counters | Social proof: followers, profile views |
| 3D Contribution Graph | Visual commit history (auto-generated) |
| The Short Version | One-paragraph professional identity |
| Sample Project | Template showing how to present a project |
| Featured Projects | Categorized project table |
| Tech Stack | Visual skill icons + domain badges |
| Tech Wire | Auto-updating dev news ticker |
| Latest Posts | Auto-updating blog feed |
| GitHub Analytics | Streak, stats, languages, activity graph |
| Connect | Social links |

## Automated Workflows

### Tech News Ticker (`news-ticker.yml`)
- **Schedule:** Every 6 hours
- **Sources:** Hacker News, Dev.to, GitHub Blog
- **Action:** Fetches top stories, updates README between `<!-- NEWS:START -->` and `<!-- NEWS:END -->` markers
- **Manual trigger:** Yes, via workflow_dispatch

### Blog Feed (`blog-feed.yml`)
- **Schedule:** Every 6 hours
- **Source:** Your blog RSS feed (configure in `.github/scripts/update_blog.py`)
- **Action:** Fetches latest posts, updates README between `<!-- BLOG:START -->` and `<!-- BLOG:END -->` markers
- **Setup:** Edit `BLOG_FEED_URL` in `update_blog.py`

### 3D Contribution Graph (`profile-3d.yml`)
- **Schedule:** Daily at 00:00 UTC
- **Action:** Generates 3D SVG of your contribution history
- **Output:** `profile-3d-contrib/profile-gitblock.svg` (referenced in README)

### Activity Update (`update-readme.yaml`)
- **Schedule:** Every 24 hours
- **Action:** Updates README with recent GitHub activity

### PR Smoke Check (`smoke.yml`)
- **Trigger:** On pull request
- **Action:** Auto-detects project type (Python/Node) and runs build

### Dependabot (`dependabot.yml` + `dependabot-automerge.yml`)
- **Schedule:** Weekly for GitHub Actions
- **Auto-merge:** Non-major version updates

## How to Customize

### Setting Up Your Blog Feed

1. Edit `.github/scripts/update_blog.py`
2. Change `BLOG_FEED_URL` to your blog's RSS/Atom feed URL:

```python
BLOG_FEED_URL = "https://qdriven.github.io/blog/feed.xml"  # Jekyll/Hugo
# or
BLOG_FEED_URL = "https://dev.to/feed/qdriven"              # Dev.to
# or
BLOG_FEED_URL = "https://medium.com/feed/@qdriven"         # Medium
```

3. Push and trigger the workflow manually to test

### Adding Your Own Projects

1. Replace the "Sample Project" section with your own project
2. Add screenshots/GIFs to `Public/` directory
3. Reference them as `./Public/your-image.gif` in README

### Changing News Sources

Edit `.github/scripts/update_news.py` and modify `NEWS_SOURCES`:

```python
{
    "name": "Your Source",
    "url": "https://example.com/rss",
    "category": "Category"
}
```

### Adding Profile Images

1. Place images in `Public/`
2. They'll be tracked by Git LFS (see `.gitattributes`)
3. Reference in README: `<img src="./Public/your-image.png" />`

### Migrating Old Avatar

```bash
mv assets/me-notion-png.png Public/avatar.png
# Then update README badge if needed
```

## Next Steps

- [ ] Push all changes to GitHub
- [ ] Trigger `profile-3d.yml` manually to generate first 3D graph
- [ ] Configure `BLOG_FEED_URL` in `update_blog.py`
- [ ] Add your own project screenshots/GIFs to `Public/`
- [ ] Replace sample project section with your real projects
- [ ] Update social links in Connect section
- [ ] Customize tech stack badges to match your actual skills
- [ ] Pin your best 4-6 repositories on GitHub
- [ ] Optionally add more RSS sources to `update_news.py`
