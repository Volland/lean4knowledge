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

## Publication

Sites registration is private; identity is in `.openai/hosting.json`. No custom domain or DNS was changed. For another origin, update `BASE` and hosting-specific privacy text, then rebuild.

The privacy page is a preview draft. Confirm final hosting entities, processor terms, retention, and international transfers before public operation. Provider details and B2B terms were adapted from the author's public legal pages; obsolete EU ODR wording was removed. This is not certification of legal compliance.

Amazon US uses the supplied ASIN at https://www.amazon.com/dp/B0HPH5JJZF. Its URL responds, but retailer challenge content prevents independent verification of US availability.

The project stack is a conceptual architecture, not an assertion that all four projects are automatically integrated. Course code is pedagogical and has not been compiled as part of the website build.
