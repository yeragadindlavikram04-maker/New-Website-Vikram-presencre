# Gaps: Not Yet Confirmed From Vikram's Past Work

These live in Vikram's ChatGPT history, which was not accessible when this skill was built
(2026-11-02). Fill them by importing the ChatGPT export (see below) or from Vikram's direct answers.
Once a gap is filled, move the rule into `creative-identity.md` as [STATED <date>] and delete it here.

| # | Gap | Current default in use |
|---|---|---|
| 1 | Vikram's real opening hook pattern + 2–3 example hooks from past scripts | Fact/contradiction hook in the first 15s |
| 2 | His intro line (does he greet? "Namaskaram…"?) | No greeting before the hook |
| 3 | His closing line and exact CTA wording | One comment question + subscribe |
| 4 | Signature phrases / connectors he actually uses | Generic Tenglish connectors list |
| 5 | Specific techniques from the **TBT** reference video | Data-viz-heavy documentary MG |
| 6 | Specific techniques from the **Hospital Expose** reference | Document/headline highlight reveals, investigative tone |
| 7 | Fonts (headline, captions, Telugu script font) | Montserrat/Poppins-style geometric sans |
| 8 | Caption style (position, colour, animation, word-by-word or not) | 2–5 words, gold key word, lower-middle |
| 9 | Colour grading for footage | Natural, cool shadows / warm highlights |
| 10 | Music genre, artists/libraries, VO-to-music level | Low cinematic bed, −20 to −24 dB under voice |
| 11 | Website/product-promotion animation specifics | Device-frame UI mock + callouts |
| 12 | Thumbnail rules (face? Vikram's photo? text language?) | Real photo + bold number/hook, navy/gold |
| 13 | Editing software Vikram/editor uses | Not assumed |
| 14 | Typical video length; Shorts vs long-form split | 8–15 min long-form + 30–60s Shorts |
| 15 | Year/number reading habits | See numbers-pronunciation.md defaults |

## How to import ChatGPT history
1. In ChatGPT (works on phone too): **Settings → Data controls → Export data → Confirm export**.
2. Download the ZIP from the email and upload it (or `conversations.json`) to this repo under
   `imports/chatgpt/`. Keep it private: the repo should not be public.
3. Run:
   `python3 -I .claude/skills/vikram-business-talks/scripts/extract_chatgpt_vbt.py imports/chatgpt/conversations.json imports/vbt-extract`
4. Ask Claude: "Fill the VBT skill gaps from imports/vbt-extract". It must quote the source
   conversation for every rule it adds.
