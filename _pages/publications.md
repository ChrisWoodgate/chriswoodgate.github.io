---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  You can also find my articles on <a href="{{site.author.googlescholar}}" style="color:#52adc8;">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

<h2> Preprints </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'preprint' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2> Published Articles </h2>

{% for post in site.publications reversed %}
  {% if post.published == 'journal' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
