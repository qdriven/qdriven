# GitHub Profile Improvements Documentation

This document outlines the structure and improvements applied to the qdriven GitHub profile.

## Structure

### Directory Layout

```
qdriven/
├── README.md                    # Main profile page
├── Public/                      # Images, GIFs, screenshots for README
├── all.md                       # Project inventory (internal reference)
├── simplify-prompts.md          # Profile writing prompts
├── references.md                # Reference links
├── self-fulfill.yaml            # Misc config
├── .gitattributes               # LFS tracking for media
├── .github/
│   ├── dependabot.yml           # Dependency management
│   ├── news-template.md         # News section template
│   ├── scripts/
│   │   └── update_news.py       # Tech news fetcher
│   └── workflows/
│       ├── news-ticker.yml      # Auto-update tech news (6h)
│       ├── update-readme.yaml   # Auto-update activity (24h)
│       ├── smoke.yml            # PR quality check
│       └── dependabot-automerge.yml
└── PROFILE_IMPROVEMENTS.md      # This file
```

### What Each Section Does

| README Section | Purpose |
|---|---|
| Badges + counters | Social proof: followers, profile views |
| The Short Version | One-paragraph professional identity |
| Example Project Showcase | Template showing how to present a project (replace with your own) |
| Featured Projects | Categorized project table |
| Tech Stack | Visual skill icons + domain badges |
| Tech Wire | Auto-updating dev news ticker |
| GitHub Analytics | Streak, stats, languages, activity graph |
| Connect | Social links |

## Automated Workflows

### Tech News Ticker (`news-ticker.yml`)
- **Schedule:** Every 6 hours
- **Sources:** Hacker News, Dev.to, GitHub Blog
- **Action:** Fetches top stories, updates README between `<!-- NEWS:START -->` and `<!-- NEWS:END -->` markers
- **Manual trigger:** Yes, via workflow_dispatch

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

### Adding Your Own Projects
1. Replace the "Example Project Showcase" section with your own project
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

## Next Steps

- [ ] Add your own project screenshots/GIFs to `Public/`
- [ ] Replace example project section with your real projects
- [ ] Update social links in Connect section
- [ ] Customize tech stack badges
- [ ] Pin your best 4-6 repositories on GitHub
