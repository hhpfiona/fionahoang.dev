# all the words on the site live here so copy edits never touch layout code
# build.py imports everything from this file

# links used in the hero pills sidebar and contact card
EMAIL = "hhpfiona@gmail.com"
GITHUB = "https://github.com/hhpfiona"
LINKEDIN = "https://www.linkedin.com/in/fiona-hoang"
ACL = "https://aclanthology.org/people/phuong-hanh-hoang/"

# background section one string per paragraph
ABOUT = [
    "Most recently, I spent a year as a software engineer co-op at Huawei Canada's Noah's Ark Lab, on the Mobile AI Infrastructure team, where I self-hosted vision-language models on GPU clusters and built the framework that let them test apps on real phones. Before and alongside that, I spent two years as a research engineer at the University of Toronto's Lee Language Lab, where I worked on URIEL+, a database of how the world's languages relate to one another, and co-authored five papers along the way.",
    "I graduated from the University of Toronto in 2026 with an Honours Bachelor of Science, with High Distinction, in Computer Science and Psychology.",
    "Healthcare has always been close to home for me, since both my mom and brother work in the industry, and mental health in particular is something I care about deeply. That's what first drew me to psychology. A few cognitive science courses in, I started drawing connections between how psychology thinks about “cognition” and “data”, and how computer science does. A few more courses after that, I found myself in computer science. Half of software engineering is arguing about which box something belongs in, so it's turned out more useful than I expected!",
]

# experience entries in the order the page shows them
EXPERIENCE = [
    dict(title="Research Engineer", org="Lee Language Lab, University of Toronto",
         team="with Prof. En-Shiun Annie Lee", dates="2024 – Aug 2026", years="2024–26",
         desc="Extended the URIEL+ typological knowledge base and co-authored four papers built on it, plus a SIGCSE paper on gender disparity in STEM education. Reviewed code for the URIEL+ papers.",
         tags=["Knowledge bases", "Research engineering", "Code review", "5 papers"]),
    dict(title="Software Engineer Co-op", org="Huawei Canada, Noah's Ark Lab",
         team="Mobile AI Infrastructure", dates="May 2025 – May 2026", years="2025–26",
         desc="Self-hosted model inference on NVIDIA GPUs, including serving Qwen2-VL locally instead of through an API. Worked on a device framework that handles device failures, timeouts and retries, with automated tests, and reviewed teammates' code.",
         tags=["Model serving", "NVIDIA GPUs", "Fault tolerance", "Automated testing"]),
]

# papers newest first note is for workshop tracks and stays empty otherwise
PAPERS = [
    dict(venue="EACL 2026", note="Student Research Workshop", url="https://aclanthology.org/2026.eacl-srw.8/",
         title="Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"),
    dict(venue="LREC 2026", note="", url="https://aclanthology.org/2026.lrec-1.863/",
         title="Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"),
    dict(venue="EMNLP 2025", note="", url="https://aclanthology.org/2025.emnlp-main.1310/",
         title="Less is More: The Effectiveness of Compact Typological Language Representations"),
    dict(venue="COLING 2025", note="", url="https://aclanthology.org/2025.coling-main.463/",
         title="URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base"),
    dict(venue="SIGCSE Virtual 2024", note="", url="https://doi.org/10.1145/3649165.3690102",
         title="A Faculty Initiative Addressing Gender Disparity at a Small STEM-Focused University: A Case Study"),
]

PROJECT = dict(name="PluralTree", url="https://github.com/hhpfiona/PluralTree", meta="LLM systems research, University of Toronto, 2026",
               desc="A research pipeline for improving how culturally accurate a language model's answers are, built in the University of Toronto's LLM systems research course. I've since handed it off, and someone else is carrying it forward.")

# code sets the lang attribute so screen readers pronounce each greeting properly
LANGS = [
    dict(code="en", word="Hello", name="English", level="Fluent", pct=100),
    dict(code="vi", word="Xin chào", name="Vietnamese", level="Fluent, mother tongue", pct=100),
    dict(code="fr", word="Bonjour", name="French", level="Advanced", pct=75),
    dict(code="es", word="Hola", name="Spanish", level="Learning", pct=30),
    dict(code="zh", word="你好", name="Mandarin", level="Learning", pct=25),
]

LANG_COPY = [
    "When I was younger, I promised myself I'd be fluent in ten languages by the time I turned thirty. Polyglots seemed like the coolest people alive, and I fully intended to become one.",
    "So far, I'm at five. Two of those are fluent, although I'll admit that's cheating a little: Vietnamese is my mother tongue, so I should be good at it regardless, and English was never really optional for someone living in Canada. French is getting there, slowly but stubbornly (<span lang="fr">j'en suis à une série de 200 jours sur Duolingo</span>), while Spanish and Mandarin are still very much works in progress.",
    "Somewhere along the way, I also picked up Python, and then a handful of other programming languages after it. I'm counting them toward the ten. Nobody has told me they don't count!",
    "That childhood goal is also how my research ended up in multilingual NLP. I care about the languages technology tends to leave behind, from endangered languages to dead ones, although the dead ones do have one advantage: they never complain about the output.",
]

CONTACT = "I'm looking for entry-level software roles, whether that's backend, infrastructure, ML or research engineering, in Toronto, remote in Canada, or further afield. If anything here caught your eye, I'd love to hear from you."

# page head with fonts and css slotted in by build.py
# braces in the css would break str.format so css goes in as one value
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fiona Hoang</title>
<meta name="description" content="Fiona Hoang, software engineer. AI infrastructure at Huawei Canada, research engineering at the University of Toronto. Computer Science and Psychology.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<style>
{css}
</style>
</head>
"""


# wraps each string in a p tag so content lists stay plain text
def paras(ps, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "\n".join(f"<p{c}>{p}</p>" for p in ps)
