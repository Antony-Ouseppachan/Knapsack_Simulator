import re
import time
import streamlit as st

st.set_page_config(
    page_title="0/1 Knapsack DP Laboratory",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded"
)

st.html("""
<style>
    :root {
        --color-primary: #0f172a;
        --color-accent: #2563eb;
        --color-border: #cbd5e1;
        --color-cell-curr: #fef08a;
        --color-cell-curr-border: #ca8a04;
        --color-cell-skip: #bfdbfe;
        --color-cell-skip-border: #2563eb;
        --color-cell-take: #ede9fe;
        --color-cell-take-border: #7c3aed;
        --color-cell-path: #bbf7d0;
        --color-cell-path-border: #16a34a;
    }

    body, .stApp {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    .top-meta-banner {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 6px;
    }
    .badge-pill {
        display: inline-flex;
        align-items: center;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        background: rgba(37, 99, 235, 0.12);
        color: #3b82f6;
        border: 1px solid rgba(37, 99, 235, 0.3);
    }
    .badge-secondary {
        background: rgba(128, 128, 128, 0.12);
        color: #94a3b8;
        border: 1px solid rgba(128, 128, 128, 0.25);
    }

    .main-header {
        border-bottom: 1px solid rgba(128, 128, 128, 0.2);
        padding-bottom: 12px;
        margin-bottom: 18px;
    }
    .main-header h1 {
        font-size: 1.85rem;
        font-weight: 800;
        margin: 4px 0;
        letter-spacing: -0.025em;
    }
    .main-header p {
        font-size: 0.95rem;
        color: #94a3b8;
        margin: 0;
    }

    .stats-strip {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 18px;
    }
    .stat-card {
        background: var(--secondary-background-color, #1e293b);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 6px;
        padding: 10px 14px;
    }
    .stat-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #94a3b8;
        font-weight: 600;
    }
    .stat-val {
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 2px;
        font-family: "JetBrains Mono", Consolas, monospace;
    }

    div[data-testid="stButton"] > button {
        width: 100% !important;
        min-height: 44px !important;
        border-radius: 6px !important;
        font-size: 0.92rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em !important;
        padding: 8px 14px !important;
        transition: all 0.15s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15) !important;
    }

    div[data-testid="stButton"] > button:not([kind="primary"]) {
        background-color: #1e293b !important;
        border: 1.5px solid #475569 !important;
        color: #ffffff !important;
    }

    div[data-testid="stButton"] > button:not([kind="primary"]) * {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
    }

    div[data-testid="stButton"] > button:not([kind="primary"]):hover:not(:disabled) {
        background-color: #334155 !important;
        border-color: #3b82f6 !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    div[data-testid="stButton"] > button:not([kind="primary"]):hover:not(:disabled) * {
        color: #93c5fd !important;
    }

    div[data-testid="stButton"] > button[kind="primary"],
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"] {
        background-color: #2563eb !important;
        border: 1.5px solid #1d4ed8 !important;
        color: #ffffff !important;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.35) !important;
    }

    div[data-testid="stButton"] > button[kind="primary"] *,
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"] * {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 0.92rem !important;
    }

    div[data-testid="stButton"] > button[kind="primary"]:hover:not(:disabled),
    div[data-testid="stButton"] > button[data-testid="baseButton-primary"]:hover:not(:disabled) {
        background-color: #1d4ed8 !important;
        border-color: #1e40af !important;
        box-shadow: 0 4px 14px rgba(29, 78, 216, 0.45) !important;
        transform: translateY(-1px) !important;
    }

    div[data-testid="stButton"] > button:disabled,
    div[data-testid="stButton"] > button[disabled] {
        background-color: #0f172a !important;
        border: 1.5px solid #334155 !important;
        opacity: 0.5 !important;
        cursor: not-allowed !important;
        transform: none !important;
        box-shadow: none !important;
    }

    div[data-testid="stButton"] > button:disabled *,
    div[data-testid="stButton"] > button[disabled] * {
        color: #94a3b8 !important;
        font-weight: 600 !important;
    }

    .matrix-wrapper {
        overflow-x: auto;
        border: 1px solid rgba(128, 128, 128, 0.25);
        border-radius: 6px;
        background: var(--secondary-background-color, #1e293b);
        padding: 14px;
        margin: 10px 0;
    }
    table.matrix-table {
        border-collapse: collapse;
        margin: 0 auto;
        font-family: "JetBrains Mono", Consolas, Menlo, monospace;
        font-size: 0.88rem;
    }
    table.matrix-table th, table.matrix-table td {
        border: 1px solid rgba(128, 128, 128, 0.25);
        padding: 7px 10px;
        text-align: center;
        min-width: 44px;
        height: 38px;
        box-sizing: border-box;
    }
    table.matrix-table th {
        background: rgba(128, 128, 128, 0.12);
        font-weight: 700;
        font-size: 0.8rem;
    }
    table.matrix-table th.axis-label {
        background: rgba(128, 128, 128, 0.18);
        text-align: left;
        white-space: nowrap;
        padding-left: 12px;
        padding-right: 14px;
        font-weight: 600;
    }

    table.matrix-table td.cell-uncomputed {
        background: transparent;
        color: rgba(128, 128, 128, 0.35);
    }
    table.matrix-table td.cell-filled {
        background: rgba(128, 128, 128, 0.06);
        font-weight: 600;
    }
    table.matrix-table td.cell-current {
        background: #fef08a !important;
        color: #713f12 !important;
        font-weight: 800;
        border: 2px solid #ca8a04 !important;
        box-shadow: 0 0 10px rgba(202, 138, 4, 0.45);
    }
    table.matrix-table td.cell-skip {
        background: #bfdbfe !important;
        color: #1e3a8a !important;
        font-weight: 800;
        border: 2px solid #2563eb !important;
    }
    table.matrix-table td.cell-take {
        background: #ede9fe !important;
        color: #581c87 !important;
        font-weight: 800;
        border: 2px solid #7c3aed !important;
    }
    table.matrix-table td.cell-traceback {
        background: #bbf7d0 !important;
        color: #14532d !important;
        font-weight: 800;
        border: 2px solid #16a34a !important;
    }

    .legend-bar {
        display: flex;
        flex-wrap: wrap;
        gap: 16px;
        align-items: center;
        padding: 10px 14px;
        background: rgba(128, 128, 128, 0.08);
        border: 1px solid rgba(128, 128, 128, 0.2);
        border-radius: 6px;
        font-size: 0.82rem;
        margin-top: 10px;
    }
    .legend-item {
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .legend-box {
        width: 14px;
        height: 14px;
        border-radius: 3px;
        display: inline-block;
    }

    .mono {
        font-family: "JetBrains Mono", Consolas, monospace;
    }
</style>
""")


# 1. ALGORITHM ENGINE & STATE GENERATOR

def parse_input_vector(s: str):
    """Parse comma or whitespace separated positive integers."""
    tokens = re.split(r'[\s,]+', s.strip())
    tokens = [t for t in tokens if t]
    return [int(t) for t in tokens]


def compute_dp_matrix_and_trace(weights, values, capacity):
    """
    Simulates bottom-up Dynamic Programming table construction for 0/1 Knapsack,
    recording detailed analytical steps for interactive playback.
    """
    n = len(weights)
    W = capacity

    dp = [[0] * (W + 1) for _ in range(n + 1)]
    steps = []

    for i in range(1, n + 1):
        wi = weights[i - 1]
        vi = values[i - 1]
        for j in range(1, W + 1):
            skip_val = dp[i - 1][j]
            fits = (wi <= j)

            if not fits:
                take_val = None
                chosen_val = skip_val
                decision = "EXCLUDE_OVERCAPACITY"
            else:
                take_val = vi + dp[i - 1][j - wi]
                if take_val > skip_val:
                    chosen_val = take_val
                    decision = "INCLUDE_SUPERIOR"
                elif take_val == skip_val:
                    chosen_val = skip_val
                    decision = "TIE_EXCLUDE"
                else:
                    chosen_val = skip_val
                    decision = "EXCLUDE_SUPERIOR"

            dp[i][j] = chosen_val

            steps.append({
                "type": "FILL",
                "i": i,
                "j": j,
                "weight": wi,
                "value": vi,
                "fits": fits,
                "skip_val": skip_val,
                "take_val": take_val,
                "take_ref_coord": (i - 1, j - wi) if fits else None,
                "skip_ref_coord": (i - 1, j),
                "chosen_val": chosen_val,
                "decision": decision
            })

    curr_i = n
    curr_j = W
    traceback_steps = []
    selected_items = []

    while curr_i > 0 and curr_j > 0:
        val_curr = dp[curr_i][curr_j]
        val_above = dp[curr_i - 1][curr_j]
        wi = weights[curr_i - 1]
        vi = values[curr_i - 1]

        was_included = (val_curr != val_above)

        if was_included:
            selected_items.append(curr_i)
            next_j = curr_j - wi
            next_i = curr_i - 1
            traceback_steps.append({
                "type": "TRACEBACK",
                "i": curr_i,
                "j": curr_j,
                "item_index": curr_i,
                "weight": wi,
                "value": vi,
                "included": True,
                "curr_val": val_curr,
                "above_val": val_above,
                "next_coord": (next_i, next_j)
            })
            curr_j = next_j
            curr_i = next_i
        else:
            next_i = curr_i - 1
            traceback_steps.append({
                "type": "TRACEBACK",
                "i": curr_i,
                "j": curr_j,
                "item_index": curr_i,
                "weight": wi,
                "value": vi,
                "included": False,
                "curr_val": val_curr,
                "above_val": val_above,
                "next_coord": (next_i, curr_j)
            })
            curr_i = next_i

    steps.extend(traceback_steps)
    selected_items.reverse()

    steps.append({
        "type": "TERMINATION",
        "optimal_value": dp[n][W],
        "selected_items": selected_items,
        "total_weight": sum(weights[idx - 1] for idx in selected_items)
    })

    return dp, steps, selected_items


def compute_greedy_heuristic(weights, values, capacity):
    """
    Computes greedy heuristic selection based on Value-to-Weight density ratio (v/w).
    """
    items = []
    for idx, (w, v) in enumerate(zip(weights, values), start=1):
        ratio = v / w if w > 0 else 0
        items.append({"id": idx, "weight": w, "value": v, "ratio": ratio})

    items_sorted = sorted(items, key=lambda x: x["ratio"], reverse=True)

    rem_cap = capacity
    greedy_val = 0
    greedy_items = []

    for it in items_sorted:
        if it["weight"] <= rem_cap:
            greedy_items.append(it["id"])
            greedy_val += it["value"]
            rem_cap -= it["weight"]

    return greedy_val, greedy_items, items_sorted


# 2. MATRIX TABLE RENDERER

def render_matrix_table(weights, values, capacity, dp, steps, active_step_index):
    """
    Renders high-contrast, professional HTML DP matrix with exact step highlights.
    """
    n = len(weights)
    W = capacity

    cell_state = [[(1 if (i == 0 or j == 0) else 0) for j in range(W + 1)] for i in range(n + 1)]
    traceback_path = set()
    current_coord = None
    skip_coord = None
    take_coord = None

    if active_step_index >= 0:
        for idx in range(min(active_step_index + 1, len(steps))):
            s = steps[idx]
            if s["type"] == "FILL":
                cell_state[s["i"]][s["j"]] = 1
            elif s["type"] == "TRACEBACK":
                traceback_path.add((s["i"], s["j"]))

        current_s = steps[active_step_index]
        if current_s["type"] == "FILL":
            current_coord = (current_s["i"], current_s["j"])
            skip_coord = current_s["skip_ref_coord"]
            take_coord = current_s["take_ref_coord"]
        elif current_s["type"] == "TRACEBACK":
            current_coord = (current_s["i"], current_s["j"])

    header_th = ['<th class="axis-label">Items \\ Capacity [j]</th>']
    for j in range(W + 1):
        header_th.append(f"<th>{j}</th>")

    rows_markup = [f"<tr>{''.join(header_th)}</tr>"]

    for i in range(n + 1):
        if i == 0:
            row_title = "i = 0 [Base: 0 items]"
        else:
            w_i = weights[i - 1]
            v_i = values[i - 1]
            ratio_i = round(v_i / w_i, 2)
            row_title = f"i = {i} [w={w_i}, v={v_i}, v/w={ratio_i}]"

        cols_markup = [f'<th class="axis-label">{row_title}</th>']

        for j in range(W + 1):
            is_computed = (cell_state[i][j] == 1)
            display_val = str(dp[i][j]) if is_computed else "·"
            coord = (i, j)

            if coord in traceback_path:
                cls_name = "cell-traceback"
                title_tip = f"Traceback path at ({i}, {j})"
            elif coord == current_coord:
                cls_name = "cell-current"
                title_tip = f"Active target cell: DP[{i}][{j}]"
            elif coord == take_coord:
                cls_name = "cell-take"
                title_tip = f"Include reference: DP[{i-1}][{j - weights[i-1]}]"
            elif coord == skip_coord:
                cls_name = "cell-skip"
                title_tip = f"Exclude reference: DP[{i-1}][{j}]"
            elif is_computed:
                cls_name = "cell-filled"
                title_tip = f"Computed value: DP[{i}][{j}] = {dp[i][j]}"
            else:
                cls_name = "cell-uncomputed"
                title_tip = "Pending calculation"

            cols_markup.append(f'<td class="{cls_name}" title="{title_tip}">{display_val}</td>')

        rows_markup.append(f"<tr>{''.join(cols_markup)}</tr>")

    table_html = f"""
    <div class="matrix-wrapper">
        <table class="matrix-table">
            {''.join(rows_markup)}
        </table>
    </div>
    """
    return table_html


# 3. APPLICATION WORKFLOW & LAYOUT

st.html("""
<div class="top-meta-banner">
    <span class="badge-pill">DAA Laboratory</span>
    <span class="badge-pill badge-secondary">Dynamic Programming</span>
    <span class="badge-pill badge-secondary">Bottom-Up Paradigm</span>
</div>
<div class="main-header">
    <h1>0/1 Knapsack Dynamic Programming Laboratory</h1>
    <p>Interactive algorithm execution engine, state construction visualizer, and rigorous DAA theoretical laboratory.</p>
</div>
""")

with st.sidebar:
    st.markdown("### Problem Specification")

    dataset_mode = st.selectbox(
        "Problem Instances",
        [
            "Standard DAA Benchmark (4 items, Cap = 7)",
            "Greedy Counterexample (3 items, Cap = 50)",
            "Textbook DAA Instance (5 items, Cap = 10)",
            "Custom Configuration"
        ]
    )

    if dataset_mode == "Standard DAA Benchmark (4 items, Cap = 7)":
        preset_w, preset_v, preset_c = "1, 3, 4, 5", "1, 4, 5, 7", 7
    elif dataset_mode == "Greedy Counterexample (3 items, Cap = 50)":
        preset_w, preset_v, preset_c = "10, 20, 30", "60, 100, 120", 50
    elif dataset_mode == "Textbook DAA Instance (5 items, Cap = 10)":
        preset_w, preset_v, preset_c = "2, 3, 4, 5, 7", "3, 4, 5, 8, 10", 10
    else:
        preset_w, preset_v, preset_c = "1, 3, 4, 5", "1, 4, 5, 7", 7

    weights_raw = st.text_input("Item Weights (w_1, w_2, ...)", value=preset_w)
    values_raw = st.text_input("Item Values (v_1, v_2, ...)", value=preset_v)
    capacity_val = st.number_input("Knapsack Capacity (W)", min_value=1, max_value=60, value=preset_c, step=1)

    load_problem_btn = st.button("Initialize / Reset State", use_container_width=True, type="primary")

    st.markdown("---")
    st.markdown("### Algorithmic Parameters")
    st.markdown("""
    - **Methodology:** Dynamic Programming
    - **Time Complexity:** 𝒪(n · W)
    - **Space Complexity:** 𝒪(n · W)
    - **Optimality:** Globally Optimal
    """)

validation_error = None
try:
    weights = parse_input_vector(weights_raw)
    values = parse_input_vector(values_raw)
    capacity = int(capacity_val)

    if len(weights) == 0:
        validation_error = "Weights list cannot be empty."
    elif len(weights) != len(values):
        validation_error = f"Dimension mismatch: {len(weights)} weights provided vs {len(values)} values."
    elif any(w <= 0 for w in weights) or any(v <= 0 for v in values):
        validation_error = "Weights and values must be strictly positive integers."
    elif capacity < 1:
        validation_error = "Knapsack capacity W must be at least 1."
    elif len(weights) > 12:
        validation_error = "For clear matrix display, item count is capped at 12."
except Exception as parse_ex:
    validation_error = f"Input syntax error: {parse_ex}"

if validation_error:
    st.error(f"[ERROR] {validation_error}")
    st.stop()

current_state_key = (tuple(weights), tuple(values), capacity)
if ('problem_sig' not in st.session_state or 
    st.session_state.problem_sig != current_state_key or 
    load_problem_btn):
    dp_matrix, step_records, optimal_subset = compute_dp_matrix_and_trace(weights, values, capacity)
    st.session_state.problem_sig = current_state_key
    st.session_state.dp_matrix = dp_matrix
    st.session_state.steps = step_records
    st.session_state.optimal_subset = optimal_subset
    st.session_state.active_step = -1
    st.session_state.is_playing = False

dp = st.session_state.dp_matrix
steps = st.session_state.steps
total_steps = len(steps)
curr_k = st.session_state.active_step

fill_count = (curr_k + 1) if curr_k >= 0 else 0
progress_pct = int((fill_count / total_steps) * 100) if total_steps > 0 else 0

st.html(f"""
<div class="stats-strip">
    <div class="stat-card">
        <div class="stat-label">Problem Size</div>
        <div class="stat-val">{len(weights)} items &bull; W={capacity}</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Matrix Subproblems</div>
        <div class="stat-val">{(len(weights)+1) * (capacity+1)} cells</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Execution Progress</div>
        <div class="stat-val">{progress_pct}% [{fill_count}/{total_steps}]</div>
    </div>
    <div class="stat-card">
        <div class="stat-label">Optimal Value Achieved</div>
        <div class="stat-val">{dp[len(weights)][capacity]}</div>
    </div>
</div>
""")

tab_simulator, tab_math, tab_greedy, tab_code, tab_viva = st.tabs([
    "Execution Simulator",
    "Mathematical Foundation",
    "DP vs Greedy Analysis",
    "Lab Implementations",
    "Exam & Viva Guide"
])


# Tab 1: Execution Simulator

with tab_simulator:
    b_first, b_prev, b_next, b_last, b_play = st.columns([1, 1, 1, 1, 1.4])

    with b_first:
        if st.button("⏮ Start", use_container_width=True, disabled=(curr_k <= -1)):
            st.session_state.active_step = -1
            st.session_state.is_playing = False
            st.rerun()

    with b_prev:
        if st.button("◀ Previous", use_container_width=True, disabled=(curr_k <= -1)):
            st.session_state.active_step = max(-1, curr_k - 1)
            st.session_state.is_playing = False
            st.rerun()

    with b_next:
        if st.button("Next ▶", use_container_width=True, disabled=(curr_k >= total_steps - 1)):
            st.session_state.active_step = min(total_steps - 1, curr_k + 1)
            st.session_state.is_playing = False
            st.rerun()

    with b_last:
        if st.button("End ⏭", use_container_width=True, disabled=(curr_k >= total_steps - 1)):
            st.session_state.active_step = total_steps - 1
            st.session_state.is_playing = False
            st.rerun()

    with b_play:
        is_playing = st.session_state.get('is_playing', False)
        play_caption = "❚❚ Pause" if is_playing else "▶ Auto Play"
        play_btn_type = "primary" if is_playing else "secondary"
        if st.button(play_caption, use_container_width=True, type=play_btn_type):
            st.session_state.is_playing = not is_playing
            st.rerun()

    col_scrub, col_speed = st.columns([3, 1.2])

    with col_scrub:
        scrub_step = st.slider(
            "Timeline Scrubber",
            min_value=-1,
            max_value=total_steps - 1,
            value=curr_k,
            help="Drag to jump instantly to any point during DP table filling or traceback."
        )
        if scrub_step != curr_k:
            st.session_state.active_step = scrub_step
            st.session_state.is_playing = False
            st.rerun()

    with col_speed:
        playback_speed = st.select_slider(
            "Playback Speed",
            options=["Fast (0.15s)", "Normal (0.5s)", "Slow (1.0s)"],
            value="Normal (0.5s)"
        )
        delay_map = {"Fast (0.15s)": 0.15, "Normal (0.5s)": 0.5, "Slow (1.0s)": 1.0}
        speed_delay = delay_map[playback_speed]

    st.progress(fill_count / total_steps if total_steps > 0 else 0)

    phase_badge = ""
    if curr_k < 0:
        phase_badge = ":gray[**[PHASE 0: BASE CASE INITIALIZATION]**]"
        step_title = f"Step 0 of {total_steps}: Table Initialized with Base Zeros"
    elif steps[curr_k]["type"] == "FILL":
        phase_badge = ":blue[**[PHASE 1: BOTTOM-UP CONSTRUCTION]**]"
        step_title = f"Step {curr_k + 1} of {total_steps}: Solving Subproblem DP({steps[curr_k]['i']}, {steps[curr_k]['j']})"
    elif steps[curr_k]["type"] == "TRACEBACK":
        phase_badge = ":orange[**[PHASE 2: SOLUTION TRACEBACK]**]"
        step_title = f"Step {curr_k + 1} of {total_steps}: Traceback at Item {steps[curr_k]['item_index']}, Capacity {steps[curr_k]['j']}"
    else:
        phase_badge = ":green[**[PHASE 3: GLOBAL OPTIMUM VERIFIED]**]"
        step_title = f"Step {curr_k + 1} of {total_steps}: Execution Complete"

    st.markdown(f"#### {step_title} &nbsp;&nbsp; {phase_badge}")

    col_matrix, col_analysis = st.columns([3, 2])

    with col_matrix:
        matrix_html = render_matrix_table(weights, values, capacity, dp, steps, curr_k)
        st.html(matrix_html)

        st.html("""
        <div class="legend-bar">
            <span class="legend-item"><span class="legend-box" style="background:#fef08a; border:1px solid #ca8a04;"></span> Target Cell: DP[i][j]</span>
            <span class="legend-item"><span class="legend-box" style="background:#bfdbfe; border:1px solid #2563eb;"></span> Exclude Ref: DP[i-1][j]</span>
            <span class="legend-item"><span class="legend-box" style="background:#ede9fe; border:1px solid #7c3aed;"></span> Include Ref: DP[i-1][j - w_i]</span>
            <span class="legend-item"><span class="legend-box" style="background:#bbf7d0; border:1px solid #16a34a;"></span> Optimal Traceback Path</span>
        </div>
        """)

    with col_analysis:
        if curr_k < 0:
            with st.container(border=True):
                st.caption("PHASE 0: BASE CASE INITIALIZATION")
                st.markdown("""
                **Definition of Base Cases:**
                - `DP[0][j] = 0` for all `0 ≤ j ≤ W`: With zero candidate items available, maximum value is strictly 0.
                - `DP[i][0] = 0` for all `0 ≤ i ≤ n`: When knapsack capacity is 0, no item can be carried, yielding total value 0.
                """)
                st.info("Click **Next ▶** or **▶ Auto Play** to begin subproblem computation.")

        elif steps[curr_k]["type"] == "FILL":
            st_data = steps[curr_k]
            cur_i = st_data["i"]
            cur_j = st_data["j"]
            w_i = st_data["weight"]
            v_i = st_data["value"]
            fits = st_data["fits"]
            skip_v = st_data["skip_val"]
            take_v = st_data["take_val"]
            chosen = st_data["chosen_val"]

            exclude_selected = (not fits) or (chosen == skip_v and take_v <= skip_v)
            include_selected = fits and (chosen == take_v)

            if not fits:
                formula_eval = f"DP[{cur_i}][{cur_j}] = DP[{cur_i - 1}][{cur_j}] = {chosen}"
            else:
                formula_eval = f"DP[{cur_i}][{cur_j}] = max( {skip_v}, {v_i} + {take_v - v_i} ) = {chosen}"

            with st.container(border=True):
                st.caption(f"SUBPROBLEM STATE: DP[{cur_i}][{cur_j}]")
                st.markdown(f"Evaluating candidate **Item {cur_i}**: Weight = `{w_i}`, Value = `{v_i}` under sub-capacity `j = {cur_j}`.")

                b1_col, b2_col = st.columns(2)

                with b1_col:
                    with st.container(border=True):
                        if exclude_selected:
                            st.markdown(":blue[**BRANCH 1: EXCLUDE**] `[CHOSEN]`")
                        else:
                            st.markdown("**BRANCH 1: EXCLUDE**")
                        st.metric("Exclude Value", f"DP[{cur_i - 1}][{cur_j}] = {skip_v}")
                        st.caption(f"Preserves capacity for first {cur_i - 1} items.")

                with b2_col:
                    with st.container(border=True):
                        if not fits:
                            st.markdown(":red[**BRANCH 2: INCLUDE**] `[INFEASIBLE]`")
                            st.metric("Capacity Deficit", f"{w_i - cur_j} over cap")
                            st.caption(f"Item weight ({w_i}) exceeds capacity ({cur_j}).")
                        else:
                            if include_selected:
                                st.markdown(":violet[**BRANCH 2: INCLUDE**] `[CHOSEN]`")
                            else:
                                st.markdown("**BRANCH 2: INCLUDE**")
                            st.metric("Include Value", f"{v_i} + DP[{cur_i - 1}][{cur_j - w_i}] = {take_v}")
                            st.caption(f"Gains {v_i}; solves subproblem for remaining cap ({cur_j - w_i}).")

                st.info(f"**Recurrence Decision:** `{formula_eval}`")

        elif steps[curr_k]["type"] == "TRACEBACK":
            tb = steps[curr_k]
            it_idx = tb["item_index"]
            inc = tb["included"]
            w_i = tb["weight"]
            v_i = tb["value"]
            curr_v = tb["curr_val"]
            abv_v = tb["above_val"]
            nxt = tb["next_coord"]

            with st.container(border=True):
                st.caption(f"PHASE 2: TRACEBACK VERIFICATION (ITEM {it_idx})")
                if inc:
                    st.success(f"""
                    **ITEM {it_idx} WAS INCLUDED:**
                    - Cell value `DP[{tb['i']}][{tb['j']}] = {curr_v}` differs from `DP[{tb['i'] - 1}][{tb['j']}] = {abv_v}`.
                    - This confirms Item {it_idx} was selected into the optimal subset.
                    - Deduct weight: `{tb['j']} - {w_i} = {nxt[1]}`. Jump to coordinate `({nxt[0]}, {nxt[1]})`.
                    """)
                else:
                    st.info(f"""
                    **ITEM {it_idx} WAS EXCLUDED:**
                    - Cell value `DP[{tb['i']}][{tb['j']}] = {curr_v}` equals cell directly above `DP[{tb['i'] - 1}][{tb['j']}] = {abv_v}`.
                    - The optimal solution does not include Item {it_idx}.
                    - Capacity remains `{tb['j']}`. Move up to row `{nxt[0]}`.
                    """)

        else:
            term = steps[curr_k]
            tot_w = term["total_weight"]
            opt_v = term["optimal_value"]
            sel = term["selected_items"]
            items_str = ", ".join(f"Item {idx}" for idx in sel) if sel else "None"

            with st.container(border=True):
                st.caption("PHASE 3: OPTIMAL SOLUTION SUMMARY")
                st.metric("Optimal Knapsack Value", f"{opt_v}")
                st.markdown(f"""
                - **Selected Subset:** **{items_str}**
                - **Total Weight Consumed:** **{tot_w} / {capacity}** ({round(tot_w / capacity * 100, 1)}% efficiency)
                - **Residual Knapsack Capacity:** **{capacity - tot_w}**
                """)

        st.markdown("#### Item Specification Table")
        current_taken = set()
        if curr_k >= 0:
            for s in steps[:curr_k + 1]:
                if s["type"] == "TRACEBACK" and s["included"]:
                    current_taken.add(s["item_index"])

        inventory_rows = [
            {
                "Item": f"Item {idx}",
                "Weight (w_i)": w,
                "Value (v_i)": v,
                "Ratio (v_i / w_i)": round(v / w, 2),
                "Traceback Status": "SELECTED [✓]" if idx in current_taken else "Pending / Excluded"
            }
            for idx, (w, v) in enumerate(zip(weights, values), start=1)
        ]
        st.dataframe(inventory_rows, use_container_width=True, hide_index=True)

    if st.session_state.get('is_playing', False):
        if curr_k < total_steps - 1:
            time.sleep(speed_delay)
            st.session_state.active_step += 1
            st.rerun()
        else:
            st.session_state.is_playing = False
            st.rerun()


# Tab 2: Mathematical Foundation

with tab_math:
    st.markdown("### Formal Dynamic Programming Formulation")

    st.markdown("""
    The **0/1 Knapsack Problem** is a constrained combinatorial optimization problem. Given $n$ items, each with weight $w_i \in \mathbb{Z}^+$ and value $v_i \in \mathbb{Z}^+$, and a total knapsack capacity $W \in \mathbb{Z}^+$, determine a binary decision vector $x \in \{0, 1\}^n$ such that:
    """)

    st.latex(r"""
    \max \sum_{i=1}^n v_i x_i \quad \text{subject to} \quad \sum_{i=1}^n w_i x_i \le W, \quad x_i \in \{0, 1\}
    """)

    st.markdown("---")
    st.markdown("### Bellman Recurrence Equation")

    st.markdown("""
    Let $DP[i, j]$ denote the maximum value achievable considering a subset of the first $i$ items with capacity $j$, where $0 \le i \le n$ and $0 \le j \le W$.
    """)

    st.latex(r"""
    DP[i, j] = 
    \begin{cases} 
      0 & \text{if } i = 0 \text{ or } j = 0 \\
      DP[i - 1, j] & \text{if } w_i > j \\
      \max\Big( DP[i - 1, j], \; v_i + DP[i - 1, j - w_i] \Big) & \text{if } w_i \le j
    \end{cases}
    """)

    st.markdown("---")
    st.markdown("### Two Fundamental Principles of Dynamic Programming")

    c_p1, c_p2 = st.columns(2)
    with c_p1:
        st.markdown("""
        #### 1. Optimal Substructure
        An optimal solution to the problem contains optimal solutions to subproblems:
        - If item $i$ is not included in the optimal solution for capacity $j$, the optimal solution is identically $DP[i-1, j]$.
        - If item $i$ is included, the remaining items $1 \dots i-1$ must form the optimal solution for residual capacity $j - w_i$.
        """)

    with c_p2:
        st.markdown("""
        #### 2. Overlapping Subproblems
        The recursive space involves evaluating the same subproblem coordinates $(i, j)$ repeatedly across various branch paths.
        - Rather than incurring exponential $O(2^n)$ cost with naive recursion, the bottom-up table memoizes each subproblem result exactly once in $O(1)$ operations.
        """)

    st.markdown("---")
    st.markdown("### Complexity Analysis")
    st.markdown("""
    | Metric | Complexity | Notes |
    | :--- | :--- | :--- |
    | **Time Complexity** | $\mathcal{O}(n \cdot W)$ | Pseudo-polynomial time; dependent on the numeric value of $W$, not the length of its binary representation. |
    | **Space Complexity** | $\mathcal{O}(n \cdot W)$ | Full matrix required for solution backtracking. Can be optimized to $\mathcal{O}(W)$ if only value is needed. |
    | **Backtracking Time**| $\mathcal{O}(n)$ | Tracing back from $(n, W)$ takes at most $n$ comparison steps. |
    """)


# Tab 3: DP vs Greedy Analysis

with tab_greedy:
    st.markdown("### Algorithmic Comparison: Dynamic Programming vs Greedy Heuristic")
    st.markdown("""
    A common misconception in DAA exams is attempting to solve 0/1 Knapsack using the **Greedy approach** (selecting items with highest value-to-weight ratio $v_i / w_i$).
    
    While the greedy approach yields the optimal solution for the **Fractional Knapsack** problem, it often fails for **0/1 Knapsack** because items cannot be divided.
    """)

    g_val, g_items, items_sorted = compute_greedy_heuristic(weights, values, capacity)
    dp_val = dp[len(weights)][capacity]
    dp_items = st.session_state.optimal_subset

    col_g1, col_g2, col_g3 = st.columns(3)
    with col_g1:
        st.metric(
            label="DP Optimal Value",
            value=f"{dp_val}",
            help="Guaranteed global optimum produced by bottom-up Dynamic Programming."
        )
    with col_g2:
        st.metric(
            label="Greedy Heuristic Value",
            value=f"{g_val}",
            delta=f"{g_val - dp_val}" if g_val != dp_val else "Matches DP (Rare)",
            delta_color="normal"
        )
    with col_g3:
        optimality_gap = round((1 - g_val / dp_val) * 100, 2) if dp_val > 0 else 0
        st.metric(
            label="Optimality Gap",
            value=f"{optimality_gap}%",
            help="Percentage loss in value incurred by greedy choice."
        )

    st.markdown("#### Item Density Ordering (Sorted by $v_i / w_i$)")
    density_table_data = [
        {
            "Item": f"Item {it['id']}",
            "Weight (w_i)": it["weight"],
            "Value (v_i)": it["value"],
            "Density (v_i / w_i)": round(it["ratio"], 3),
            "Greedy Decision": "CHOSEN [✓]" if it["id"] in g_items else "SKIPPED",
            "DP Optimal Decision": "CHOSEN [✓]" if it["id"] in dp_items else "SKIPPED"
        }
        for it in items_sorted
    ]
    st.dataframe(density_table_data, use_container_width=True, hide_index=True)

    st.markdown("""
    > **Theoretical Insight:**  
    > The greedy heuristic fails because taking a high-density item can leave unused knapsack capacity that cannot accommodate any remaining item. Dynamic Programming evaluates the global trade-off between packing fewer high-density items vs combinations of lower-density items that pack the knapsack more tightly.
    """)


# Tab 4: Lab Implementations

with tab_code:
    st.markdown("### Lab-Ready Multi-Language Implementations")

    code_lang = st.radio(
        "Target Programming Language",
        ["Python 3", "C++ (Standard STL)", "Java (Standard BCA Class)", "C (ANSI C)"],
        horizontal=True
    )

    if code_lang == "Python 3":
        st.code("""
def knapsack_01(weights: list[int], values: list[int], capacity: int):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi, vi = weights[i - 1], values[i - 1]
        for j in range(1, capacity + 1):
            if wi > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], vi + dp[i - 1][j - wi])

    chosen_items = []
    curr_i, curr_j = n, capacity
    while curr_i > 0 and curr_j > 0:
        if dp[curr_i][curr_j] != dp[curr_i - 1][curr_j]:
            chosen_items.append(curr_i)
            curr_j -= weights[curr_i - 1]
        curr_i -= 1

    chosen_items.reverse()
    return dp[n][capacity], chosen_items

w = [1, 3, 4, 5]
v = [1, 4, 5, 7]
cap = 7
max_val, items = knapsack_01(w, v, cap)
print(f"Optimal Value: {max_val}, Items: {items}")
        """, language="python")

    elif code_lang == "C++ (Standard STL)":
        st.code("""
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct KnapsackResult {
    int max_value;
    vector<int> selected_items;
};

KnapsackResult knapsack01(const vector<int>& weights, const vector<int>& values, int W) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; ++i) {
        int wi = weights[i - 1];
        int vi = values[i - 1];
        for (int j = 1; j <= W; ++j) {
            if (wi > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], vi + dp[i - 1][j - wi]);
            }
        }
    }

    vector<int> selected;
    int curr_i = n, curr_j = W;
    while (curr_i > 0 && curr_j > 0) {
        if (dp[curr_i][curr_j] != dp[curr_i - 1][curr_j]) {
            selected.push_back(curr_i);
            curr_j -= weights[curr_i - 1];
        }
        curr_i--;
    }
    reverse(selected.begin(), selected.end());

    return {dp[n][W], selected};
}

int main() {
    vector<int> weights = {1, 3, 4, 5};
    vector<int> values = {1, 4, 5, 7};
    int W = 7;

    KnapsackResult res = knapsack01(weights, values, W);
    cout << "Optimal Value: " << res.max_value << endl;
    cout << "Selected Items: ";
    for (int item_id : res.selected_items) cout << item_id << " ";
    cout << endl;

    return 0;
}
        """, language="cpp")

    elif code_lang == "Java (Standard BCA Class)":
        st.code("""
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Knapsack01 {
    public static void solve(int[] weights, int[] values, int W) {
        int n = weights.length;
        int[][] dp = new int[n + 1][W + 1];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= W; j++) {
                if (weights[i - 1] > j) {
                    dp[i][j] = dp[i - 1][j];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]]);
                }
            }
        }

        System.out.println("Maximum Value: " + dp[n][W]);

        List<Integer> chosen = new ArrayList<>();
        int currI = n, currJ = W;
        while (currI > 0 && currJ > 0) {
            if (dp[currI][currJ] != dp[currI - 1][currJ]) {
                chosen.add(currI);
                currJ -= weights[currI - 1];
            }
            currI--;
        }
        Collections.reverse(chosen);

        System.out.println("Selected Items: " + chosen);
    }

    public static void main(String[] args) {
        int[] weights = {1, 3, 4, 5};
        int[] values  = {1, 4, 5, 7};
        int capacity = 7;

        solve(weights, values, capacity);
    }
}
        """, language="java")

    else:
        st.code("""
#include <stdio.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

void knapsack(int W, int weights[], int values[], int n) {
    int dp[n + 1][W + 1];

    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            if (i == 0 || j == 0) {
                dp[i][j] = 0;
            } else if (weights[i - 1] <= j) {
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]]);
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    printf("Optimal Value: %d\\n", dp[n][W]);

    printf("Selected Items: ");
    int curr_i = n, curr_j = W;
    while (curr_i > 0 && curr_j > 0) {
        if (dp[curr_i][curr_j] != dp[curr_i - 1][curr_j]) {
            printf("Item %d ", curr_i);
            curr_j -= weights[curr_i - 1];
        }
        curr_i--;
    }
    printf("\\n");
}

int main() {
    int weights[] = {1, 3, 4, 5};
    int values[]  = {1, 4, 5, 7};
    int capacity = 7;
    int n = sizeof(values) / sizeof(values[0]);

    knapsack(capacity, weights, values, n);
    return 0;
}
        """, language="c")


# Tab 5: Exam & Viva Guide

with tab_viva:
    st.markdown("### DAA Examination Revision & Viva Guide")

    v1_col, v2_col = st.columns(2)

    with v1_col:
        with st.container(border=True):
            st.markdown("**Q1: Why does Greedy fail for 0/1 Knapsack but work for Fractional Knapsack?**")
            st.markdown("""
            In **Fractional Knapsack**, items can be broken down continuously. Taking the highest value density ($v_i / w_i$) is guaranteed to pack the knapsack with maximum value per weight unit.
            
            In **0/1 Knapsack**, items are indivisible ($x_i \in \{0, 1\}$). Taking a high-density item can leave unused slack capacity that cannot fit any remaining item. A combination of slightly lower-density items that pack the capacity completely can yield a strictly higher total value.
            """)

        with st.container(border=True):
            st.markdown("**Q2: What are the two core prerequisites for Dynamic Programming?**")
            st.markdown("""
            1. **Optimal Substructure:** The globally optimal solution to the problem is composed of optimal solutions to its constituent subproblems.
            2. **Overlapping Subproblems:** The recursive problem-solving tree evaluates the exact same state coordinates $(i, j)$ repeatedly across different paths, which enables efficient memoization or table lookup in $\\mathcal{O}(1)$ time.
            """)

    with v2_col:
        with st.container(border=True):
            st.markdown("**Q3: What is the difference between 0/1 Knapsack and Unbounded Knapsack?**")
            st.markdown("""
            - **0/1 Knapsack:** Each item can be chosen at most once ($x_i \in \{0, 1\}$). The transition references row $i-1$:  
              $$DP[i, j] = \\max(DP[i-1, j], \\; v_i + DP[i-1, j - w_i])$$
            - **Unbounded Knapsack:** Each item can be chosen multiple times ($x_i \in \{0, 1, 2, \\dots\}$). The transition references the **current** item state $i$ again:  
              $$DP[i, j] = \\max(DP[i-1, j], \\; v_i + DP[i, j - w_i])$$
            """)

        with st.container(border=True):
            st.markdown("**Q4: Summary Comparison Table (BCA DAA Exam Reference)**")
            st.markdown("""
            | Problem Variant | Paradigm | Item Divisibility | Time Complexity | Optimality Guarantee |
            | :--- | :--- | :--- | :--- | :--- |
            | **Fractional Knapsack** | Greedy Method | Divisible ($0 \\le x_i \\le 1$) | $\\mathcal{O}(n \\log n)$ | Globally Optimal |
            | **0/1 Knapsack** | Dynamic Programming | Indivisible ($x_i \\in \\{0, 1\\}$) | $\\mathcal{O}(n \\cdot W)$ | Globally Optimal |
            | **Unbounded Knapsack** | Dynamic Programming | Indivisible, multiple copies | $\\mathcal{O}(n \\cdot W)$ | Globally Optimal |
            """)


# Academic & Algorithmic Learning Reference

st.markdown("---")
st.markdown("## Academic & Algorithmic Learning Reference")
st.caption("Complete theoretical study guide, pseudocode standards, complexity derivations, and multi-language lab implementations for Design & Analysis of Algorithms (DAA).")

ref_col1, ref_col2 = st.columns(2)

with ref_col1:
    with st.container(border=True):
        st.markdown("### 1. Procedural Algorithm Specification")
        st.markdown("""
        The **0/1 Knapsack Problem** via Dynamic Programming proceeds through four formal stages:

        1. **State Definition:**  
           Define subproblem $DP[i, j]$ as the maximum value achievable using a subset of the first $i$ items ($1 \le i \le n$) under sub-capacity $j$ ($0 \le j \le W$).
        
        2. **Base Case Initialization:**  
           Set $DP[0, j] = 0$ for all $j \in [0, W]$ (0 candidate items available) and $DP[i, 0] = 0$ for all $i \in [0, n]$ (0 capacity available).

        3. **Bottom-Up State Transitions:**  
           Iterate row-wise ($i = 1 \dots n$) and column-wise ($j = 1 \dots W$):
           - If item weight exceeds capacity ($w_i > j$): Item $i$ cannot be placed; copy state above:  
             $$DP[i, j] = DP[i-1, j]$$
           - If item fits ($w_i \le j$): Take the maximum of excluding versus including item $i$:  
             $$DP[i, j] = \max\Big( DP[i-1, j], \; v_i + DP[i-1, j - w_i] \Big)$$

        4. **Traceback (Reconstruction):**  
           Start at $(n, W)$. If $DP[i, j] \ne DP[i-1, j]$, item $i$ was included; deduct $w_i$ from $j$ and decrement $i$. Otherwise, item $i$ was excluded; decrement $i$. Repeat until $i = 0$ or $j = 0$.
        """)

with ref_col2:
    with st.container(border=True):
        st.markdown("### 2. Standard Pseudocode (CLRS Textbook Style)")
        st.code("""
ALGORITHM Knapsack01(W, weights, values, n)
// Input: Knapsack capacity W, weights[1..n], values[1..n], item count n
// Output: DP table of size (n+1) x (W+1) with optimal value at DP[n, W]

for j = 0 to W do
    DP[0, j] = 0
end for

for i = 1 to n do
    DP[i, 0] = 0
    for j = 1 to W do
        if weights[i] > j then
            DP[i, j] = DP[i - 1, j]
        else
            DP[i, j] = max( DP[i - 1, j], 
                            values[i] + DP[i - 1, j - weights[i]] )
        end if
    end for
end for

return DP[n, W]
        """, language="text")

        st.markdown("#### Traceback Pseudocode")
        st.code("""
ALGORITHM TracebackKnapsack(DP, weights, n, W)
// Input: Computed DP matrix, weights[1..n], n, W
// Output: Array S of selected item indices

S = empty list
i = n
j = W

while i > 0 and j > 0 do
    if DP[i, j] != DP[i - 1, j] then
        S.append(i)
        j = j - weights[i]
    end if
    i = i - 1
end while

return reversed(S)
        """, language="text")

opt_c1, opt_c2 = st.columns(2)

with opt_c1:
    with st.container(border=True):
        st.markdown("#### The 1D Space-Optimization Technique: $\\mathcal{O}(W)$")
        st.markdown("""
        Notice that computing row $i$ only requires values from the immediate previous row $i-1$. Therefore, we do not need to preserve all $n+1$ rows if only the maximum value is required.
        
        We can compress the table into a single 1D array of size $W+1$:
        - **Critical Rule:** The inner capacity loop **MUST run backwards** from $W$ down to $w_i$.
        - **Why backwards?** If traversed forward ($j = w_i \to W$), values updated earlier in the current iteration would be reused, which solves the **Unbounded Knapsack Problem** (allowing unlimited item reuse) rather than the **0/1 Knapsack Problem**!
        """)
        st.code("""
def knapsack_1d(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], v + dp[j - w])
    return dp[W]
        """, language="python")

with opt_c2:
    with st.container(border=True):
        st.markdown("#### Asymptotic Complexity Derivations")
        st.markdown("""
        ##### Time Complexity Derivation:
        - The nested loops iterate $n$ times for items and $W$ times for capacities.
        - Inside each iteration, table lookup and maximum evaluation take constant time $\\mathcal{O}(1)$.
        - Overall Time: $\\sum_{i=1}^n \\sum_{j=1}^W \\mathcal{O}(1) = \\mathbf{\\mathcal{O}(n \\cdot W)}$.
        - **Pseudo-Polynomial Time:** $W$ represents the *magnitude* of the capacity, not the length of its binary encoding ($k = \\lfloor \\log_2 W \\rfloor + 1$). In terms of input bits $k$, the time is $\\mathcal{O}(n \\cdot 2^k)$, which is exponential with respect to input length. Hence, 0/1 Knapsack is **weakly NP-complete**.

        ##### Space Complexity:
        - **Standard 2D Matrix:** $\\mathcal{O}(n \\cdot W)$ space, required when full traceback/path recovery is needed.
        - **1D Space Optimized:** $\\mathcal{O}(W)$ space, when only the maximum attainable value is required.
        """)
