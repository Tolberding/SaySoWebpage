# Focused YouTube search/conversion update

The app page `/youtube-to-checklist/` explains the actual import flow, free versus
paid scope, review requirements, and recovery paths. The existing
`/youtube-tutorial-checklist/` remains a manual method/template guide. Reciprocal
links distinguish these intents without adding thin pages or changing URLs.

Feature provenance: read-only inspection of [Tolberding/Donezo](https://github.com/Tolberding/Donezo)
commit `30ab0cc1e161ab9695eaca017456668da865552e`:
`SaySo/Views/URLImportSheet.swift` (Paste YouTube Link, Analyze Video, editable
preview, Make it Sticky), `SaySo/Views/Subscription/PaywallView.swift` (regular
lists, website and YouTube imports free; unlimited TikTok/Instagram paid), and
`docs/YouTube-Import-Reliability-2026-10-22.md` (fallible network extraction).
These inspected files have no local modifications. This is committed-source evidence,
not verification of the released build 119 binary. The checkout project settings
still declare 1.0.28/build 117; build-time overrides and the source-to-binary mapping
were not established here. The reliability note also retains its historical
not-yet-uploaded release status. No native app files changed.

On 2026-10-25, Apple's live public lookup API
(`https://itunes.apple.com/lookup?id=6758558171&country=us`) returned version 1.0.29,
released 2026-10-23. Its description corroborates supported YouTube/webpage
imports, source-dependent extraction quality, and optional paid subscriptions.
It does not enumerate the exact free/paid split or button labels. Those details
are supported by the committed source above, not independently verified in build
119. No contradictory public claim was found. The web search cache showed the
older 1.0.28 listing, so it was not used to establish the live version.
No import-speed claim or guarantee added.

Asset provenance: existing tracked `assets/app-preview-poster.png`, visually
checked as a promotional taco-cooking checklist preview. Captions and alternative
text now identify it accurately. The paper-folding list is labeled illustrative,
not measured import output. No new generated image or third-party footage.

Validation: `python3 scripts/check_site.py`; `git diff --check`; isolated headless
Chrome at 390px and 1440px for both edited pages (screenshots reviewed, no overflow
or broken images, keyboard skip link first). Static HTML has no package manifest,
build step, or pre-existing test command. Use `python3 scripts/check_site.py --live`
after publication to compare all 12 sitemap pages byte-for-byte and check legacy
host redirects. Preserve the existing Google verification HTML in publication.

No web analytics mechanism existed to extend. No tracker, credentials, campaign
tokens, or cookie settings were added. Measure search performance in the current
host's Search Console property; App Store links alone do not establish download
attribution. Rankings and indexing are not guaranteed.
