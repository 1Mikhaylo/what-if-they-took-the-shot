# Design System — "What If They Took The Shot?"

> **LOGIC:** When building a specific page, first check `design-system/pages/[page-name].md`.
> If that file exists, its rules **override** this Master file.
> If not, strictly follow the rules below.

---

**Project:** What If They Took The Shot?
**Category:** Sports Analytics / Statistical Modeling Dashboard
**Platform:** Streamlit (Python)
**Generated:** 2026-02-18

---

## Design Philosophy

A **dark-mode data observatory** for football shot analysis.  The aesthetic bridges premium sports broadcasting with academic statistical rigor — think Sky Sports meets a Bayesian research paper. Every design decision optimizes for **data legibility**, **statistical clarity**, and **analytical trust**.

---

## Color Palette

### Core Tokens

| Role | Hex | CSS Variable | Usage |
|------|-----|-------------|-------|
| Background (Primary) | `#0A0E1A` | `--bg-primary` | Main app background |
| Background (Surface) | `#111827` | `--bg-surface` | Cards, containers, sidebar |
| Background (Elevated) | `#1F2937` | `--bg-elevated` | Hover states, active panels |
| Border | `#374151` | `--border-default` | Card borders, dividers |
| Border (Subtle) | `#1F2937` | `--border-subtle` | Soft separators |

### Text Hierarchy

| Role | Hex | CSS Variable | Min Contrast |
|------|-----|-------------|------------|
| Primary Text | `#F9FAFB` | `--text-primary` | 15.3:1 on `#0A0E1A` |
| Secondary Text | `#D1D5DB` | `--text-secondary` | 10.7:1 on `#0A0E1A` |
| Muted Text | `#9CA3AF` | `--text-muted` | 6.3:1 on `#0A0E1A` |
| Caption/Label | `#6B7280` | `--text-caption` | 4.5:1 on `#0A0E1A` |

### Accent Colors — Semantic & Data

| Role | Hex | CSS Variable | Purpose |
|------|-----|-------------|---------|
| Pitch Green | `#10B981` | `--color-pitch` | Pitch viz, positive outcomes, goals |
| xG Blue | `#3B82F6` | `--color-xg` | xG values, primary data accent |
| Shot Gold | `#F59E0B` | `--color-shot` | Highlight shots, CTA, key findings |
| Miss Red | `#EF4444` | `--color-miss` | Missed chances, negative deviation |
| Bayesian Purple | `#8B5CF6` | `--color-bayesian` | Prior/posterior distributions, uncertainty |
| Cyan Accent | `#06B6D4` | `--color-accent` | Secondary data series, links |

### Gradient Tokens

| Name | Value | Usage |
|------|-------|-------|
| xG Gradient | `linear-gradient(135deg, #3B82F6, #8B5CF6)` | xG value displays, headers |
| Heat Gradient | `linear-gradient(90deg, #3B82F6, #F59E0B, #EF4444)` | Probability heatmaps |
| Pitch Gradient | `radial-gradient(ellipse at center, #10B981 0%, #064E3B 100%)` | Pitch background |
| Surface Glow | `radial-gradient(ellipse at top, rgba(59,130,246,0.08) 0%, transparent 70%)` | Subtle header glow |

### Streamlit Color Config

```python
# .streamlit/config.toml
[theme]
primaryColor = "#3B82F6"
backgroundColor = "#0A0E1A"
secondaryBackgroundColor = "#111827"
textColor = "#F9FAFB"
font = "sans serif"
```

---

## Typography

### Recommended Pairing: **Exo + Roboto Mono**

| Role | Font | Weight | Size | Usage |
|------|------|--------|------|-------|
| Display / Hero | Exo | 700 (Bold) | 2.5rem / 40px | Page titles, hero stats |
| Heading H1 | Exo | 600 (SemiBold) | 1.75rem / 28px | Section headers |
| Heading H2 | Exo | 600 (SemiBold) | 1.25rem / 20px | Card titles |
| Heading H3 | Exo | 500 (Medium) | 1.125rem / 18px | Subsection labels |
| Body | Exo | 400 (Regular) | 1rem / 16px | Paragraphs, descriptions |
| Body (Small) | Exo | 400 (Regular) | 0.875rem / 14px | Helper text, tooltips |
| Data Value | Roboto Mono | 500 (Medium) | 1.5rem / 24px | xG values, probabilities, stats |
| Data Label | Roboto Mono | 400 (Regular) | 0.75rem / 12px | Axis labels, data annotations |
| Code/Formula | Roboto Mono | 400 (Regular) | 0.875rem / 14px | Equations, model params |

**Why this pairing:**
- **Exo** — Futuristic geometric sans-serif with a sporty, modern edge. Excellent for headlines while remaining highly readable at body sizes. The slight tech feel aligns with statistical modeling.
- **Roboto Mono** — Industry-standard monospace for data display. Tabular figures ensure numeric alignment. Pairs seamlessly with Exo's geometric structure.

**Google Fonts Import:**
```css
@import url('https://fonts.googleapis.com/css2?family=Exo:wght@300;400;500;600;700&family=Roboto+Mono:wght@300;400;500;700&display=swap');
```

**Streamlit CSS Override:**
```css
/* Inject via st.markdown with unsafe_allow_html=True */
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo:wght@300;400;500;600;700&family=Roboto+Mono:wght@300;400;500;700&display=swap');

html, body, [class*="st-"] {
    font-family: 'Exo', sans-serif;
}

/* Target data values and metrics */
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"],
code, pre {
    font-family: 'Roboto Mono', monospace;
}
</style>
```

### Alternative Pairing: **Fira Code + Fira Sans**
Use if you want a more code/developer-centric feel. Same family cohesion — Fira Code for data, Fira Sans for labels.

---

## Spacing System

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | `4px` / `0.25rem` | Tight gaps, inline elements |
| `--space-sm` | `8px` / `0.5rem` | Icon gaps, badge padding |
| `--space-md` | `16px` / `1rem` | Standard padding, card internal |
| `--space-lg` | `24px` / `1.5rem` | Section padding, card gaps |
| `--space-xl` | `32px` / `2rem` | Column gaps |
| `--space-2xl` | `48px` / `3rem` | Section margins |
| `--space-3xl` | `64px` / `4rem` | Page-level separators |

---

## Shadows & Elevation

| Level | Value | Usage |
|-------|-------|-------|
| `--shadow-sm` | `0 1px 3px rgba(0,0,0,0.3)` | Subtle card lift |
| `--shadow-md` | `0 4px 12px rgba(0,0,0,0.4)` | Cards, buttons |
| `--shadow-lg` | `0 8px 24px rgba(0,0,0,0.5)` | Modals, popovers |
| `--shadow-glow-blue` | `0 0 20px rgba(59,130,246,0.15)` | Active panels, focus |
| `--shadow-glow-green` | `0 0 20px rgba(16,185,129,0.15)` | Pitch elements |
| `--shadow-glow-gold` | `0 0 20px rgba(245,158,11,0.15)` | Key findings, highlights |

---

## UI Style: Dark Analytics + Glass Accents

### Core Style Rules
- **Base:** OLED-optimized dark (#0A0E1A) for comfortable extended analysis sessions
- **Cards:** Semi-transparent glass panels (`rgba(17,24,39,0.8)`, `backdrop-filter: blur(12px)`, `border: 1px solid rgba(55,65,81,0.5)`)
- **Data Panels:** Opaque dark surfaces for chart containers — no blur behind charts (readability first)
- **Glow Effects:** Subtle colored glow on key metrics only. Never on body text.
- **Transitions:** All interactive elements — `transition: all 200ms ease-out`
- **Border Radius:** `8px` for cards, `6px` for buttons/inputs, `50%` for avatars/badges

### Streamlit Glass Card Component

```python
def glass_card(title: str, content: str):
    """Reusable glass-effect card for Streamlit."""
    st.markdown(f"""
    <div style="
        background: rgba(17, 24, 39, 0.8);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(55, 65, 81, 0.5);
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 16px;
    ">
        <h3 style="
            font-family: 'Exo', sans-serif;
            color: #F9FAFB;
            font-weight: 600;
            margin: 0 0 12px 0;
        ">{title}</h3>
        <div style="color: #D1D5DB;">{content}</div>
    </div>
    """, unsafe_allow_html=True)
```

---

## Chart & Visualization System

### Recommended Library: **Plotly**
Best choice for Streamlit — native integration via `st.plotly_chart()`, interactive by default, supports all required chart types.

### Chart Type Matrix

| Visualization Need | Best Chart | Library | Color Guidance |
|--------|-----------|---------|-------|
| Shot positions on pitch | Scatter over SVG pitch | Plotly + Custom SVG | Marker color = xG gradient (blue→gold→red) |
| Player finishing profiles | Radar / Spider Chart | Plotly | Single: `#3B82F6` at 20% fill. Multi: distinct accent colors |
| xG distribution | Violin / Box Plot | Plotly | Box: `#3B82F6`. Median: `#F59E0B`. Outliers: `#EF4444` |
| Shot probability heatmap | Heat Map | Plotly | Cool→Hot gradient (`#3B82F6` → `#F59E0B` → `#EF4444`) |
| Bayesian prior/posterior | Area / Line Chart | Plotly | Prior: `#8B5CF6` dashed. Posterior: `#3B82F6` solid. Credible interval: fill at 15% opacity |
| Counterfactual comparison | Grouped Bar / Dumbbell | Plotly | Actual: `#3B82F6`. Counterfactual: `#F59E0B` |
| Uncertainty / credible intervals | Ribbon / Confidence Band | Plotly | Center line: accent solid. Band: same accent at 10-20% fill |
| Shot outcome breakdown | Donut Chart | Plotly | Goal: `#10B981`, Saved: `#3B82F6`, Missed: `#EF4444`, Blocked: `#6B7280` |

### Plotly Dark Theme Template

```python
import plotly.graph_objects as go
import plotly.io as pio

xg_template = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Exo, sans-serif',
            color='#D1D5DB',
            size=13
        ),
        title=dict(
            font=dict(family='Exo, sans-serif', size=18, color='#F9FAFB'),
            x=0, xanchor='left'
        ),
        xaxis=dict(
            gridcolor='rgba(55,65,81,0.3)',
            zerolinecolor='rgba(55,65,81,0.5)',
            tickfont=dict(family='Roboto Mono, monospace', size=11)
        ),
        yaxis=dict(
            gridcolor='rgba(55,65,81,0.3)',
            zerolinecolor='rgba(55,65,81,0.5)',
            tickfont=dict(family='Roboto Mono, monospace', size=11)
        ),
        colorway=[
            '#3B82F6', '#10B981', '#F59E0B', '#EF4444',
            '#8B5CF6', '#06B6D4', '#EC4899', '#6366F1'
        ],
        hoverlabel=dict(
            bgcolor='#1F2937',
            bordercolor='#374151',
            font=dict(family='Exo, sans-serif', color='#F9FAFB')
        )
    )
)
pio.templates['xg_dark'] = xg_template
pio.templates.default = 'xg_dark'
```

---

## Layout Patterns

### App Structure (Streamlit)

```
┌──────────────────────────────────────────────────────┐
│  ⚽ What If They Took The Shot?     [Model v2.1]     │  ← Sticky header
├─────────┬────────────────────────────────────────────┤
│ Sidebar │  Main Content Area                         │
│         │                                            │
│ Filters │  ┌─ Metric Bar ──────────────────────────┐ │
│ Model   │  │ xG: 0.34  │ Goals: 12  │ Δ: +2.1    │ │
│ Params  │  └────────────────────────────────────────┘ │
│         │                                            │
│ Player  │  ┌─ Primary Viz ─────────────────────────┐ │
│ Select  │  │                                       │ │
│         │  │     Interactive Pitch / Chart          │ │
│ Match   │  │                                       │ │
│ Context │  └────────────────────────────────────────┘ │
│         │                                            │
│         │  ┌─ Panel ──────┐ ┌─ Panel ──────────────┐ │
│         │  │ Radar Chart  │ │ Distribution / Post  │ │
│         │  └──────────────┘ └──────────────────────┘ │
└─────────┴────────────────────────────────────────────┘
```

### Page Layout Principles
1. **Sidebar** — All controls (filters, model params, player select). Keep viz area uncluttered.
2. **Metric Bar** — Top of main content. Monospaced numbers. Key stats at a glance.
3. **Primary Viz** — Full-width interactive chart (pitch / main analysis). 60-70% of viewport.
4. **Secondary Panels** — 2-column grid below. Supporting charts and data tables.
5. **Progressive Disclosure** — Use `st.expander()` for advanced settings and raw data.

---

## Effects & Animations

### Allowed Effects
| Effect | Implementation | When to Use |
|--------|---------------|------------|
| Subtle card glow | `box-shadow: 0 0 20px rgba(accent, 0.15)` | Active/focused card |
| Metric counter | CSS counter-increment or JS | Hero stat reveals |
| Fade-in on load | `opacity: 0 → 1`, `200ms ease-out` | Card/section entry |
| Chart tooltip | Plotly default hover | All interactive charts |
| Sidebar collapse | Streamlit native | Maximize viz area |

### Forbidden Effects
| Effect | Reason |
|--------|--------|
| Parallax scrolling | Causes nausea; not useful for data apps |
| Glitch animations | Distracting; undermines analytical trust |
| Auto-playing animations | Disrupts focused analysis |
| Heavy 3D transforms | Performance cost, no value for data viz |
| CRT scanlines | Reduces chart legibility |
| Layout-shifting hovers | Hover scale transforms that push content |

### Accessibility
- Respect `prefers-reduced-motion: reduce` — disable all non-essential animations
- Maximum 1-2 animated elements visible at any time
- Use `ease-out` for entering elements, `ease-in` for exiting
- All transitions: 150-300ms. Never exceed 500ms.
- Minimum text contrast: 4.5:1 (WCAG AA). Target: 7:1 (WCAG AAA)

---

## Component Specs (Streamlit Custom CSS)

### Metric Card

```python
def metric_card(label: str, value: str, delta: str = None, color: str = "#3B82F6"):
    delta_html = ""
    if delta:
        delta_color = "#10B981" if delta.startswith("+") else "#EF4444"
        delta_html = f'<span style="color:{delta_color}; font-size:0.875rem; font-family:Roboto Mono, monospace;">{delta}</span>'

    st.markdown(f"""
    <div style="
        background: rgba(17, 24, 39, 0.8);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(55, 65, 81, 0.5);
        border-radius: 8px;
        padding: 20px;
        text-align: center;
    ">
        <div style="
            font-family: 'Exo', sans-serif;
            color: #9CA3AF;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        ">{label}</div>
        <div style="
            font-family: 'Roboto Mono', monospace;
            color: {color};
            font-size: 1.75rem;
            font-weight: 500;
            line-height: 1;
        ">{value}</div>
        {f'<div style="margin-top:6px;">{delta_html}</div>' if delta else ''}
    </div>
    """, unsafe_allow_html=True)
```

### Section Header

```python
def section_header(title: str, subtitle: str = None):
    sub_html = f'<p style="color:#9CA3AF; margin:4px 0 0 0; font-size:0.875rem;">{subtitle}</p>' if subtitle else ''
    st.markdown(f"""
    <div style="margin: 32px 0 16px 0; border-left: 3px solid #3B82F6; padding-left: 16px;">
        <h2 style="
            font-family: 'Exo', sans-serif;
            color: #F9FAFB;
            font-weight: 600;
            font-size: 1.25rem;
            margin: 0;
        ">{title}</h2>
        {sub_html}
    </div>
    """, unsafe_allow_html=True)
```

---

## Anti-Patterns (Do NOT Use)

- ❌ **Light mode default** — Dark is essential for data-heavy analysis and extended use
- ❌ **Emojis as icons** — Use SVG icons (Lucide, Heroicons, or Simple Icons)
- ❌ **Missing cursor:pointer** — All clickable elements must have `cursor: pointer`
- ❌ **Layout-shifting hovers** — No `transform: scale()` that shifts neighboring content
- ❌ **Low contrast text** — Maintain 4.5:1 minimum. Never use `#6B7280` on `#0A0E1A` for body text
- ❌ **Instant state changes** — Always use transitions (150-300ms)
- ❌ **Invisible focus states** — Focus rings must be visible for keyboard users
- ❌ **Slow chart rendering** — Lazy load heavy charts. Use Plotly's efficient webgl renderer for scatter plots >1000 points
- ❌ **Rainbow colormaps** — Use perceptually uniform colormaps (viridis, plasma) for heatmaps
- ❌ **Unlabeled uncertainty** — Always annotate credible intervals with confidence level (e.g., "90% CI")

---

## Pre-Delivery Checklist

- [ ] Dark theme applied globally via `.streamlit/config.toml`
- [ ] Exo + Roboto Mono loaded and applied via CSS injection
- [ ] All numeric values displayed in Roboto Mono
- [ ] Icons are SVG, not emojis
- [ ] All charts use the `xg_dark` Plotly template
- [ ] Chart colors follow the semantic palette (xG blue, shot gold, miss red, etc.)
- [ ] Cards have glass effect with proper backdrop-filter
- [ ] Text contrast meets WCAG AA (4.5:1) minimum
- [ ] `cursor: pointer` on all interactive elements
- [ ] Transitions are 150-300ms, ease-out
- [ ] `prefers-reduced-motion` respected
- [ ] Sidebar used for controls; main area reserved for visualizations
- [ ] Responsive layout tested at 768px and 1440px
- [ ] Uncertainty visualizations include labeled credible intervals
