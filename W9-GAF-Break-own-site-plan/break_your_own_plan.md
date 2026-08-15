# Break Your Own Site — Week 9
**Live URL:** https://abdul-salam.vercel.app/

---

## 1. Try to Break It — Findings

Test each of these on the **live** site, not localhost:

- [ ] Open in a browser you haven't used to build it (e.g. Firefox if you built in Chrome, or your phone's browser)
- [ ] Open on mobile — does the layout hold, are the endpoint cards/nav readable?
- [ ] Click **every** link: Book a call, CV (PDF), Email, GitHub, LinkedIn, and all 4 project GitHub links + 4 Live demo links
- [ ] Note any link that still goes to `#` (dead placeholder) or 404s
- [ ] Reload the page a few times — anything flash/break on load (fonts not loaded yet, layout shift)?
- [ ] Try keyboard-only navigation (Tab through the links) — does focus show clearly?

**Findings (raw list, before triage):**
1.
2.
3.

---

## 2. Findability and Speed

- [ ] Added Open Graph + Twitter meta tags (title, description, preview image) — done in code
- [ ] Replaced all `REPLACE-WITH-YOUR-VERCEL-URL` placeholders with the real domain
- [ ] Added a favicon — done (inline SVG)
- [ ] Searched my own name / site on Google — does it appear? (may take days to index if brand new — note that honestly if so)
- [ ] Ran a free speed check — [PageSpeed Insights](https://pagespeed.web.dev/) or [GTmetrix](https://gtmetrix.com/) — paste score here:

**Speed check result:**
- Performance score: ___
- Any flagged issues:

---

## 3. Triage

**Fix-now** (broken links, real bugs, missing meta):
1.
2.

**Known limitation** (acknowledged, not hidden — e.g. "Book a call currently goes to a placeholder; no Calendly link set up yet"):
1.
2.

---

## 4. Fixes Applied

For each fix-now item, what was changed:

1. **Issue:** [e.g. "CV link was #"]
   **Fix:** [e.g. "Linked to hosted resume.pdf in repo"]

2. **Issue:**
   **Fix:**

---

## 5. Hardening Review

**Reviewer:** [mentor or peer]
**Feedback:**

**Must-fixes from review, addressed:**
1.
2.
