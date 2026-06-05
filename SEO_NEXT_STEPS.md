# SaySo SEO Launch Next Steps

This site is ready to submit to Google Search Console from a technical standpoint:

- Production URL: `https://sayso-app.netlify.app/`
- Sitemap URL: `https://sayso-app.netlify.app/sitemap.xml`
- Robots URL: `https://sayso-app.netlify.app/robots.txt`
- Canonical URLs are absolute Netlify URLs.
- The homepage includes `SoftwareApplication` structured data.
- Use-case pages include visible FAQ content and matching `FAQPage` structured data.
- App Store CTAs point to `https://apps.apple.com/us/app/sayso-task-companion/id6758558171`.

## Google Search Console

1. Add `https://sayso-app.netlify.app/` as a URL-prefix property.
2. Verify ownership through Netlify using the HTML file or meta-tag verification method.
3. Submit `https://sayso-app.netlify.app/sitemap.xml`.
4. Request indexing for:
   - `https://sayso-app.netlify.app/`
   - `https://sayso-app.netlify.app/hands-free-task-manager/`
   - `https://sayso-app.netlify.app/voice-task-manager-iphone/`
   - `https://sayso-app.netlify.app/youtube-to-checklist/`
   - `https://sayso-app.netlify.app/recipe-task-app/`
5. Review indexing, query, click-through, and page experience data after Google has crawled the site.

## Custom Domain

The preferred next SEO and brand step is to move from the Netlify subdomain to a branded custom domain.

1. Choose a domain such as `saysoapp.com`, `getsayso.app`, or another available SaySo-branded domain.
2. Add the domain in Netlify project settings for `sayso-app`.
3. Update DNS records at the registrar to point to Netlify.
4. Let Netlify issue the SSL certificate.
5. Update every canonical URL, Open Graph URL, sitemap URL, and robots sitemap URL from `https://sayso-app.netlify.app/` to the new domain.
6. Add the new domain property in Google Search Console and submit the updated sitemap.
7. Keep Netlify redirects from the old subdomain to the custom domain if possible.
