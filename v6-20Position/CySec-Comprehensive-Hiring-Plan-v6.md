# CYBERSECURITY BU — COMPREHENSIVE HIRING PLAN

**Version:** 6.0
**Date:** June 24, 2026
**Status:** v6 — General roles + HR levels + Rate-card base salary, 8-5-7
**Classification:** CONFIDENTIAL

> This is the current version. It re-bases the plan on the company HR job-level framework and the consultant Rate-card "Rate"-tab benchmark per the v6 Levels, Titles & Salary Framework (`CySec-v6-Levels-Titles-Salary-Framework.md`). Cost is the gross base benchmark salary — no burden multiplier. All previous versions (v5.0–v5.5) are deprecated and archived under `ARCHIVE-HISTORICAL-VERSIONS/`.

---

## TABLE OF CONTENTS

1. [Executive Summary](#1-executive-summary)
2. [Organizational Structure](#2-organizational-structure)
3. [Wave Hiring Strategy](#3-wave-hiring-strategy)
4. [Financial Analysis](#4-financial-analysis)
5. [Position Details](#5-position-details)
6. [Implementation Timeline](#6-implementation-timeline)
7. [Risk Mitigation](#7-risk-mitigation)
8. [Appendices](#8-appendices)

---

## 1. EXECUTIVE SUMMARY

### 1.1 Overview

This document outlines the strategic hiring plan for the Cybersecurity Business Unit (BU): **20 positions** across the cyber-core practice and its general support functions over a 12-month period, structured in three revenue-triggered waves. Titles, levels, and salary follow the **company HR job-level framework** and the **consultant Rate-card "Rate" tab benchmark**; positions are paid at the gross base benchmark salary.

### 1.2 Key Metrics

| Metric | Value |
|--------|-------|
| **Total Positions** | 23 (3 existing + 20 hires) |
| **Existing Leadership** | 3 |
| **Positions to Hire** | 20 |
| **Hiring Timeline** | 12 months |
| **Revenue Target** | RM12,000,000 |
| **Wave Structure** | 8-5-7 |
| **Level Distribution** | L5 ×3 · L4 ×8 · L3 ×2 · L1 ×7 |
| **Total Annual Base (Min–Max)** | RM2,262,000 – RM3,074,400 |
| **Base as % of Revenue** | 18.9% – 25.6% |
| **25% Revenue Cap** | Within cap across low-to-mid band; only the band ceiling reaches 25.6% (see §4.4) |

### 1.3 Strategic Alignment

1. **General roles, not cyber-dedicated.** The org isn't large enough for dedicated cyber versions of cross-functional roles. Support functions (Technical Presales, DevSecOps, Product/PM, Business Analyst, Blockchain, Professional Services, Sales) are **general** with a **dotted line** to the Cybersecurity practice.
2. **Cyber-core stays in the practice:** Offensive Security, Threat Intelligence, GRC, and Government Security report into the Cybersecurity practice on solid lines.
3. **Compartmentalisation & secondment.** Sensitive work is **compartmentalised**; a future spinoff of the cyber practice is handled by **secondment** of general support staff rather than duplicate dedicated hires.
4. **Pay at benchmark base salary.** Salary equals the Rate-card "Rate" tab benchmark (gross base salary). At base, the total sits **within the 25% revenue cap** across the low-to-mid band (see §4.4).
5. **Phasing by org chart.** Near-term core roles (Technical Presales, Staff Engineer – DevSecOps, GRC Specialist, Product Manager) are **Wave 1**; the rest are growth (Waves 2–3).

### 1.4 Wave Structure Summary (8-5-7)

| Wave | Trigger | Positions | Focus | Annual Base Range |
|------|---------|-----------|-------|-------------------|
| **Wave 1** | Board Approval | 8 | Near-term core (org-chart roles) | RM954,000 – RM1,288,800 |
| **Wave 2** | RM4M+ SOWs | 5 | Revenue closers + senior cyber practice leads | RM834,000 – RM1,047,600 |
| **Wave 3** | RM8M+ Recurring | 7 | Scale-up bench | RM474,000 – RM738,000 |
| **Total** | — | **20** | — | **RM2,262,000 – RM3,074,400** |

**Wave 1 Positions (8):** Technical Presales, Presales Engineer, Product Manager – Government Security, GRC Specialist, Staff Engineer – DevSecOps, Engineer – DevSecOps, Technical Account Manager, Product Manager

> **Note:** The former Senior Project Manager and Junior PM roles are removed. **Product Manager (L5)** is the product owner, general with a dotted line to the cyber practice. Business Analyst is retained.

---

## 2. ORGANIZATIONAL STRUCTURE

### 2.1 Leadership Team (3 Existing)

| Position | Reports To | Status |
|----------|------------|--------|
| BU Head, Cyber Security | C-Suite | Existing |
| Principal Cybersecurity Architect | BU Head | Existing |
| Principal Blockchain Architect | BU Head | Existing |

### 2.2 Team Structure

Solid lines = cyber-core (in practice). Dotted lines = general functions seconded to / supporting the practice.

```
BU Head
├── Principal Cybersecurity Architect  [cyber-core, solid line]
│   ├── Product Manager – Government Security (L4) .......... W1
│   ├── VORON / GRC Team
│   │   ├── GRC Specialist (L4, Specialist/Team Lead) . W1
│   │   └── GRC Analyst (L1) .......................... W3
│   ├── OffSec Team
│   │   ├── Team Lead – Offensive Security (L4) ....... W2
│   │   ├── Staff Engineer – Offensive Security (L4) .. W2
│   │   └── Engineer – Offensive Security (L1) ........ W3
│   └── CTI Team
│       ├── Team Lead – Threat Intelligence (L4) ...... W2
│       ├── Senior Engineer – Threat Intelligence (L3)  W3
│       ├── Engineer – Threat Intelligence (L1) ....... W3
│       └── Engineer – Threat Intelligence
│           (Distributed Intel) (L1) .................. W3
├── Principal Blockchain Architect
│   └── Staff Engineer – Blockchain (L4) [general, dotted to cyber] . W3
│
│   ── General functions (dotted line to the Cybersecurity practice) ──
├── Solutions / Presales
│   ├── Technical Presales (L4) ....................... W1
│   └── Presales Engineer (L1) ....................... W1
├── DevSecOps
│   ├── Staff Engineer – DevSecOps (L4) .............. W1
│   └── Engineer – DevSecOps (L1) ................... W1
├── Product / PM
│   ├── Product Manager (L5) ........................ W1
│   └── Business Analyst (L1) ....................... W3
├── Sales
│   ├── Account Manager – Enterprise (L5) ........... W2
│   └── Account Manager – Government (L5) ........... W2
└── Professional Services
    └── Technical Account Manager (Consultant, L3) ... W1
```

### 2.3 Team Responsibilities

| Team | Class | Focus Area | Key Deliverables |
|------|-------|------------|------------------|
| **Government Security** | Cyber-core | Gov security compliance & governance | Risk assessments, audits, regulator coordination |
| **VORON / GRC** | Cyber-core | GRC, security consulting, assessments | GRC platform ops, risk & compliance |
| **OffSec** | Cyber-core | Offensive security, research, red teaming | Vulnerability research, exploit dev, red team |
| **CTI** | Cyber-core | Cyber threat intelligence | Threat monitoring, intelligence reports |
| **Blockchain** | General | Blockchain development, smart contracts, Web3 | DApp development, smart contract auditing |
| **Solutions / Presales** | General | Presales, solution engineering | Solution architecture, demos/POCs, RFP/RFI |
| **DevSecOps** | General | Security in CI/CD, infrastructure security | Security automation, pipelines, cloud security |
| **Product / PM** | General | Product ownership & business analysis | Roadmap, requirements, delivery tracking |
| **Sales** | General | Business development | Lead generation, deal closing |
| **Professional Services** | General | Account management & delivery coordination | Account health, retention, delivery coordination |

---

## 3. WAVE HIRING STRATEGY

### 3.1 Wave 1: Near-Term Core (8 Roles)

**Trigger:** Board approval · **Timeline:** Months 1-3 · **Annual Base:** RM954,000 – RM1,288,800

#### 3.1.1 Rationale

Wave 1 stands up the org-chart core capability with paired junior capacity where it scales:

1. **Solutions/Presales pod**: Technical Presales (L4) + Presales Engineer (L1) build demos, POCs, and collateral to win pipeline.
2. **DevSecOps pod**: Staff Engineer – DevSecOps (L4) + Engineer – DevSecOps (L1) stand up and operate security automation / CI/CD.
3. **Product ownership**: Product Manager (L5) owns the product roadmap and prioritisation.
4. **Account Management**: Technical Account Manager (Consultant, L3) owns post-sale relationships and delivery coordination.
5. **Governance & GRC**: Product Manager – Government Security (L4) and GRC Specialist (L4) lead compliance, governance, and GRC platform deployment.

#### 3.1.2 Wave 1 Positions

| # | v6 Title | Level | Function | Class | Monthly Benchmark (RM) | Annual Base (RM) |
|---|----------|------:|----------|-------|------------------------|------------------|
| 1 | Technical Presales | L4 | Solutions/Presales | General | 11,500 – 15,500 | 138,000 – 186,000 |
| 2 | Presales Engineer | L1 | Solutions/Presales | General | 4,000 – 7,000 | 48,000 – 84,000 |
| 3 | Product Manager – Government Security | L4 | Gov Sec | Cyber-core | 11,500 – 15,500 | 138,000 – 186,000 |
| 4 | GRC Specialist *(Specialist/Team Lead)* | L4 | VORON/GRC | Cyber-core | 11,500 – 15,500 | 138,000 – 186,000 |
| 5 | Staff Engineer – DevSecOps | L4 | DevSecOps | General | 11,500 – 15,500 | 138,000 – 186,000 |
| 6 | Engineer – DevSecOps | L1 | DevSecOps | General | 4,000 – 7,000 | 48,000 – 84,000 |
| 7 | Technical Account Manager *(Consultant)* | L3 | Professional Services | General | 8,000 – 11,000 | 96,000 – 132,000 |
| 8 | Product Manager | L5 | Product/PM | General | 17,500 – 20,400 | 210,000 – 244,800 |
| **Total** | | | | | | **954,000 – 1,288,800** |

#### 3.1.3 Wave 1 Success Criteria

- [ ] All 8 positions filled within 90 days
- [ ] Solutions/Presales pod: Demo/POC environment + reusable collateral established
- [ ] Product: Roadmap and prioritisation framework established
- [ ] GRC: GRC platform (VoronCitadel) deployed
- [ ] Governance: Security governance framework established
- [ ] DevSecOps pod: CI/CD security pipeline implemented and operated
- [ ] TAM: Account-management framework and delivery coordination established

### 3.2 Wave 2: RM4M+ SOWs (5 Roles)

**Trigger:** RM4,000,000+ in signed SOWs · **Timeline:** Months 4-8 · **Annual Base:** RM834,000 – RM1,047,600

#### 3.2.1 Rationale

Wave 2 converts pipeline into closed revenue and stands up the senior cyber-core practices SOWs demand:

1. **Sales Closers**: Account Manager – Enterprise (L5) and Account Manager – Government (L5) convert pipeline to revenue.
2. **OffSec Practice**: Team Lead – Offensive Security (L4) + Staff Engineer – Offensive Security (L4) deliver offensive engagements.
3. **CTI Practice**: Team Lead – Threat Intelligence (L4) establishes threat-intelligence operations.

#### 3.2.2 Wave 2 Positions

| # | v6 Title | Level | Function | Class | Monthly Benchmark (RM) | Annual Base (RM) |
|---|----------|------:|----------|-------|------------------------|------------------|
| 1 | Account Manager – Enterprise | L5 | Sales | General | 17,500 – 20,400 | 210,000 – 244,800 |
| 2 | Account Manager – Government | L5 | Sales | General | 17,500 – 20,400 | 210,000 – 244,800 |
| 3 | Team Lead – Offensive Security | L4 | OffSec | Cyber-core | 11,500 – 15,500 | 138,000 – 186,000 |
| 4 | Staff Engineer – Offensive Security | L4 | OffSec | Cyber-core | 11,500 – 15,500 | 138,000 – 186,000 |
| 5 | Team Lead – Threat Intelligence | L4 | CTI | Cyber-core | 11,500 – 15,500 | 138,000 – 186,000 |
| **Total** | | | | | | **834,000 – 1,047,600** |

#### 3.2.3 Wave 2 Success Criteria

- [ ] All 5 positions filled within 120 days of trigger
- [ ] Enterprise + Government pipeline targets achieved
- [ ] OffSec practice (Team Lead + Staff Engineer) delivering engagements
- [ ] CTI practice operational

### 3.3 Wave 3: RM8M+ Recurring (7 Roles)

**Trigger:** RM8,000,000+ in recurring revenue · **Timeline:** Months 9-12 · **Annual Base:** RM474,000 – RM738,000

#### 3.3.1 Rationale

Wave 3 completes the structure with engineer/IC support across the practices and brings the Blockchain senior online:

1. **Blockchain Practice**: Staff Engineer – Blockchain (L4) spins up blockchain delivery.
2. **Intelligence Operations**: Senior Engineer and Engineers expand CTI intel capacity.
3. **Practice Support**: GRC Analyst and OffSec Engineer complete the VORON and OffSec benches.
4. **Product Support**: Business Analyst provides requirements and analysis under the Product Manager.

#### 3.3.2 Wave 3 Positions

| # | v6 Title | Level | Function | Class | Monthly Benchmark (RM) | Annual Base (RM) |
|---|----------|------:|----------|-------|------------------------|------------------|
| 1 | Staff Engineer – Blockchain | L4 | Blockchain | General | 11,500 – 15,500 | 138,000 – 186,000 |
| 2 | GRC Analyst | L1 | VORON/GRC | Cyber-core | 4,000 – 7,000 | 48,000 – 84,000 |
| 3 | Engineer – Offensive Security | L1 | OffSec | Cyber-core | 4,000 – 7,000 | 48,000 – 84,000 |
| 4 | Senior Engineer – Threat Intelligence | L3 | CTI | Cyber-core | 8,000 – 11,000 | 96,000 – 132,000 |
| 5 | Engineer – Threat Intelligence | L1 | CTI | Cyber-core | 4,000 – 7,000 | 48,000 – 84,000 |
| 6 | Engineer – Threat Intelligence *(Distributed Intel)* | L1 | CTI | Cyber-core | 4,000 – 7,000 | 48,000 – 84,000 |
| 7 | Business Analyst | L1 | Product/PM | General | 4,000 – 7,000 | 48,000 – 84,000 |
| **Total** | | | | | | **474,000 – 738,000** |

---

## 4. FINANCIAL ANALYSIS

### 4.1 Cost Structure

```
Cost = Benchmark Base Salary (gross monthly × 12)
```
Benchmark = "Monthly Salary (Ref)" from the Rate-card "Rate" tab (gross, monthly). Cost is the gross base salary; no multiplier is applied.

### 4.2 Benchmark by Level

| Level | HR Band | Monthly Benchmark (RM) | Annual Base (RM) |
|------:|---------|------------------------|------------------|
| L5 | Manager | 17,500 – 20,400 | 210,000 – 244,800 |
| L4 | Assistant Manager | 11,500 – 15,500 | 138,000 – 186,000 |
| L3 | Senior Executive | 8,000 – 11,000 | 96,000 – 132,000 |
| L1 | Executive | 4,000 – 7,000 | 48,000 – 84,000 |

### 4.3 Wave Cost Breakdown

| Wave | Positions | Annual Base (Min–Max) |
|------|-----------|-----------------------|
| Wave 1 | 8 | RM954,000 – RM1,288,800 |
| Wave 2 | 5 | RM834,000 – RM1,047,600 |
| Wave 3 | 7 | RM474,000 – RM738,000 |
| **Total** | **20** | **RM2,262,000 – RM3,074,400** |

### 4.4 Budget / Cap Reconciliation

| Measure | Value | vs RM12M Revenue |
|---|---|---|
| Annual base salary | RM2.26M – RM3.07M | 18.9% – 25.6% |
| 25% revenue cap | RM3,000,000 | — |

At benchmark base salary, the total is **18.9% – 25.6%** of RM12M revenue — **within the 25% cap across the low-to-mid band**. Only the absolute top of the band (max benchmark for every role) reaches **25.6%**, marginally over. Setting offers anywhere below the band ceiling keeps the plan inside 25%; no cap relaxation is required at planned salary levels.

### 4.5 36-Month Runway (estimated, base salary)

Year 1 phased (W1 ~10mo, W2 ~5mo, W3 ~1mo); Years 2–3 full run-rate; flat RM12M revenue.

| Year | Base (Min–Max) | Cumulative (Max) |
|------|----------------|------------------|
| Year 1 (phased) | RM1,182,000 – RM1,572,000 | RM1,572,000 |
| Year 2 (full) | RM2,262,000 – RM3,074,400 | RM4,646,400 |
| Year 3 (full) | RM2,262,000 – RM3,074,400 | RM7,720,800 |
| **36-mo total** | **RM5,706,000 – RM7,720,800** | |

---

## 5. POSITION DETAILS

### 5.1 Wave 1 Positions (8)

#### 5.1.1 Technical Presales (L4) — Solutions/Presales [General]
**Reports To:** BU Head (dotted line to cyber practice) · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Own the technical narrative across the deal lifecycle; develop solution architectures and proposals; build demos/POCs; respond to RFPs/RFIs. 5+ years presales/solution engineering; cybersecurity or blockchain background.

#### 5.1.2 Presales Engineer (L1) — Solutions/Presales [General]
**Reports To:** Technical Presales · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Build/maintain demo and POC environments; draft RFP/RFI sections; research competitors; maintain the collateral library. 1–2 years technical/presales-support; foundational cybersecurity/blockchain knowledge.

#### 5.1.3 Product Manager – Government Security (L4) — Gov Sec [Cyber-core]
**Reports To:** Principal Cybersecurity Architect · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Lead government security compliance and governance; manage risk assessments and audits; coordinate with regulators. 5+ years gov security/compliance; CISSP/CISM; Malaysian gov frameworks (ISMS, PDPA).

#### 5.1.4 GRC Specialist (L4, Specialist/Team Lead) — VORON/GRC [Cyber-core]
**Reports To:** Principal Cybersecurity Architect · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Lead GRC platform operations, risk management, and compliance; deploy VoronCitadel; develop control frameworks. 5+ years GRC/compliance; CISSP/CISA/CRISC; ISO 27001/NIST.

#### 5.1.5 Staff Engineer – DevSecOps (L4) — DevSecOps [General]
**Reports To:** Principal Cybersecurity Architect (dotted line) · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Design/implement DevSecOps pipelines and security automation; integrate security into CI/CD; manage cloud security. 5+ years DevOps/DevSecOps; CI/CD tools; cloud; scripting.

#### 5.1.6 Engineer – DevSecOps (L1) — DevSecOps [General]
**Reports To:** Staff Engineer – DevSecOps · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Support pipeline development; implement automation scripts; monitor alerts; document configurations. 2+ years DevOps/security; CI/CD basics; scripting; cloud basics.

#### 5.1.7 Technical Account Manager (Consultant, L3) — Professional Services [General]
**Reports To:** BU Head (dotted line) · **Benchmark:** RM8,000 – RM11,000/mo · **Annual Base:** RM96,000 – RM132,000
Own post-sale client relationships; coordinate delivery across teams; track account health; run QBRs; manage escalations; identify expansion. 2–4 years technical account management/customer success; client communication.

#### 5.1.8 Product Manager (L5) — Product/PM [General]
**Reports To:** BU Head (dotted line) · **Benchmark:** RM17,500 – RM20,400/mo · **Annual Base:** RM210,000 – RM244,800
Own the product roadmap and prioritisation; define requirements and outcomes; coordinate engineering and go-to-market; manage the product lifecycle. 7+ years product management; cybersecurity/technology products. Replaces the former Junior PM role.

---

### 5.2 Wave 2 Positions (5)

#### 5.2.1 Account Manager – Enterprise (L5) — Sales [General]
**Reports To:** BU Head (dotted line) · **Benchmark:** RM17,500 – RM20,400/mo · **Annual Base:** RM210,000 – RM244,800
Develop enterprise relationships; pursue opportunities; develop proposals; achieve targets. 5+ years enterprise sales; cybersecurity/technology sales.

#### 5.2.2 Account Manager – Government (L5) — Sales [General]
**Reports To:** BU Head (dotted line) · **Benchmark:** RM17,500 – RM20,400/mo · **Annual Base:** RM210,000 – RM244,800
Develop government relationships; identify procurement opportunities; develop tender proposals. 5+ years gov sector sales; Malaysian procurement.

#### 5.2.3 Team Lead – Offensive Security (L4) — OffSec [Cyber-core]
**Reports To:** Principal Cybersecurity Architect · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Lead offensive security research and exploit development; manage disclosure; develop tooling; mentor engineers. 7+ years offensive research; exploit dev; programming.

#### 5.2.4 Staff Engineer – Offensive Security (L4) — OffSec [Cyber-core]
**Reports To:** Team Lead – Offensive Security · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Conduct red team engagements and adversary simulations; develop attack playbooks; document findings. 5+ years red team; OSCP/OSCE/OSEP; MITRE ATT&CK.

#### 5.2.5 Team Lead – Threat Intelligence (L4) — CTI [Cyber-core]
**Reports To:** Principal Cybersecurity Architect · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Establish and manage threat intelligence operations; develop frameworks; lead threat hunting; produce intel reports. 7+ years threat intelligence; GCTI; MISP/OpenCTI.

---

### 5.3 Wave 3 Positions (7)

#### 5.3.1 Staff Engineer – Blockchain (L4) — Blockchain [General]
**Reports To:** Principal Blockchain Architect (dotted line to cyber) · **Benchmark:** RM11,500 – RM15,500/mo · **Annual Base:** RM138,000 – RM186,000
Develop blockchain applications and smart contracts; conduct audits; design decentralized architectures. 5+ years blockchain dev; Ethereum/Solidity.

#### 5.3.2 GRC Analyst (L1) — VORON/GRC [Cyber-core]
**Reports To:** GRC Specialist · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Support assessments and platform operations; control testing and gap analysis; compliance documentation. 2+ years GRC/security/IT audit.

#### 5.3.3 Engineer – Offensive Security (L1) — OffSec [Cyber-core]
**Reports To:** Team Lead – Offensive Security · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Support vulnerability research; analyze malware; document findings; participate in CTFs. 2+ years security research; Python/C/C++.

#### 5.3.4 Senior Engineer – Threat Intelligence (L3) — CTI [Cyber-core]
**Reports To:** Team Lead – Threat Intelligence · **Benchmark:** RM8,000 – RM11,000/mo · **Annual Base:** RM96,000 – RM132,000
Deep-dive research on threat actors and campaigns; malware analysis; develop threat profiles. 3+ years research/threat intel; malware analysis/RE.

#### 5.3.5 Engineer – Threat Intelligence (L1) — CTI [Cyber-core]
**Reports To:** Team Lead – Threat Intelligence · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Analyze threat intel data; monitor threats; produce reports; support threat hunting. 2+ years threat intel/security analysis; MITRE ATT&CK; SIEM.

#### 5.3.6 Engineer – Threat Intelligence (Distributed Intel) (L1) — CTI [Cyber-core]
**Reports To:** Team Lead – Threat Intelligence · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Collect/analyze distributed intel sources; monitor dark web/forums; track IOCs. 2+ years intel collection; OSINT/HUMINT.

#### 5.3.7 Business Analyst (L1) — Product/PM [General]
**Reports To:** Product Manager (dotted line) · **Benchmark:** RM4,000 – RM7,000/mo · **Annual Base:** RM48,000 – RM84,000
Gather and document requirements; facilitate workshops; develop user stories; support product planning. 2+ years business analysis; CBAP preferred; Agile.

---

## 6. IMPLEMENTATION TIMELINE

```
Month 1-3:  Wave 1 Execution (8 roles) — on board approval
Month 4-8:  Wave 2 Execution (5 roles) — on RM4M+ SOWs
Month 9-12: Wave 3 Execution (7 roles) — on RM8M+ recurring revenue
```

| Milestone | Target Date | Success Criteria |
|-----------|-------------|------------------|
| BU Approval | Month 0 | Board approval |
| Wave 1 Complete | Month 3 | All 8 positions filled |
| RM4M SOWs Achieved | Month 4 | Signed SOWs totaling RM4M+ |
| Wave 2 Complete | Month 8 | All 5 positions filled |
| RM8M Recurring Achieved | Month 9 | Recurring revenue RM8M+ |
| Wave 3 Complete | Month 12 | All 7 positions filled |

---

## 7. RISK MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Labour ratio near 25% cap at band ceiling | Low | Medium | Base total is 18.9%–25.6% of RM12M — within cap across low-to-mid band; set offers below the ceiling to stay under 25% |
| Talent shortage | Medium | High | Pay at full Rate-card benchmark base; employer branding |
| Extended hiring timelines | High | Medium | Parallel hiring tracks |
| Cyber spinoff / compartmentalisation | Medium | Medium | General support staff seconded to the practice; sensitive work compartmentalised |
| Revenue shortfall | Medium | High | Flexible wave triggers tied to SOWs and recurring revenue |

---

## 8. APPENDICES

### 8.1 Appendix A: Function Cost Distribution

| Function | Class | Positions | Annual Base (Min) | Annual Base (Max) |
|----------|-------|-----------|-------------------|-------------------|
| Government Security | Cyber-core | 1 | RM138,000 | RM186,000 |
| VORON / GRC | Cyber-core | 2 | RM186,000 | RM270,000 |
| OffSec | Cyber-core | 3 | RM324,000 | RM456,000 |
| CTI | Cyber-core | 4 | RM330,000 | RM486,000 |
| Blockchain | General | 1 | RM138,000 | RM186,000 |
| Solutions / Presales | General | 2 | RM186,000 | RM270,000 |
| DevSecOps | General | 2 | RM186,000 | RM270,000 |
| Product / PM | General | 2 | RM258,000 | RM328,800 |
| Sales | General | 2 | RM420,000 | RM489,600 |
| Professional Services | General | 1 | RM96,000 | RM132,000 |
| **Total** | | **20** | **RM2,262,000** | **RM3,074,400** |

### 8.2 Appendix B: Level Distribution

| Level | Count | Roles |
|------:|------:|-------|
| L5 | 3 | Product Manager, Account Manager – Enterprise, Account Manager – Government |
| L4 | 8 | Technical Presales, Product Manager – Government Security, GRC Specialist, Staff Engineer – DevSecOps, Team Lead – Offensive Security, Staff Engineer – Offensive Security, Team Lead – Threat Intelligence, Staff Engineer – Blockchain |
| L3 | 2 | Technical Account Manager, Senior Engineer – Threat Intelligence |
| L1 | 7 | Presales Engineer, Engineer – DevSecOps, GRC Analyst, Engineer – Offensive Security, Engineer – Threat Intelligence, Engineer – Threat Intelligence (Distributed Intel), Business Analyst |
| **Total** | **20** | |

### 8.3 Appendix C: Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 5.0 | June 10, 2026 | Hadri | 24-position structure (5-7-9) |
| 5.3 | June 10, 2026 | Hadri | Balanced 7-7-7 structure |
| 5.4 | June 23, 2026 | Hadri | Support-pod 8-5-8 (PM removed, Jr Presales added) |
| 5.5 | June 23, 2026 | Hadri | Junior Professional Services removed → 7-5-8, 20 hires |
| **6.0** | **June 24, 2026** | **Hadri** | **Re-based on HR job-level framework + Rate-card benchmark. General (dotted) vs cyber-core split, company-convention titles, Jr PM → Product Manager (L5) → 8-5-7, 20 hires. Removed COGS (cost = base salary); Technical Presales. Base RM2,262,000–3,074,400 (18.9%–25.6% of RM12M)** |

---

**END OF DOCUMENT**
