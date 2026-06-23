#!/usr/bin/env python3
"""
CySec BU - COGS Calculator (v5.5 — Support-Pod 7-5-8 Structure, 20 Hires)
Based on MSP_Cost_Calculator.xlsx formula: 1.44x multiplier
"""

# COGS Formula Components (from TECH Cost--Burdened sheet)
COGS_MULTIPLIER = 1.44  # 1 + COLA(10%) + EPF(11%) + SOCSO(1.45%) + Health(RM100) + Bonus(10%) + PTO(12hrs)

# Salary Ranges (RM/month) - 30% reduction applied
SALARY_RANGES = {
    'Lead': {'min': 4900, 'max': 7840},
    'Senior': {'min': 4900, 'max': 7840},
    'IC': {'min': 3500, 'max': 5600},
    'Junior': {'min': 3500, 'max': 5600},
    'Junior/Intermediate': {'min': 3500, 'max': 5600},
}

REVENUE_TARGET = 12_000_000
REVENUE_CAP = 0.25 * REVENUE_TARGET  # RM3,000,000

# Wave Structure (v5.5 — 20 hires, 7-5-8)
WAVES = {
    'Wave 1': [
        {'name': 'Presales Consultant', 'level': 'Senior', 'team': 'Sales'},
        {'name': 'Jr Presales Consultant', 'level': 'Junior', 'team': 'Sales'},
        {'name': 'Gov Sec PM', 'level': 'Senior', 'team': 'Cybersecurity'},
        {'name': 'Sr GRC Specialist', 'level': 'Senior', 'team': 'VORON'},
        {'name': 'Sr DevSecOps', 'level': 'Senior', 'team': 'DevSecOps'},
        {'name': 'Jr DevSecOps', 'level': 'Junior', 'team': 'DevSecOps'},
        {'name': 'Technical Account Manager', 'level': 'Junior/Intermediate', 'team': 'Professional Services'},
    ],
    'Wave 2': [
        {'name': 'Sales Specialist (Enterprise)', 'level': 'Senior', 'team': 'Sales'},
        {'name': 'Sales Specialist (Government)', 'level': 'Senior', 'team': 'Sales'},
        {'name': 'Lead Researcher', 'level': 'Lead', 'team': 'OffSec'},
        {'name': 'Red Team', 'level': 'Senior', 'team': 'OffSec'},
        {'name': 'CTI Lead', 'level': 'Lead', 'team': 'CTI'},
    ],
    'Wave 3': [
        {'name': 'Sr Blockchain Dev', 'level': 'Senior', 'team': 'Blockchain'},
        {'name': 'Jr GRC Specialist', 'level': 'Junior', 'team': 'VORON'},
        {'name': 'Jr Researcher', 'level': 'Junior', 'team': 'OffSec'},
        {'name': 'TI Analyst', 'level': 'IC', 'team': 'CTI'},
        {'name': 'TI Researcher', 'level': 'IC', 'team': 'CTI'},
        {'name': 'Dist Intel Analyst', 'level': 'IC', 'team': 'CTI'},
        {'name': 'Business Analyst', 'level': 'IC', 'team': 'PM Team'},
        {'name': 'Jr PM', 'level': 'Junior', 'team': 'PM Team'},
    ],
}

# Year-1 phasing (months each wave is active in the first 12 months)
YEAR1_ACTIVE_MONTHS = {'Wave 1': 10, 'Wave 2': 5, 'Wave 3': 1}
INFLATION = 0.05  # estimated annual salary inflation for the 36-month runway


def monthly_cost(level, use_min=True):
    salary = SALARY_RANGES[level]['min'] if use_min else SALARY_RANGES[level]['max']
    return round(salary * COGS_MULTIPLIER)  # round monthly burdened to nearest RM (matches plan docs)


def wave_monthly(positions, use_min=True):
    return sum(monthly_cost(p['level'], use_min) for p in positions)


def main():
    print("=" * 80)
    print("CySec BU - COGS Calculator (v5.5 — 7-5-8, 20 Hires)")
    print("=" * 80)
    print(f"\nCOGS Multiplier: {COGS_MULTIPLIER}x")
    print("Formula: 1 + COLA(10%) + EPF(11%) + SOCSO(1.45%) + Health(RM100) + Bonus(10%) + PTO(12hrs)")

    total_min = total_max = 0
    wave_annual = {}

    for wave_name, positions in WAVES.items():
        w_min = wave_monthly(positions, True)
        w_max = wave_monthly(positions, False)
        a_min, a_max = w_min * 12, w_max * 12
        wave_annual[wave_name] = (a_min, a_max)

        print(f"\n{wave_name} ({len(positions)} roles):")
        print("-" * 70)
        print(f"{'Position':<32} {'Level':<20} {'Monthly Min':>10} {'Monthly Max':>12}")
        print("-" * 70)
        for p in positions:
            print(f"{p['name']:<32} {p['level']:<20} "
                  f"RM{monthly_cost(p['level'], True):>7,.0f} RM{monthly_cost(p['level'], False):>9,.0f}")
        print("-" * 70)
        print(f"{'Wave Annual':<32} {'':<20} RM{a_min:>7,.0f} RM{a_max:>9,.0f}")
        total_min += a_min
        total_max += a_max

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nTotal Positions to Hire: {sum(len(p) for p in WAVES.values())}")
    print(f"Total Annual Cost (Min): RM{total_min:,.0f}")
    print(f"Total Annual Cost (Max): RM{total_max:,.0f}")
    print(f"\nRevenue Target: RM{REVENUE_TARGET:,.0f}   |   25% Cap: RM{REVENUE_CAP:,.0f}")
    print(f"Cost as % of Revenue: {total_min/REVENUE_TARGET*100:.1f}% – {total_max/REVENUE_TARGET*100:.1f}%")
    print(f"Headroom under cap: RM{REVENUE_CAP-total_max:,.0f} – RM{REVENUE_CAP-total_min:,.0f}")

    # 36-Month Budget Runway (estimated)
    print("\n" + "=" * 80)
    print("36-MONTH BUDGET RUNWAY (ESTIMATED)")
    print("=" * 80)
    print("Year 1 phased onboarding; Years 2-3 full run-rate; revenue flat at RM12M.\n")

    y1_min = sum(wave_annual[w][0] / 12 * YEAR1_ACTIVE_MONTHS[w] for w in WAVES)
    y1_max = sum(wave_annual[w][1] / 12 * YEAR1_ACTIVE_MONTHS[w] for w in WAVES)

    rows = [
        ('Year 1 (phased)', y1_min, y1_max),
        ('Year 2 (full)', total_min, total_max),
        ('Year 3 (full)', total_min, total_max),
    ]
    cum_min = cum_max = 0
    print(f"{'Year':<18} {'Cost Min':>14} {'Cost Max':>14} {'Cum Max':>14}  Cap OK?")
    print("-" * 76)
    for label, c_min, c_max in rows:
        cum_min += c_min
        cum_max += c_max
        ok = "OK" if c_max <= REVENUE_CAP else "OVER"
        print(f"{label:<18} RM{c_min:>11,.0f} RM{c_max:>11,.0f} RM{cum_max:>11,.0f}   {ok}")
    print("-" * 76)
    print(f"{'36-Month Total':<18} RM{cum_min:>11,.0f} RM{cum_max:>11,.0f}")

    rev_36 = REVENUE_TARGET * 3
    print(f"\n36-month cost as % of cumulative revenue (RM{rev_36:,.0f}): "
          f"{cum_min/rev_36*100:.1f}% – {cum_max/rev_36*100:.1f}%")
    print(f"Cumulative headroom under 25% cap (RM{REVENUE_CAP*3:,.0f}): "
          f"RM{REVENUE_CAP*3-cum_max:,.0f} – RM{REVENUE_CAP*3-cum_min:,.0f}")

    # Inflation-adjusted 36-month total
    infl_min = y1_min + total_min * (1 + INFLATION) + total_min * (1 + INFLATION) ** 2
    infl_max = y1_max + total_max * (1 + INFLATION) + total_max * (1 + INFLATION) ** 2
    print(f"\nWith ~{INFLATION*100:.0f}%/yr salary inflation (Years 2-3): "
          f"36-month total RM{infl_min:,.0f} – RM{infl_max:,.0f}")
    print("=" * 80)


if __name__ == "__main__":
    main()
