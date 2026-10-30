# Lean 4 Knowledge

Static website about Lean 4, graph engineering, formal ontologies, and certified reasoning, by Volodymyr Pavlyshyn.

## Run locally

Requires Python 3; no application dependencies.

```sh
python3 build.py
python3 check.py
python3 -m http.server 4173 --directory dist
```

Open http://localhost:4173. Equivalent npm scripts: build, check, dev.

## Edit

- `build.py`: pages, navigation, project profiles, resources, book and author; production origin in `BASE`.
- `articles.py`: five original supporting articles with sources.
- `courses.py`: two mini-courses, six lessons, worked exercise answers.
- `legal.py`: German legal text adapted from pavlyshyn.me.
- `illustrations.py`: original SVG tree, article diagrams, downloadable proof pipeline, favicon.
- `dist/assets/style.css` and `app.js`: source assets retained by the build.
- `dist/assets/author.jpg` and `bulletproof-knowledge.jpg`: locally hosted portrait and actual cover.
- `dist/`: portable static output, 16 pages plus 404.

No application analytics, cookies, local storage, external font loads, embedded services, or visitor forms. Hosting may separately use authentication/security mechanisms.

## Validation

Internal link/fragment/asset checks, primary headings, image alternatives, JavaScript syntax, and 35 external URL checks. Local Chrome QA covered desktop/tablet/mobile overflow, images, stack selector, filters/search/empty state, lesson accordions, and mobile menu. Browser tools live only under /tmp/lean4-qa.

## GitHub Pages deployment

The production origin is `https://lean4knowledge.com`. The build generates `dist/CNAME`, `.nojekyll`, canonical links, social image URLs, and a sitemap for that domain.

`.github/workflows/pages.yml` builds and checks the site, then uploads `dist/` and deploys it with GitHub Pages. It runs on pushes to `main` and can also be started manually. Put this project directory's contents at the root of the hosting repository so GitHub discovers the workflow.

In the hosting repository, select **Settings → Pages → Source → GitHub Actions**. Set the custom domain to `lean4knowledge.com` and retain/configure its GitHub Pages DNS records. The workflow does not change DNS or the repository's custom-domain setting. Custom Actions deployments require the domain in repository settings; the generated CNAME also supports branch-based hosting.

The GitHub repository is https://github.com/Volland/lean4knowledge. The `origin` remote uses `git@github.com:Volland/lean4knowledge.git`. The earlier private Sites deployment is separate; its `.openai/hosting.json` is retained only as historical deployment metadata, and GitHub Pages does not use it.

The privacy notice now describes GitHub Pages, using the author's original notice and GitHub's published privacy documentation. It contains no private-preview hosting placeholders. It does not assert an unverified processing agreement or fixed log retention period.

Amazon US uses the supplied ASIN at https://www.amazon.com/dp/B0HPH5JJZF. Its URL responds, but retailer challenge content prevents independent verification of US availability.

The project stack is a conceptual architecture, not an assertion that all four projects are automatically integrated. Course code is pedagogical and has not been compiled as part of the website build.
