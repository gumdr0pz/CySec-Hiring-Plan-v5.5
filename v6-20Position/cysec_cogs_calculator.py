#!/usr/bin/env python3
"""
CySec BU - COGS Calculator (v6 — General roles, HR levels, Rate-card benchmark)
Salary benchmark = "Monthly Salary (Ref)" from Consultant Rate card v1.6 (Rate tab).
Burdened = benchmark x 1.44 (COGS multiplier retained). 20 hires, 8-5-7 waves.
"""

COGS_MULTIPLIER = 1.44
REVENUE_TARGET = 12_000_000

# HR job levels -> monthly benchmark range (RM), from the Rate tab
LEVELS = {
    'L1': {'name': 'Executive / Engineer',           'min': 4000,  'max': 7000},
    'L3': {'name': 'Senior Executive / Sr Engineer', 'min': 8000,  'max': 11000},
    'L4': {'name': 'Specialist / Staff Engineer',    'min': 11500, 'max': 15500},
    'L5': {'name': 'Manager / Sr Staff Engineer',    'min': 17500, 'max': 20400},
}

# Role mapping (v6): (title, function, level, general 'G' / cyber-core 'C')
WAVES = {
    'Wave 1': [
        ('Solutions Architect',                  'Solutions/Presales', 'L4', 'G'),
        ('Presales Engineer',                    'Solutions/Presales', 'L1', 'G'),
        ('Consultant - Government Security',     'Gov Sec',            'L4', 'C'),
        ('GRC Specialist',                       'VORON/GRC',          'L4', 'C'),
        ('Staff Engineer - DevSecOps',           'DevSecOps',          'L4', 'G'),
        ('Engineer - DevSecOps',                 'DevSecOps',          'L1', 'G'),
        ('Technical Account Manager',            'Professional Svcs',  'L3', 'G'),
        ('Product Manager',                      'Product/PM',         'L5', 'G'),
    ],
    'Wave 2': [
        ('Account Manager - Enterprise',         'Sales',              'L5', 'G'),
        ('Account Manager - Government',         'Sales',              'L5', 'G'),
        ('Team Lead - Offensive Security',       'OffSec',             'L4', 'C'),
        ('Staff Engineer - Offensive Security',  'OffSec',             'L4', 'C'),
        ('Team Lead - Threat Intelligence',      'CTI',                'L4', 'C'),
    ],
    'Wave 3': [
        ('Staff Engineer - Blockchain',          'Blockchain',         'L4', 'G'),
        ('GRC Analyst',                          'VORON/GRC',          'L1', 'C'),
        ('Engineer - Offensive Security',        'OffSec',             'L1', 'C'),
        ('Senior Engineer - Threat Intelligence','CTI',                'L3', 'C'),
        ('Engineer - Threat Intelligence (TI)',  'CTI',                'L1', 'C'),
        ('Engineer - Threat Intelligence (DI)',  'CTI',                'L1', 'C'),
        ('Business Analyst',                     'Product/PM',         'L1', 'G'),
    ],
}

YEAR1_ACTIVE_MONTHS = {'Wave 1': 10, 'Wave 2': 5, 'Wave 3': 1}


def annual_burdened(level, use_min=True):
    m = LEVELS[level]['min'] if use_min else LEVELS[level]['max']
    return m * COGS_MULTIPLIER * 12


def main():
    print("=" * 90)
    print("CySec BU - COGS Calculator (v6 — HR levels + Rate-card benchmark, 20 hires)")
    print("=" * 90)
    print(f"Burdened = benchmark x {COGS_MULTIPLIER}.  Benchmark = Rate tab 'Monthly Salary (Ref)'.")

    total_min = total_max = 0
    wave_b = {}
    for wave, roles in WAVES.items():
        wmin = sum(annual_burdened(l, True) for _, _, l, _ in roles)
        wmax = sum(annual_burdened(l, False) for _, _, l, _ in roles)
        wave_b[wave] = (wmin, wmax)
        print(f"\n{wave} ({len(roles)} roles):")
        print("-" * 90)
        for title, func, lvl, gc in roles:
            tag = 'general' if gc == 'G' else 'cyber-core'
            print(f"  {title:<40} {lvl} {func:<18} {tag:<10} "
                  f"RM{annual_burdened(lvl,True):>9,.0f}-{annual_burdened(lvl,False):>9,.0f}")
        print(f"  {'WAVE ANNUAL (burdened)':<40}{'':32}RM{wmin:>9,.0f}-{wmax:>9,.0f}")
        total_min += wmin
        total_max += wmax

    print("\n" + "=" * 90)
    print("SUMMARY (at full benchmark)")
    print("=" * 90)
    base_min, base_max = total_min / COGS_MULTIPLIER, total_max / COGS_MULTIPLIER
    print(f"Total hires: 20")
    print(f"Annual base salary:      RM{base_min:,.0f} - RM{base_max:,.0f}  "
          f"({base_min/REVENUE_TARGET*100:.1f}% - {base_max/REVENUE_TARGET*100:.1f}% of revenue)")
    print(f"Annual burdened (x1.44): RM{total_min:,.0f} - RM{total_max:,.0f}  "
          f"({total_min/REVENUE_TARGET*100:.1f}% - {total_max/REVENUE_TARGET*100:.1f}% of revenue)")
    print(f"\n25% cap (RM3,000,000): BREACHED -> relaxed per decision.")
    print(f"  Revenue needed for max burdened to equal 25%: RM{total_max/0.25:,.0f}")
    print(f"  Implied cap to fit max burdened at RM12M: {total_max/REVENUE_TARGET*100:.0f}%")

    print("\n" + "=" * 90)
    print("36-MONTH BUDGET RUNWAY (estimated, burdened)")
    print("=" * 90)
    y1_min = sum(wave_b[w][0] / 12 * YEAR1_ACTIVE_MONTHS[w] for w in WAVES)
    y1_max = sum(wave_b[w][1] / 12 * YEAR1_ACTIVE_MONTHS[w] for w in WAVES)
    rows = [('Year 1 (phased)', y1_min, y1_max),
            ('Year 2 (full)', total_min, total_max),
            ('Year 3 (full)', total_min, total_max)]
    cmin = cmax = 0
    for label, a, b in rows:
        cmin += a; cmax += b
        print(f"  {label:<18} RM{a:>11,.0f} - RM{b:>11,.0f}   cum(max) RM{cmax:>12,.0f}")
    print(f"  {'36-MONTH TOTAL':<18} RM{cmin:>11,.0f} - RM{cmax:>11,.0f}")


if __name__ == "__main__":
    main()
