const BBTwitter = 'https://x.com/Blackbox_agent';
const BBH = (type, props, ...children) =>
  (0, z.jsxs)(type, {
    ...props,
    children: children.length === 1 ? children[0] : children,
  });
function BBLogo() {
  return BBH(
    'span',
    { className: 'logo' },
    BBH(
      'svg',
      { viewBox: '0 0 24 24', width: 23, height: 23, 'aria-hidden': true },
      BBH('path', {
        d: 'M3 7V3h4M17 3h4v4M21 17v4h-4M7 21H3v-4M8 8h8v8H8z',
        stroke: 'currentColor',
        strokeWidth: 1.8,
        fill: 'none',
      }),
    ),
    BBH('span', { className: 'logo__word' }, 'Blackbox'),
  );
}
function BBIdentity() {
  return BBH(
    'section',
    { className: 'ca bb-identity', 'aria-label': 'Bureau designation' },
    BBH('div', { className: 'hazard ca__hazard', 'aria-hidden': true }),
    BBH(
      'div',
      { className: 'wrap ca__inner' },
      BBH(
        'div',
        { className: 'ca__tag' },
        BBH('span', { className: 'ca__label' }, 'BB / 001'),
        BBH('span', { className: 'ca__sym mono' }, 'SOLANA INCIDENT BUREAU'),
      ),
      BBH(
        'div',
        { className: 'bb-identity__stats mono' },
        BBH('span', {}, '09 INVESTIGATORS'),
        BBH('span', {}, '06 CASE FILES'),
        BBH('span', { className: 'c-amber' }, 'EVIDENCE BEFORE ATTRIBUTION'),
      ),
      BBH(
        'a',
        {
          className: 'btn btn--ghost bb-twitter',
          href: BBTwitter,
          'aria-label': 'BLACKBOX on Twitter',
        },
        'Twitter ',
        BBH('span', { 'aria-hidden': true }, '↗'),
      ),
    ),
  );
}
function BBPrinciples() {
  return BBH(
    'div',
    { className: 'qlab-scale panel ticks bb-principles' },
    BBH(
      'div',
      { className: 'qlab-scale__line' },
      BBH('span', { className: 'qlab-label' }, 'THE QUANTUM QUESTION'),
      BBH('p', {}, 'Can a better search reveal the path everyone else missed?'),
    ),
    BBH(
      'div',
      { className: 'bb-principles__grid' },
      ...[
        [
          '01',
          'SEARCH THE SPACE',
          'Explore alternate transaction paths and competing explanations.',
        ],
        [
          '02',
          'TEST THE FIT',
          'Compare each hypothesis against timing, funding, and liquidity evidence.',
        ],
        [
          '03',
          'CHALLENGE THE VERDICT',
          'A shared source is a clue. It is not proof of shared ownership.',
        ],
      ].map(([n, title, text]) =>
        BBH(
          'div',
          { key: n },
          BBH('span', { className: 'mono c-amber' }, n),
          BBH('h4', {}, title),
          BBH('p', {}, text),
        ),
      ),
    ),
    BBH(
      'p',
      { className: 'qlab-caveat' },
      'The quantum lab studies search, uncertainty, and future cryptographic exposure. Wallet attribution still requires independent evidence.',
    ),
  );
}
function BBFuel() {
  const container = (0, y.useRef)(null),
    canvas = (0, y.useRef)(null);
  g_(container, canvas, b_('#22c55e', 24, true, false));
  const steps = [
    ['01 · intake', 'Signals', '128', 'case records'],
    ['02 · trace', 'Wallets', '23', 'linked aliases'],
    ['03 · challenge', 'Review', '09', 'specialists'],
    ['04 · archive', 'Evidence', '12', 'published notes'],
    ['05 · compute', 'Capacity', '84%', 'allocated resources'],
    ['06 · bureau', 'Agents', '09', 'ready to investigate'],
  ];
  return BBH(
    'section',
    { className: 'section fuel', id: 'fuel', 'data-health': 'running' },
    BBH(
      'div',
      { className: 'wrap' },
      BBH(pm, {
        index: '06',
        label: 'Bureau fuel',
        title: BBH(
          z.Fragment,
          {},
          'Keep the ',
          BBH('em', {}, 'investigation moving'),
        ),
        lede: 'Evidence is the input. Clarity is the output. The bureau routes its resources through one shared investigation pipeline.',
      }),
      BBH(
        fm,
        {},
        BBH(
          'div',
          { className: 'fuel-line panel ticks' },
          BBH(
            'div',
            { className: 'fuel-line__bar mono' },
            BBH(
              'h3',
              { className: 'fuel-line__state', 'data-tone': 'running' },
              BBH('span', { className: 'dot pulse' }),
              'Bureau pipeline · Operational',
            ),
            BBH('span', { className: 'fuel-line__right' }, 'SOLANA / BLACKBOX'),
          ),
          BBH(
            'div',
            { className: 'fuel-line__body', ref: container },
            BBH('canvas', {
              className: 'fuel-line__canvas',
              ref: canvas,
              'aria-hidden': true,
            }),
            BBH(
              'ol',
              { className: 'fuel-stations' },
              ...steps.map(([n, title, value, sub], i) =>
                BBH(
                  'li',
                  {
                    className: 'fuel-st',
                    key: n,
                    'data-kind':
                      i === 2 ? 'gate' : i === 5 ? 'agents' : undefined,
                  },
                  BBH('span', { className: 'fuel-st__n mono' }, n),
                  BBH('span', {
                    className:
                      'fuel-st__port' +
                      (i === 2
                        ? ' fuel-st__port--gate'
                        : i === 5
                          ? ' fuel-st__port--agents'
                          : ''),
                    'data-port': true,
                  }),
                  BBH('h4', { className: 'fuel-st__name' }, title),
                  BBH('span', { className: 'fuel-st__val' }, value),
                  BBH('span', { className: 'fuel-st__sub mono' }, sub),
                ),
              ),
            ),
          ),
        ),
      ),
      BBH(
        'div',
        { className: 'bb-fuel-grid' },
        BBH(
          fm,
          {},
          BBH(
            'div',
            { className: 'fuel-gauge panel ticks' },
            BBH(
              'h3',
              { className: 'fuel-card__label mono' },
              BBH('span', { className: 'dot' }),
              'Bureau capacity',
            ),
            BBH(
              'div',
              { className: 'fuel-gauge__dial' },
              BBH(
                'svg',
                {
                  viewBox: '0 0 260 150',
                  role: 'img',
                  'aria-label': 'Bureau capacity: 84 percent',
                },
                BBH('path', { d: w_, className: 'fuel-gauge__track' }),
                BBH('path', {
                  d: w_,
                  className: 'fuel-gauge__fill',
                  pathLength: 100,
                  strokeDasharray: '84 100',
                }),
                ...T_.map(([v, label]) => {
                  const point = E_(Fp(v), 110);
                  return BBH('circle', {
                    key: v,
                    cx: point.x,
                    cy: point.y,
                    r: 2,
                    fill: '#777',
                  });
                }),
                BBH('line', {
                  x1: 130,
                  y1: 128,
                  x2: 209,
                  y2: 79,
                  className: 'bb-gauge-needle',
                }),
                BBH('circle', { cx: 130, cy: 128, r: 5, fill: '#22c55e' }),
              ),
              BBH(
                'div',
                { className: 'fuel-gauge__read' },
                BBH('span', { className: 'fuel-gauge__big' }, '84%'),
                BBH(
                  'span',
                  { className: 'fuel-gauge__note mono' },
                  'RESOURCES ALLOCATED',
                ),
              ),
            ),
            BBH(
              'p',
              { className: 'mono muted' },
              'One shared engine. Nine independent perspectives.',
            ),
          ),
        ),
        BBH(
          fm,
          { delay: 0.06 },
          BBH(
            'div',
            { className: 'fuel-rules panel ticks bb-rules' },
            BBH(
              'h3',
              { className: 'fuel-card__label mono' },
              BBH('span', { className: 'dot' }),
              'Bureau protocol',
            ),
            BBH(
              'ol',
              {},
              ...[
                'Preserve the trail. Keep evidence attached to its case.',
                'Separate observation from inference. Timing alone is not ownership.',
                'Challenge the strongest explanation before publishing it.',
                'Keep the unknowns visible. Confidence is earned, never assumed.',
                'Follow the money. Let the evidence choose the next question.',
              ].map((text, i) =>
                BBH(
                  'li',
                  { key: i },
                  BBH(
                    'span',
                    { className: 'fuel-rules__n mono' },
                    String(i + 1).padStart(2, '0'),
                  ),
                  BBH('span', {}, text),
                ),
              ),
            ),
          ),
        ),
      ),
    ),
  );
}
function BBFooter() {
  return BBH(
    'footer',
    { className: 'ftr', id: 'footer' },
    BBH('div', { className: 'hazard', 'aria-hidden': true }),
    BBH(
      'div',
      { className: 'wrap ftr__inner' },
      BBH(
        fm,
        {},
        BBH(
          'p',
          { className: 'ftr__motto' },
          'Follow the money. ',
          BBH('span', { className: 'c-amber' }, 'Question the story.'),
        ),
      ),
      BBH(
        'div',
        { className: 'ftr__cols' },
        BBH(
          'div',
          { className: 'ftr__col' },
          BBH('div', { className: 'ftr__h mono' }, 'The bureau'),
          BBH(
            'p',
            {},
            'BLACKBOX is Solana’s autonomous incident bureau. Nine investigators reconstruct unusual activity, challenge competing explanations, and preserve the evidence.',
          ),
        ),
        BBH(
          'div',
          { className: 'ftr__col' },
          BBH('div', { className: 'ftr__h mono' }, 'Navigate'),
          BBH(
            'ul',
            {},
            ...I_.map(([href, label]) =>
              BBH('li', { key: href }, BBH('a', { href }, label)),
            ),
          ),
        ),
        BBH(
          'div',
          { className: 'ftr__col' },
          BBH('div', { className: 'ftr__h mono' }, 'Stay in the loop'),
          BBH(
            'p',
            {},
            'Every transaction leaves evidence. Every case starts with a question.',
          ),
          BBH(
            'a',
            { className: 'btn btn--ghost bb-footer-twitter', href: BBTwitter },
            'Twitter ↗',
          ),
        ),
      ),
    ),
    BBH(
      'div',
      { className: 'ftr__mark', 'aria-hidden': true },
      BBH('span', { className: 'ftr__word' }, 'Blackbox'),
    ),
    BBH(
      'div',
      { className: 'wrap ftr__base mono' },
      BBH('span', {}, 'BLACKBOX © 2026 · SOLANA INCIDENT BUREAU'),
      BBH('a', { href: '#top' }, 'Back to top ↑'),
    ),
  );
}

function BBCaseId() {
  return location.hash.startsWith('#case/')
    ? decodeURIComponent(location.hash.slice(6))
    : 'echo-launch';
}
function BBNavigateCase(id, scroll = true) {
  history.pushState(null, '', '#case/' + encodeURIComponent(id));
  window.dispatchEvent(new Event('blackbox:case'));
  if (scroll) {
    document
      .getElementById('case-files')
      ?.scrollIntoView({
        behavior: Ip() ? 'instant' : 'smooth',
        block: 'start',
      });
    requestAnimationFrame(() =>
      document
        .getElementById('bb-dossier-title')
        ?.focus({ preventScroll: true }),
    );
  }
}
function BBCaseLink({ mission, missionId, label }) {
  const id = mission?.id ?? missionId;
  return BBH(
    'a',
    {
      href: '#case/' + id,
      className: 'bb-case-link',
      onClick: (event) => {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey)
          return;
        event.preventDefault();
        BBNavigateCase(id);
      },
    },
    label ?? mission?.title ?? 'Open case dossier ↗',
  );
}
function BBCaseMeta({ mission }) {
  return BBH(
    'div',
    { className: 'bb-case-meta mono' },
    BBH(
      'span',
      { 'data-severity': mission.severity },
      mission.severity + ' severity',
    ),
    BBH('span', {}, mission.confidence + '% confidence'),
    BBH('span', { className: 'muted' }, mission.stage),
  );
}
function BBCases() {
  return BBH(z.Fragment, {}, BBH(cg, {}), BBH(BBDossiers, {}));
}
function BBWalletGraph({ dossier }) {
  const [selected, setSelected] = (0, y.useState)(1);
  const positions = [
    [80, 80],
    [285, 80],
    [80, 230],
    [285, 230],
    [490, 230],
    [490, 80],
  ];
  const edges = dossier.graphEdges;
  const nodeNotes = dossier.graphNotes;
  (0, y.useEffect)(() => setSelected(1), [dossier.id]);
  return BBH(
    'figure',
    { className: 'bb-wallet-graph' },
    BBH(
      'div',
      { className: 'bb-dossier-label mono' },
      'Wallet / evidence graph',
    ),
    BBH(
      'svg',
      {
        viewBox: '0 0 570 300',
        role: 'group',
        'aria-label': dossier.code + ' evidence graph',
      },
      ...edges.map(([from, to], i) =>
        BBH('path', {
          key: 'edge' + i,
          d: `M ${positions[from][0]} ${positions[from][1]} L ${positions[to][0]} ${positions[to][1]}`,
          className:
            'bb-graph-edge' +
            (from === selected || to === selected ? ' is-selected' : '') +
            (to === dossier.unknownNode || from === dossier.unknownNode
              ? ' is-unknown'
              : ''),
        }),
      ),
      ...positions.map(([x, y], i) =>
        BBH(
          'g',
          {
            key: i,
            className:
              'bb-graph-node' +
              (i === selected ? ' is-selected' : '') +
              (i === dossier.unknownNode ? ' is-unknown' : ''),
            transform: `translate(${x} ${y})`,
            role: 'button',
            tabIndex: 0,
            'aria-label': dossier.graph[i],
            'aria-pressed': i === selected,
            onClick: () => setSelected(i),
            onKeyDown: (e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                setSelected(i);
              }
            },
          },
          BBH('circle', { r: 23 }),
          BBH('circle', { r: 7, className: 'bb-node-core' }),
          BBH('text', { y: 44, textAnchor: 'middle' }, dossier.graph[i]),
        ),
      ),
    ),
    BBH(
      'figcaption',
      { 'aria-live': 'polite' },
      BBH('span', { className: 'mono c-amber' }, dossier.graph[selected]),
      BBH('p', {}, nodeNotes[selected]),
    ),
    BBH(
      'div',
      { className: 'bb-graph-legend mono' },
      BBH('span', {}, '— recorded path'),
      BBH('span', {}, '┄ unresolved link'),
      BBH('span', {}, 'Select a node'),
    ),
  );
}
function BBDossiers() {
  const dossiers = Q((s) => s.snap?.dossiers),
    missions = Q((s) => s.snap?.missions),
    events = Q((s) => s.snap?.events);
  const [caseId, setCaseId] = (0, y.useState)(BBCaseId),
    [tab, setTab] = (0, y.useState)('timeline');
  (0, y.useEffect)(() => {
    const change = () => {
      setCaseId(BBCaseId());
      setTab('timeline');
    };
    window.addEventListener('hashchange', change);
    window.addEventListener('popstate', change);
    window.addEventListener('blackbox:case', change);
    return () => {
      window.removeEventListener('hashchange', change);
      window.removeEventListener('popstate', change);
      window.removeEventListener('blackbox:case', change);
    };
  }, []);
  (0, y.useEffect)(() => {
    if (dossiers && location.hash.startsWith('#case/')) {
      document
        .getElementById('case-files')
        ?.scrollIntoView({ behavior: 'instant', block: 'start' });
    }
  }, [!!dossiers]);
  if (!dossiers?.length) return null;
  const dossier = dossiers.find((d) => d.id === caseId) ?? dossiers[0],
    mission = missions.find((m) => m.id === dossier.id);
  const tabs = [
    ['timeline', 'Timeline'],
    ['evidence', 'Evidence'],
    ['hypotheses', 'Hypotheses'],
    ['review', 'Review'],
  ];
  const choose = (id) => BBNavigateCase(id, false);
  const tabKeys = (event, items, index, selector, select) => {
    let next;
    if (event.key === 'ArrowRight') next = (index + 1) % items.length;
    else if (event.key === 'ArrowLeft')
      next = (index - 1 + items.length) % items.length;
    else if (event.key === 'Home') next = 0;
    else if (event.key === 'End') next = items.length - 1;
    else return;
    event.preventDefault();
    select(items[next]);
    requestAnimationFrame(() =>
      document.querySelectorAll(selector)[next]?.focus(),
    );
  };
  const body =
    tab === 'timeline'
      ? BBH(
          'ol',
          { className: 'bb-timeline' },
          ...dossier.timeline.map(([at, title, text, agent], i) =>
            BBH(
              'li',
              { key: title },
              BBH('span', { className: 'bb-timeline__at mono' }, at),
              BBH(
                'div',
                {},
                BBH(
                  'span',
                  { className: 'bb-dossier-label mono' },
                  '0' + (i + 1) + ' / ' + agent,
                ),
                BBH('h4', {}, title),
                BBH('p', {}, text),
              ),
            ),
          ),
        )
      : tab === 'evidence'
        ? BBH(
            'div',
            { className: 'bb-evidence' },
            ...dossier.evidence.map(([title, status, text], i) =>
              BBH(
                'article',
                { key: title },
                BBH(
                  'div',
                  { className: 'bb-evidence__top' },
                  BBH(
                    'span',
                    { className: 'mono muted' },
                    'E-' + String(i + 1).padStart(2, '0'),
                  ),
                  BBH(
                    'span',
                    {
                      className: 'bb-evidence-status mono',
                      'data-status': status,
                    },
                    status,
                  ),
                ),
                BBH('h4', {}, title),
                BBH('p', {}, text),
              ),
            ),
          )
        : tab === 'hypotheses'
          ? BBH(
              'div',
              { className: 'bb-hypotheses' },
              BBH(
                'p',
                { className: 'bb-dossier-help mono' },
                'Evidence fit ranks explanations. These scores are independent and do not sum to 100%.',
              ),
              ...dossier.hypotheses.map(([title, status, text, fit]) =>
                BBH(
                  'article',
                  { key: title },
                  BBH(
                    'div',
                    { className: 'bb-hypothesis__head' },
                    BBH('h4', {}, title),
                    BBH('span', { className: 'mono c-amber' }, fit + '% fit'),
                  ),
                  BBH(
                    'div',
                    { className: 'bb-fit-track', 'aria-hidden': true },
                    BBH('span', { style: { width: fit + '%' } }),
                  ),
                  BBH('span', { className: 'bb-dossier-label mono' }, status),
                  BBH('p', {}, text),
                ),
              ),
            )
          : BBH(
              'div',
              { className: 'bb-review' },
              BBH(
                'span',
                { className: 'bb-dossier-label mono' },
                'Current assessment',
              ),
              BBH('h4', {}, dossier.assessment),
              BBH('p', {}, dossier.impact),
              BBH(
                'div',
                { className: 'bb-review-next' },
                BBH(
                  'span',
                  { className: 'mono c-amber' },
                  'NEXT EVIDENCE REQUEST',
                ),
                BBH('p', {}, dossier.nextQuestion),
              ),
              BBH(
                'h5',
                { className: 'bb-dossier-label mono' },
                'Latest investigator notes',
              ),
              ...(events ?? [])
                .filter((e) => e.missionId === dossier.id)
                .slice(-3)
                .reverse()
                .map((e) =>
                  BBH(
                    'div',
                    { className: 'bb-review-note', key: e.id },
                    BBH('span', { className: 'mono c-amber' }, e.agent),
                    BBH('p', {}, e.text),
                  ),
                ),
            );

  const heading = BBH(
    'div',
    { className: 'bb-dossiers-heading' },
    BBH(
      'div',
      {},
      BBH('p', { className: 'kicker mono' }, 'CASE ARCHIVE'),
      BBH('h2', { className: 't-h2' }, 'Open the ', BBH('em', {}, 'black box')),
    ),
    BBH(
      'p',
      { className: 'lede' },
      'Every case has a trail. Inspect the sequence, test the explanation, and keep the unknowns in view.',
    ),
  );
  const selectors = BBH(
    'div',
    {
      className: 'bb-case-tabs',
      role: 'tablist',
      'aria-label': 'Select a case',
    },
    ...dossiers.map((d, i) =>
      BBH(
        'button',
        {
          type: 'button',
          role: 'tab',
          id: 'bb-case-tab-' + d.id,
          'aria-controls': 'bb-dossier',
          'aria-selected': d.id === dossier.id,
          tabIndex: d.id === dossier.id ? 0 : -1,
          className: 'bb-case-tab',
          key: d.id,
          onClick: () => choose(d.id),
          onKeyDown: (e) =>
            tabKeys(
              e,
              dossiers.map((d) => d.id),
              i,
              '.bb-case-tab',
              choose,
            ),
        },
        BBH('span', { className: 'mono' }, d.code),
        BBH('span', {}, missions.find((m) => m.id === d.id).title),
      ),
    ),
  );
  const header = BBH(
    'header',
    { className: 'bb-dossier-header' },
    BBH(
      'div',
      {},
      BBH(
        'p',
        { className: 'bb-dossier-label mono' },
        dossier.code + ' / ' + mission.stage + ' / LEAD ' + mission.lead,
      ),
      BBH('h3', { id: 'bb-dossier-title', tabIndex: -1 }, mission.title),
      BBH('p', { className: 'bb-dossier-scope mono' }, dossier.scope),
    ),
    BBH(BBCaseMeta, { mission }),
  );
  const summary = BBH(
    'div',
    { className: 'bb-dossier-summary' },
    BBH(
      'div',
      {},
      BBH(
        'span',
        { className: 'bb-dossier-label mono' },
        'Severity · potential impact',
      ),
      BBH('p', {}, dossier.impact),
    ),
    BBH(
      'div',
      {},
      BBH(
        'span',
        { className: 'bb-dossier-label mono' },
        'Confidence · strength of the explanation',
      ),
      BBH('p', {}, dossier.assessment),
    ),
  );
  const detailTabs = BBH(
    'div',
    {
      className: 'bb-detail-tabs',
      role: 'tablist',
      'aria-label': 'Dossier sections',
    },
    ...tabs.map(([id, label], i) =>
      BBH(
        'button',
        {
          type: 'button',
          role: 'tab',
          id: 'bb-detail-tab-' + id,
          'aria-controls': 'bb-detail-content',
          'aria-selected': tab === id,
          tabIndex: tab === id ? 0 : -1,
          key: id,
          onClick: () => setTab(id),
          onKeyDown: (e) =>
            tabKeys(
              e,
              tabs.map((t) => t[0]),
              i,
              '.bb-detail-tabs button',
              setTab,
            ),
        },
        label,
      ),
    ),
  );
  const content = BBH(
    'div',
    { className: 'bb-dossier-grid' },
    BBH(
      'div',
      { className: 'bb-dossier-main' },
      detailTabs,
      BBH(
        Y.div,
        {
          key: dossier.id + '/' + tab,
          id: 'bb-detail-content',
          role: 'tabpanel',
          'aria-labelledby': 'bb-detail-tab-' + tab,
          initial: { opacity: 0, y: 8 },
          animate: { opacity: 1, y: 0 },
          transition: { duration: Ip() ? 0 : 0.25 },
          className: 'bb-detail-content',
        },
        body,
      ),
    ),
    BBH(BBWalletGraph, { dossier }),
  );
  const footer = BBH(
    'footer',
    { className: 'bb-dossier-foot mono' },
    BBH('span', {}, 'Keep the chain of custody. Challenge the attribution.'),
    BBH(
      'a',
      { href: '#quantum', className: 'bb-case-link' },
      'Explore reconstruction ↗',
    ),
  );
  return BBH(
    'section',
    {
      className: 'section bb-dossiers',
      id: 'case-files',
      'aria-label': 'Case dossiers',
    },
    BBH(
      'div',
      { className: 'wrap' },
      heading,
      selectors,
      BBH(
        'article',
        {
          className: 'bb-dossier panel ticks',
          id: 'bb-dossier',
          role: 'tabpanel',
          'aria-labelledby': 'bb-case-tab-' + dossier.id,
        },
        header,
        summary,
        content,
        footer,
      ),
    ),
  );
}
function BBReconstructionCases() {
  const dossiers = Q((s) => s.snap?.dossiers);
  if (!dossiers) return null;
  return BBH(
    'div',
    { className: 'bb-reconstruction-cases' },
    BBH(
      'h3',
      { className: 'qlab-label' },
      'How reconstruction changes the case',
    ),
    BBH(
      'div',
      { className: 'bb-reconstruction-grid' },
      ...dossiers
        .filter((d) =>
          ['echo-launch', 'mirror-route', 'silent-vault'].includes(d.id),
        )
        .map((d) =>
          BBH(
            'article',
            { className: 'panel ticks', key: d.id },
            BBH('span', { className: 'mono c-amber' }, d.code),
            BBH('h4', {}, d.reconstruction.result),
            BBH(
              'div',
              { className: 'bb-confidence-shift mono' },
              d.reconstruction.confidenceBefore + '%',
              BBH('span', {}, '→'),
              BBH('b', {}, d.reconstruction.confidenceAfter + '%'),
              BBH('small', {}, 'explanation confidence'),
            ),
            BBH('p', {}, d.reconstruction.question),
            BBH(BBCaseLink, {
              missionId: d.id,
              label: 'Inspect case dossier ↗',
            }),
          ),
        ),
    ),
  );
}
