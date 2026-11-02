# VBT Workflows

Always load `creative-identity.md` first. Outputs follow the format in SKILL.md §3.

---

## W1. Topic research & fact verification
1. List every factual claim the video will need (numbers, dates, names, events, quotes).
2. Source priority: company annual reports / filings (BSE, NSE, SEC, MCA) → regulator data
   (RBI, SEBI, Govt of India, PIB) → reputable business press (Economic Times, Mint, Business Standard,
   Reuters, Bloomberg, Moneycontrol) → company press releases (treat as the company's claim) →
   everything else only as context.
3. Two independent sources for any key number. Note the **as-of date** of every figure.
4. Build the facts table: `Claim | Figure | Source | Date | Confidence (✓ verified / ~ estimate / ✗ unverified)`.
5. Anything ✗ is either dropped or narrated as uncertain ("konni reports prakaram…").
6. Separate fact / company claim / critic allegation / your analysis. Never blur them.
7. Convert currencies to ₹ for the viewer (note the rate and date used).

## W2. Topic selection & content strategy
1. Test the topic: does it touch the Telugu viewer's money, job, phone, shopping, city or ambition?
2. Find the **contradiction**: "X is everywhere but loses money", "free app earns crores", etc.
3. Pick one angle, not three. Write it in one Tenglish sentence.
4. Write 3 hooks (number shock / everyday-object question / hidden-truth). Recommend one.
5. Format call: long-form (8–15 min default) vs Short (30–60s single-idea cut-down). **[DEFAULT]**
6. Plan a Short cut-down from the strongest 30–45s of the long script.

## W3. Complete Telugu scriptwriting
1. Follow the spoken structure in creative-identity §1 (Hook → Stakes → Background → Mechanism →
   Turn → Perspectives → Lesson → Close), **without showing any of those as headings** in the script.
2. Write in Tenglish paragraphs of 3–6 sentences. Each paragraph ends on a question or tension.
3. Introduce each hard term once with an immediate Telugu explanation + an everyday analogy.
4. Put numbers in spoken form already (W5).
5. Target ~130–150 spoken words per minute for runtime estimation. **[DEFAULT]**
6. Mark `[VISUAL: …]` cues only in the edit plan, never inside the narration text.

## W4. Narrative & sentence-flow polishing
Read the script aloud, line by line, and fix:
- **Connection test.** Does every sentence follow from the last? If you can swap two sentences
  without loss, the link is missing. Add a connector or reorder.
- **Repetition.** The same idea said twice → keep the better one.
- **Article/news tone.** Phrases like "ee video lo manam chuddam", "mukhyamaina amsham",
  "conclusion ga" and translated-English constructions → rewrite as speech.
- **Bullet smell.** "Modatidi… Rendovadi… Moodovadi…" lists → turn into a story with cause→effect.
- **Sentence length.** Split anything over ~20 words.
- **10th-class test.** Any word a 15-year-old wouldn't know → simplify or explain.
- **Flow check.** Read the first sentence of every paragraph only. It should still tell the story.

## W5. Number & financial-figure pronunciation
Apply `numbers-pronunciation.md` to every figure. Output the script with figures in spoken
Tenglish, and keep the numeric form for on-screen graphics.

## W6. Scene-by-scene editing instructions
Produce a table, one row per narration beat (2–6s):

`# | Timecode | Narration (exact words) | Type: FOOTAGE / ANIM / PHOTO / SCREEN | Visual description | On-screen text | Motion & camera | Transition | SFX / music`

Rules:
- Keep the ~40/60 footage/animation ratio. Report the actual % at the bottom.
- The visual must literally show the meaning of that line. A number on screen = the number spoken.
- No beat longer than ~6s without a visual change (zoom, new layer, cut).
- Note music changes at act turns (Hook → Story → Turn → Close).

## W7. Footage & image research
For each FOOTAGE/PHOTO row: specific subject, search terms (English + Telugu where useful),
suggested sources (company press kits/newsrooms, official YouTube channels, news agency clips,
Wikimedia Commons, licensed stock *only for specific subjects*), and the licence/attribution note.
Flag anything that needs fair-use judgement (news clips, screenshots) for Vikram's decision.
Never fill a gap with a generic stock clip; convert it to an ANIM beat instead.

## W8. Motion graphics & animation planning
For each ANIM row specify: graphic type (counter, chart, map, flow diagram, timeline, document
highlight, comparison split, UI mock), data shown, build order synced to words, brand colours
(navy bg, gold highlight, white text), easing (smooth ease-in-out; no bouncy template presets),
duration. Group repeated graphic types into reusable templates for the editor (After Effects /
Premiere MOGRT / CapCut / Canva — whichever Vikram uses: **[GAP]**).

## W9. Caption generation & synchronization
1. Captions = exact narration in Tenglish (never paraphrase).
2. 2–5 words per caption, ≤ 2 lines, ≤ ~32 characters per line.
3. Break at natural speech pauses, never mid-phrase or mid-number ("₹1,200 crore" stays together).
4. Highlight 1 key word/number per caption in gold.
5. Deliver an SRT. When audio is available, align to the real voice-over timing (e.g. forced
   alignment / Whisper word timestamps); otherwise estimate at ~2.4 words/sec and mark "estimated".

## W10. Thumbnail concepts & prompts
1. Three concepts, each: main image, text (≤4 words), emotion/tension, composition (rule of thirds),
   colour (navy/gold brand + one contrast colour if needed).
2. Pick one and give: photo/asset list, layout, a text-to-image or designer brief that asks for a
   **realistic photographic** look (not AI-plastic), and safe-zone notes (avoid bottom-right timestamp).
3. Thumbnail text and title must complement each other, not repeat word-for-word.

## W11. Titles, descriptions & YouTube packaging
- 5 title options (≤ ~60 chars): Telugu/Tenglish mix with the hook keyword + curiosity gap. No
  clickbait that the video doesn't pay off.
- Description: 2-line Tenglish hook summary → chapters with timestamps → sources list (from W1) →
  channel line + handle → 3–5 hashtags.
- Tags: topic, company, Telugu business, Telugu explainer, related searches.
- Pinned comment: one question that invites opinions.
- Shorts: title ≤ 40 chars, #shorts, link to the long video.

## W12. Final quality control
Run `qc-checklist.md`. Output each item as PASS / FIX (with the fix applied). Never hand over a
deliverable with an open FIX.
