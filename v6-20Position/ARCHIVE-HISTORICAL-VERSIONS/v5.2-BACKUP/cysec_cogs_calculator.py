#!/usr/bin/env python3
"""
CySec BU - COGS Calculator for 21 Hires
Based on MSP_Cost_Calculator.xlsx formula: 1.44x multiplier
"""

# COGS Formula Components (from TECH Cost--Burdened sheet)
COGS_MULTIPLIER = 1.44  # 1 + COLA(10%) + EPF(11%) + SOCSO(1.45%) + Health(RM100) + Bonus(10%) + PTO(12hrs)

# Salary Ranges (RM/month) - 30% reduction applied
SALARY_RANGES = {
    'Lead': {'min': 4900, 'max': 7840},
    'Senior': {'min': 4900, 'max': 7840},
    'IC': {'min': 3500, 'max': 5600},
    'Junior': {'min': 3500, 'max': 5600}
}

# Wave Structure (21 hires)
WAVES = {
    'Wave 1': [
        {'name': 'Gov Sec PM', 'level': 'Senior', 'team': 'Cybersecurity'},
        {'name': 'Sr Consult', 'level': 'Senior', 'team': 'VORON'},
        {'name': 'Sr DevSecOps', 'level': 'Senior', 'team': 'DevSecOps'},
        {'name': 'PM', 'level': 'Senior', 'team': 'PM Team'},
        {'name': 'Sr PS', 'level': 'Senior', 'team': 'Professional Services'}
    ],
    'Wave 2': [
        {'name': 'Lead Researcher', 'level': 'Lead', 'team': 'OffSec'},
        {'name': 'Red Team', 'level': 'Senior', 'team': 'OffSec'},
        {'name': 'CTI Lead', 'level': 'Lead', 'team': 'CTI'},
        {'name': 'Sr Dev', 'level': 'Senior', 'team': 'Blockchain'},
        {'name': 'Sales Specialist 1', 'level': 'Senior', 'team': 'Sales'},
        {'name': 'Sales Specialist 2', 'level': 'Senior', 'team': 'Sales'},
        {'name': 'Presales Consult', 'level': 'Senior', 'team': 'Sales'}
    ],
    'Wave 3': [
        {'name': 'Jr Consult', 'level': 'Junior', 'team': 'VORON'},
        {'name': 'Jr Researcher', 'level': 'Junior', 'team': 'OffSec'},
        {'name': 'Analyst', 'level': 'IC', 'team': 'CTI'},
        {'name': 'Research', 'level': 'IC', 'team': 'CTI'},
        {'name': 'Dist Intel', 'level': 'IC', 'team': 'CTI'},
        {'name': 'Jr DevSecOps', 'level': 'Junior', 'team': 'DevSecOps'},
        {'name': 'BA', 'level': 'IC', 'team': 'PM Team'},
        {'name': 'Jr PM', 'level': 'Junior', 'team': 'PM Team'},
        {'name': 'Jr PS', 'level': 'Junior', 'team': 'Professional Services'}
    ]
}

def calculate_monthly_cost(level, use_min=True):
    """Calculate monthly cost with COGS multiplier"""
    salary = SALARY_RANGES[level]['min'] if use_min else SALARY_RANGES[level]['max']
    return salary * COGS_MULTIPLIER

def calculate_annual_cost(level, use_min=True):
    """Calculate annual cost with COGS multiplier"""
    return calculate_monthly_cost(level, use_min) * 12

def main():
    print("=" * 80)
    print("CySec BU - COGS Calculator for 21 Hires")
    print("=" * 80)
    print(f"\nCOGS Multiplier: {COGS_MULTIPLIER}x")
    print("Formula: 1 + COLA(10%) + EPF(11%) + SOCSO(1.45%) + Health(RM100) + Bonus(10%) + PTO(12hrs)")
    print()
    
    total_min = 0
    total_max = 0
    
    for wave_name, positions in WAVES.items():
        wave_min = 0
        wave_max = 0
        
        print(f"\n{wave_name}:")
        print("-" * 60)
        print(f"{'Position':<25} {'Level':<10} {'Monthly (Min)':<15} {'Monthly (Max)':<15}")
        print("-" * 60)
        
        for pos in positions:
            monthly_min = calculate_monthly_cost(pos['level'], use_min=True)
            monthly_max = calculate_monthly_cost(pos['level'], use_min=False)
            wave_min += monthly_min
            wave_max += monthly_max
            print(f"{pos['name']:<25} {pos['level']:<10} RM{monthly_min:,.0f}{'':>8} RM{monthly_max:,.0f}")
        
        annual_min = wave_min * 12
        annual_max = wave_max * 12
        
        print("-" * 60)
        print(f"{'Wave Total':<25} {'':<10} RM{wave_min:,.0f}{'':>8} RM{wave_max:,.0f}")
        print(f"{'Annual':<25} {'':<10} RM{annual_min:,.0f}{'':>8} RM{annual_max:,.0f}")
        
        total_min += annual_min
        total_max += annual_max
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nTotal Positions: 21")
    print(f"Total Annual Cost (Min): RM{total_min:,.0f}")
    print(f"Total Annual Cost (Max): RM{total_max:,.0f}")
    print(f"\nRevenue Target: RM12,000,000")
    print(f"25% Cap: RM3,000,000")
    print(f"\nCost as % of Revenue (Min): {total_min/12000000*100:.1f}%")
    print(f"Cost as % of Revenue (Max): {total_max/12000000*100:.1f}%")
    print(f"\nHeadroom (Min): RM{3000000-total_min:,.0f}")
    print(f"Headroom (Max): RM{3000000-total_max:,.0f}")
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
