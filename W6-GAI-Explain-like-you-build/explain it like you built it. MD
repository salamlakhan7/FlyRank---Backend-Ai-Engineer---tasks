# Explain It Like You Built It
**Piece explained:** How the styling works — CSS variables and the "API-endpoint look"

---

If you open up my site's code, near the top there's a small block where I define a handful of colors once and give each one a nickname — like calling my dark background color "ink" and my green accent color "signal." Everywhere else in the file, instead of typing the actual color code over and over, I just say "use ink here" or "use signal there."

The point of doing it this way is simple: if I ever want to change my accent color, I change it in exactly one place, and every button, dot, and border that uses it updates automatically. Without this, I'd have to hunt through hundreds of lines and change the same color by hand every time it appears — and I'd probably miss a few.

The second piece — making my projects look like API responses instead of plain boxes — isn't one special trick, it's a few ordinary ideas stacked together:

1. I used a monospace font (where every letter takes up the same width) for the labels. That's the same style of font code editors and terminals use, so it visually signals "this is technical" before you even read the words.
2. I styled the word "GET" as a small solid-colored badge — a background color, a little padding, and slightly rounded corners — the same way tools like Postman color-code HTTP methods.
3. I used a layout trick called flexbox to push the "200 OK" text all the way to the right side of its row automatically, while the method and path stay on the left — mimicking how a terminal or log line lays out a status.

None of these are complicated on their own. What makes it read as "an API response" instead of "three random text elements" is combining a technical font, a colored badge, and right-aligned status text — plus naming the pieces GET, path, and status code, so the pattern is unmistakable even though it's really just plain HTML and CSS underneath.
