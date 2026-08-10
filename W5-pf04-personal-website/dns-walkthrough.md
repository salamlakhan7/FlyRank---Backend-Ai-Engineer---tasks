# DNS Walkthrough — Personal Website (PF-04)
**Abdul Salam**

This is a plain-language walkthrough of how my site's domain works today, and what will change when my FlyRank subdomain (`abdul.flyrank.ai`, for example) is provisioned later.

## What a CNAME record is

A CNAME (Canonical Name) record is a DNS entry that says "this domain name is really just another name for that domain name." It doesn't point to an IP address directly — it points to *another hostname*, which is then looked up in turn. Think of it like a forwarding label on a mailbox: mail addressed to Name A actually gets redirected to Name B's address, and Name B is the one that actually knows how to receive it.

## The record my site will hold

Once my FlyRank subdomain is provisioned, Ops will create a CNAME record that looks roughly like:

```
Name:  abdul.flyrank.ai
Type:  CNAME
Value: [my-site].vercel-dns.com   (or Netlify/host equivalent)
```

That record tells anyone asking about `abdul.flyrank.ai` to go look up my hosting provider's address instead — my host (Vercel) is still the one actually serving the site's files.

## What happens when someone types my address

Here's the full chain, step by step, from someone typing `abdul.flyrank.ai` into a browser to the page appearing on their screen:

1. **You type the address.** Your browser needs to turn that human-readable name into a computer-readable IP address before it can request anything.

2. **The resolver is asked first.** Your device sends the request to a "resolver" — usually run by your internet provider or a public one like Google's (8.8.8.8). Its job is to go find the answer on your behalf and hand it back.

3. **The resolver asks a nameserver.** If the resolver doesn't already know the answer (cached from a recent lookup), it asks the nameserver responsible for the `flyrank.ai` domain. A nameserver is essentially the "source of truth" for a domain's DNS records.

4. **The nameserver returns the record.** For `abdul.flyrank.ai`, the nameserver returns the CNAME record — "this name really points to `[my-site].vercel-dns.com`." The resolver then has to repeat steps 3-4 for *that* name too, since a CNAME just points further down the chain, until it eventually reaches an actual IP address.

5. **The resolver responds to your browser.** Once the full chain resolves to a real IP address, the resolver hands that IP back to your browser.

6. **Your browser connects and requests the page.** Your browser opens a connection to that IP address, requests the site over HTTPS, and my host (Vercel) serves the actual HTML/CSS/JS files — the same files sitting in this repo.

7. **HTTPS certificate check.** Along the way, your browser also checks that the site has a valid SSL certificate for that domain (this is what gives the padlock icon) before it will load and display the page safely.

## Why I'm writing this before I need it

Right now my site lives on a free URL (e.g. `abdul-portfolio.vercel.app`) and there's no FlyRank subdomain to configure yet — nothing above has been set up in practice. This walkthrough is the checklist I'll follow when the subdomain *is* granted: add the custom domain in my host's settings, confirm the CNAME record matches what Ops created, wait for propagation, and check the padlock loads correctly. Writing it now, while I don't need it yet, means I'm not learning DNS under deadline pressure at capstone time — I just execute the steps above.
