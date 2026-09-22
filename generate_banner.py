#!/usr/bin/env python3
"""Generate the 'perception scan' animated GitHub profile banner SVG, v2:
   - welcoming title
   - livelier radial-gradient + starfield + drifting glow background
   - a small robot mascot that hops from detection to detection
   Everything you'd want to tweak lives in CONFIG below.
"""
import random

# ============================== CONFIG ==============================
W, H = 900, 240
DURATION = 7.0          # seconds per full loop -- change freely, timing below is %-based

TITLE = "// WELCOME TO MY PAGE"
SUBTITLE = "SYSTEMS ONLINE  ·  GLAD YOU STOPPED BY"
HANDLE = "github.com/USERNAME"

BOXES = [
    # (label, confidence)
    ("PERCEPTION", 98),
    ("AUTONOMY STACK", 96),
    ("SENSOR FUSION", 97),
    ("EV SYSTEMS", 94),
    ("C++ / PYTHON", 99),
]

COLOR_BEAM   = "#4ce0ff"
COLOR_BOT    = "#ffb545"
COLOR_BOT_DK = "#8a5200"
COLOR_TEXT   = "#eafcff"
COLOR_ACCENT = "#7fe7ff"
BG_GLOW_A    = "#1d3a52"   # cyan-ish ambient blob
BG_GLOW_B    = "#3a2a66"   # violet ambient blob

random.seed(7)
# ======================================================================

BOX_W, BOX_H = 168, 60
CORNER = 11
CY = 112
BASELINE_Y = 205
BEAM_W = 140
JUMP_H = 46

N = len(BOXES)
MARGIN = 90
box_x = [MARGIN + i * (W - 2 * MARGIN) / (N - 1) for i in range(N)]

def sweep_fraction(x):
    return (x + BEAM_W) / (W + BEAM_W) * 100

peaks = [sweep_fraction(x) for x in box_x]

def clamp(v, lo=0, hi=100):
    return max(lo, min(hi, v))

box_windows = []
for p in peaks:
    p0 = clamp(p - 4)
    p1 = clamp(p)
    p2 = clamp(p + 11)
    p3 = clamp(p + 17)
    box_windows.append((p0, p1, p2, p3))

def box_keyframes_css(cls, p0, p1, p2, p3):
    return f"""
@keyframes {cls} {{
  0%   {{ opacity: 0; transform: translateY(6px) scale(0.94); }}
  {p0:.2f}%  {{ opacity: 0; transform: translateY(6px) scale(0.94); }}
  {p1:.2f}%  {{ opacity: 1; transform: translateY(0) scale(1); }}
  {p2:.2f}%  {{ opacity: 1; transform: translateY(0) scale(1); }}
  {p3:.2f}%  {{ opacity: 0; transform: translateY(-4px) scale(0.97); }}
  100% {{ opacity: 0; transform: translateY(-4px) scale(0.97); }}
}}
"""

def box_markup(i, cx, label, conf):
    left, top = cx - BOX_W / 2, CY - BOX_H / 2
    right, bottom = cx + BOX_W / 2, CY + BOX_H / 2
    c = CORNER
    return f'''
  <g class="detbox box{i}" style="transform-origin:{cx}px {CY}px;">
    <rect x="{left:.1f}" y="{top:.1f}" width="{BOX_W}" height="{BOX_H}" rx="3"
          fill="#03181f" fill-opacity="0.55"/>
    <path d="M {left:.1f} {top+c:.1f} V {top:.1f} H {left+c:.1f}" fill="none" stroke="{COLOR_BEAM}" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M {right-c:.1f} {top:.1f} H {right:.1f} V {top+c:.1f}" fill="none" stroke="{COLOR_BEAM}" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M {right:.1f} {bottom-c:.1f} V {bottom:.1f} H {right-c:.1f}" fill="none" stroke="{COLOR_BEAM}" stroke-width="2.2" stroke-linecap="round"/>
    <path d="M {left+c:.1f} {bottom:.1f} H {left:.1f} V {bottom-c:.1f}" fill="none" stroke="{COLOR_BEAM}" stroke-width="2.2" stroke-linecap="round"/>
    <text x="{cx:.1f}" y="{CY-4:.1f}" text-anchor="middle" font-family="'Courier New', monospace"
          font-size="13" font-weight="700" fill="{COLOR_TEXT}" letter-spacing="0.5">{label}</text>
    <text x="{cx:.1f}" y="{CY+16:.1f}" text-anchor="middle" font-family="'Courier New', monospace"
          font-size="10" fill="{COLOR_ACCENT}" fill-opacity="0.85">CONF {conf}%</text>
    <line x1="{cx:.1f}" y1="{bottom:.1f}" x2="{cx:.1f}" y2="{BASELINE_Y}" stroke="#215a6b" stroke-width="1.2"/>
    <circle cx="{cx:.1f}" cy="{BASELINE_Y}" r="3" fill="{COLOR_BEAM}"/>
  </g>
'''

box_css = "\n".join(box_keyframes_css(f"box{i}", *w) for i, w in enumerate(box_windows))
box_svg = "\n".join(box_markup(i, x, l, c) for i, (x, (l, c)) in enumerate(zip(box_x, BOXES)))

# --------------------------------------------------------------- bot path
POSE = {
    "hidden": dict(sx=1.00, sy=1.00, rot=0,  y=0, shadow_s=1.0, shadow_o=0.0, op=0),
    "land":   dict(sx=1.18, sy=0.78, rot=-3, y=0, shadow_s=1.05, shadow_o=0.38, op=1),
    "stand":  dict(sx=1.00, sy=1.00, rot=0,  y=0, shadow_s=1.00, shadow_o=0.32, op=1),
    "crouch": dict(sx=1.12, sy=0.82, rot=-4, y=0, shadow_s=1.00, shadow_o=0.32, op=1),
    "apex":   dict(sx=0.85, sy=1.20, rot=9,  y=-JUMP_H, shadow_s=0.5, shadow_o=0.15, op=1),
}

events = [(0.0, box_x[0], "hidden")]
w0 = box_windows[0]
events.append((clamp(w0[0] - 3), box_x[0], "hidden"))
events.append((w0[1] - 2, box_x[0], "hidden"))
events.append((w0[1], box_x[0], "land"))
events.append((w0[1] + 3, box_x[0], "stand"))

for i in range(N - 1):
    p2_i = box_windows[i][2]
    p1_next = box_windows[i + 1][1]
    events.append((p2_i, box_x[i], "crouch"))
    mid_t = (p2_i + p1_next) / 2
    mid_x = (box_x[i] + box_x[i + 1]) / 2
    events.append((mid_t, mid_x, "apex"))
    events.append((p1_next, box_x[i + 1], "land"))
    events.append((p1_next + 3, box_x[i + 1], "stand"))

events.append((96, box_x[-1], "stand"))
events.append((98, box_x[-1], "hidden"))
events.append((100, box_x[-1], "hidden"))

def bot_kf_line(t, x, pose):
    d = POSE[pose]
    return f'  {t:.2f}% {{ opacity: {d["op"]}; transform: translate({x:.1f}px,{d["y"]:.1f}px) rotate({d["rot"]}deg) scale({d["sx"]},{d["sy"]}); }}'

def shadow_kf_line(t, x, pose):
    d = POSE[pose]
    return f'  {t:.2f}% {{ opacity: {d["shadow_o"]}; transform: translate({x:.1f}px,0px) scale({d["shadow_s"]},1); }}'

bot_css = "@keyframes bothop {\n" + "\n".join(bot_kf_line(*e) for e in events) + "\n}"
shadow_css = "@keyframes botshadow {\n" + "\n".join(shadow_kf_line(*e) for e in events) + "\n}"

BOT_FEET_Y = BASELINE_Y
bot_markup = f'''
  <ellipse class="botshadow" cx="0" cy="{BOT_FEET_Y}" rx="15" ry="4" fill="#000814"/>
  <g class="bothop" style="transform-origin:0px {BOT_FEET_Y}px;">
    <g transform="translate(0,{BOT_FEET_Y})">
      <line x1="0" y1="-31" x2="0" y2="-24" stroke="{COLOR_BOT}" stroke-width="2"/>
      <circle class="blinkdot" cx="0" cy="-32" r="2.6" fill="{COLOR_BEAM}"/>
      <rect x="-11" y="-24" width="22" height="20" rx="6" fill="{COLOR_BOT}" stroke="{COLOR_BOT_DK}" stroke-width="1"/>
      <circle cx="-4.2" cy="-16" r="2.7" fill="#0a1620"/>
      <circle cx="4.2" cy="-16" r="2.7" fill="#0a1620"/>
      <circle cx="-4.6" cy="-16.6" r="1" fill="#baf6ff"/>
      <circle cx="3.8" cy="-16.6" r="1" fill="#baf6ff"/>
      <line x1="-5" y1="-4" x2="-5" y2="0" stroke="{COLOR_BOT}" stroke-width="4" stroke-linecap="round"/>
      <line x1="5" y1="-4" x2="5" y2="0" stroke="{COLOR_BOT}" stroke-width="4" stroke-linecap="round"/>
    </g>
  </g>
'''

# --------------------------------------------------------------- background
grid = []
for x in range(0, W + 1, 60):
    grid.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#12303d" stroke-width="1" opacity="0.28"/>')
for y in range(0, H + 1, 48):
    grid.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#12303d" stroke-width="1" opacity="0.28"/>')

stars = []
for i in range(28):
    sx = random.uniform(10, W - 10)
    sy = random.uniform(10, H - 40)
    r = random.uniform(0.5, 1.6)
    dur = random.uniform(2.2, 4.4)
    delay = random.uniform(0, 4)
    op = random.uniform(0.35, 0.85)
    stars.append(
        f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="{r:.2f}" fill="#cdeeff" '
        f'style="animation:twinkle {dur:.2f}s ease-in-out {delay:.2f}s infinite; opacity:{op:.2f};"/>'
    )

svg = f'''<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{TITLE}">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="32%" r="80%">
      <stop offset="0%" stop-color="#15304a"/>
      <stop offset="45%" stop-color="#0a1620"/>
      <stop offset="100%" stop-color="#04090f"/>
    </radialGradient>
    <radialGradient id="glowA" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{BG_GLOW_A}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="{BG_GLOW_A}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{BG_GLOW_B}" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="{BG_GLOW_B}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="beamGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{COLOR_BEAM}" stop-opacity="0"/>
      <stop offset="85%" stop-color="{COLOR_BEAM}" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#8ef3ff" stop-opacity="0.55"/>
    </linearGradient>
    <style>
      .scanbeam {{ animation: sweep {DURATION}s linear infinite; }}
      @keyframes sweep {{
        0%   {{ transform: translateX(-{BEAM_W}px); }}
        100% {{ transform: translateX({W}px); }}
      }}
      .blinkdot {{ animation: blink 1.6s ease-in-out infinite; }}
      @keyframes blink {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0.15; }} }}
      @keyframes twinkle {{ 0%,100% {{ opacity:0.15; }} 50% {{ opacity:1; }} }}
      .glowdrift1 {{ animation: drift1 21s ease-in-out infinite; }}
      .glowdrift2 {{ animation: drift2 27s ease-in-out infinite; }}
      @keyframes drift1 {{ 0%,100% {{ transform: translate(-70px,-20px); }} 50% {{ transform: translate(70px,20px); }} }}
      @keyframes drift2 {{ 0%,100% {{ transform: translate(60px,20px); }} 50% {{ transform: translate(-60px,-20px); }} }}
      .detbox {{ animation-duration: {DURATION}s; animation-timing-function: linear; animation-iteration-count: infinite; }}
      {box_css}
      .bothop {{ animation: bothop {DURATION}s linear infinite; }}
      {bot_css}
      .botshadow {{ animation: botshadow {DURATION}s linear infinite; }}
      {shadow_css}
    </style>
  </defs>

  <rect x="0" y="0" width="{W}" height="{H}" fill="url(#bgGrad)"/>
  <ellipse class="glowdrift1" cx="260" cy="90" rx="260" ry="180" fill="url(#glowA)"/>
  <ellipse class="glowdrift2" cx="620" cy="150" rx="240" ry="170" fill="url(#glowB)"/>
  {"".join(stars)}
  {"".join(grid)}

  <line x1="0" y1="{BASELINE_Y}" x2="{W}" y2="{BASELINE_Y}" stroke="#173e4a" stroke-width="1.4" opacity="0.7"/>

  <text x="20" y="30" font-family="'Courier New', monospace" font-size="15" font-weight="700" fill="{COLOR_BEAM}" letter-spacing="1">{TITLE}</text>
  <circle class="blinkdot" cx="21" cy="45" r="3.5" fill="#39ff88"/>
  <text x="30" y="49" font-family="'Courier New', monospace" font-size="11" fill="{COLOR_ACCENT}" fill-opacity="0.8" letter-spacing="0.5">{SUBTITLE}</text>

  {box_svg}

  <g class="scanbeam">
    <rect x="0" y="0" width="{BEAM_W}" height="{H}" fill="url(#beamGrad)"/>
    <rect x="{BEAM_W-3}" y="0" width="3" height="{H}" fill="#eafcff"/>
  </g>

  {bot_markup}

  <text x="895" y="230" text-anchor="end" font-family="'Courier New', monospace" font-size="10" fill="#3d6b80">{HANDLE}</text>
</svg>
'''

out_path = "/tmp/claude-0/-home-claude/cdd6dbac-bb73-5562-9be4-5c7b21b4cb22/scratchpad/perception-scan-v2.svg"
with open(out_path, "w") as f:
    f.write(svg)
print("written", len(svg), "bytes ->", out_path)
