"""Build the static research homepage from publications.json. Python standard library only."""
from pathlib import Path
from html import escape as e
import json

ROOT = Path(__file__).resolve().parent
ORIGIN = 'https://jiweiqi.github.io'
PAPERS = json.loads((ROOT / 'publications.json').read_text(encoding='utf-8'))
GROUPS = {
    'sciml': ('01', 'Scientific machine learning', 'Differentiable simulation · Stiff systems · Reaction network discovery'),
    'uq': ('02', 'Uncertainty quantification', 'Active subspaces · Sensitivity analysis · Bayesian inference'),
    'applications': ('03', 'Reviews & applications', 'Research reviews · Energy · Mobility'),
    'kinetics': ('04', 'Combustion kinetics', 'Ignition experiments · Reaction kinetics'),
}
BIO = 'I am an Associate Professor and PhD supervisor in the School of Engineering Science at the University of Chinese Academy of Sciences. Previously, I was a Senior Research Scientist at Bosch and Apple, following postdoctoral research at MIT. I received my PhD from Tsinghua University.'
RESEARCH = 'My research focuses on scientific machine learning and uncertainty quantification, with an emphasis on learning physical dynamics, differentiable simulation and sensitivity analysis.'
LINKEDIN = 'https://www.linkedin.com/in/weiqiji'
TYPES = {'journal-article': 'Journal article', 'conference-paper': 'Conference paper', 'preprint': 'Preprint', 'workshop-paper': 'Workshop paper'}
RELATED = {
    'shared-subspaces': ['surrogate-subspace','turbulent-uq','flamelet-subspace'],
    'turbulent-uq': ['shared-subspaces','flamelet-subspace'],
    'ignition-sensitivity': ['premixed-sensitivity','kinetics-neural-ode'],
    'premixed-sensitivity': ['ignition-sensitivity','flamelet-subspace'],
    'mechanism-reduction-uq': ['shared-subspaces','sgd-kinetics'],
    'flamelet-subspace': ['shared-subspaces','turbulent-uq'],
    'shock-tube-bayes': ['kinetics-neural-ode','sgd-kinetics'],
    'crnn': ['biomass-crnn','stiff-neural-ode'],
    'stiff-pinn': ['stiff-neural-ode','crnn'],
    'stiff-neural-ode': ['stiff-pinn','arrhenius-jl'],
    'arrhenius-jl': ['sgd-kinetics','kinetics-neural-ode','neural-network-uq'],
    'sgd-kinetics': ['arrhenius-jl','hychem','kinetics-neural-ode'],
    'biomass-crnn': ['crnn'], 'kinet':['crnn','kinetics-neural-ode'],
    'inverse-combustors':['cellbox-adjoint','arrhenius-jl'],
    'cellbox-adjoint':['inverse-combustors','stiff-neural-ode'],
    'surrogate-subspace':['shared-subspaces','turbulent-uq'],
}
BY_ID = {p['id']: p for p in PAPERS}

def write(path, content):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding='utf-8')

def tags(p):
    return '<div class="tags">' + ''.join(f'<span class="tag">{e(t)}</span>' for t in p['keywords']) + '</div>'

def authors(p):
    return ', '.join('<strong>Weiqi Ji</strong>' if a == 'Weiqi Ji' else e(a) for a in p['authors'])

def venue(p):
    extra = str(p.get('volume') or '')
    if p.get('issue'): extra += f"({p['issue']})"
    if p.get('pages'): extra += f", {p['pages']}"
    return e(p['venue']) + (', ' + e(extra.lstrip(', ')) if extra else '') + f" · {p['year']}"

def bibtex(p):
    kind = 'article' if p['type'] == 'journal-article' else 'inproceedings' if p['type'] in ['conference-paper','workshop-paper'] else 'misc'
    fields = {'title': '{' + p['title'] + '}', 'author': ' and '.join(p['authors']), 'year': str(p['year'])}
    fields['journal' if kind == 'article' else 'booktitle' if kind == 'inproceedings' else 'howpublished'] = p['venue']
    for key in ['volume','pages','doi']:
        if p.get(key): fields[key] = str(p[key])
    if p.get('issue'): fields['number'] = str(p['issue'])
    if p.get('arxiv_id'): fields.update(eprint=p['arxiv_id'], archivePrefix='arXiv')
    fields['url'] = ORIGIN + '/papers/' + p['id'] + '/'
    return '@' + kind + '{' + p['id'].replace('-','') + str(p['year']) + ',\n' + ',\n'.join('  ' + k + ' = {' + v.replace('&',r'\&').replace('%',r'\%') + '}' for k,v in fields.items()) + '\n}\n'

def resources(p, overview=False):
    base = '/papers/' + p['id'] + '/'
    links = []
    if overview: links.append((base,'Read paper'))
    if p.get('pdf'): links.append((base+'paper.pdf','PDF'))
    elif p.get('external_pdf_url'): links.append((p['external_pdf_url'],'PDF ↗'))
    if p.get('fulltext_url'): links.append((base+'fulltext.txt','Full text'))
    if p.get('doi'): links.append(('https://doi.org/'+p['doi'],'DOI'))
    if p.get('code_url'): links.append((p['code_url'],'GitHub'))
    if p.get('related_code_url'): links.append((p['related_code_url'],'Related GitHub code'))
    links.extend([(base+'citation.bib','BibTeX')])
    if not overview: links.append((base+'index.md','Markdown'))
    return '<div class="links">' + ''.join(f'<a href="{e(url)}">{e(label)}</a>' for url,label in links) + '</div>'

def sidebar():
    nav = ''.join(f'<a href="/#{key}">{title}</a>' for key,(_,title,_) in GROUPS.items())
    return f'''<aside class="sidebar"><div class="sidebar-inner">
<div class="monogram" aria-hidden="true">WJ</div><h2 class="name">Weiqi Ji<span class="chinese" lang="zh-Hans">季维奇</span></h2>
<p class="affiliation">Associate Professor<br>PhD Supervisor<br>School of Engineering Science<br>University of Chinese Academy of Sciences</p>
<div class="profile-links"><a href="https://people.ucas.ac.cn/~0084227">UCAS</a><a href="https://scholar.google.com/citations?user=9b4iknkAAAAJ">Scholar</a><a href="https://orcid.org/0000-0002-7097-0219">ORCID</a><a href="https://github.com/jiweiqi">GitHub</a><a href="{LINKEDIN}">LinkedIn</a></div>
<nav aria-label="Research topics">{nav}<a href="/#downloads">Research files</a></nav>
<p class="sidebar-note">Research publications<br>and reproducible methods.</p></div></aside>'''

def page(title, description, body, path='/', extra='', paper=False, structured=None, indexable=True):
    schema = json.dumps(structured or {},ensure_ascii=False).replace('<','\\u003c')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(description)}"><link rel="canonical" href="{ORIGIN}{path}">
<meta name="author" content="Weiqi Ji"><meta name="robots" content="{'index,follow' if indexable else 'noindex'}"><meta property="og:type" content="{'article' if paper else 'website'}"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{ORIGIN}{path}">
<link rel="stylesheet" href="/assets/site.css"><link rel="alternate" type="application/json" href="/publications.json" title="Publication metadata">
{extra}<script type="application/ld+json">{schema}</script></head>
<body class="{'paper' if paper else 'home'}"><a class="skip" href="#main">Skip to content</a><div class="shell">{sidebar()}<main class="main" id="main">{body}
<footer class="footer"><span>Weiqi Ji</span><a href="https://github.com/jiweiqi/jiweiqi.github.io">Source on GitHub</a></footer></main></div>{'' if paper else '<script src="/assets/search.js" defer></script>'}</body></html>'''

def article(p):
    text=' '.join([p['title'],*p['authors'],p['summary'],*p['keywords'],p.get('abstract',''),str(p['year']),p.get('doi') or '']).lower()
    return f'''<article class="publication" data-topic="{p['topic']}" data-search="{e(text)}"><div class="year">{p['year']}</div><div>
<h3><a href="/papers/{p['id']}/">{e(p['title'])}</a></h3><p class="authors">{authors(p)}</p><p class="venue">{venue(p)} <span class="badge">{TYPES[p['type']]}</span></p>
<p class="summary">{e(p['summary'])}</p>{tags(p)}{resources(p,True)}</div></article>'''

def main():
    local_pdfs = sum(bool(p.get('pdf')) for p in PAPERS)
    body = f'''<header class="intro"><p class="eyebrow">Research / Publications</p><h1>Machine learning for<br>physical systems.</h1>
<p class="topic-line">Scientific machine learning · Uncertainty quantification · Sensitivity analysis</p>
<p class="bio">{BIO}</p><p>{RESEARCH}</p>
<div class="stats"><span><strong>{len(PAPERS)}</strong> papers &amp; preprints</span><span><strong>{local_pdfs}</strong> archived PDFs</span><span><strong>4</strong> research themes</span></div></header>
<div class="toolbox"><div class="search-field"><label for="paper-search">Search publications</label><input id="paper-search" type="search" placeholder="Title, method, author, DOI…" autocomplete="off"></div><div class="topic-field"><label for="topic-filter">Research area</label><select id="topic-filter"><option value="">All research areas</option>{''.join(f'<option value="{k}">{v[1]}</option>' for k,v in GROUPS.items())}</select></div></div>
<p class="results-status" id="results-status" role="status" aria-live="polite">{len(PAPERS)} publications</p><noscript><p>All publications are listed below. Use your browser’s Find command to search this page.</p></noscript><p id="empty-state" class="empty" hidden>No publications match this search. Try a different method or clear the research-area filter.</p>'''
    for group,(number,title,subtitle) in GROUPS.items():
        ps=sorted([p for p in PAPERS if p['topic']==group],key=lambda p:(-p['year'],p['title']))
        body += f'<section class="publication-section" id="{group}"><div class="section-head"><span class="section-number">{number}</span><h2>{title}<small>{subtitle}</small></h2></div>' + ''.join(article(p) for p in ps) + '</section>'
    body += '''<section class="access" id="downloads"><p class="eyebrow">Research files</p><h2>Read, cite, and explore.</h2><p>Each paper has a permanent page with its citation, research summary and available full text. Download the complete metadata or browse the repository for research with Codex and other tools.</p><div class="links"><a href="/publications.bib">All citations · BibTeX</a><a href="/publications.json">Metadata · JSON</a><a href="/publications.md">Paper index · Markdown</a><a href="/llms.txt">Text entry point</a><a href="https://github.com/jiweiqi/jiweiqi.github.io">Browse repository</a></div></section>'''
    person={'@context':'https://schema.org','@type':'ProfilePage','mainEntity':{'@type':'Person','name':'Weiqi Ji','url':ORIGIN,'description':BIO+' '+RESEARCH,'jobTitle':'Associate Professor and PhD Supervisor','worksFor':{'@type':'CollegeOrUniversity','name':'University of Chinese Academy of Sciences'},'alumniOf':{'@type':'CollegeOrUniversity','name':'Tsinghua University'},'sameAs':['https://orcid.org/0000-0002-7097-0219','https://people.ucas.ac.cn/~0084227','https://github.com/jiweiqi',LINKEDIN],'knowsAbout':['Scientific machine learning','Uncertainty quantification','Active subspaces','Sensitivity analysis','Chemical kinetics']}}
    write('index.html',page('Weiqi Ji · 季维奇 | Scientific Machine Learning & UQ','Weiqi Ji: scientific machine learning, uncertainty quantification, CRNN, Stiff-PINN and neural ODEs. Research profile, publications, PDFs and code.',body,structured=person))
    for p in PAPERS:
        base='papers/'+p['id']+'/'
        bib=bibtex(p);write(base+'citation.bib',bib)
        meta=f'<meta name="citation_title" content="{e(p["title"])}">\n<meta name="citation_publication_date" content="{p["year"]}">\n'
        meta+=''.join(f'<meta name="citation_author" content="{e(a)}">\n' for a in p['authors'])
        if p.get('doi'):meta+=f'<meta name="citation_doi" content="{e(p["doi"])}">\n'
        if p.get('pdf'):meta+=f'<meta name="citation_pdf_url" content="{ORIGIN}/{base}paper.pdf">\n'
        if p['type']!='preprint':
            meta+=f'<meta name="citation_{"journal_title" if p["type"]=="journal-article" else "conference_title"}" content="{e(p["venue"])}">\n'
        if p.get('arxiv_id'):meta+=f'<meta name="citation_arxiv_id" content="{p["arxiv_id"]}">\n'
        for key,value in [('volume',p.get('volume')),('issue',p.get('issue')),('firstpage',(p.get('pages') or '').split('-')[0])]:
            if value:meta+=f'<meta name="citation_{key}" content="{e(str(value))}">\n'
        body=f'<div class="breadcrumb"><a href="/#{p["topic"]}">Publications / {GROUPS[p["topic"]][1]}</a></div><p class="eyebrow">{p["year"]} / {TYPES[p["type"]]}</p><h1>{e(p["title"])}</h1><p class="authors">{authors(p)}</p><p class="venue">{venue(p)}</p><div class="paper-actions">{resources(p)}</div>'
        if p.get('abstract'):body+=f'<section><h2>Abstract</h2><p class="abstract">{e(p["abstract"])}</p></section>'
        body+=f'<section><h2>Research summary</h2><p>{e(p["summary"])}</p>{tags(p)}</section>'
        if p.get('pdf'):body+=f'<p class="source">PDF: {e(p["pdf"]["version"])} · <a href="{e(p["pdf"]["source_url"])}">Source</a>. The linked PDF is the reference for equations, figures and tables.</p>'
        else:body+=f'<p class="source">A PDF is not currently archived in this collection. <a href="{e("https://doi.org/"+p["doi"] if p.get("doi") else p["sources"][0])}">Publication record</a>.</p>'
        if p.get('arxiv_id'):body+=f'<p class="source">Preprint record: <a href="https://arxiv.org/abs/{p["arxiv_id"]}">arXiv:{p["arxiv_id"]}</a>.</p>'
        if p.get('correction_url'):body+=f'<p class="source"><a href="{p["correction_url"]}">Author correction for this article</a>.</p>'
        body+=f'<section><h2>Cite this work</h2><pre>{e(bib)}</pre></section>'
        if p['id'] in RELATED:
            body+='<section><h2>Related work in this collection</h2><div class="related">'+''.join(f'<a href="/papers/{s}/">{e(BY_ID[s]["title"])} ({BY_ID[s]["year"]})</a>' for s in RELATED[p['id']])+'</div></section>'
        schema={'@context':'https://schema.org','@type':'ScholarlyArticle','name':p['title'],'headline':p['title'],'author':[{'@type':'Person','name':a,**({'sameAs':'https://orcid.org/0000-0002-7097-0219'} if a=='Weiqi Ji' else {})} for a in p['authors']],'datePublished':str(p['year']),'url':ORIGIN+'/'+base,'identifier':p.get('doi') or p.get('arxiv_id'),'keywords':p['keywords'],'description':p['summary'],'isPartOf':{'@type':'Periodical' if p['type']=='journal-article' else 'CreativeWork','name':p['venue']}}
        if p.get('abstract'):schema['abstract']=p['abstract']
        if p.get('pdf'):schema['encoding']={'@type':'MediaObject','contentUrl':p['pdf']['url'],'encodingFormat':'application/pdf'}
        write(base+'index.html',page(p['title']+' | Weiqi Ji',p['summary'],body,'/'+base,meta,True,schema))
        md=f'# {p["title"]}\n\n'+', '.join(p['authors'])+f'\n\n{p["venue"]}, {p["year"]}. {TYPES[p["type"]]}.\n\n'
        if p.get('doi'):md+=f'DOI: https://doi.org/{p["doi"]}\n\n'
        md+=f'Canonical page: {ORIGIN}/{base}\n\n'
        if p.get('abstract'):md+='## Abstract\n\n'+p['abstract']+'\n\n'
        md+='## Research summary\n\n'+p['summary']+'\n\nKeywords: '+', '.join(p['keywords'])+'\n\n## Resources\n\n'
        for label,url in [('PDF',(p.get('pdf') or {}).get('url') or p.get('external_pdf_url')),('Extracted full text',p.get('fulltext_url')),('GitHub',p.get('code_url')),('Related GitHub code',p.get('related_code_url')),('BibTeX',ORIGIN+'/'+base+'citation.bib')]:
            if url:md+=f'- [{label}]({url})\n'
        md+='\n## Sources\n\n'+''.join(f'- {url}\n' for url in p['sources'])
        md+='\n## Citation\n\n```bibtex\n'+bib+'```\n'
        write(base+'index.md',md)
    write('publications.bib','\n'.join(bibtex(p) for p in PAPERS))
    md='# Weiqi Ji · 季维奇 — Research publications\n\n'+ORIGIN+'\n\n'
    for group,(_,title,subtitle) in GROUPS.items():
        md+=f'## {title}\n\n'
        for p in sorted([x for x in PAPERS if x['topic']==group],key=lambda x:-x['year']):
            md+=f'- **{p["year"]}** [{p["title"]}]({ORIGIN}/papers/{p["id"]}/index.md) — {p["summary"]}\n'
        md+='\n'
    write('publications.md',md)
    llms='# Weiqi Ji (季维奇)\n\n'+BIO+'\n\n'+RESEARCH+'\n\n[LinkedIn]('+LINKEDIN+')\n\n## Catalog\n\n- [Research homepage]('+ORIGIN+'/): publication pages and research themes.\n- [Structured metadata]('+ORIGIN+'/publications.json): titles, authors, publication types, DOI, abstracts, summaries, GitHub repositories and full-text locations.\n- [BibTeX]('+ORIGIN+'/publications.bib): citations for the collection.\n- [Markdown index]('+ORIGIN+'/publications.md): papers grouped by research topic.\n\n## Full text\n\n'
    for p in PAPERS:
        llms+=f'- [{p["title"]}]({ORIGIN}/papers/{p["id"]}/index.md)'
        if p.get('fulltext_url'):llms+=f' | [text]({p["fulltext_url"]}) | [PDF]({p["pdf"]["url"]})'
        elif p.get('external_pdf_url'):llms+=f' | [PDF]({p["external_pdf_url"]})'
        if p.get('code_url'):llms+=f' | [GitHub]({p["code_url"]})'
        if p.get('related_code_url'):llms+=f' | [related code]({p["related_code_url"]})'
        llms+='\n'
    llms+='\nPDF text extraction may lose mathematical notation and table layout. Consult the PDF when studying equations, figures or tables. Publication type and preprint identifiers are recorded separately in the catalog.\n'
    write('llms.txt',llms)
    urls=[ORIGIN+'/']+[ORIGIN+'/papers/'+p['id']+'/' for p in PAPERS]
    write('sitemap.xml','<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{e(u)}</loc></url>\n' for u in urls)+'</urlset>\n')
    write('robots.txt','User-agent: *\nAllow: /\n\nSitemap: '+ORIGIN+'/sitemap.xml\n')
    write('404.html',page('Page not found | Weiqi Ji','Return to the research publication index.','<h1>Page not found</h1><p><a href="/">Browse research publications</a></p>','/404.html',indexable=False))
    print(f'Built homepage, {len(PAPERS)} paper pages, metadata and citations; {local_pdfs} local PDFs.')

if __name__=='__main__':main()
