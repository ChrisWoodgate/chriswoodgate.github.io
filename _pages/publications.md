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

I have authored a book outlining our approach for modelling atomic arrangements in multicomponent alloys, which is set to be published by Springer Nature in late-2024 as part of the <a href="https://www.springer.com/series/0856" style="color:#52adc8;">Springer Series in Materials Science</a>. More details can be found via <a href="https://link.springer.com/book/9783031620201" style="color:#52adc8;">this link</a> or on the <a href="/book" style="color:#52adc8;">book page</a> of this site.

<h2> Preprints </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'preprint' %}
    {% include archive-preprint.html %}
  {% endif %}
{% endfor %}

<h2> Journal Articles </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'journal' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
