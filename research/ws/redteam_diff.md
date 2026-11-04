# Red team, second pass: review of the v1 to v2 diff

Reviewer persona: skeptical macro economist and former bank regulator (Red Team A on v1). Date: 2026-11-04.
Scope: `ws/phase6_diff.md`, `changelog.md`, and `plays.csv` (number checks only). Arithmetic was recomputed from `plays.csv`.

## What checks out

- The central-estimate formula is applied correctly: every priced row in `plays.csv` matches midpoint minus σ²/2 with σ = (high - low) / 2.563, to within 0.02 points.
- Option A: weight x stress = 24.975%, which rounds to 25.0%. The weighted central return is 5.695%, which rounds to 5.70%. Both are correct.
- Option B stress: 25.0 + 2.5% x (83 + 92 + 77 + 85) = 33.4%. Correct.
- Option A after-tax: 0.60 x 3.19 + 0.40 x 6.06 = 4.34%. The arithmetic is correct. The real-return figures (+0.6 and -0.5) follow from it.
- Panel ranges match the min and max of the five estimators. The 2030 Bear mean (50.8, shown as 51) and the 2035 means are correct.
- Exec summary cells were checked against `plays.csv` excess and stress columns: V/MA, BK, BLK, CRCL, M-08, M-02, M-01, M-04, M-07, L-02 and L-03 all match. The 75-row tier counts (51/13/11) match.
- CRCL's 74% drawdown, Circle's 62% cost ratio and the ±$739M rate sensitivity are arithmetically correct.
- The September CPI of 3.7% is consistent with secondary reports of the 2026-10-14 BLS release.

## Findings

1. **High. Target: Section 6 Method v2 (changelog C1); all rankings; Option A vs B.**
   Problem: The bands are read as the 10th to 90th percentile of annual returns. For incumbents this cannot be right. V's band of 7 to 10 implies σ = 1.2% a year, so the compounding drag is 0.007 points. That sits next to a stress drawdown of 50% for the same stock. MA, BK, BLK, ICE and STT have the same problem. Their bands are 10-year CAGR point spreads, not distributions of annual returns.
   Crypto bands are one-year ranges, so they take the full drag (IBIT loses 14.9 points). The method therefore removes almost nothing from incumbents and a lot from crypto. The report's own caveat ("bands mix one-year and multi-year framings") names the problem but does not correct it. The +4.3 to +4.8 point excess for V/MA and Option A's 5.70% are overstated relative to their risk.
   Fix: For each row, state the horizon of its band. For 10-year CAGR bands, widen the band to a defensible 10-90 range of 10-year CAGR, about ±6 points for large-cap financials, or apply a drag based on realized annual volatility (about 20% to 30% for these names, which gives 2 to 4.5 points of drag on annual returns). Then re-rank and recompute Option A and B.
   If that is not done before finalizing, add to Section 6 and personalized_plays.md: "Incumbent central estimates carry almost no volatility drag because their bands are 10-year point spreads. They are not comparable with the one-year crypto bands."

2. **High. Target: R-01, R-02, R-03 centrals; exec summary Retail rank 4 (CRCL); Option B.**
   Problem: For CRCL, COIN and HOOD, the band endpoints are explicitly the WS5 bear, base and bull scenario outcomes (`return_method_detail`). Reading them as 10th and 90th percentiles assigns Bear about a 10% probability. The report's own panel puts 2030 Bear at 51%.
   Weighted with the panel's 51/42/7, the centrals are CRCL 2.3% (not 7.49%), COIN -2.1% (not 1.16%) and HOOD -3.1% (not 0.23%). CRCL's +3.3 points and its rank-4 place therefore contradict the headline probabilities. Retiring scenario weighting fixed a category error for one-year stress bands. It does not apply to bands that are themselves scenario outcomes.
   Fix: For rows whose bands are scenario endpoints, set central = panel-weighted scenario value (CRCL 2.28, excess -1.93). Remove CRCL from the Retail top five, or mark it (J) with that number shown. Recompute Option B's central (it falls by about 0.13 points for CRCL alone).

3. **High. Target: Section 4C variant "T including represented assets: 50%"; changelog C8.**
   Problem: Section 4B defines 2030 Bear as S < $500B **and** T < $100B. It also says represented T is already $435B. Under that definition, Bear in the represented variant requires T to fall 77% by 2030, so its probability should be near zero, not 50%. Either the variant silently used different thresholds, or the reported figure is wrong.
   Fix: State the thresholds used in the represented variant. If they are unchanged, rerun it and report the near-zero Bear result. Then say plainly that the Bear label depends on the choice of T measure.

4. **High. Target: Exec summary, "Is it happening?"**
   Problem: v2 changes the answer from "Partly" to "Yes, on regulated and permissioned rails." The next bullet says no segment passes the rejection test. The "Yes" rests on Broadridge's self-reported DLR volume ([Interested source], [Low]) and RWA.xyz represented value. Section 1 itself says represented value is "records on a ledger, not settlement in central bank money." The change is not in the changelog.
   Fix: Replace it with: "Partly. Closest on permissioned wholesale rails, on self-reported operator volumes. Barely on public-chain tokenization. Not yet in payments or retail CBDCs. No segment yet passes the rejection test." Log the wording change.

5. **High. Target: new v2 facts (Sections 1, 2, 3, 4A, 5).**
   Problem: v2 adds load-bearing facts that never went through Phase 4 verification. Several are sourced to the red-team text itself:
   - CRS IN12722 Fed payment accounts ("per Red Team A")
   - DTCC live trades on Canton and Besu on 2026-07-15 ("per Red Team B")
   - DTC giving no collateral value to tokenized positions (Red Team B)
   - the BIS WP 1270 revision magnitudes
   - Open USD coalition (2026-06-30); Rosa and Roubini (2026-05-21)
   - Tron revenue and the 60% fee cut
   - the 2026-09-16 hike with two dissents
   - $396B represented and $39.4B distributed
   Reviewer assertions are not sources, yet several carry [Moderate].
   Fix: Run a verification pass (the verification.md format) on these rows before finalizing. Until then, tag each one [Unverified] or [Low] and cite the primary source.

6. **High. Target: Exec summary, Large rank 4 "Digital Asset (Canton) ... repriced from the 2026 round (M-06, L-04 revised) (J)."**
   Problem: The matrix contradicts it. M-06 says "No verified 2026 valuations in session." L-04 says "No verified Canton or Digital Asset round in session" and still has a -100 to 30 band (central -47.9%, excess -52.1). No changelog entry revises L-04. The top-five entry rests on a round the matrix says does not exist, and Section 5 now flags Canton's single-application concentration.
   Fix: Either cite the round, re-score L-04 in `plays.csv` and log the change, or replace the entry with L-09 (rank 3 by score, excess -2.19) or with "unscored (J) [Unverified]."

7. **Medium. Target: Exec summary and Section 4C panel mean 2030; personalized_plays.md "Bull tail (7% in 2030)".**
   Problem: The 2030 means are 50.8 / 41.4 / 7.6. Standard or largest-remainder rounding gives 51 / 41 / 8, not 51 / 42 / 7. The Bull probability is rounded down.
   Fix: Use 51 / 41 / 8 in the exec summary, Section 4C and changelog C3, and "8% in 2030" in personalized_plays.md. 2035 (46 / 43 / 11) is acceptable.

8. **Medium. Target: Section 4C panel design (changelog C3, A6).**
   Problem: The model enters twice (base and drivers-only). The two red teams' numbers were critique positions, one of them from an advocate persona, not forecasts. Without the red teams, the panel gives 2030 Bear 56%, so the move from 57% to 51% comes almost entirely from adding the reviewers, not from new evidence. The report does not say this.
   Fix: Add one line: "Excluding the red-team estimates, 2030 Bear is 56%. Counting the model once, it is 49%. The headline shift reflects reviewer judgment, not new data."

9. **Medium. Target: Exec summary Retail top five (changelog C2).**
   Problem: By excess return, the order is V/MA (4.76, 4.28), BK 3.76, staked ETH R-22 3.31, CRCL 3.28, BLK 3.27. The table omits R-22 and puts BLK above CRCL, with no (J) on either. That breaks the C2 rule that overrides are marked.
   Fix: Mark rank 3 (BLK) and rank 4 (CRCL) (J). Add: "R-22 staked ETH (+3.3 pts, stress 85%) omitted (J): ordinary-income staking rewards, liquidity mismatch (B14)."

10. **Medium. Target: Exec summary inference "Every crypto-native public equity except Circle scores below T-bills."**
    Problem: SECZ (R-08) has a central of 5.61% and an excess of +1.40, so the statement is false.
    Fix: Change it to "except Circle and Securitize (SECZ, +1.4 pts, de-SPAC with thin float)."

11. **Medium. Target: Section 7 sizing rule.**
    Problem: "A 40% loss limit leaves room for only about 40% in equities" is wrong arithmetic. At 50% to 80% stress, the limit allows 50% to 80% in equities (40/0.8 to 40/0.5). Option B also holds 50% in equities and options at 33.4% stress, which contradicts the sentence.
    Fix: "With incumbents at 50% to 80% stress and the rest in cash, a 40% limit allows 50% to 80% in equities. The allocation targets 40% (Option A) to 50% (Option B) to keep a buffer of 7 to 15 points. Crypto options come out of that budget."

12. **Medium. Target: Option B COIN line; changelog A18/A19 disposition "Partly adopted".**
    Problem: COIN has two rows. R-02 has a central of 1.16%; A-04 has -6.78%. Option B uses the favorable one. V is the reverse: R-09 is used at 8.49% instead of A-01 at 8.97%. The disposition should have been adopted: one central per ticker for allocation. Using A-04 for COIN, Option B's central is 5.21%.
    Fix: Use one row per ticker in allocations, either the lower central or a documented blend, and state which. Change A18/A19 to "Adopted for allocations."

13. **Medium. Target: Section 7 risk row, Section 5 fee-pool bullet, personalized V/MA kill criterion, changelog C12.**
    Problem: The Credit Card Competition Act (S. 3623 / H.R. 7035) is a network-routing mandate for credit cards. Unlike Durbin's debit rule, it does not cap interchange. "Interchange caps enacted (Credit Card Competition Act style)" mislabels the mechanism.
    Fix: Use "Credit card routing mandate (Credit Card Competition Act) or a direct interchange cap enacted." Section 13 also says the risk was added to "V/MA kill criteria," but the `plays.csv` kill criteria for R-09, R-10, A-01 and A-02 are unchanged. Update them, or reword Section 13 to say "personalized_plays.md kill criteria."

14. **Medium. Target: Exec summary Recommendation and Section 11 vs personalized_plays.md.**
    Problem: The exec summary and Section 11 say to keep issuer, distributor and token exposure "as small, capped options." The recommended personal allocation (Option A) holds none, and personalized_plays.md says Option B lowers the central return and raises stress.
    Fix: Add to the exec summary: "For the Section 0 investor, the recommended core holds no options. Options enter only through Option B or reserve trigger (b)."

15. **Medium. Target: Exec summary "real yield of about 0.5%"; personalized after-tax and real table.**
    Problem: There are three separate issues.
    - The exec summary's +0.5% real T-bill yield is pre-tax. personalized_plays.md shows -0.5% after tax for the same California investor, so the report gives opposite signs without labels.
    - The real comparison deflates a 10-year expected return by trailing headline CPI, which is energy-driven per the BLS reports. A 10-year expected inflation measure should be used.
    - The 4.21% 3-month bill is treated as a 10-year return, which ignores the roll and rate path.
    Fix:
    - Label the exec summary figure "pre-tax, ex post."
    - In personalized_plays.md, deflate by the 10-year breakeven (FRED T10YIE, dated) and state that the T-bill leg assumes today's bill rate persists.
    - Add the 10-year Treasury yield as a second benchmark for the 10-year horizon.

16. **Medium. Target: changelog A23 "Not adopted"; Section 7 theft row (80%).**
    Problem: Incidents above $500M include Poly Network (2021), Ronin (2022), Bybit (2025) and Binance (2026-10-29), which the report itself cites. That is about 0.67 a year. A Poisson rate gives P(at least one in 5 years) of about 95%. "Same two incidents" is not a reason to keep 80%.
    Fix: Adopt. Set the 5-year probability to 90% to 95% and cite the incident base rate.

17. **Medium. Target: changelog A11 "Added to the watch list."**
    Problem: The diff of Section 12 contains no Treasury clearing mandate entry, so the changelog misstates what was done.
    Fix: Add catalyst rows for the SEC Treasury clearing mandate compliance dates: cash 2026-12-31 and repo 2027-06-30 (verify the current dates). Watch for demand for tokenized collateral and DLR repo volume.

18. **Medium. Target: M-08 (Mid rank 1, (J)).**
    Problem: The central of 7.49% is gross yield minus fees, with no expected credit loss. It is now promoted to rank 1 by judgment. Yield is not expected return for private credit.
    Fix: Subtract an expected loss of about 1 to 2 points a year (state the default and loss-given-default assumption). Show the excess as roughly +1.3 to +2.3 pts, and keep the (J) with that number.

19. **Medium. Target: personalized_plays.md rebalancing rule R3.**
    Problem: "Exceeds 50%, trim to 40% (A) or 50% (B)" lets Option A drift 10 points above target before acting. For Option B the trigger equals the target, so it fires on any drift and the trim does nothing.
    Fix: "R3: equity plus option weight exceeds target by 5 points (45% for A, 55% for B). Trim to target."

20. **Low. Target: plays.csv R-36 and R-02 vs changelog C7.**
    Problem: R-36 is still framed on cuts only ("each 100bp cut"; kill "Two cuts priced"). The v2 regime is a hike priced, with symmetric sensitivity. R-36 also uses $316M after costs (RLDC 42.7%), while Section 4A uses $276M.
    Fix: Make R-36 symmetric, pick one after-cost figure, and state its basis.

21. **Low. Target: Option B central (changelog C6, personalized_plays.md).**
    Problem: The recomputed value is 5.4045%, which rounds to 5.40%, not 5.41%.
    Fix: Show 5.40% (or 5.2% if finding 12 is adopted, lower still with finding 2).

22. **Low. Target: personalized_plays.md T-bill central 4.20% vs the benchmark 4.21% everywhere else.**
    Fix: Use 4.21% or footnote that the R-27 midpoint is 4.20%.

23. **Low. Target: Section 4A "Markets lean toward a hike" vs Section 12 "A hike (priced)" and changelog C7 "December hike priced."**
    Problem: The inference compares a bond-equivalent CMT (4.21%) with EFFR. On a discount basis (4.03%) the spread is 15 bp. The degree of pricing is asserted without a futures source.
    Fix: Cite fed funds futures or OIS pricing for 2026-12-09, or use "leans toward" consistently.

24. **Low. Target: Section 6 "Each row has a band, a central estimate..."**
    Problem: Twelve rows have no band or central (R-32, R-33, M-06, M-12, L-05 to L-08, L-10, A-05 to A-07).
    Fix: "Each priced row (63 of 75) has..."

25. **Low. Target: unlogged edits.**
    Problem: These changes are not in the changelog:
    - driver sensitivity changed from 3.6 to 3.7 points
    - MiCA row dropped from Section 3
    - Tether's $1.3B to $1.8B rate sensitivity and the "issuer equity is a rate bet" inference dropped
    - prior-cycle drawdown facts (BTC -77% to -86%, COIN -92%) dropped from Section 7 and the personal risk flags, though Option B holds these assets
    - "The binding constraints are demand and macro, not law" is labeled Fact but is an inference
    Fix: Log each change, restore the drawdown history in the Option B risk flags, and relabel the Fact as an Inference.

26. **Low. Target: CRCL kill criterion.**
    Problem: personalized_plays.md uses USDC below $55B, while `plays.csv` R-01 uses below $65B.
    Fix: Align on one threshold.

27. **Low. Target: changelog B13 and A9, both "Noted".**
    Problem: The Arc presale caveat ($182M non-recurring, refund contingency) is one sentence and CRCL is a top-five pick. Deferring it to "the next revision" is not justified. Deposit-franchise economics (A9) is missing from the Section 13 residual weaknesses.
    Fix: Add the Arc caveat to Section 6's CRCL row now. Add "6. Bank deposit-franchise effects not modeled (A9)" to the residual weaknesses.

28. **Low. Target: after-tax arithmetic.**
    Problem: There are three smaller issues:
    - BENJI is taxed at the T-bill rate on a 4.2% yield, not its 3.85% central, and only the portion from US obligations is exempt from California tax.
    - Taxing the whole equity return each year ignores deferral over a 10-year hold. This is conservative but unstated.
    - Option B has no after-tax figure. It is about 4.1% on the same assumptions.
    Fix: Note the annual-realization assumption, use 3.85% for BENJI, and add an Option B after-tax figure of about 4.1%.

## Verdict

**Acceptable after listed fixes.** The allocation arithmetic is right, and the direction of the conclusions survives: Option A over Option B, and incumbents' core franchises over crypto exposure. Findings 1 to 6 must be fixed before finalizing, because they change which plays rank in the top five and which facts can be cited. Findings 7 to 19 are consistency and disposition fixes that take one or two lines each.
