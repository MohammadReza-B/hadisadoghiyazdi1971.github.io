---
layout: single  # یا single با کلاس rtl-layout
classes: wide 
title: "AI-based Bowtie with RAG engine"
permalink: /projects/AIBasedBowtieRAG/
author_profile: true
sidebar:
  nav: "projects"
header:
  overlay_image: "/assets/images/background.jpg"
  overlay_filter: 0.3
  overlay_color: "#5e616c"
  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
---

# AI-based Bowtie with RAG Engine Analysis

In this case we use [Khazaeeni2006] in our AI-based Bowtie with RAG engine. Following notes used from [Khazaeeni2006] using RAG.

## Output of RAG

To validate the framework, we utilized comprehensive risk documentation from multiple BOT infrastructure projects in Iran. The input text contained detailed analysis of political, economic, and operational risks associated with these complex projects.

### BOT Projects Under Analysis

**Table: BOT Projects Underway in Iran**

| Project Name              | Stage of Work            | Concession Holder Company             |
| ------------------------- | ------------------------ | ------------------------------------- |
| Isfahan South Power Plant | In Operation             | Isfahan South Power Plant Co. (MAPNA) |
| Zanjan Power Plant        | Contract Signed          | MAPNA International & Quest (UAE)     |
| Pars-e-Sar Power Plant    | Under Negotiation        | Consortium led by Edison              |
| Aliabad Power Plant       | Under Negotiation        | OGER (Saudi Arabia)                   |
| Tabriz Power Plant        | Under Negotiation        | ZENEL (Saudi Arabia)                  |
| Shirvan Power Plant       | Under Negotiation        | Sumitomo (Japan)                      |
| Zanjan Power Plants (4-2) | Feasibility Study - BOO* | -                                     |
| Isfahan Power Plants (4)  | Feasibility Study - BOO* | -                                     |

*BOO: Build-Own-Operate

### Risk Documentation Analysis

The risk documentation analyzed contained comprehensive information about various risk categories including political risks (regulatory changes), economic risks (inflation), construction delays, and market uncertainties. The text detailed specific risk mitigation strategies such as risk allocation frameworks, Take-or-pay agreements, and MIGA insurance.

### AI-Generated Bowtie Components

- **Hazard:** Project Failure / Financial Loss
- **Top Event:** Disruption of Operational Continuity
- **Threats:** Political Instability, Economic Inflation, Construction Delays, Regulatory Changes, Market Volatility
- **Preventive Barriers:** Risk Allocation Framework, Take-or-pay Agreements, MIGA Insurance, Comprehensive Risk Assessment, Government Support Mechanisms
- **Consequences:** Stakeholder Bankruptcy, Reputation Damage, Service Disruption, Financial Loss
- **Mitigative Barriers:** Crisis Management Programs, Contract Modification Mechanisms, Insurance Coverage, Diversification Strategies

### Visualization Analysis

The system successfully mapped these entities into a Mermaid flowchart, correctly placing "Take-or-pay agreements" as a preventive barrier against "Economic risks" and "MIGA insurance" as a transference mechanism for political risks. The diagram demonstrated proper causal relationships and logical structure consistent with Bowtie construction best practices.

---



```mermaid
flowchart LR
    subgraph Hazard
        H["<b>Project Failure</b><br>Severe Financial Losses<br>and Operational Disruptions"]
    end

    subgraph Threats
        T1["<b>Political Risks</b><br>Regulatory Changes, Political Instability"]
        T2["<b>Economic Risks</b><br>Inflation, Currency Fluctuations, Market Recession"]
        T3["<b>Legal Risks</b><br>Regulation Changes"]
        T4["<b>Development Risks</b><br>Financing Delays"]
        T5["<b>Execution Risks</b><br>Construction Delays, Technical Issues"]
        T6["<b>Market Risks</b><br>Demand Changes"]
        T7["<b>Operational Risks</b><br>Operational Problems"]
    end

    subgraph Preventive_Barriers
        B1["<b>Risk Allocation Models</b><br>Among Stakeholders"]
        B2["<b>Contractual Agreements</b><br>Take-or-pay"]
        B3["<b>Insurance Mechanisms</b><br>MIGA"]
        B4["<b>Comprehensive Risk Assessment</b><br>and Planning"]
        B5["<b>Governance Structures</b><br>and Shareholder Agreements"]
        B6["<b>Avoidance & Mitigation Strategies</b>"]
    end

    subgraph Top_Event
        TE[("<b>Top Event</b><br>BOT Project Failure")]
    end

    subgraph Mitigative_Barriers
        M1["<b>Risk Control Programs</b><br>and Crisis Management"]
        M2["<b>Insurance Coverage</b><br>and Financial Support"]
        M3["<b>Contract Amendment Mechanisms</b><br>e.g., Tariff Adjustment"]
        M4["<b>Risk Sharing Agreements</b>"]
        M5["<b>Risk Acceptance Programs</b>"]
    end

    subgraph Consequences
        C1["<b>Severe Financial Losses</b>"]
        C2["<b>Project Delay or Cancellation</b>"]
        C3["<b>Damage to Stakeholder Reputation</b>"]
        C4["<b>Infrastructure Service Disruption</b>"]
        C5["<b>Legal Disputes</b>"]
        C6["<b>Social and Economic Impacts</b>"]
    end

    subgraph Digital_Twin_AI
        DT["<b>Digital Twin & AI Intelligence Layer</b>"]
        DT1["<b>Physics-based Digital Twin</b>"]
        DT2["<b>Real-time Sensor Integration</b>"]
        DT3["<b>Degradation Prediction Models</b>"]
        DT4["<b>What-if Scenario Engine</b>"]
        AI1["<b>Adaptive Risk Allocation</b>"]
        AI2["<b>Smart Insurance Activation</b>"]
        AI3["<b>Risk Mitigation Recommendations</b>"]
    end

    subgraph Multi_Layer
        L1["<b>Physical/Technical</b><br>Infrastructure, Equipment"]
        L2["<b>Control & Instrumentation</b><br>Control Systems, Safety"]
        L3["<b>Human & Organizational</b><br>Management Teams, Processes"]
        L4["<b>Digital/Cyber</b><br>Digital Systems, Data"]
        L5["<b>Management & Governance</b><br>Governance Structures, Regulations"]
    end

    H -- Threat Path --> TE
    
    T1 == Threat Flow ==> B1
    T2 == Threat Flow ==> B2
    T3 == Threat Flow ==> B3
    T4 == Threat Flow ==> B4
    T5 == Threat Flow ==> B5
    T6 == Threat Flow ==> B6
    T7 == Threat Flow ==> B1
    
    B1 -- Preventive Barrier --> TE
    B2 -- Preventive Barrier --> TE
    B3 -- Preventive Barrier --> TE
    B4 -- Preventive Barrier --> TE
    B5 -- Preventive Barrier --> TE
    B6 -- Preventive Barrier --> TE
    
    TE -- Mitigation Path --> M1
    TE -- Mitigation Path --> M2
    TE -- Mitigation Path --> M3
    TE -- Mitigation Path --> M4
    TE -- Mitigation Path --> M5
    
    M1 -. Consequence Flow .-> C1
    M2 -. Consequence Flow .-> C2
    M3 -. Consequence Flow .-> C3
    M4 -. Consequence Flow .-> C4
    M5 -. Consequence Flow .-> C5
    
    M1 -. Consequence Flow .-> C6
    M2 -. Consequence Flow .-> C6
    M3 -. Consequence Flow .-> C6
    M4 -. Consequence Flow .-> C6
    M5 -. Consequence Flow .-> C6

    DT -.- AI_Support -.-> B1
    DT -.- AI_Support -.-> B2
    DT -.- AI_Support -.-> B3
    DT -.- AI_Support -.-> B4
    DT -.- AI_Support -.-> B5
    DT -.- AI_Support -.-> B6
    DT -.- AI_Support -.-> M1
    DT -.- AI_Support -.-> M2
    DT -.- AI_Support -.-> M3
    DT -.- AI_Support -.-> M4
    DT -.- AI_Support -.-> M5

    L1 -- Layer Influence --> B1
    L2 -- Layer Influence --> B2
    L3 -- Layer Influence --> B3
    L4 -- Layer Influence --> B4
    L5 -- Layer Influence --> B5
    
    L1 -- Layer Influence --> M1
    L2 -- Layer Influence --> M2
    L3 -- Layer Influence --> M3
    L4 -- Layer Influence --> M4
    L5 -- Layer Influence --> M5

    style H fill:#ffff99,stroke:#333,stroke-width:2px
    style T1 fill:#99ccff,stroke:#333
    style T2 fill:#99ccff,stroke:#333
    style T3 fill:#99ccff,stroke:#333
    style T4 fill:#99ccff,stroke:#333
    style T5 fill:#99ccff,stroke:#333
    style T6 fill:#99ccff,stroke:#333
    style T7 fill:#99ccff,stroke:#333
    style B1 fill:#90ee90,stroke:#333
    style B2 fill:#90ee90,stroke:#333
    style B3 fill:#90ee90,stroke:#333
    style B4 fill:#90ee90,stroke:#333
    style B5 fill:#90ee90,stroke:#333
    style B6 fill:#90ee90,stroke:#333
    style TE fill:#ff4d4d,stroke:#333,stroke-width:2px,color:#fff
    style M1 fill:#ffa64d,stroke:#333
    style M2 fill:#ffa64d,stroke:#333
    style M3 fill:#ffa64d,stroke:#333
    style M4 fill:#ffa64d,stroke:#333
    style M5 fill:#ffa64d,stroke:#333
    style C1 fill:#ff9999,stroke:#333
    style C2 fill:#ff9999,stroke:#333
    style C3 fill:#ff9999,stroke:#333
    style C4 fill:#ff9999,stroke:#333
    style C5 fill:#ff9999,stroke:#333
    style C6 fill:#ff9999,stroke:#333
    style DT fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style DT1 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style DT2 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style DT3 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style DT4 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style AI1 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style AI2 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style AI3 fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5
    style L1 fill:#e6e6fa,stroke:#333
    style L2 fill:#e6e6fa,stroke:#333
    style L3 fill:#e6e6fa,stroke:#333
    style L4 fill:#e6e6fa,stroke:#333
    style L5 fill:#e6e6fa,stroke:#333

    linkStyle 0 stroke:#ff4d4d,stroke-width:3px
    linkStyle 1 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 2 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 3 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 4 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 5 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 6 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 7 stroke:#4169E1,stroke-width:2px,stroke-dasharray: 5 5
    linkStyle 8 stroke:#228B22,stroke-width:2px
    linkStyle 9 stroke:#228B22,stroke-width:2px
    linkStyle 10 stroke:#228B22,stroke-width:2px
    linkStyle 11 stroke:#228B22,stroke-width:2px
    linkStyle 12 stroke:#228B22,stroke-width:2px
    linkStyle 13 stroke:#228B22,stroke-width:2px
    linkStyle 14 stroke:#FF8C00,stroke-width:2px
    linkStyle 15 stroke:#FF8C00,stroke-width:2px
    linkStyle 16 stroke:#FF8C00,stroke-width:2px
    linkStyle 17 stroke:#FF8C00,stroke-width:2px
    linkStyle 18 stroke:#FF8C00,stroke-width:2px
    linkStyle 19 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 20 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 21 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 22 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 23 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 24 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 25 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 26 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 27 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 28 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 29 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 30 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 31 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 32 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 33 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 34 stroke:#20B2AA,stroke-width:2px
    linkStyle 35 stroke:#20B2AA,stroke-width:2px
    linkStyle 36 stroke:#20B2AA,stroke-width:2px
    linkStyle 37 stroke:#20B2AA,stroke-width:2px
    linkStyle 38 stroke:#20B2AA,stroke-width:2px
    linkStyle 39 stroke:#20B2AA,stroke-width:2px
    linkStyle 40 stroke:#20B2AA,stroke-width:2px
    linkStyle 41 stroke:#20B2AA,stroke-width:2px
    linkStyle 42 stroke:#20B2AA,stroke-width:2px
    linkStyle 43 stroke:#20B2AA,stroke-width:2px
```


Interestingly, for display it briefly, we use my AI-Based Bow-tie and this is the result:

```mermaid
flowchart LR
    subgraph Hazard
        H["<b>Project Failure</b><br>Financial Loss & Operational Disruption"]
    end

    subgraph Threats
        T1["<b>Political</b><br>Regulatory Changes"]
        T2["<b>Economic</b><br>Inflation, Market Risks"]
        T3["<b>Execution</b><br>Construction Delays"]
        T4["<b>Operational</b><br>Technical Issues"]
    end

    subgraph Preventive_Barriers
        B1["<b>Risk Allocation</b><br>Stakeholder Models"]
        B2["<b>Contractual</b><br>Take-or-pay Agreements"]
        B3["<b>Insurance</b><br>MIGA Coverage"]
        B4["<b>Risk Assessment</b><br>Planning & Governance"]
    end

    subgraph Top_Event
        TE[("<b>Top Event</b><br>BOT Project Failure")]
    end

    subgraph Mitigative_Barriers
        M1["<b>Crisis Management</b>"]
        M2["<b>Insurance Support</b>"]
        M3["<b>Contract Amendments</b><br>Tariff Adjustments"]
    end

    subgraph Consequences
        C1["<b>Financial Losses</b>"]
        C2["<b>Reputation Damage</b>"]
        C3["<b>Service Disruption</b>"]
    end

    subgraph AI_Support
        AI["<b>AI Intelligence Layer</b><br>Risk Mitigation & Prediction"]
    end

    H -- Threat Path --> TE
    
    T1 --> B1
    T2 --> B2
    T3 --> B3
    T4 --> B4
    
    B1 --> TE
    B2 --> TE
    B3 --> TE
    B4 --> TE
    
    TE --> M1
    TE --> M2
    TE --> M3
    
    M1 --> C1
    M1 --> C2
    M2 --> C3
    M3 --> C1
    
    AI -. Support .-> B1
    AI -. Support .-> B2
    AI -. Support .-> M1
    AI -. Support .-> M2

    style H fill:#ffff99,stroke:#333,stroke-width:2px
    style T1 fill:#99ccff,stroke:#333
    style T2 fill:#99ccff,stroke:#333
    style T3 fill:#99ccff,stroke:#333
    style T4 fill:#99ccff,stroke:#333
    style B1 fill:#90ee90,stroke:#333
    style B2 fill:#90ee90,stroke:#333
    style B3 fill:#90ee90,stroke:#333
    style B4 fill:#90ee90,stroke:#333
    style TE fill:#ff4d4d,stroke:#333,stroke-width:2px,color:#fff
    style M1 fill:#ffa64d,stroke:#333
    style M2 fill:#ffa64d,stroke:#333
    style M3 fill:#ffa64d,stroke:#333
    style C1 fill:#ff9999,stroke:#333
    style C2 fill:#ff9999,stroke:#333
    style C3 fill:#ff9999,stroke:#333
    style AI fill:#dda0dd,stroke:#333,stroke-dasharray: 5 5

    linkStyle 0 stroke:#ff4d4d,stroke-width:3px
    linkStyle 1 stroke:#4169E1,stroke-width:2px
    linkStyle 2 stroke:#4169E1,stroke-width:2px
    linkStyle 3 stroke:#4169E1,stroke-width:2px
    linkStyle 4 stroke:#228B22,stroke-width:2px
    linkStyle 5 stroke:#228B22,stroke-width:2px
    linkStyle 6 stroke:#228B22,stroke-width:2px
    linkStyle 7 stroke:#228B22,stroke-width:2px
    linkStyle 8 stroke:#FF8C00,stroke-width:2px
    linkStyle 9 stroke:#FF8C00,stroke-width:2px
    linkStyle 10 stroke:#FF8C00,stroke-width:2px
    linkStyle 11 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 12 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 13 stroke:#FF4500,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 14 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 15 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
    linkStyle 16 stroke:#9370DB,stroke-width:2px,stroke-dasharray: 3 3
```

## References

Khazaeeni, G., & Ahmadi, L. (2006). Risk management in mega-projects with the BOT approach. *Proceedings of the 2nd International Project Management Conference*.



