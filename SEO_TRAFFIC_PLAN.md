# SaySo SEO Traffic Plan

Updated: 2026-09-02

## Current Snapshot

- Production site: https://sayso-app.netlify.app/
- App Store listing: https://apps.apple.com/us/app/sayso-task-companion/id6758558171
- The tracked local repo matches GitHub `main`.
- The site already has canonical URLs, a sitemap, robots.txt, App Store CTAs, `SoftwareApplication` schema on the homepage, and FAQ schema on the homepage plus use-case pages.
- Google-visible results currently show the App Store listing strongly, while the Netlify domain appears mainly for legal/support pages in quick checks. That suggests the site is indexable, but product and use-case pages likely need stronger authority, keyword focus, and internal/external links.

## Priority 1: Foundation Wins

1. Move to a branded custom domain.
   - Use a memorable domain such as `saysoapp.com`, `getsayso.app`, or another SaySo-owned domain.
   - 301 redirect the Netlify subdomain to the branded domain.
   - Update canonical URLs, Open Graph URLs, sitemap URLs, robots sitemap URL, structured data URLs, App Store support/privacy links, and Search Console properties.

2. Set up measurement.
   - Google Search Console for the production domain.
   - Bing Webmaster Tools for additional index visibility.
   - Privacy-friendly analytics such as Plausible, Fathom, or Netlify Analytics.
   - Track CTA clicks with event names like `app_store_click_home`, `app_store_click_recipe`, and `app_store_click_youtube`.

3. Refresh sitemap dates whenever pages change.
   - Current `lastmod` values are `2026-06-05`.
   - Update to the deployment date when new SEO pages or major content revisions ship.

## Priority 2: Keyword Clusters

Build pages around high-intent searches where SaySo has a clear use case.

### Voice Task Capture

- voice to do list app
- voice task manager iPhone
- voice controlled to do list app
- speak tasks into checklist
- hands-free to do list
- AI voice task app
- voice productivity app for iPhone

Recommended pages:

- `/voice-to-do-list-app/`
- `/voice-controlled-to-do-list/`
- `/ai-voice-task-app/`

### YouTube and Tutorial Workflows

- YouTube tutorial checklist
- turn YouTube video into checklist
- follow YouTube tutorial hands free
- video to task list app
- timestamped checklist from video

Recommended pages:

- Keep improving `/youtube-to-checklist/`.
- Add `/youtube-tutorial-checklist/`.
- Add `/video-to-task-list/`.

### Cooking and Recipe Workflows

- hands-free cooking app
- recipe task app
- voice controlled recipe app
- recipe checklist app
- cook from recipe without touching phone

Recommended pages:

- Keep improving `/recipe-task-app/`.
- Add `/hands-free-cooking-app/`.
- Add `/voice-controlled-recipe-app/`.

### DIY, Repair, Fitness, and Crafts

- DIY checklist app
- hands-free repair instructions
- furniture assembly checklist app
- workout checklist app
- craft tutorial checklist

Recommended pages:

- `/diy-checklist-app/`
- `/furniture-assembly-checklist/`
- `/workout-routine-checklist/`

## Priority 3: Page Template For SEO Landing Pages

Each new page should include:

- One clear query-matched H1.
- A concise hero promise with an App Store CTA above the fold.
- A short "how it works" section with 3 steps.
- Real use cases for the query.
- A comparison section that explains why SaySo is different from generic notes, reminders, or traditional to-do apps.
- FAQ content with matching structured data.
- Internal links to related SaySo use-case pages.
- A final CTA that repeats the App Store badge.

## Priority 4: Conversion Improvements

1. Add sticky mobile App Store CTA after the user scrolls past the hero.
2. Add campaign-specific App Store links using Apple campaign tokens if available in App Store Connect.
3. Put the strongest conversion message near every CTA:
   - "Download SaySo for iPhone"
   - "Turn videos, recipes, and webpages into guided tasks"
   - "Hands-free when your hands are busy"
4. Add social proof as soon as there are more reviews, testimonials, or usage proof.
5. Add visual proof on use-case pages, not just the homepage.

## Priority 5: Content and Link Acquisition

Publish helpful articles that answer specific workflow questions, then link back to the app pages.

Suggested articles:

- How to follow a YouTube tutorial without pausing every minute
- How to cook from a recipe without touching your phone
- How to turn a webpage into a checklist on iPhone
- Best voice task manager apps for iPhone
- Why voice-first task apps work better for messy, hands-busy work

Distribution:

- App Store optimization: align screenshots, subtitle, keywords, and description with the same clusters.
- Reddit and forum participation where people ask for voice-based task tools.
- Short-form demos showing one workflow per video: recipe, YouTube tutorial, DIY repair, workout, web article.
- Product Hunt, BetaList, indie app directories, iOS app newsletters, and productivity/cooking creator outreach.

## First Implementation Batch

1. Create a branded-domain migration checklist once a domain is chosen.
2. Add 4 new SEO pages:
   - `/voice-to-do-list-app/`
   - `/hands-free-cooking-app/`
   - `/youtube-tutorial-checklist/`
   - `/webpage-to-checklist/`
3. Add internal links from the homepage and existing use-case pages.
4. Update sitemap and robots.
5. Add privacy-friendly analytics or Netlify Analytics.
6. Add click tracking to every App Store CTA.
