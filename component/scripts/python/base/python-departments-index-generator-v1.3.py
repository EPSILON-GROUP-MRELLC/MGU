import os

BASE_DIR = "departments"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Malone University - Explore knowledge, courses, and community resources.">
  <title>{title}</title>
  <link rel="icon" href="images/favicon.ico" type="image/x-icon">
  <style>
    /* [Your existing CSS from v2.py goes here] */
  </style>
</head>
<body>
  <a href="#main-content" class="skip-link">Skip to content</a>
  <header class="navbar" role="navigation" aria-label="Main Navigation">
    <div class="logo-container">
      <img src="logo.png" alt="Malone University Logo" class="logo-img">
      <span class="school-name">Malone University</span>
    </div>
    <ul class="nav-links" id="nav-links">
      <li><a href="#">Home</a></li>
      <li><a href="#">Departments</a></li>
      <li><a href="#">Courses</a></li>
      <li><a href="#">Community</a></li>
      <li><a href="#">Encyclopedia</a></li>
    </ul>
    <div style="display:flex;align-items:center;">
      <div class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" role="button" tabindex="0">
        <span></span><span></span><span></span>
      </div>
      <button id="theme-toggle" title="Toggle theme" aria-pressed="false">💻</button>
    </div>
  </header>

  <div class="hero">
    <h1>{h1}</h1>
    <p>Explore knowledge, courses, and community resources.</p>
  </div>

  <main id="main-content" role="main">
    <section aria-labelledby="subfolders-section">
      <h2 id="subfolders-section">Subfolders</h2>
      {subfolders_links}
    </section>
  </main>

  <footer>
    <p>© 2025 Malone University. Building the future, on our own terms.</p>
    <p>
      <a href="https://twitter.com/MaloneGlobal" target="_blank" rel="noopener noreferrer">Twitter</a> |
      <a href="https://facebook.com/YOUR_HANDLE" target="_blank" rel="noopener noreferrer">Facebook</a> |
      <a href="https://instagram.com/maloneglobaluniversity" target="_blank" rel="noopener noreferrer">Instagram</a> |
      <a href="/static/terms.html">Terms</a> |
      <a href="/static/contact.html">Contact</a>
    </p>
    Updated 08/14/2025.
  </footer>

  <script>
    /* [Your existing theme & nav toggle script goes here] */
  </script>
</body>
</html>
"""

for root, dirs, files in os.walk(BASE_DIR):
    folder_name = os.path.basename(root).replace("-", " ").title()
    index_path = os.path.join(root, "index.html")

    # Generate HTML list of subfolders as links
    if dirs:
        links_html = "<ul>\n"
        for d in dirs:
            links_html += f'  <li><a href="{d}/index.html">{d.replace("-", " ").title()}</a></li>\n'
        links_html += "</ul>"
    else:
        links_html = "<p>No subfolders available.</p>"

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE.format(
            title=f"{folder_name} - Malone University",
            h1=folder_name,
            subfolders_links=links_html
        ))
    print(f"Created {index_path}")
