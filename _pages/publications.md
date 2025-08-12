---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Here you can find a list of my academic publications and preprints.  {% if site.author.googlescholar %} You can also find a list of my publications on <a href="{{site.author.googlescholar}}" style="color:#52adc8;">my Google Scholar profile</a> or via <a href="{{site.author.orcid}}" style="color:#52adc8;">my ORCID</a>. {% endif %} When I am first-author&mdash;and where it is appropriate to the nature of the work&mdash;I aim to provide open-access datasets associated with my publications, which I typically make available on <a href="https://zenodo.org" style="color:#52adc8;">Zenodo</a>.

{% include base_path %}

<h2> Book </h2>

Below are the details of my book, published in the Springer Series in Materials Science. More details can be found via <a href="https://link.springer.com/book/9783031620201" style="color:#52adc8;">this link</a> or on the <a href="/book" style="color:#52adc8;">book page</a> of this site.

{% for post in site.publications reversed %}
  {% if post.published == 'book' %}
    {% include archive-book.html %}
  {% endif %}
{% endfor %}

<h2> Preprints </h2>
Below is a list of my current preprints available on the <a href="https://arxiv.org" style="color:#52adc8;">arXiv</a>. Note that this will not always be a comprehensive list of the articles I currently have under review at any one time; particularly when I am working as part of a larger collaboration, it may not be possible to share a preprint of an article to be shared ahead of its publication in a journal.

{% for post in site.publications reversed %}
  {% if post.published == 'preprint' %}
    {% include archive-preprint.html %}
  {% endif %}
{% endfor %}

<h2> Journal Articles </h2>
Below is a list of my published articles in peer-reviewed journals. Where available, I also provide a link to a version of the article on the <a href="https://arxiv.org" style="color:#52adc8;">arXiv</a>.

{% for post in site.publications reversed %}
  {% if post.published == 'journal' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
