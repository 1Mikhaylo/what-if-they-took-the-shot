import plotly.graph_objects as go
import plotly.io as pio

# Design system colors
COLORS = {
    'bg_primary': '#0A0E1A',
    'bg_surface': '#111827',
    'text_primary': '#F9FAFB',
    'text_secondary': '#D1D5DB',
    'xg_blue': '#3B82F6',
    'pitch_green': '#10B981',
    'shot_gold': '#F59E0B',
    'miss_red': '#EF4444',
    'bayesian_purple': '#8B5CF6',
    'cyan_accent': '#06B6D4',
}

xg_template = go.layout.Template(
    layout=go.Layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Exo, sans-serif',
            color=COLORS['text_secondary'],
            size=13
        ),
        title=dict(
            font=dict(family='Exo, sans-serif', size=18, color=COLORS['text_primary']),
            x=0, xanchor='left'
        ),
        xaxis=dict(
            gridcolor='rgba(55,65,81,0.3)',
            zerolinecolor='rgba(55,65,81,0.5)',
            tickfont=dict(family='Roboto Mono, monospace', size=11, color=COLORS['text_secondary'])
        ),
        yaxis=dict(
            gridcolor='rgba(55,65,81,0.3)',
            zerolinecolor='rgba(55,65,81,0.5)',
            tickfont=dict(family='Roboto Mono, monospace', size=11, color=COLORS['text_secondary'])
        ),
        colorway=[
            COLORS['xg_blue'], COLORS['pitch_green'], COLORS['shot_gold'], 
            COLORS['miss_red'], COLORS['bayesian_purple'], COLORS['cyan_accent']
        ],
        hoverlabel=dict(
            bgcolor='#1F2937',
            bordercolor='#374151',
            font=dict(family='Exo, sans-serif', color=COLORS['text_primary'])
        )
    )
)

pio.templates['xg_dark'] = xg_template
pio.templates.default = 'xg_dark'
