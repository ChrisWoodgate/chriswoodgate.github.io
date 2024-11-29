---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  You can also find a list of my publications on <a href="{{site.author.googlescholar}}" style="color:#52adc8;">my Google Scholar profile</a> or via <a href="{{site.author.orcid}}" style="color:#52adc8;">my ORCID</a>.
{% endif %}

{% include base_path %}

<h2> Book </h2>

More details about my book can be found via <a href="https://link.springer.com/book/9783031620201" style="color:#52adc8;">this link</a> or on the <a href="/book" style="color:#52adc8;">book page</a> of this site.

{% for post in site.publications reversed %}
  {% if post.published == 'book' %}
    {% include archive-book.html %}
  {% endif %}
{% endfor %}

<!---
<h2> Preprints </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'preprint' %}
    {% include archive-preprint.html %}
  {% endif %}
{% endfor %}
--->

<h2> Journal Articles </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'journal' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
