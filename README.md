<!-- If you're reading the source: yes, even this comment was compiled. -->

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/agent-trace-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/agent-trace-light.svg">
  <img alt="A terminal running Stellar, Rohith's agent runtime. It boots a sandbox, runs a FAISS vector search on 'who is rohith?', calls github.metrics(), and streams out his profile: Adumalapelli Rohith — full-stack dev and AI systems architect, B.Tech CSE '28 @ CMRCET, 1.5 yrs at Technirmaan building backends serving 30M+ requests/day, 11x national hackathon champion, builder of Stellar and LearnWave." src="assets/agent-trace-dark.svg" width="100%">
</picture>

<p>
  <a href="https://www.linkedin.com/in/rohith-a-514a7353/">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/chip-linkedin-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/chip-linkedin-light.svg">
      <img src="assets/chip-linkedin-dark.svg" height="40" alt="linkedin.connect()">
    </picture>
  </a>
  <a href="mailto:rohith2989@gmail.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/chip-mail-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/chip-mail-light.svg">
      <img src="assets/chip-mail-dark.svg" height="40" alt="mail.send()">
    </picture>
  </a>
  <!-- TODO(rohith): swap in your real LeetCode profile URL — leetcode.com/Rohith2989 does not exist -->
  <a href="https://leetcode.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/chip-leetcode-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/chip-leetcode-light.svg">
      <img src="assets/chip-leetcode-dark.svg" height="40" alt="leetcode.solve()">
    </picture>
  </a>
  <a href="https://codeforces.com/profile/Rohith2989">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/chip-codeforces-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="assets/chip-codeforces-light.svg">
      <img src="assets/chip-codeforces-dark.svg" height="40" alt="codeforces.rate()">
    </picture>
  </a>
</p>

</div>

<details>
<summary><code>$ cat HOW_THIS_WORKS.md</code></summary>
<br>

This README isn't a template — it's a trace of an agent rendering it.

```mermaid
flowchart LR
    Q["query:<br/>who is @Rohith2989?"] --> S["stellar sandbox<br/>(docker)"]
    S --> V[("faiss index<br/>rohith.mem")]
    S --> G["github api"]
    V --> E["sse stream"]
    G --> E
    E --> R["README.md"]
    C["cron · daily"] -. refresh telemetry .-> G
```

- The terminal above is a **hand-written animated SVG** — pure CSS keyframes, no JS (GitHub wouldn't run it anyway), no generator sites.
- The numbers in `github.metrics()` are **real** — [telemetry.yml](.github/workflows/telemetry.yml) re-fetches them every day and rewrites the SVG in place.
- Both light and dark theme variants are compiled from one source by [make_light_assets.py](scripts/make_light_assets.py).

</details>

<p align="center"><sub><code>last telemetry sync: <!--SYNC-->2026-08-11<!--/SYNC--> · rendered by stellar-runtime · 0 hallucinations detected</code></sub></p>
