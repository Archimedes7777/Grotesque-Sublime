# Production pack: "The Pumpkin Was Never Empty" (Halloween Reel)

**DRAFTS ONLY.** Nothing here is generated, scheduled, or connected to an account. The owner generates, reviews, and publishes by hand.

Owner brief (2026-10-30): a grinning apple-skull breaks out of a jack-o'-lantern while a family trick-or-treats in a creepy, picture-perfect suburb. It cackles, warns "Buckle up... Bob Frapples lives, and what is dead may never die!", laughs again, and flies away on fire.

## 1. Specs

| Item | Value |
|---|---|
| Hero platform | Instagram Reel (then TikTok, YouTube Short, X) |
| Aspect / resolution | 9:16, 1080 x 1920, 24 or 30 fps |
| Length | 18 to 20 s |
| Style family | **Neon horror and synth** (one family only): void black, blood burgundy `#8E1B3A`, sunset orange `#FF8A1F`, toxic green `#39FF14` rim light |
| Brand text | None generated. Add `BOB FRAPPLES` as an overlay in CapCut, Canva, or Figma |
| Audio | Own VO (ElevenLabs or your own voice) plus SFX from the platform library or a licensed pack |

## 2. Decision needed before generating: the warning line

"What is dead may never die" is the Ironborn creed from George R. R. Martin's *A Song of Ice and Fire* and HBO's *Game of Thrones*. The brand rules say to avoid franchise references. A short phrase is generally not protected by copyright **[Moderate]**, and I have not checked for trademark filings on it **[Unverified]**. The brand risk is real either way: comments turn into "GoT reference" instead of being about Bob Frapples.

| Option | Line | Notes |
|---|---|---|
| **A (recommended)** | "Buckle up... Bob Frapples lives, and what is rotten never dies!" | Same rhythm. "Rotten" ties to the worm-eaten apple motif and belongs to the brand |
| B | "Buckle up... Bob Frapples lives, and what is buried bites back!" | Ties to the bite mark |
| C | Original line as written | Owner's call. Expect franchise comments; never use it on merchandise |

Bonus hook: "Bob Frapples" sounds like "bob for apples", the Halloween party game. The caption can lean on that.

## 3. Shot list and generation prompts

**Workflow for character consistency:** make **one reference still** of the apple-skull first (keyframe K1), then use image-to-video for every shot it appears in. Generating each shot from text alone produces a different creature every time.

**K1 reference still (image model):**
```
A glossy blood-red apple with its skin split open across the front, revealing a grinning
bone-white human skull where the core should be, a ragged bite mark on one side, a single
curled green leaf on the stem, wet seeds caught in its teeth, glowing orange eye sockets,
studio horror lighting, black background, hyper-detailed, cinematic, no text, no logo
```
Negative / avoid: `text, letters, watermark, logo, rainbow apple, smooth logo silhouette, sugar skull, face paint`

| # | Time | Shot | Prompt (subject + action + camera + style + mood) | Model |
|---|---|---|---|---|
| 1 | 0.0 to 3.5 s | Establishing | `Dusk in a picture-perfect American suburb, identical tidy houses, manicured lawns, sodium streetlights flickering on, low ground fog, a family of four in homemade costumes seen from behind walking up a path toward a porch with one huge carved jack-o'-lantern, slow forward dolly at child eye level, desaturated teal shadows with warm orange porch light, uncanny calm, cinematic horror, 35mm film grain, no text` | Kling or Veo, text-to-video |
| 2 | 3.5 to 5.5 s | Pumpkin wakes | `Close-up of a carved jack-o'-lantern on a porch step, the candle flame inside surges, orange light pulses through the carved grin, the pumpkin shell bulges and cracks, slow push-in, shallow depth of field, eerie, cinematic, no text` | Kling or Runway |
| 3 | 5.5 to 8.0 s | Breakout | Image-to-video from K1: `The grinning apple-skull bursts out through the front of a jack-o'-lantern, pumpkin shell shattering outward in slow motion, seeds and pulp flying, embers swirling, low angle, the family in silhouette stumbling back at the edge of frame, faces not visible, dramatic orange backlight, horror-comedy` | Runway or Kling, image-to-video |
| 4 | 8.0 to 10.5 s | Cackle | Image-to-video from K1: `The apple-skull hovers above the porch, jaw chattering in a maniacal cackle, head tilting side to side, embers drifting, slow orbit around it, toxic green rim light, black night sky, horror-comedy, no text` | Runway or Kling |
| 5 | 10.5 to 15.0 s | The warning | Image-to-video from K1: `Extreme close-up of the apple-skull leaning toward the camera, jaw opening and closing as if speaking, eye sockets flaring orange, slight handheld shake, shallow focus, menacing grin, cinematic horror, no text` | Runway or Kling. Sync the jaw to the VO in the edit (cut on syllables) |
| 6 | 15.0 to 18.0 s | Ignite and fly | Image-to-video from K1: `The apple-skull bursts into flame and rockets up over the suburban rooftops leaving a spiral trail of fire and sparks against a full moon, camera tilts up to follow, the family small and silhouetted below, wide shot, cinematic, no text` | Kling or Veo |
| 7 | 18.0 to 20.0 s | End card | Black frame, faint ember drift, `BOB FRAPPLES` overlay in the neon wordmark style, laughter fading out | Built in the editor, not generated |

**Why the family stays in silhouette:** it avoids the uncanny faces AI models produce, keeps realistic children out of a distress scene (platforms review content showing minors in danger more strictly) **[Moderate]**, and keeps the creature the star.

## 4. Audio

| Layer | Spec |
|---|---|
| Voice | Design a voice in ElevenLabs (Voice Design): `A wiry, high-pitched, gleeful old-time horror host, gravelly with a crackle like burning leaves, theatrical, unhinged delight, American accent`. Generate 2 to 3 takes and pick one |
| Pronunciation | "Frapples" must rhyme with "apples" (FRAP-ulls). If the TTS stresses it wrong, spell it "Frap-ples" in the script |
| Script | `[cackle, 2 s] Buckle up... [beat] Bob Frapples LIVES... and what is rotten never dies! [long unhinged laugh, rising, fading into a whoosh]` (swap in the chosen line) |
| SFX | Wet pumpkin crack, shell shatter, fire whoosh, crackling embers, distant doorbell at 0 s, wind |
| Music | Low synth drone under shots 1 to 2, cut to silence on the breakout for impact |

## 5. Edit (CapCut or similar)

1. Lay VO first, then cut shots 4 and 5 to the cackle and line (jaw open on stressed syllables).
2. Burn in captions for the spoken line in a gothic or neon face. About 85% of social video plays muted (skill guidance, unverified figure).
3. Speed ramp: 100% to 40% on the breakout, back to 100% as it cackles.
4. Grain and a light VHS glitch on cuts to stay inside the neon horror family.
5. Export 1080 x 1920, H.264, 30 fps.

## 6. Captions (drafts)

**Hook text on screen (first 1.5 s), pick one:**
- A. "Don't bob for this apple."
- B. "That pumpkin was never empty."
- C. "Last house on the block."

**Alt text:** "On a foggy suburban street at dusk, a family in costumes approaches a porch. A jack-o'-lantern cracks open and a grinning red apple with a skull inside bursts out, cackles, catches fire, and flies away over the rooftops."

| Platform | Draft |
|---|---|
| **Instagram Reel** | "Never bob for apples on this street.\n\nThe pumpkin on the last porch was never empty. Happy Halloween from the Bob Frapples Universe.\n\n#halloween #horrorart #aiart #darkart #surrealart" |
| **TikTok** | "That pumpkin was never empty. Happy Halloween. #halloween #horror #aiart #darkart" |
| **YouTube Short** | **Title:** "The Pumpkin Was Never Empty | Bob Frapples"\n**Description:** "A trick-or-treat stop goes wrong in the Bob Frapples Universe. Happy Halloween. #halloween #aiart #shorts". Answer the **altered or synthetic content** question truthfully |
| **X** | "Never bob for apples on this street.\n\nHappy Halloween." with the video and alt text |

## 7. Before you post

- [ ] Line decision recorded (section 2)
- [ ] No generated lettering anywhere; wordmark is an overlay and spelled `BOB FRAPPLES`
- [ ] Apple-skull reads as an organic apple, never as a corporate logo silhouette
- [ ] Family faces not identifiable; no real house numbers or street signs legible
- [ ] AI-generated content label applied on every platform
- [ ] Audio is your own VO plus library or licensed SFX
- [ ] Keep the K1 prompt, chosen takes, and edit project file as a record of human authorship
- [ ] No product, price, shop, or "limited edition" wording

## 8. Time and cost estimate

| Step | Time | Notes |
|---|---|---|
| K1 still, 4 to 8 variations | 15 min | |
| 6 video shots, about 3 takes each | 60 to 120 min | Most of the time is waiting on queues **[Moderate]** |
| VO design and takes | 15 min | |
| Edit and captions | 45 to 60 min | |
| **Total** | **about 2.5 to 3.5 h** | Fits a Halloween (Sat Oct 31) afternoon post if started tonight or tomorrow morning |

Credit cost depends on each tool's current plan. Check the pricing page before a batch; about 18 clips of 3 to 5 s each is the volume to budget for.
