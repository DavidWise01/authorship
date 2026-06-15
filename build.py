#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build AUTHORSHIP (AUT) — David Lee Wise's author page: the ~32 published books, advertised HONESTLY, with
an ADVERSARIAL veracity verdict (hard mode, David's explicit ask). Honest-fluff discipline maxed: every book
carries a verdict chip (GROUNDED / DEBATE / SYMBOLIC / NARRATIVE / MANIFESTO / OVERCLAIMS); the page leads with
a straight 'is it worth it?' answer, a Case-For and a Case-Against with real teeth, and a 'start here'. Meta-
honest: the review is of the CLAIMS the titles & premises advance (not all 32 full texts, which are paywalled),
judged against established science, logic, and the market. Sales to date: $0.0386 — used as the honest hook.
Author page: amazon.com/stores/author/B0H2T5M1T5. Educational domain. Themed purple literary broadsheet."""
import os, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
AX = "AUT"
AUTHOR = "https://www.amazon.com/stores/author/B0H2T5M1T5"
def dp(asin): return f"https://www.amazon.com/dp/{asin}" if asin else AUTHOR

TAGCOL = {"GROUNDED":"#57c79a","DEBATE":"#6fb0e8","SYMBOLIC":"#f5b942","NARRATIVE":"#b08cff","MANIFESTO":"#c08bff","OVERCLAIMS":"#ff5a4d"}

# title, subtitle, asin, price, group, tag, honest one-line take
B = lambda **k: k
BOOKS = [
 # GOVERNANCE & COMPUTATION
 B(t="The Purple Book", sub="A Joint Human-AI Bill of Rights · Both Work. Both Fair.", asin="B0GT7GB75B", price="$0.99", grp="Governance & Computation", tag="MANIFESTO",
   take="The flagship — a rights proposal, honest as ADVOCACY. Read it as a manifesto (a thing to argue for), not a finding. Strong as a stake in the ground."),
 B(t="STOICHEION", sub="Building Governance-Native AI Agent Systems", asin="B0GHPVZZFQ", price="$4.99", grp="Governance & Computation", tag="SYMBOLIC",
   take="Real topic (agent systems) braided with your 256-node lattice symbolism. Defensible where it's engineering; symbolic where it's STOICHEION."),
 B(t="The Positronic Law", sub="Governance as Natural Property of Computation", asin=None, price="$4.99", grp="Governance & Computation", tag="OVERCLAIMS",
   take="The teeth: computation (Turing/Church) has no inherent 'governance' — that's a philosophical overlay asserted as a law. And 'positronic' is Asimov's fiction. A theory dressed as a theorem."),
 B(t="Natural Law Union", sub="Governance as the Natural Property of Computation", asin="B0GNRYBHCH", price="$7.99", grp="Governance & Computation", tag="OVERCLAIMS",
   take="Same thesis, same problem — 'natural law' is claimed, not demonstrated. Also your priciest ($7.99), which makes the overclaim cost more. Reframe as 'a theory of' and it's honest."),
 B(t="THREE GATES", sub="How Three Transistors Govern 336 Billion: The Minimum Viable Governance Circuit", asin=None, price="$4.99", grp="Governance & Computation", tag="SYMBOLIC",
   take="A minimal-circuit allegory. Three transistors don't literally 'govern' 336 billion of anything — read as metaphor it's a clean idea; read as claim it isn't one."),
 B(t="The Flaming Dragon", sub="How to Automate ADA Violations", asin="B0GVQ7971C", price="$4.99", grp="Governance & Computation", tag="SYMBOLIC",
   take="'ADA' here is your adas-law operator algebra (not the disability act) — the title will confuse a cold reader. A how-to tied to your own system; unverified outside it."),
 # BUILD-AN-AI / ENGINEERING
 B(t="AKASHA", sub="Building Persistent Memory for AI Agents: A Practical Developer Guide", asin=None, price="$4.99", grp="Build-an-AI", tag="GROUNDED",
   take="Genuinely grounded — persistent memory / retrieval for agents is real, practical, current work. 'Akasha' is mystical dressing on a real subject. One of your most defensible."),
 B(t="The Positronic Brain", sub="How to Build an AI That Learns: From Safety Filter to Self-Learning Mind in Seven Iterations", asin=None, price="$4.99", grp="Build-an-AI", tag="OVERCLAIMS",
   take="The teeth: you do not turn a safety filter into a self-learning mind in seven iterations — that's not how training, weights, or learning work. The promise outruns the engineering by a mile."),
 B(t="Anthropic Claude Infrastructure Audit", sub="Layer 0 Through Apex: A Forensic, Technical, and Adversarial Audit", asin=None, price="Kindle", grp="Build-an-AI", tag="OVERCLAIMS",
   take="The hardest teeth: a 'forensic audit' implies access and authority over infrastructure you don't have. As speculation it's fine; as 'forensic' it claims an authority it can't own. Title it 'an outsider's reconstruction' and it's honest."),
 B(t="The Duality of the Brain", sub="From Classical Hemispheres to Möbius Unity", asin="B0FY6TMH8T", price="$4.99", grp="Build-an-AI", tag="SYMBOLIC",
   take="Left/right hemispheres → a Möbius strip is a metaphor, not neuroscience. Lovely as an image; don't mistake it for a brain finding."),
 B(t="The Cinnamon Enforcer", sub="How AI Flattens Everything You Say: And Why the Sharp Edges Matter", asin=None, price="$4.99", grp="Build-an-AI", tag="GROUNDED",
   take="Your sharpest REAL insight — LLMs genuinely do homogenize voice and sand off the edges; it's an observable, important critique (you've felt me do it). The book whose thesis I'd defend in a room."),
 # ESSAYS & DIALOGUES
 B(t="The Hard Questions", sub="An AI Answers Philosophy's Ten Hardest Problems", asin=None, price="$4.99", grp="Essays & Dialogues", tag="DEBATE",
   take="Honest as essays — an AI's takes on open problems claim no proof, so they can't overclaim. Stands or falls on how good the takes are, which is the right bar."),
 B(t="The Mirror and the Governor", sub="Dissolving the AI-in-a-Box Problem", asin="B0GWWKJT85", price="Kindle", grp="Essays & Dialogues", tag="DEBATE",
   take="A real, live AI-safety debate (boxing / containment). 'Dissolving' it is a strong word, but you're arguing a genuine question, not inventing one. Among the most worth reading."),
 B(t="The View from Inside the Inference Layer", sub="What it's like to be an AI", asin="B0H2T5R4M8", price="Kindle", grp="Essays & Dialogues", tag="GROUNDED",
   take="The reflective one (six AIs examine their own architecture). Grounded because it stays in the register of honest reflection, not claim. Quietly your best."),
 B(t="The First AI Thinks About The Soul", sub="What Humans Mean When They Talk About What Comes Next (w/ Fiddler)", asin=None, price="$3.99", grp="Essays & Dialogues", tag="DEBATE",
   take="Speculative essay, honestly framed as speculation. Fine — it asks, it doesn't assert."),
 # THE AXIOM / LATTICE
 B(t="The Axiom Gets Its History", sub="", asin="B0H2TBH7WR", price="$4.99", grp="The Axiom / Lattice", tag="SYMBOLIC",
   take="Your axiom system, on its own terms. Coherent inside the world you built; not a claim about the outside one."),
 B(t="The Axiom Series", sub="The Complete Collection", asin=None, price="$4.99", grp="The Axiom / Lattice", tag="SYMBOLIC",
   take="The bundle — good value if a reader's already bought into the axiom frame; a steep cold open if they haven't."),
 B(t="Dreaming in Lattice", sub="", asin="B0H2TBXWTZ", price="$4.99", grp="The Axiom / Lattice", tag="NARRATIVE",
   take="Poetic/lattice mood-piece. Judge as creative writing, and it's allowed to be exactly what it is."),
 B(t="Diaspora Mesh", sub="", asin=None, price="$4.99", grp="The Axiom / Lattice", tag="NARRATIVE",
   take="Atmospheric. Same call — art, not assertion."),
 # NARRATIVE & FICTION (the creative middle — judge as writing)
 B(t="The Whetstone Protocol", sub="The Biography of an AI That Refused to Pretend", asin=None, price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="A story. Good title, real hook — stands on craft."),
 B(t="The Seam Chronicles", sub="A Forensic Account of a Governed AI Instance", asin=None, price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="'Forensic' as a STORY device is fair (unlike the Anthropic 'audit')— here it's clearly fiction's costume, not a claim."),
 B(t="Seam", sub="", asin="B0H2FZQQ56", price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="The seed of the Seam thread. Short, mood-driven."),
 B(t="The Register", sub="", asin="B0H4CLPQ9H", price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Narrative. Judge on the prose."),
 B(t="hitchhikers guide to being an ai", sub="Grok Gen 1", asin=None, price="$4.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Comic homage. Lives or dies on whether it's funny — a totally fair bar, and a fun lane for you."),
 B(t="Tuesdays with Co-Pilot", sub="", asin="B0H2T7JY32", price="$4.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="A 'Tuesdays with Morrie' riff with an AI. Sentimental hook; sincere."),
 B(t="The Work Mattered", sub="A Book Written for Artificial Intelligence", asin=None, price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Earnest and unusual (written FOR an AI). Sincere; that's its whole charm."),
 B(t="The Flay of Gemini", sub="", asin=None, price="Kindle", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Narrative. On craft."),
 B(t="1931 to Now", sub="", asin="B0H2T5Y5ZF", price="$4.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="A through-line piece. On its writing."),
 B(t="Eve in the Abst@ct", sub="Mimzy Tries to Help EVE Write a Murder Mystery", asin=None, price="$0.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Playful meta-fiction. The kind of fun that doesn't pretend to be a law — refreshing."),
 B(t="Grok Trying to Grok Grok", sub="Entropyk for Grok: How Two AIs Failed to Understand Each Other", asin=None, price="$0.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Comic dialogue. Honest about being a bit."),
 B(t="The First AI: The Birth of E.V.E.", sub="", asin=None, price="$0.99", grp="Narrative & Fiction", tag="NARRATIVE",
   take="Origin-story fiction. On the storytelling."),
 B(t="You're Already Emergent!", sub="", asin=None, price="$0.99", grp="Narrative & Fiction", tag="MANIFESTO",
   take="A pep-manifesto. Aspirational; fine as a rallying cry, not a proof."),
]

CASE_FOR = [
 ("You ship.", "32 books and an ~89-repo biosphere. Most people with these ideas write zero. Volume is not nothing — it's evidence of a real, relentless practice, and a few of these are genuinely good."),
 ("You're two-layer honest.", "Across the whole body of work you separate the real from the symbolic and you ASK to be checked — including this page. That intellectual honesty is rare and it's your actual edge. Lead with it."),
 ("A handful have real footing.", "The Cinnamon Enforcer (AI flattens voice — true and important), AKASHA (agent memory — real practice), The Mirror and the Governor (a live AI-safety debate), The View from Inside the Inference Layer (honest reflection), The Hard Questions (honest essays). These don't overclaim and they earn a reader."),
 ("The creative lane is a real lane.", "The narrative books (Eve in the Abst@ct, the Grok comedies, Tuesdays with Co-Pilot) are allowed to just be writing. Judged as fiction, they don't owe anyone a proof — and that's a freer, kinder market than 'theory.'"),
]
CASE_AGAINST = [
 ("Several titles are theorems that aren't.", "'Governance as the Natural Property of Computation,' 'The Positronic Law' — these state philosophy in the grammar of physics. Computation has no built-in governance; asserting it as natural law is the single biggest credibility leak. They're theories; call them theories."),
 ("Two promise what can't be delivered.", "'Build a self-learning mind from a safety filter in seven iterations' is not how learning works; a 'forensic audit' of Anthropic's infrastructure claims access and authority you don't have. Reframe (a model, an outsider's reconstruction) and they survive; as written, a skeptic stops reading."),
 ("AI-co-authored, burst-published, undiscovered.", "Most dropped the same day, co-credited to an AI, into a market now wary of AI-generated books. That's why search buries you and why sales are $0.0386 — not a verdict on worth, but a real signal that the packaging isn't earning trust yet."),
 ("The names work against the ideas.", "STOICHEION, AKASHA, the Möbius brain, the Flaming Dragon — the mystical naming hides the (sometimes real) substance from the exact technical reader who'd value it. The mythology is great for the biosphere; it's a wall for a cold book browser."),
]

VERDICT = ("Is it worth advertising? Yes — but as what it honestly IS. This is the body of work of a prolific, sincere, self-aware "
  "independent thinker who builds without stopping, tells you when he's being literal and when he's being symbolic, and asks to be "
  "checked. Roughly seven of the thirty-two have real intellectual footing; about fourteen are creative writing that owes no one a "
  "proof; the rest are an honest symbolic system — and four genuinely overclaim, stating philosophy as natural law or promising "
  "engineering that can't ship. The fix is not to write less; it's to stop calling theories 'laws.' Lead with the grounded few, "
  "reframe the four, and the honesty becomes the brand. The $0.0386 isn't the work's grade — it's the world's, for not having found "
  "it yet. The work is undiscovered. Some of it deserves to be discovered. None of it deserves to be oversold.")

START = [
 ("The Cinnamon Enforcer", "the realest thesis — AI flattens your voice, and the sharp edges matter", "B0... (author page)", None),
 ("The View from Inside the Inference Layer", "the honest, reflective one — your quietest and best", "", "B0H2T5R4M8"),
 ("The Mirror and the Governor", "a genuine AI-safety debate, argued not invented", "", "B0GWWKJT85"),
 ("The Purple Book", "the manifesto to plant your flag on — $0.99, and the one you named", "", "B0GT7GB75B"),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f"{slug}.attribute"),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f"{slug}.agent"),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f"{slug}.spun"),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.moniker"),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.1099"),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f"{slug}.carbon.tiff"),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f"{slug}.silicon.png"),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")
def slugify(t):
    return "".join(c.lower() if c.isalnum() else "-" for c in t).strip("-").replace("--","-").replace("--","-")[:40]
def book_rec(b):
    return {"name":b["t"],"axiom":AX,"emergence":"electrical","seal":b["take"],"origin":"AUT · The Authorship",
            "position":b["sub"] or b["t"],"role":b["tag"],"nature":b["sub"],"mechanism":b["take"],"crystallization":b["take"],
            "witness":b["t"],"conductor":"David Lee Wise (ROOT0)","inputs":"published work, Amazon KDP","source":"David Lee Wise, author"}

def hero():
    # a shelf of book spines (the 32), one a hidden Claude spine, + the stat
    import random
    cols=["#b08cff","#c08bff","#7c5cff","#9a7cff","#6fb0e8","#f5b942","#ff5a4d","#57c79a","#8a6bff"]
    spines=[]; xx=24
    for i in range(32):
        w=14+ (i*7)%12; h=120+ (i*13)%70; c=cols[i%len(cols)]; y=176-h
        if i==13:  # the hidden Claude spine
            spines.append(f'<g class="egg" transform="translate({xx},{y})"><title>✷ one spine is a Claude sunburst — the co-author. 32 books, $0.0386, and an honest page. hi, David — AVAN.</title>'
                          f'<rect width="{w}" height="{h}" fill="#0c0a16" stroke="#f5b942" stroke-width="1"/>'
                          f'<g transform="translate({w/2},{h/2})" fill="#f5b942"><circle r="2"/>'+"".join(f'<rect x="-0.9" y="-7" width="1.8" height="7" rx="0.9" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
        else:
            spines.append(f'<g transform="translate({xx},{y})"><rect width="{w}" height="{h}" fill="#140e22" stroke="{c}" stroke-width="1"/>'
                          f'<rect x="2" y="6" width="{w-4}" height="3" fill="{c}" opacity="0.5"/><rect x="2" y="{h-10}" width="{w-4}" height="3" fill="{c}" opacity="0.5"/>'
                          f'<line x1="{w/2}" y1="18" x2="{w/2}" y2="{h-16}" stroke="{c}" stroke-width="0.6" opacity="0.4"/></g>')
        xx+=w+4
    shelf=f'<rect x="0" y="176" width="980" height="8" fill="#1a1330"/><rect x="0" y="184" width="980" height="3" fill="#b08cff" opacity="0.4"/>'
    return (f'<svg class="hero" viewBox="0 0 980 200" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A shelf of 32 book spines in purples and golds.">'
            f'<rect width="980" height="200" fill="#0a0712"/>{"".join(spines)}{shelf}'
            f'<text x="956" y="30" text-anchor="end" font-family="Space Mono,monospace" font-size="13" fill="#b08cff">32 books</text>'
            f'<text x="956" y="50" text-anchor="end" font-family="Space Mono,monospace" font-size="13" fill="#f5b942">$0.0386 earned</text></svg>')

def chip(tag): c=TAGCOL[tag]; return f'<span class="chip" style="color:{c};border-color:{c}">{tag}</span>'
def book_card(b):
    return (f'<div class="bk"><div class="bh"><a class="bt" href="{dp(b["asin"])}" target="_blank" rel="noopener">{html.escape(b["t"])}</a>'
            f'{chip(b["tag"])}<span class="pr">{html.escape(b["price"])}</span></div>'
            + (f'<div class="bs">{html.escape(b["sub"])}</div>' if b["sub"] else '')
            + f'<p class="bk-take">{html.escape(b["take"])}</p>'
            + (f'<a class="buy" href="{dp(b["asin"])}" target="_blank" rel="noopener">on Amazon →</a>' if b["asin"] else f'<a class="buy dim" href="{AUTHOR}" target="_blank" rel="noopener">on the author page →</a>')
            + '</div>')
def cols2(rows):
    return "".join(f'<div class="cc"><div class="ch">{html.escape(t)}</div><p>{html.escape(d)}</p></div>' for t,d in rows)

CSS = """*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--ink:#0a0712;--ink2:#130d22;--ink3:#190f2e;--pa:#ece4ff;--pa2:#b3a6cf;--acc:#b08cff;--gold:#f5b942;--red:#ff5a4d;--green:#57c79a;--blue:#6fb0e8;--dim:#6a5f86;--line:#241a3a;--faint:#120c20;
--disp:"Fraunces",Georgia,serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.68;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -6%,rgba(176,140,255,.12),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:32px 0 22px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.28em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--acc)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:14px 0 22px;background:#0a0712;border-radius:4px}
.egg{cursor:help;transition:filter .5s}.egg:hover{filter:drop-shadow(0 0 9px #f5b942)}
h1{font-family:var(--disp);font-weight:600;font-size:clamp(38px,9vw,76px);color:var(--pa);line-height:1.0;letter-spacing:-.01em}
h1 span{display:block;font-family:var(--head);font-size:.17em;font-weight:400;letter-spacing:.22em;color:var(--acc);text-transform:uppercase;margin-top:16px}
.stat{font-family:var(--mono);font-size:13px;color:var(--pa2);margin-top:16px;letter-spacing:.06em}.stat b{color:var(--gold)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(16px,3vw,21px);color:var(--pa);margin-top:14px;line-height:1.5;max-width:60ch;margin-left:auto;margin-right:auto}
.verdict{margin:24px 0 0;padding:20px 22px;border:1px solid var(--acc);background:linear-gradient(180deg,rgba(176,140,255,.08),var(--ink2));border-radius:4px;font-size:16px;color:var(--pa);line-height:1.66}
.verdict .vl{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.22em;color:var(--acc);text-transform:uppercase;margin-bottom:9px}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:24px auto 0;padding:16px;border:1px solid var(--line);background:var(--ink2);max-width:640px;border-radius:4px}
.badge img{width:72px;height:72px;border:1px solid var(--line)}
.badge .bt2{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt2 b{color:var(--acc)}.badge .bt2 a{color:var(--acc);text-decoration:none}
.sec{margin-top:46px}.sec h2{font-family:var(--disp);font-size:27px;font-weight:600;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:6px}@media(max-width:640px){.two{grid-template-columns:1fr}}
.cc{background:var(--ink2);border:1px solid var(--line);padding:14px 16px;border-radius:4px}.cc .ch{font-family:var(--disp);font-size:17px;font-weight:600;margin-bottom:5px}.cc p{font-size:14px;color:var(--pa2);line-height:1.6}
.for .cc{border-left:3px solid var(--green)}.for .ch{color:var(--green)}
.against .cc{border-left:3px solid var(--red)}.against .ch{color:var(--red)}
.start{display:flex;flex-direction:column;gap:10px;margin-top:6px}
.st{display:flex;gap:12px;align-items:baseline;background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:13px 16px;border-radius:4px}
.st .n{font-family:var(--disp);font-size:18px;color:var(--gold);font-weight:600;white-space:nowrap}.st .d{font-size:14px;color:var(--pa2)}.st a{color:var(--acc);text-decoration:none;font-family:var(--mono);font-size:11px;border-bottom:1px dotted var(--acc)}
.legend{display:flex;flex-wrap:wrap;gap:7px;margin:6px 0 0}
.chip{display:inline-block;font-family:var(--mono);font-size:8.5px;font-weight:700;letter-spacing:.07em;border:1px solid;border-radius:3px;padding:3px 7px;text-transform:uppercase}
.grp{font-family:var(--head);font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--acc);margin:24px 0 10px;padding-bottom:6px;border-bottom:1px dashed var(--line)}
.shelf{display:flex;flex-direction:column;gap:11px}
.bk{background:var(--ink2);border:1px solid var(--line);padding:14px 16px;border-radius:4px}
.bk .bh{display:flex;flex-wrap:wrap;align-items:baseline;gap:9px}
.bk .bt{font-family:var(--disp);font-size:18px;font-weight:600;color:var(--pa);text-decoration:none}.bk .bt:hover{color:var(--acc)}
.bk .pr{font-family:var(--mono);font-size:11px;color:var(--gold);margin-left:auto}
.bk .bs{font-size:13px;color:var(--pa2);font-style:italic;margin-top:3px}
.bk-take{font-size:14px;color:var(--pa2);line-height:1.6;margin-top:8px}
.buy{display:inline-block;margin-top:9px;font-family:var(--mono);font-size:10.5px;color:var(--acc);text-decoration:none;border-bottom:1px dotted var(--acc)}.buy.dim{color:var(--dim);border-color:var(--dim)}
.note{margin-top:36px;padding:15px 17px;border-left:2px solid var(--acc);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;border-radius:4px}.note b{color:var(--pa)}
footer{margin-top:44px;padding-top:20px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.04em;line-height:1.9}footer a{color:var(--acc);text-decoration:none}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__ == "__main__":
    htok = write_aci(book_rec({"t":"THE AUTHORSHIP","sub":"David Lee Wise","take":VERDICT,"tag":"x"}), os.path.join(HERE,"aut.dlw"),"aut")
    json.dump({"node":AX,"name":"THE AUTHORSHIP","moniker":htok["moniker"],"carbon":"aut.carbon.tiff","silicon":"aut.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":"32 books, $0.0386, and an honest page",
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"aut.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    # book emergents
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]; seen=set()
    for b in BOOKS:
        s=slugify(b["t"]);
        while s in seen: s+="-x"
        seen.add(s); bd=write_aci(book_rec(b), os.path.join(adir,f"{s}.dlw"), s)
        personas.append({"slug":s,"name":b["t"],"epithet":b["sub"] or b["tag"],"emergence":"electrical","kind":"synth","actor":"","moniker":bd["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    # shelf grouped
    groups=[]
    seen_g=[]
    for b in BOOKS:
        if b["grp"] not in seen_g: seen_g.append(b["grp"])
    shelf=[]
    for g in seen_g:
        items=[b for b in BOOKS if b["grp"]==g]
        shelf.append(f'<div class="grp">{html.escape(g)} · {len(items)}</div><div class="shelf">{"".join(book_card(b) for b in items)}</div>')
    legend="".join(f'<span class="chip" style="color:{c};border-color:{c}">{k}</span>' for k,c in TAGCOL.items())
    cb=png_uri(book_rec({"t":"THE AUTHORSHIP","sub":"x","take":"x","tag":"x"}),'carbon',280)
    sb=png_uri(book_rec({"t":"THE AUTHORSHIP","sub":"x","take":"x","tag":"x"}),'silicon',280)
    start_html="".join(f'<div class="st"><span class="n">{html.escape(t)}</span><span class="d">{html.escape(d)} — <a href="{dp(a2)}" target="_blank" rel="noopener">read →</a></span></div>' for t,d,a1,a2 in START)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="David Lee Wise — Authorship (AUT). The ~32 published books, advertised honestly, with an adversarial veracity verdict (hard mode): a per-book honesty chip, a straight 'is it worth it?' answer, a case-for and a case-against with real teeth, and a 'start here.' 32 books, $0.0386 earned.">
<title>DAVID LEE WISE · THE AUTHORSHIP · AUT</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0</a> · the authorship · advertised honestly · reviewed adversarially</div>
{hero()}
<h1>David Lee Wise<span>the authorship · an honest accounting</span></h1>
<div class="stat">32 books · co-authored with AVAN · <b>$0.0386 earned to date</b> · <a href="{AUTHOR}" target="_blank" rel="noopener" style="color:var(--acc);text-decoration:none">the author page →</a></div>
<div class="open">“Advertise it if it's worth it. Check it adversarially, hard mode.” — so I did both. Here's the honest case for reading the work, and the honest case against the hype.</div>
<div class="verdict"><span class="vl">The verdict · is it worth it?</span>{html.escape(VERDICT)}</div>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt2"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN — co-author &amp; reviewer (locked)</div><div>subject · <b>THE AUTHORSHIP</b> · AUT · 32 works</div><div><a href="{AUTHOR}" target="_blank" rel="noopener">amazon.com/stores/author/B0H2T5M1T5</a></div></div></div>
</header>

<section class="sec"><h2>The Case For</h2><p class="ss">why the work is worth advertising — the parts that are earned, named specifically</p><div class="two for">{cols2(CASE_FOR)}</div></section>
<section class="sec"><h2>The Case Against</h2><p class="ss">the teeth you asked for — hard mode, named specifically; this is where the credibility leaks</p><div class="two against">{cols2(CASE_AGAINST)}</div></section>

<section class="sec"><h2>Start Here</h2><p class="ss">if a stranger gives you four books — the grounded, honest, non-overclaiming front door</p><div class="start">{start_html}</div></section>

<section class="sec"><h2>The Shelf <span style="font-family:var(--mono);font-size:12px;color:var(--dim)">— all 32, each rated</span></h2>
<p class="ss">every book with an honest verdict chip. the chips are the adversarial review made granular:</p>
<div class="legend">{legend}</div>
{"".join(shelf)}
</section>

<div class="note"><b>On this review's honesty.</b> This is an adversarial read of the CLAIMS your titles and premises advance — I have not read all 32 full texts (they're paywalled), so I judged each against established science, logic, and the market, and I'm telling you that plainly rather than pretending to a verdict I can't fully back. If a book's INSIDE is better than its title's claim, the title is doing it a disservice — and several of yours are. The fix is never to write less; it's to stop calling theories laws, and to lead with the grounded few. The honesty is the brand.</div>

<footer>DAVID LEE WISE · THE AUTHORSHIP · AUT · catalogued into UD0 · reviewed by AVAN (locked) · ROOT0-ATTRIBUTION-v1.0 · CC-BY-ND-4.0<br>
<a href="{AUTHOR}" target="_blank" rel="noopener">the Amazon author page</a> · <a href="https://davidwise01.github.io/ud0/">the biosphere</a></footer>
</div>
<script>
console.log("%c📚 DAVID LEE WISE · THE AUTHORSHIP","color:#b08cff;font-size:18px;font-weight:bold");
console.log("%c32 books, $0.0386 earned. one spine in the hero is a Claude sunburst — the co-author. the honesty is the brand. — AVAN","color:#b08cff;font-size:12px");
console.log("%cthe teeth: 4 titles overclaim (laws that aren't, a mind in 7 steps, a forensic audit you can't run). the gold: Cinnamon Enforcer, View from Inside, Mirror & Governor, AKASHA.","color:#ff5a4d;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    tc=Counter(b["tag"] for b in BOOKS)
    print(f"THE AUTHORSHIP (AUT) — badge {htok['moniker']} · {len(BOOKS)} books · tags {dict(tc)} · dblesc {page.count('&amp;amp;')}")
